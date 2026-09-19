# ThesHit — build status (updated 2026-09-04)

Mirror of https://the-faction.mn.co — one folder per space/course/module,
each with study-guide.md + exam.md + notes.md, plus study-guide.speech.txt +
study-guide.mp3 (voice en-US-GuyNeural via `uvx edge-tts`), and a per-space
`_audio/<Space>__study-guides.mp3` audiobook.

## DONE (real scraped content + audio)
- 01_the-foundation .......... 13/13 layers  ✅ full + audiobook
- 03_the-industry / vertical-1_education ... modules 01–03 ✅ (04–07 stub)
- 04_the-vault / course-1_security-foundations ... 7/7 ✅
- 04_the-vault / course-2_compliance-and-regulation ... 7/7 ✅
- 04_the-vault / course-3_ai-code-auditing ... module 01 ✅ (02–07 stub)
- 05_the-launchpad / course-1_freelancing-and-clients ... 7/7 ✅
- 05_the-launchpad / course-2_idea-validation ... modules 01–06 ✅ (07 stub)
- 06_the-frontier / course-1_agent-orchestration ... 7/7 ✅
- 06_the-frontier / course-2_prompt-engineering ... modules 01–05 ✅ (06–07 stub)

## REMAINING — 90 modules are still stubs (need scrape from site, then audio)
- 02_the-mastery ................................... 49  (all 7 courses × 7)
- 03_the-industry vertical-1 m04–m07 ............... 4
- 03_the-industry vertical-2_construction .......... 7
- 03_the-industry vertical-3_healthcare ............ 7
- 04_the-vault course-3 m02–m07 ................... 6
- 05_the-launchpad course-2 m07 ................... 1
- 05_the-launchpad course-3_positioning-and-offers . 7
- 06_the-frontier course-2 m06–m07 ................ 2
- 06_the-frontier course-3_context-engineering ..... 7
  TOTAL ......................................... 90

## PIPELINE (reusable)
1. Browser (Claude-in-Chrome ext / browser-use stub) -> open https://the-faction.mn.co/posts/<slug>
   for each module study guide -> save verbatim text as study-guide.md
   (or download PDF/infographic into the module folder when text is image-only)
2. OCR (Tesseract stub) - if artifact is PDF/PNG/infographic -> text -> draft study-guide.md
   `_scripts/ocr_stub.py` + `_scripts/OCR.md` (dry-run default; `THESHIT_OCR_LIVE=1` for local OCR)
3. Convert-MdToSpeech (strip markdown) -> study-guide.speech.txt
4. `uvx edge-tts --voice en-US-GuyNeural --file study-guide.speech.txt --write-media study-guide.mp3`
5. Per space: ffmpeg concat all study-guide.mp3 (sorted) -> _audio/<Space>__study-guides.mp3

## BLOCKER
Claude browser extension not connected this session — cannot reach the
login-gated Mighty Networks site to scrape the 90 study guides.
## ADDED 2026-09-10
- OCR wire ............... `_scripts/ocr_stub.py` + `_scripts/OCR.md` (Tesseract 5.4.0; after scrape, before/alongside speech). Ops: `operations/THESHIT-OCR-WIRE-2026-09-10.md`
- 08_clief-notes/ ........ full Clief Notes archive moved from first system project `rooms/learning/clief-notes` (SUVE). Pointer left at old path.
