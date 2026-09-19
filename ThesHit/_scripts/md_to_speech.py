import re, sys, io

def convert(md: str) -> str:
    lines = md.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    out = []
    in_fence = False
    for ln in lines:
        if re.match(r'^\s*```', ln):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        t = ln
        t = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', t)
        t = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', t)
        t = re.sub(r'`([^`]*)`', r'\1', t)
        t = re.sub(r'\*\*([^*]+)\*\*', r'\1', t)
        t = re.sub(r'\*([^*]+)\*', r'\1', t)
        t = re.sub(r'^\s{0,3}#{1,6}\s*', '', t)
        t = re.sub(r'^\s*>\s?', '', t)
        t = re.sub(r'^\s*[-*+]\s+', '', t)
        t = re.sub(r'^\s*\d+\.\s+', '', t)
        t = t.replace('**', '')
        t = re.sub(r'_{2,}', '', t)
        out.append(t.rstrip())
    text = "\n".join(out)
    text = re.sub(r'(\n\s*){3,}', '\n\n', text)
    return text.strip()

def main():
    src = sys.argv[1]
    dst = sys.argv[2]
    md = io.open(src, encoding="utf-8-sig").read()
    speech = convert(md)
    if len(speech) < 200:
        print(f"SKIP tiny ({len(speech)}): {src}")
        sys.exit(1)
    with io.open(dst, "w", encoding="utf-8") as f:
        f.write(speech)
    print(f"OK {len(speech)}: {dst}")

if __name__ == "__main__":
    main()
