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
$ # Try viewing this README in mkdn!
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
- Supports tables
  - And table alignment.
  - Because tables are a commonly used feature by LLMs. It is essential to include it.


## Screenshots

![image](https://github.com/user-attachments/assets/40e2b8ac-b3b6-42e0-941d-e7004ef5c4d7)
![image](https://github.com/user-attachments/assets/54586b50-92a9-45ea-88ea-cf68ee5625de)
![image](https://github.com/user-attachments/assets/c47a2413-d3f3-4021-b2b8-ea3ef42e1791)
![image](https://github.com/user-attachments/assets/2c6cc043-47e8-48b7-becf-4a8e06e1c262)
![image](https://github.com/user-attachments/assets/2b918f8b-2378-41c3-9f2d-739ade1eb37a)
![image](https://github.com/user-attachments/assets/288bc33f-fa14-47e8-bdb5-b6a952293f78)
![image](https://github.com/user-attachments/assets/cc70bc49-8b69-490b-a713-a67a35de6286)
