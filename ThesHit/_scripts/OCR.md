# ThesHit — OCR (Tesseract stub)

**Status:** stub + docs — dry-run by default; live local OCR behind `THESHIT_OCR_LIVE=1`  
**Date:** 2026-09-10  
**Policy:** no network; files first. OCR sits **after** browser scrape / PDF download, **before or alongside** speech (Convert-MdToSpeech → edge-tts).

## Where it fits (pipeline)

1. **Browser scrape** (browser-use stub / Claude-in-Chrome) → save PDF, infographic PNG, or verbatim `study-guide.md`
2. **OCR (this step)** — if the artifact is a scanned PDF / image / infographic → extract text → draft `study-guide.md` / `notes.md`
3. **Speech** — Convert-MdToSpeech → `study-guide.speech.txt` → `uvx edge-tts` → mp3
4. **Audiobook** — ffmpeg concat per space

Clear place for **T-009 PDF** when the login-gated scrape lane delivers a PDF: drop the file under the module folder, then run this stub (live) to get text for the study-guide.

## Paths

| Piece | Path |
|-------|------|
| This stub | `D:\ThesHit\ThesHit\_scripts\ocr_stub.py` |
| This how-to | `D:\ThesHit\ThesHit\_scripts\OCR.md` |
| browser-use (upstream step) | `D:\ThesHit\ThesHit\_scripts\BROWSER-USE.md` |
| Wave 4 install (Tesseract 5.4.0) | `D:\first system project\operations\WAVE4-INSTALL-2026-09-10.md` |
| Ops summary | `D:\first system project\operations\THESHIT-OCR-WIRE-2026-09-10.md` |
| Skill pointer | `D:\first system project\rooms\production\skills\theshit-ocr\SKILL.md` |
| Related skill | `rooms/production/skills/ocr-pipeline` (generic Learning/Tools OCR) |
| Poppler helper | `D:\first system project\scripts\pdftoppm.cmd` |

## PATH tip (Wave 4)

Tesseract lands at `C:\Program Files\Tesseract-OCR\tesseract.exe`.  
**Open a NEW shell** after install so PATH picks it up (see `operations/WAVE4-INSTALL-2026-09-10.md`).

```bat
tesseract --version
```

Expect `tesseract v5.4.0...`.

### Poppler / pdftoppm (SUVE 2026-09-10)

- **Available:** Poppler **25.07.0** via winget (`pdftoppm version 25.07.0`).
- **Helper:** `D:\first system project\scripts\pdftoppm.cmd` (preferred by stub).
- **Also on PATH:** WinGet package `...\poppler-25.07.0\Library\bin\pdftoppm.exe`.
- Stub resolution order: `THESHIT_PDFTOPPM` → project `scripts/pdftoppm.cmd` → PATH → known WinGet path.
- Live PDF flow: `pdftoppm -png` → temp PNG(s) → tesseract → combined `--out` / `<stem>.ocr.txt`.

```bat
pdftoppm -v
"D:\first system project\scripts\pdftoppm.cmd" -v
```

## Dry-run (default)

```bat
cd /d D:\ThesHit\ThesHit\_scripts
py -3.12 ocr_stub.py --help
py -3.12 ocr_stub.py --path D:\ThesHit\ThesHit\some-module\guide.png --module 09_anything-about-game
py -3.12 ocr_stub.py --path D:\ThesHit\ThesHit\_scripts\fixtures\ocr_smoke.pdf --max-pages 1
py -3.12 ocr_stub.py --list-steps
```

- Does **not** call the network.
- Does **not** run tesseract unless live flag is set.
- Exit 0 on success.
- PDF dry-run prints planned `pdftoppm` → temp PNG → `tesseract` steps.

## Live local OCR

```bat
cd /d D:\ThesHit\ThesHit\_scripts
set THESHIT_OCR_LIVE=1
py -3.12 ocr_stub.py --path C:\path\to\local.png --lang eng
set THESHIT_OCR_LIVE=1
py -3.12 ocr_stub.py --path C:\path\to\local.pdf --lang eng --max-pages 1 --out out.ocr.txt
```

- Image → `tesseract <img> <outbase> -l eng txt` → `<stem>.ocr.txt` (or `--out`)
- PDF → `pdftoppm` (prefer `scripts/pdftoppm.cmd`) renders first/all pages to **temp** PNGs → tesseract per page → combined text at `--out` or `<stem>.ocr.txt`
- Never downloads; file must already exist on disk

## Smoke fixture

Tiny 1-page PDF (expected OCR string `THESHIT OCR SMOKE OK`):

`D:\ThesHit\ThesHit\_scripts\fixtures\ocr_smoke.pdf`

## Related

- `_scripts/BROWSER-USE.md` — scrape first, **then OCR**
- `_STATUS.md` — PIPELINE step for OCR
- `_NEXT-SCRAPE.md` — OCR pointer for T-009 PDF arrival
- `operations/WAVE4-INSTALL-2026-09-10.md` — Tesseract 5.4.0 + PATH
