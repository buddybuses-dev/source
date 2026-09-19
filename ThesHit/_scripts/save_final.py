import json, sys, io, re, os

ROOT = r"C:\Users\Mizgin2\ThesHit"

def main():
    json_path = sys.argv[1]
    data = json.load(io.open(json_path, encoding="utf-8"))
    texts = [item["text"] for item in data if item.get("type") == "text" and item["text"].startswith("Title:")]
    assert len(texts) == 1, f"expected 1 get_page_text blob, got {len(texts)}"
    body = texts[0].split("---\n", 1)[-1]

    manifest = json.load(io.open(os.path.join(ROOT, "_scripts", "manifest.json"), encoding="utf-8"))

    parts = re.split(r"@@@MODULE (\d+)@@@\n", body)
    # parts[0] is empty/junk before first marker, then alternating idx, content
    results = []
    for i in range(1, len(parts), 2):
        idx = int(parts[i])
        content = parts[i+1]
        # trim trailing content that isn't ours (shouldn't happen, but strip trailing whitespace)
        content = content.rstrip() + "\n"
        entry = manifest[idx]
        out_dir = os.path.join(ROOT, entry["dir"].replace("/", os.sep))
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "study-guide.md")
        with io.open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        results.append((idx, entry["dir"], len(content)))
    for r in results:
        print(r)
    print(f"TOTAL SAVED: {len(results)}")

if __name__ == "__main__":
    main()
