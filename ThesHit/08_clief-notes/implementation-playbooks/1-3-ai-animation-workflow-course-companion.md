# 1.3 AI Animation Workflow: Course Companion

Kilde: https://www.skool.com/cliefnotes/classroom/d3907117?md=9c4b772439eb435485cab0cb1aca6e95

**Én referanseside for hele animasjonsflyten.** De **fire stegene**:
`Script` (hva som skal sies — idéer/notater → ren tekst) →
`Spec` (kontrakt mellom stemme og visuelt — markdown med beats, filosofi, nøkkelmomenter) →
`Build` (Claude skriver koden — React-komponenter, scener, animasjonsfiler) →
`Render` (Remotion lager video — ferdig MP4/MOV).

Mappestruktur: `Animation Studio/` med `CLAUDE.md` (kontekstfil), `scripts/` (long-form/
short-form), `specs/[navn].md`, `projects/[navn]/src/{compositions,components,scenes}` +
`remotion.config.ts`, `output/`. Nesten identisk mønster med vår `production`-rom-tilnærming.

**Kategori:** Playbooks — Animasjon
