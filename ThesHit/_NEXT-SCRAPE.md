# Neste scrape-modul (plan only — ingen scrape)

## Anbefaling
1. Lokaliserbar modul med tydelig output-mappe under ThesHit
2. Ingen nettverkskall for denne plan-filen
3. Etter Anders-ja: en modul om gangen

## Status
Clief Notes flyttet til 08_clief-notes. Anything unpacked i 09_.


---

## browser-use stub (2026-09-10)

- **Stub script:** `_scripts/browser_use_stub.py` (dry-run; no browser unless future live + `THESHIT_BROWSER_LIVE=1`; stub refuses live).
- **How-to:** `_scripts/BROWSER-USE.md` â†’ points at `D:\first system project\rooms\production\repos\agent-frameworks\browser-use`.
- **Tickets:** T-009 (wire browser-gated path), T-010 (run/validate later).
- **Ops note:** `D:\first system project\operations\THESHIT-BROWSER-USE-STUB-2026-09-10.md`
- **Policy:** no live scrape / no aider in this stub pass.

---

## OCR stub (2026-09-10)

- **Stub script:** `_scripts/ocr_stub.py` (dry-run; live local OCR only with `THESHIT_OCR_LIVE=1`; never network).
- **How-to:** `_scripts/OCR.md` - PDF/infographic -> text -> study-guide; PATH tip; Wave 4 Tesseract 5.4.0.
- **Pipeline slot:** after browser scrape / PDF drop, before Convert-MdToSpeech / edge-tts.
- **T-009 PDF:** when login-gated scrape delivers a PDF, drop under module folder -> run OCR stub (live) -> study-guide text.
- **Ops note:** `D:\first system project\operations\THESHIT-OCR-WIRE-2026-09-10.md`
- **Install:** `operations/WAVE4-INSTALL-2026-09-10.md` (new shell for PATH).

