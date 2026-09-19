# 1.1 Starting the Build Process

Kilde: https://www.skool.com/cliefnotes/classroom/2a86a1d1?md=c7a59d0fa0c145549dc9126470b7f82f

**Rammeverk for å avgjøre OM du skal bygge et eget UI, og hvordan avgrense det før du
skriver kode.** «Verktøy-stigen» — du trenger ikke alltid noe custom:
- **Nivå 1: Claude Projects** (claude.ai) — prosjekt-instruksjoner + knowledge-filer, last
  opp `CLAUDE.md` + kontekst-docs + maler. Ingen kode.
- **Nivå 2: Claude Cowork** (i appen) — mer kontroll, fortsatt i Anthropics grensesnitt.
- **Nivå 3: VS Code + Claude Code** — full lesbarhet, Claude jobber i din faktiske workspace.
  «Der de fleste bør lande.»
- **Nivå 4: Custom Front-End** — eget grensesnitt rundt Claude Code, full kontroll, designet
  for din arbeidsflyt. (= `platform/jarvis-local/` hos oss.)
Hvert nivå legger til kompleksitet — gå bare opp når du faktisk trenger det.

**Kategori:** Building Your Stack — Custom UI
