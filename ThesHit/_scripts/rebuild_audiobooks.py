import os, subprocess, sys

ROOT = r"C:\Users\Mizgin2\ThesHit"
FFMPEG = None
for cand in [r"C:\Users\Mizgin2\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin\ffmpeg.exe"]:
    if os.path.exists(cand):
        FFMPEG = cand
        break
if FFMPEG is None:
    FFMPEG = "ffmpeg"

SPACES = [
    ("01_the-foundation", "The Foundation"),
    ("02_the-mastery", "The Mastery"),
    ("03_the-industry", "The Industry"),
    ("04_the-vault", "The Vault"),
    ("05_the-launchpad", "The Launchpad"),
    ("06_the-frontier", "The Frontier"),
]

def safe_name(title):
    import re
    s = re.sub(r'[^A-Za-z0-9]+', '-', title).strip('-')
    return s

def main():
    for space_dir, title in SPACES:
        spdir = os.path.join(ROOT, space_dir)
        mp3s = []
        for root, dirs, files in os.walk(spdir):
            if "_audio" in root:
                continue
            if "study-guide.mp3" in files:
                mp3s.append(os.path.join(root, "study-guide.mp3"))
        mp3s.sort()
        if not mp3s:
            print(f"{space_dir}: no mp3s found, skipping")
            continue
        audio_dir = os.path.join(spdir, "_audio")
        os.makedirs(audio_dir, exist_ok=True)
        concat_path = os.path.join(audio_dir, "_concat.txt")
        with open(concat_path, "w", encoding="ascii", errors="replace", newline="\n") as f:
            for m in mp3s:
                f.write("file '" + m.replace("\\", "/") + "'\n")
        book_name = f"{safe_name(title)}__study-guides.mp3"
        book_path = os.path.join(audio_dir, book_name)
        if os.path.exists(book_path):
            os.remove(book_path)
        r = subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y",
                             "-f", "concat", "-safe", "0", "-i", concat_path,
                             "-c", "copy", book_path], capture_output=True, text=True)
        if os.path.exists(book_path):
            size_mb = os.path.getsize(book_path) / 1e6
            # duration via ffprobe
            ffprobe = FFMPEG.replace("ffmpeg.exe", "ffprobe.exe")
            dur = subprocess.run([ffprobe, "-hide_banner", "-loglevel", "error",
                                   "-show_entries", "format=duration", "-of", "csv=p=0", book_path],
                                  capture_output=True, text=True).stdout.strip()
            try:
                mins = float(dur) / 60
            except Exception:
                mins = -1
            print(f"{space_dir}: {len(mp3s)} tracks -> {book_name}  {size_mb:.1f}MB  {mins:.1f} min")
        else:
            print(f"{space_dir}: FFMPEG FAILED: {r.stderr}")

if __name__ == "__main__":
    main()
