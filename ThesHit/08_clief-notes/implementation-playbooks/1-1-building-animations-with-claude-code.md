# 1.1 Building Animations with Claude Code

Kilde: https://www.skool.com/cliefnotes/classroom/d3907117?md=f7a33a9888604a08a7e48bb876682691

**Hele animasjonsflyten fra script til ferdig video.** Sett opp et to-workspace mappesystem,
skriv en spec, la Claude Code bygge animasjoner fra den, og render til noe du kan redigere i
CapCut. Krever Claude Code + Node.js (se Foundation 4.1). Kjernepoeng: **flyten er ikke ett
verktøy — det er et mappesystem.** Du skriver på engelsk, i et dokument, i en mappe; Claude
Code følger en serie prompts. «Animasjoner som tok en uke for hånd tar nå under en time», og
resultatet trenger ikke ligne forfatterens — alt Claude kan lage i et React-rammeverk kan bli
animasjon.

## Fra videoen (transkribert)

- **Verktøy:** Claude Code + **Remotion** (bibliotek: React/TypeScript-komponenter → video, ramme for ramme) + Node.js + Remotions egne **skills fra GitHub** (`npx`-install, eller la Claude gjøre det). En Remotion-skill er en stor mengde prompts/instruksjoner + underfiler (3D, decode-sjekk, DOM, Tailwind) så Claude ikke må lese alt på én gang — «koden i skillen kjører ikke, den er en forklaring Claude leser».
- **To workspaces (bare mapper):** `script-lab/` (alle long-form + short-form scripts) og `animation-studio/` (workflowen). Fire stadier: **script → spec → build → render.** Claude kan automatisere alle fire, eller du kan gripe inn på ett hvilket som helst.
- **Spec'en er det harde, ikke koden.** Spec = en *kontrakt mellom voiceover-opptaket og animasjonen* som sikrer at scriptets timing bæres over. Den inneholder fire ting: **beat map** (hvert øyeblikk), **visual philosophy**, **hva seeren skal forstå**, **key moments** + **audio sync points**. Den inneholder *ikke* frame-nummer, pikselposisjoner, component props eller kode — «jeg prøvde det, det gjorde animasjonene verre; gi koden litt kreativ frihet».
- **Build:** hver scene er en React-komponent (en «beat» — f.eks. en velocity-gauge på frame ~800). «Gjør gauge'n større» = Claude redigerer variabelen, du trenger ikke røre koden.
- **Render:** be Claude rendre ut → video → CapCut for lyd/voiceover/captions. Kan også bruke OBS-skjermopptak for å slippe codec-feil.
- Jake demonstrerer dette via **remote-access fra telefonen** (melder datamaskinen sin — eget kurs kommer). Han lagde også PowerPointen i videoen med Claude Code i **4 prompts** fra sitt eget materiale.
- Nevner **Model Workspace Protocol** (GitHub-repo) som begrunnelsen bak metoden, og et research-paper om software-historie tilbake til 70-tallet (gratis).

**Relevans for oss:** dette er `rooms/production/` sin pipeline i detalj — `script-lab/` + `animation-studio/` = to rom med `brief→spec→build→render`. Spec-definisjonen (beat map + visual philosophy + key moments + audio sync, *ingen* kode/piksler) er en presis mal for `operations/DISPATCH.md` Mission Brief for medieoppgaver. «Gi koden kreativ frihet» = agent.md Constraints skal ramme inn, ikke mikrostyre (jf. Foundation 3.3 feil 4). Remotion-skill-mønsteret (hoved-skill + underfiler, lastes ved behov) = mal for våre `rooms/*/SKILL.md`.

**Kategori:** Playbooks — Animasjon
