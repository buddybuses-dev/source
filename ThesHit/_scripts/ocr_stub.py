#!/usr/bin/env python3
"""
ThesHit OCR STUB - dry-run by default.

Fits AFTER browser scrape / download of PDF or infographic, BEFORE (or
alongside) Convert-MdToSpeech -> edge-tts. Never hits the network.

Live OCR only when THESHIT_OCR_LIVE=1 and a local file exists:
  - image (png/jpg/jpeg/tif/tiff/webp/bmp/gif) -> tesseract
  - PDF -> pdftoppm (Poppler) render page(s) to temp PNG, then tesseract

Usage:
  py -3.12 ocr_stub.py --path sample.png
  py -3.12 ocr_stub.py --path doc.pdf --lang eng --list-steps
  set THESHIT_OCR_LIVE=1
  py -3.12 ocr_stub.py --path sample.png --out out.txt
  set THESHIT_OCR_LIVE=1
  py -3.12 ocr_stub.py --path doc.pdf --out out.txt
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".webp", ".bmp", ".gif"}
PDF_EXTS = {".pdf"}

# Prefer project helper (SUVE Poppler wrapper), then PATH / known winget layout.
PROJECT_PDFTOPPM_CMD = Path(r"D:\first system project\scripts\pdftoppm.cmd")
KNOWN_PDFTOPPM_EXE = Path(
    r"C:\Users\Mizgin2\AppData\Local\Microsoft\WinGet\Packages"
    r"\oschwartz10612.Poppler_Microsoft.Winget.Source_8wekyb3d8bbwe"
    r"\poppler-25.07.0\Library\bin\pdftoppm.exe"
)

PLANNED_STEPS = [
    "Resolve local image/PDF path under ThesHit (no network)",
    "If PDF: render pages to temp PNG via pdftoppm (Poppler 25.07.0)",
    "Run tesseract on each image -> plain text / markdown snippet",
    "Write OCR text into module study-guide.md (or notes.md) draft",
    "Hand off to Convert-MdToSpeech -> edge-tts (existing pipeline)",
]


def env_live() -> bool:
    return os.environ.get("THESHIT_OCR_LIVE", "0").strip() in (
        "1",
        "true",
        "TRUE",
        "yes",
        "YES",
    )


def which(cmd: str) -> str | None:
    return shutil.which(cmd)


def resolve_pdftoppm() -> str | None:
    """Prefer THESHIT_PDFTOPPM, then project scripts/pdftoppm.cmd, PATH, known install."""
    override = os.environ.get("THESHIT_PDFTOPPM", "").strip()
    if override and Path(override).is_file():
        return override
    if PROJECT_PDFTOPPM_CMD.is_file():
        return str(PROJECT_PDFTOPPM_CMD)
    found = which("pdftoppm")
    if found:
        return found
    if KNOWN_PDFTOPPM_EXE.is_file():
        return str(KNOWN_PDFTOPPM_EXE)
    return None


def resolve_tesseract() -> str | None:
    found = which("tesseract")
    if found:
        return found
    candidate = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
    if candidate.is_file():
        return str(candidate)
    return None


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description=(
            "ThesHit OCR stub (dry-run unless THESHIT_OCR_LIVE=1; never network)"
        ),
    )
    p.add_argument(
        "--path",
        "-p",
        default="",
        help="Local image or PDF path (required for dry-run plan / live OCR)",
    )
    p.add_argument(
        "--lang",
        "-l",
        default="eng",
        help="Tesseract language pack (default: eng)",
    )
    p.add_argument(
        "--out",
        "-o",
        default="",
        help="Optional output text path (live mode; default: <stem>.ocr.txt beside input)",
    )
    p.add_argument(
        "--module",
        default="",
        help="Optional ThesHit module folder name (documented in plan only)",
    )
    p.add_argument(
        "--max-pages",
        type=int,
        default=0,
        help="PDF live: max pages to render (0 = all; smoke often uses 1)",
    )
    p.add_argument(
        "--list-steps",
        action="store_true",
        help="Only print planned pipeline steps and exit",
    )
    return p


def classify(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in IMAGE_EXTS:
        return "image"
    if ext in PDF_EXTS:
        return "pdf"
    return "unknown"


def print_plan(
    path: Path | None,
    kind: str,
    lang: str,
    live: bool,
    module: str,
    max_pages: int,
) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    mode = "LIVE" if live else "DRY-RUN"
    tess = resolve_tesseract() or r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pdftoppm = resolve_pdftoppm()
    print(f"[theshit-ocr-stub] {now}")
    print(f"  mode:      {mode}")
    print(f"  path:      {path if path else '(none)'}")
    print(f"  kind:      {kind}")
    print(f"  lang:      {lang}")
    print(f"  module:    {module or '(n/a)'}")
    print(f"  max_pages: {max_pages or 'all'}")
    print(f"  live_env:  THESHIT_OCR_LIVE={os.environ.get('THESHIT_OCR_LIVE', '0')}")
    print(f"  tesseract: {tess}")
    print(
        f"  pdftoppm:  {pdftoppm or 'NOT FOUND (install Poppler / scripts/pdftoppm.cmd)'}"
    )
    print("  planned steps:")
    for i, step in enumerate(PLANNED_STEPS, 1):
        print(f"    {i}. {step}")
    if path and kind == "image":
        out = path.with_suffix(".ocr.txt")
        print()
        print("  planned command(s):")
        print(f'    tesseract "{path}" "{out.with_suffix("")}" -l {lang} txt')
    elif path and kind == "pdf":
        stem = path.with_suffix("")
        ppm = pdftoppm or "pdftoppm"
        page_range = ""
        if max_pages and max_pages > 0:
            page_range = f" -f 1 -l {max_pages}"
        print()
        print("  planned command(s):")
        print(f'    {ppm} -png{page_range} "{path}" "<temp>/{path.stem}_page"')
        print(
            f'    tesseract "<temp>/{path.stem}_page-1.png" '
            f'"{stem}_page-1" -l {lang} txt'
        )
        print("    ... (repeat per rendered page; concat -> --out or <stem>.ocr.txt)")
    print()
    if live:
        print("Live mode enabled - will attempt local OCR only (no network).")
    else:
        print("Dry-run complete. No OCR executed. No network.")


def run_tesseract_image(image: Path, out_txt: Path, lang: str) -> tuple[int, str]:
    tess = resolve_tesseract()
    if not tess:
        print("ERROR: tesseract not found on PATH.", file=sys.stderr)
        print(
            "Open a NEW shell so PATH includes C:\\Program Files\\Tesseract-OCR",
            file=sys.stderr,
        )
        print(
            "See operations/WAVE4-INSTALL-2026-09-10.md",
            file=sys.stderr,
        )
        return 2, ""
    # tesseract outbase without .txt - it appends .txt
    out_base = out_txt.with_suffix("")
    out_base.parent.mkdir(parents=True, exist_ok=True)
    cmd = [tess, str(image), str(out_base), "-l", lang, "txt"]
    print(f"  exec: {' '.join(cmd)}")
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        print(proc.stdout, end="")
        print(proc.stderr, file=sys.stderr, end="")
        return proc.returncode, ""
    written = Path(str(out_base) + ".txt")
    text = ""
    if written.is_file():
        text = written.read_text(encoding="utf-8", errors="replace")
        print(f"  wrote: {written} ({written.stat().st_size} bytes)")
        preview = text[:400]
        print("  preview:")
        for line in preview.splitlines()[:12]:
            print(f"    {line}")
    return 0, text


def run_live_pdf(path: Path, lang: str, out: str, max_pages: int) -> int:
    pdftoppm = resolve_pdftoppm()
    if not pdftoppm:
        print("PDF live OCR needs render-to-image first.", file=sys.stderr)
        print(
            "pdftoppm (Poppler) not found. Expected scripts/pdftoppm.cmd or PATH.",
            file=sys.stderr,
        )
        print(
            f'  planned: pdftoppm -png "{path}" "<temp>/{path.stem}_page"',
            file=sys.stderr,
        )
        return 3

    with tempfile.TemporaryDirectory(prefix="theshit-ocr-") as tmp:
        tmp_path = Path(tmp)
        prefix = tmp_path / f"{path.stem}_page"
        cmd = [pdftoppm, "-png"]
        if max_pages and max_pages > 0:
            cmd.extend(["-f", "1", "-l", str(max_pages)])
        cmd.extend([str(path), str(prefix)])
        print(f"  exec: {' '.join(cmd)}")
        # On Windows, .cmd needs shell or explicit call via cmd.exe
        if pdftoppm.lower().endswith(".cmd") or pdftoppm.lower().endswith(".bat"):
            proc = subprocess.run(
                ["cmd", "/c", pdftoppm, *cmd[1:]],
                capture_output=True,
                text=True,
            )
        else:
            proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            print(proc.stdout, end="")
            print(proc.stderr, file=sys.stderr, end="")
            return proc.returncode

        pages = sorted(tmp_path.glob(f"{path.stem}_page*.png"))
        if not pages:
            print("ERROR: pdftoppm produced no PNGs", file=sys.stderr)
            return 3

        chunks: list[str] = []
        rc = 0
        for page in pages:
            page_out = tmp_path / f"{page.stem}.ocr.txt"
            page_rc, text = run_tesseract_image(page, page_out, lang)
            if page_rc != 0:
                rc = page_rc
            else:
                chunks.append(text)

        if rc != 0:
            return rc

        combined = "\n\n".join(c.strip() for c in chunks if c.strip()) + "\n"
        out_txt = Path(out) if out else path.with_suffix(".ocr.txt")
        out_txt.parent.mkdir(parents=True, exist_ok=True)
        out_txt.write_text(combined, encoding="utf-8")
        print(f"  wrote combined: {out_txt} ({out_txt.stat().st_size} bytes)")
        preview = combined[:400]
        print("  combined preview:")
        for line in preview.splitlines()[:12]:
            print(f"    {line}")
        return 0


def run_live(path: Path, lang: str, out: str, max_pages: int) -> int:
    kind = classify(path)
    if kind == "unknown":
        print(f"ERROR: unsupported extension: {path.suffix}", file=sys.stderr)
        return 2
    if not path.is_file():
        print(f"ERROR: file does not exist: {path}", file=sys.stderr)
        return 2

    if kind == "image":
        out_txt = Path(out) if out else path.with_suffix(".ocr.txt")
        rc, _ = run_tesseract_image(path, out_txt, lang)
        return rc

    return run_live_pdf(path, lang, out, max_pages)


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    live = env_live()

    if args.list_steps:
        for i, step in enumerate(PLANNED_STEPS, 1):
            print(f"{i}. {step}")
        return 0

    path: Path | None = Path(args.path) if args.path else None
    kind = classify(path) if path else "n/a"
    print_plan(path, kind, args.lang, live, args.module, args.max_pages)

    if not live:
        return 0

    if not path:
        print("ERROR: --path required for live OCR", file=sys.stderr)
        return 2
    return run_live(path, args.lang, args.out, args.max_pages)


if __name__ == "__main__":
    sys.exit(main())
