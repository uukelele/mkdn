# 🧪 Markdown Test

## ✨ Text Styles
Normal text  
**Bold text**  
*Italic text*  
***Bold + Italic***  
~~Strikethrough~~  
`inline code`  
> Blockquote level 1  
>> Blockquote level 2  

---

## 🔗 Links
- [OpenAI](https://openai.com)
- [Localhost](http://127.0.0.1:8000/test?param=1&other=2)
- <https://example.com/raw-url>

---

## 📷 Images
### Inline image (standard)
![Test Image](https://picsum.photos/200/100)

### Reference-style image
![Ref Image][img1]

[img1]: https://picsum.photos/300/120

---

## 📋 Lists

### Unordered
- Item 1
  - Nested 1
  - Nested 2
    - Deep nested
- Item 2

### Ordered
1. First
2. Second
   1. Sub-first
   2. Sub-second

### Task list
- [x] Done task
- [ ] Not done
- [ ] Another task

---

## 📊 Tables

| Name     | Age | Role          | Emoji |
|----------|-----|---------------|-------|
| Alice    | 24  | Developer     | 👩‍💻  |
| Bob      | 30  | DevOps        | ⚙️    |
| Charlie  | 22  | Designer      | 🎨    |

### Alignment test

| Left      | Center    | Right     |
|:----------|:---------:|----------:|
| L1        | C1        | R1        |
| L2        | C2        | R2        |

---

## 💻 Code Blocks

### Python
```python
import asyncio

async def main():
    for i in range(3):
        print(f"tick {i}")
        await asyncio.sleep(0.5)

asyncio.run(main())
```

### Bash
```bash
#!/usr/bin/env bash
set -euo pipefail

for f in *.md; do
    echo "Processing $f"
done
```

### JSON
```json
{
  "name": "test",
  "valid": true,
  "items": [1, 2, 3],
  "nested": {
    "a": null
  }
}
```

### YAML
```yaml
version: "3"
services:
  web:
    image: nginx
    ports:
      - "8080:80"
```

### Rust
```rust
fn main() {
    let nums = vec![1, 2, 3];
    for n in nums {
        println!("{}", n);
    }
}
```

### SQL
```sql
SELECT users.name, COUNT(posts.id) as post_count
FROM users
LEFT JOIN posts ON posts.user_id = users.id
GROUP BY users.name;
```

### Diff
```diff
- old line
+ new line
```

---

## 🧮 Math
Inline: $E = mc^2$

Block:
$$
\int_0^1 x^2 dx = \frac{1}{3}
$$

---

## 📏 Horizontal Rule
---

---

## 🔤 Escaping
\*not italic\*  
\`not code\`  

---

## 🧱 Nested Madness
> - Quote list item
>   1. Ordered inside quote
>   2. Another item
>     - Deep bullet
>
> ```python
> print("code inside quote")
> ```

---

---

## 🧪 Edge Cases

Empty code block:
```
```

Very long line (wrapping test):
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

Unicode test:
你好 🌍 🚀 café naïve résumé

---

## 🧵 Final Section
End of test.