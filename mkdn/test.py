# testing markdown string

from pathlib import Path

data = (Path(__file__).parent / 'test.md').read_text()

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
