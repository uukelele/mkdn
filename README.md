# mkdn
CLI Markdown renderer for the terminal. With more features than the rest ;)

### Warning

For the best experience using `mkdn`, please use a `kitty` terminal or one that supports `kitty` features such as the **font size protocol** and **the graphics protocol**. This ensures that you can render things like *heading/subheadings* and *images* correctly.

## Installation

```
$ gh repo clone uukelele/mkdn
$ cd mkdn
$ pip install -e . -U
```

## Usage

```
$ mkdn /path/to/file.md
$ mkdn README.md
$ cat README.md | mkdn
$ curl 'https://raw.githubusercontent.com/uukelele/mkdn/refs/heads/main/README.md' -s | mkdn
```

## Why Use MKDN?

Here are some features that mkdn has:

- Clickable links
  - Clickable links that work even when the text is different from the link, [like this](https://github.com/uukelele/mkdn).
- Code highlighting
  - Works for all common languages.
  - You can specify in markdown or it will automatically guess the language.
  - Powered by pygments.
- LaTeX rendering
  - Instead of rendering to an image and displaying it, we convert to unicode.
  - Benefits:
    - Faster than rendering to image
    - Works across terminals without needing an image protocol
    - Rendered output can be copied and pasted
    - Respects your terminal font and theme
    - Still entirely readable
- Image rendering
  - You can pass an image, either a file path or URL, and mkdn renders the image using the terminal's image protocol if it has one.
- Font sizing for headings
  - Instead of just changing their colour, headings like `#` and `##` have different font sizes. Just like real markdown.

## Screenshots

![text](https://raw.githubusercontent.com/uukelele/mkdn/refs/heads/main/.github/assets/image.png)

![lists](https://raw.githubusercontent.com/uukelele/mkdn/refs/heads/main/.github/assets/lists.png)