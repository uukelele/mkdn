from markdown_it import MarkdownIt
from markdown_it.token import Token
from mdit_py_plugins.tasklists import tasklists_plugin

from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.formatters import Terminal256Formatter

from texicode.pipeline import render_tex

from shutil import get_terminal_size
import os
import re
from pathlib import Path
import base64
import httpx
import asyncio
from io import BytesIO
from PIL import Image
from contextvars import ContextVar

is_kitty = 'kitty' in os.getenv('TERM', '')

md = MarkdownIt(
    'commonmark',
    {
        'linkify': True,
        'breaks': True,
    }
).enable('strikethrough').use(tasklists_plugin, enabled=True)

_heading_scale = None

_blockquote_open = 0
_list_open = []
_image_cache = {}
_has_rendered_blockquote = ContextVar('_h_r_b', default=False)

width, height = get_terminal_size()

async def fetch_image(client: httpx.Client, url):
    try:
        if url.startswith('http'):
            res = await client.get(url, follow_redirects=True)
            if res.status_code >= 400: return
            img_data = res.read()
        else:
            path = Path(url)
            if not path.exists(): return
            img_data = path.read_bytes()

        img = Image.open(BytesIO(img_data))
        png_io = BytesIO()
        img.save(png_io, format='PNG')
        b64 = base64.b64encode(png_io.getvalue()).decode('ascii')

        chunk_size = 4096
        buf = []

        for i in range(0, len(b64), chunk_size):
            chunk = b64[i:i+chunk_size]
            more = 1 if i + chunk_size < len(b64) else 0

            if i == 0:
                buf.append(f'\033_Ga=T,f=100,i={len(_image_cache)},m={more};{chunk}\033\\')
            else:
                buf.append(f'\033_Gi={len(_image_cache)},m={more};{chunk}\033\\')

        _image_cache[url] = ''.join(buf) + '\n'

    except Exception as e:
        _image_cache[url] = f"[Error loading image: {e}]\n"

async def preload_images(tokens: list[Token]):
    async with httpx.AsyncClient() as client:
        tasks = []

        def find_images(tokens: list[Token]):
            for t in tokens:
                if t.type == 'image':
                    url = t.attrGet('src')
                    if url and url.startswith('http') and url not in _image_cache:
                        tasks.append(fetch_image(client, url))
                if t.children:
                    find_images(t.children)

        find_images(tokens)

        if tasks:
            await asyncio.gather(*tasks)

def highlight_code(code: str, lang: str | None = None):
    try:
        lexer = get_lexer_by_name(lang) if lang else guess_lexer(code)
    except:
        try:
            lexer = guess_lexer(lexer)
        except:
            return code
        
    return highlight(code, lexer, Terminal256Formatter(style='monokai'))


# https://github.com/dxddxx/TeXicode/blob/8d7ab0ff93f36f98669c34c78a38de63a44ce80f/src/main.py#L11-L26 | A bit modified
def process_markdown(content):

    inline_dollar = r'(?<!\$)\$(?!\$)([^\n$]+?)\$(?!\$)'
    block_dollar = r'\$\$([\s\S]+?)\$\$|\\\[([\s\S]+?)\\\]|\\begin\{(.+?)\}([\s\S]+?)\\end\{\3\}'
    latex_regex = f'{block_dollar}|{inline_dollar}'

    def replace_latex(match):
        tex_block = match.group(0)
        clean_tex_block = tex_block.strip('$')
        context = "md_inline"
        if tex_block.startswith('$$') or tex_block.startswith(r'\[') \
                or tex_block.startswith(r'\begin'):
            context = "md_block"
        return render_tex(clean_tex_block, False, False, context, {'fonts': 'normal'})

    return re.sub(latex_regex, replace_latex, content, flags=re.DOTALL)

