# Clief Notes — kort per leksjon

Ett kort per leksjon i skool.com/cliefnotes sine 7 gratis-klasserom (The Foundation,
Getting Started, Implementation Playbooks, Building Your Stack, The Archive, David's
Corner, THE LEGENDS), hver med et kort, omskrevet sammendrag (ikke ordrett —
betalt/gated kunnskapskilde). Indeks + status:
[../clief-notes-index.md](../clief-notes-index.md). Dekning + hva som mangler:
[../SOURCE-COVERAGE.md](../SOURCE-COVERAGE.md).

Filnavn: `<modul>-<nr>-<slug>.md` (Foundation i rota, resten i undermapper per klasserom).

**Status (2026-09-07):** deep-pass fullført for alle 7 gratis-klasserom (~113 kort).
22 leksjoner har YouTube-video — transkripsjoner hentet med `yt-dlp` og foldet inn som
«## Fra videoen»-seksjoner (omskrevet norsk; rå-transkripsjoner kun i `_transcripts/`,
ikke committet). Gjenstår: kun betalings-låst innhold (The Vault $27, The Drawing
Room $97) — se `SOURCE-COVERAGE.md`.

## Mest relevant for `first system project`

- `3-1`, `3-2`, `4-4` — tre-lags mappe-arkitektur = CLAUDE.md-router + ROOM.md + agents/skills
- `1-3` — 5-delt prompt-mal (identitet/task/context/constraints/output)
- `3-3` — vanlige feil, bl.a. «CLAUDE.md too long» (den skal rute, ikke være brief)
- `2-2`, `2-5`, `2-7` — «AI er 10 % av systemet, 90 % er vanlig ingeniørkunst» → METHOD.md steg 5
