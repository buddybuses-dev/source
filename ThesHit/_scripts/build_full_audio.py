"""Concatenate every module's study-guide.mp3 into one complete-course file,
in the same course/module order the site uses."""
import os, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPACES = ["01_the-foundation", "02_the-mastery", "03_the-industry",
          "04_the-vault", "05_the-launchpad", "06_the-frontier"]
FFMPEG = r"C:\Users\Mizgin2\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin\ffmpeg.exe"
if not os.path.exists(FFMPEG):
    FFMPEG = "ffmpeg"

mp3s = []
for sp in SPACES:
    spdir = os.path.join(ROOT, sp)
    for root, dirs, files in sorted(os.walk(spdir)):
        if "_audio" in root:
            continue
        if "study-guide.mp3" in files:
            mp3s.append(os.path.join(root, "study-guide.mp3"))
mp3s.sort()

out_dir = os.path.join(ROOT, "_audio_all")
os.makedirs(out_dir, exist_ok=True)
concat = os.path.join(out_dir, "_concat.txt")
with open(concat, "w", encoding="ascii", errors="replace", newline="\n") as f:
    for m in mp3s:
        f.write("file '" + m.replace("\\", "/") + "'\n")

out = os.path.join(out_dir, "ThesHit__complete-course.mp3")
if os.path.exists(out):
    os.remove(out)
subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y",
                "-f", "concat", "-safe", "0", "-i", concat, "-c", "copy", out], check=True)
size = os.path.getsize(out) / 1e6
ffprobe = FFMPEG.replace("ffmpeg.exe", "ffprobe.exe")
dur = subprocess.run([ffprobe, "-hide_banner", "-loglevel", "error",
                      "-show_entries", "format=duration", "-of", "csv=p=0", out],
                     capture_output=True, text=True).stdout.strip()
try:
    hrs = float(dur) / 3600
except Exception:
    hrs = -1
print(f"{len(mp3s)} tracks -> ThesHit__complete-course.mp3  {size:.0f}MB  {hrs:.1f} hours")
