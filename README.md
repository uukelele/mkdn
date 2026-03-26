# mkdn
CLI Markdown renderer for the terminal. With more features than the rest ;)

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