import typer
from pathlib import Path
import sys, os
import asyncio

from . import render

app = typer.Typer()

@app.callback(invoke_without_command=True)
def render_md(
    ctx: typer.Context,
    path: Path = typer.Argument(Path('-')),
    debug: bool = False,
):
    if ctx.invoked_subcommand is not None: return

    if not render.is_kitty:
        typer.secho('Warning: You are not using a kitty terminal. Viewing may not be optimized.', fg='yellow')

    if path.name == '-':
        data = sys.stdin.read()
    else:
        data = path.read_text()

    tokens = render.md.parse(data)

    if render.is_kitty: asyncio.run(render.preload_images(tokens))

    buf = []

    for t in tokens:
        if debug:
            print(f"{t.content[:5].ljust(5)} | {t.type}")
            if t.children: [print(c.type) for c in t.children]
        else: buf.append(render.render(t))

    sys.stdout.write(''.join(buf))

    # print(data)

    print()

if __name__ == "__main__":
    app()
