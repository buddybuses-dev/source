# ThesHit ↔ browser-use (STUB)

**Status:** stubs only — no live scrape / no browser launch unless explicitly enabled later.  
**Date:** 2026-09-10  
**Policy:** files first; Learning owns generic parsers; production owns `agent-frameworks`.

## Paths

| Piece | Path |
|-------|------|
| This stub script | `D:\ThesHit\ThesHit\_scripts\browser_use_stub.py` |
| browser-use clone | `D:\first system project\rooms\production\repos\agent-frameworks\browser-use` (git depth 1) |
| ThesHit root | `D:\ThesHit\ThesHit\` |
| Ops summary | `D:\first system project\operations\THESHIT-BROWSER-USE-STUB-2026-09-10.md` |
| Skill pointer | `D:\first system project\rooms\production\skills\theshit-browser-use\SKILL.md` |

## Tickets (intent)

- **T-009** — Wire browser-use into ThesHit for **browser-gated** pages (pages that need a real browser / JS / login, not plain HTTP fetch — historically `the-faction.mn.co`). Stub + docs first; live scrape later.
- **T-010** — Run / validate browser-gated scrape path for ThesHit modules (e.g. `09_anything-about-game`, notes under `08_clief-notes`) once T-009 wiring exists. Still gated on explicit live enable.

## Dry-run (default)

```bat
cd /d D:\ThesHit\ThesHit\_scripts
py browser_use_stub.py --url https://example.com --module 09_anything-about-game
```

Or:

```bat
python browser_use_stub.py --list-steps
```

- Does **not** open a browser.
- Does **not** install deps.
- Exit 0 on success.

## Live flag (NOT implemented in stub)

```bat
set THESHIT_BROWSER_LIVE=1
py browser_use_stub.py --url <TARGET> --module <MODULE>
```

Stub **refuses** to launch a browser even when the flag is set; it only documents the refuse path. Real live scrape requires a later implementation on top of `D:\first system project\rooms\production\repos\agent-frameworks\browser-use`.

## Later: browser-use venv (do not run unless asked)

When ready (separate task):

1. Create venv near production frameworks, e.g. `rooms/production/repos/agent-frameworks/browser-use/.venv` (or project-local).
2. Install browser-use per upstream README in that clone.
3. Point a thin ThesHit wrapper at that venv — keep Learning parsers generic; keep agent-frameworks production-owned.
4. Only then implement live path behind `THESHIT_BROWSER_LIVE=1`.

## Related docs

- `D:\ThesHit\ThesHit\_NEXT-SCRAPE.md` — next scrape queue / stub pointer
- `D:\ThesHit\ThesHit\_STATUS.md` — ThesHit status
- `operations/AGENT-HELPERS-HUNT-2026-09-10.md` — SUVE / browser-use hunt
- `operations/AGENT-CLI-GOAL-PLAN.md` — goal plan

## Then OCR

After a successful scrape (or a local PDF/PNG drop), run **OCR** before speech: `_scripts/ocr_stub.py` / `_scripts/OCR.md` (Tesseract; dry-run default). See `operations/THESHIT-OCR-WIRE-2026-09-10.md`.