def render(token: Token):
    global _heading_scale, _blockquote_open, _has_rendered_blockquote

    match token.type:

        # Headings
        case 'heading_open':
            lvl = int(token.tag[-1])
            if is_kitty:
                map = {
                    1: 's=2',           # 2.0x (s=2)
                    2: 's=2:n=3:d=4',   # 1.5x (s=2 * 3/4)
                    3: 's=2:n=3:d=5',   # 1.2x (s=2 * 3/5)
                    4: 's=1',           # 1.0x (s=1)
                    5: 's=1:n=4:d=5',   # 0.8x (s=1 * 4/5)
                }
                _heading_scale = map.get(lvl, 's=1')
            else:
                return '#' * lvl + ' '

        case 'heading_close':
            _heading_scale = None
            # return '\n\n\033[2m' + '─'*width + '\033[22m\n\n\n'
            return '\n\n'
        
        case 'paragraph_close':
            if _blockquote_open:
                return ('\n' + ('│ ' * _blockquote_open) + '\n')
            return '\n\n'
        
        case 'hr':
            return '\n' + ('─' * width) + '\n\n'
        
        case 'bullet_list_open':
            _list_open.append(['ul', None])
            return ''
        
        case 'ordered_list_open':
            start = int(token.attrGet('start') or 1)
            _list_open.append(['ol', start])
            return ''
        
        case 'bullet_list_close' | 'ordered_list_close':
            _list_open.pop()
            return ''
        
        case 'list_item_open':
            depth = len(_list_open)

            current = _list_open[-1]

            if current[0] == 'ul':
                map = {
                    1: '•',
                    2: '◦',
                    3: '‣',
                }
                bullet = map.get(depth, '•')
            else:
                bullet = f"{current[1]}."
                current[1] += 1

            indent = '  ' * (depth - 1)

            bc = ''
            if _blockquote_open:
                _has_rendered_blockquote.set(True)
                bc = ('│ ' * _blockquote_open)

            return f"{bc}{indent}{bullet} "
        
        case 'inline':
            if token.children:
                return ''.join([render(child) for child in token.children])
            else:
                return render_text(token.content)
            
        case 'text':
            return render_text(token.content)
        
        case 'image':
            if not is_kitty: return '[You need kitty to render images.]'
            path = token.attrGet('src')
            return _image_cache.get(path, f"[Image missing: {path}]\n")

        case 'strong_open':
            return '\033[1m'
        case 'strong_close':
            return '\033[22m'

        case 'em_open':
            return '\033[3m'
        case 'em_close':
            return '\033[23m'
        
        case 's_open':
            return '\033[9m'
        case 's_close':
            return '\033[29m'
        
        case 'blockquote_open':
            _blockquote_open += 1
            return '\033[2m'
        
        case 'blockquote_close':
            _blockquote_open -= 1
            if _blockquote_open == 0:
                return '\033[22m'
        
        case 'link_open':
            href = token.attrGet('href')
            return f'\033[4m\033]8;;{href}\033\\'
        
        case 'link_close':
            return '\033]8;;\033\\\033[24m'
        
        case 'softbreak' | 'hardbreak':
            return '\n'
               
        case 'code_inline':
            output = '\033[48;5;238m'

            if token.children:
                output += ''.join([render(child) for child in token.children])
            else:
                output += render_text(token.content)
            
            return output + '\033[0m'
        
        case 'fence':
            output = '\033[48;5;238m'

            lang = token.info.strip().split()[0] if token.info else None

            cont = token.content.splitlines()
            # cont = [line+'\033[K' for line in cont]
            ##              ^^^^^^ works on some lines, not on others, don't know why :/
            cont = '\n'.join(cont)

            output += render_text(highlight_code(cont, lang))

            return output + '\033[0m'
        
        case 'html_inline':
            if 'type="checkbox"' in token.content:
                if 'checked="checked"' in token.content:
                    return '☑ '
                else:
                    return '☐ '
                
            return token.content
        
        case _:
            return render_text(token.content)


    return render_text(token.content)

def render_text(text):
    if not text: return ''

    if not _has_rendered_blockquote.get(): text = ('│ ' * _blockquote_open) + text

    if _heading_scale:
        return f'\033]66;{_heading_scale};{text}\a'
    else:
        return text