# testing markdown string

data = "# 🧪 Markdown Test\n\n## ✨ Text Styles\nNormal text  \n**Bold text**  \n*Italic text*  \n***Bold + Italic***  \n~~Strikethrough~~  \n`inline code`  \n> Blockquote level 1  \n>> Blockquote level 2  \n\n---\n\n## 🔗 Links\n- [OpenAI](https://openai.com)\n- [Localhost](http://127.0.0.1:8000/test?param=1&other=2)\n- <https://example.com/raw-url>\n\n---\n\n## 📷 Images\n### Inline image (standard)\n![Test Image](https://picsum.photos/200/100)\n\n### Reference-style image\n![Ref Image][img1]\n\n[img1]: https://picsum.photos/300/120\n\n---\n\n## 📋 Lists\n\n### Unordered\n- Item 1\n  - Nested 1\n  - Nested 2\n    - Deep nested\n- Item 2\n\n### Ordered\n1. First\n2. Second\n   1. Sub-first\n   2. Sub-second\n\n### Task list\n- [x] Done task\n- [ ] Not done\n- [ ] Another task\n\n---\n\n## 📊 Tables\n\n| Name     | Age | Role          | Emoji |\n|----------|-----|---------------|-------|\n| Alice    | 24  | Developer     | 👩‍💻  |\n| Bob      | 30  | DevOps        | ⚙️    |\n| Charlie  | 22  | Designer      | 🎨    |\n\n### Alignment test\n\n| Left      | Center    | Right     |\n|:----------|:---------:|----------:|\n| L1        | C1        | R1        |\n| L2        | C2        | R2        |\n\n---\n\n## 💻 Code Blocks\n\n### Python\n```python\nimport asyncio\n\nasync def main():\n    for i in range(3):\n        print(f\"tick {i}\")\n        await asyncio.sleep(0.5)\n\nasyncio.run(main())\n```\n\n### Bash\n```bash\n#!/usr/bin/env bash\nset -euo pipefail\n\nfor f in *.md; do\n    echo \"Processing $f\"\ndone\n```\n\n### JSON\n```json\n{\n  \"name\": \"test\",\n  \"valid\": true,\n  \"items\": [1, 2, 3],\n  \"nested\": {\n    \"a\": null\n  }\n}\n```\n\n### YAML\n```yaml\nversion: \"3\"\nservices:\n  web:\n    image: nginx\n    ports:\n      - \"8080:80\"\n```\n\n### Rust\n```rust\nfn main() {\n    let nums = vec![1, 2, 3];\n    for n in nums {\n        println!(\"{}\", n);\n    }\n}\n```\n\n### SQL\n```sql\nSELECT users.name, COUNT(posts.id) as post_count\nFROM users\nLEFT JOIN posts ON posts.user_id = users.id\nGROUP BY users.name;\n```\n\n### Diff\n```diff\n- old line\n+ new line\n```\n\n---\n\n## 🧮 Math\nInline: $E = mc^2$\n\nBlock:\n$$\n\\int_0^1 x^2 dx = \\frac{1}{3}\n$$\n\n---\n\n## 📏 Horizontal Rule\n---\n\n---\n\n## 🔤 Escaping\n\\*not italic\\*  \n\\`not code\\`  \n\n---\n\n## 🧱 Nested Madness\n> - Quote list item\n>   1. Ordered inside quote\n>   2. Another item\n>     - Deep bullet\n>\n> ```python\n> print(\"code inside quote\")\n> ```\n\n---\n\n---\n\n## 🧪 Edge Cases\n\nEmpty code block:\n```\n```\n\nVery long line (wrapping test):\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n\nUnicode test:\n你好 🌍 🚀 café naïve résumé\n\n---\n\n## 🧵 Final Section\nEnd of test."

def main(chunked=True):
    import random, time
    
    chunks = []
    i = 0
    while i < len(data):
        size = random.randint(1, 5)
        chunk = data[i:i+size]
        chunks.append(chunk)
        i += size
    
    if chunked:
        for chunk in chunks:
            # time.sleep(random.randint(5, 20) / 100)
            time.sleep(0.1)
            print(chunk, end='', sep='', flush=True)
    else:
        print(data)

    print()

if __name__ == "__main__":
    main(chunked=False)
