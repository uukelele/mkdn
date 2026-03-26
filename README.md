# mkdn
CLI Markdown renderer for the terminal. With more features than the rest ;)

### Warning

For the best experience using `mkdn`, please use a `kitty` terminal or one that supports `kitty` feature such as the font size protocol and the graphics protocol. This ensures that you can render things like heading/subheadings and images correctly.

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