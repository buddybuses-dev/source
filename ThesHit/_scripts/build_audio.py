import os, subprocess, sys, time

ROOT = r"C:\Users\Mizgin2\ThesHit"
VOICE = "en-US-GuyNeural"
SPACES = ["01_the-foundation","02_the-mastery","03_the-industry","04_the-vault","05_the-launchpad","06_the-frontier"]

def find_modules():
    mods = []
    for sp in SPACES:
        spdir = os.path.join(ROOT, sp)
        for root, dirs, files in os.walk(spdir):
            if "_audio" in root:
                continue
            if "study-guide.md" in files:
                mods.append(root)
    return sorted(mods)

def needs_audio(moddir):
    return not (os.path.exists(os.path.join(moddir, "study-guide.speech.txt")) and
                os.path.exists(os.path.join(moddir, "study-guide.mp3")))

def main():
    only_missing = "--all" not in sys.argv
    mods = find_modules()
    targets = [m for m in mods if (needs_audio(m) or not only_missing)]
    print(f"Total modules: {len(mods)}; targets: {len(targets)}")
    report = []
    for i, moddir in enumerate(targets, 1):
        md_path = os.path.join(moddir, "study-guide.md")
        txt_path = os.path.join(moddir, "study-guide.speech.txt")
        mp3_path = os.path.join(moddir, "study-guide.mp3")
        rel = os.path.relpath(moddir, ROOT)

        # 1. md -> speech.txt
        r = subprocess.run(["python", os.path.join(ROOT, "_scripts", "md_to_speech.py"), md_path, txt_path],
                            capture_output=True, text=True)
        if r.returncode != 0:
            report.append(f"[{i}/{len(targets)}] SKIP {rel}: {r.stdout.strip()} {r.stderr.strip()}")
            print(report[-1], flush=True)
            continue

        # 2. speech.txt -> mp3 via edge-tts, with retries
        ok = False
        for attempt in range(3):
            if os.path.exists(mp3_path):
                os.remove(mp3_path)
            proc = subprocess.run(
                ["uvx", "--from", "edge-tts", "edge-tts", "--voice", VOICE,
                 "--file", txt_path, "--write-media", mp3_path],
                capture_output=True, text=True, timeout=180
            )
            if os.path.exists(mp3_path) and os.path.getsize(mp3_path) > 1024:
                ok = True
                break
            time.sleep(5)
        size_mb = os.path.getsize(mp3_path)/1e6 if os.path.exists(mp3_path) else 0
        status = "OK" if ok else "FAIL"
        line = f"[{i}/{len(targets)}] {status} {size_mb:.2f}MB  {rel}"
        report.append(line)
        print(line, flush=True)

    fails = [l for l in report if "FAIL" in l or "SKIP" in l]
    print(f"\nDone. {len(targets)-len(fails)} ok, {len(fails)} failed/skipped.")
    if fails:
        print("Failures:")
        for f in fails:
            print(" ", f)

if __name__ == "__main__":
    main()
