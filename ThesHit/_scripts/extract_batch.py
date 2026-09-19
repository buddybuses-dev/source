import json, sys, io

def main():
    json_path = sys.argv[1]
    indices = [int(x) for x in sys.argv[3].split(",")] if len(sys.argv) > 3 else None
    out_dir = r"C:\Users\Mizgin2\ThesHit\_scripts\raw"
    data = json.load(io.open(json_path, encoding="utf-8"))
    texts = [item["text"] for item in data if item.get("type") == "text" and item["text"].startswith("[get_page_text]")]
    if indices is None:
        start_index = int(sys.argv[2])
        indices = list(range(start_index, start_index + len(texts)))
    assert len(indices) == len(texts), f"Got {len(texts)} get_page_text results but {len(indices)} indices given"
    results = []
    for idx, t in zip(indices, texts):
        body = t[len("[get_page_text] "):]
        after_dashes = body.split("---", 1)[-1].strip()
        ok = not after_dashes.startswith("Loading...") and len(body) > 500
        fname = f"{idx:03d}.txt"
        if ok:
            with io.open(f"{out_dir}\\{fname}", "w", encoding="utf-8") as f:
                f.write(body)
            results.append((idx, fname, "OK", len(body)))
        else:
            results.append((idx, fname, "FAIL-short", len(body)))
    for r in results:
        print(r)

if __name__ == "__main__":
    main()
