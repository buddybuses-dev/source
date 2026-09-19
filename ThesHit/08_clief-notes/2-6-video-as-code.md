# 2.6 Video as Code: My AI Animation Stack

Kilde: https://www.skool.com/cliefnotes/classroom/036893d9?md=3a82e3222c2c4cbc9d07c6f9f6d4265a

**Én person erstatter en ukes animasjonsarbeid med under en time — ved å behandle video som
kode.** Poenget er ikke polerte resultater, det er prosessen: infrastruktur (dokumentasjon,
spesifikasjoner, komponent-bibliotek) — software engineering brukt på et kreativt problem.
De fire verktøyene: (1) **Claude Code** (eller en annen kode-agent — Codex, Aider), (2) en
**kodeeditor** (VS Code, Cursor), (3) **Remotion** (React-komponenter → video, ramme for
ramme), (4) en **videoeditor** (CapCut). Samme mønster som resten av kurset: struktur og
gjenbrukbare byggeklosser rundt et generativt verktøy. Relevant for `production`-rommet
(video-pipelines) og `automation`-rommet.

## Fra videoen (transkribert)

- **Det harde arbeidet er ikke AI-en eller koden — det er spec'en.** En markdown-fil som presist beskriver: struktur, hva som skjer i hver scene, timing, hvilke visuelle elementer, når de dukker opp, hva som skal fremheves, hva som holdes i bakgrunnen. David Ogilvy: *«Give me the freedom of a tight brief.»* En løs spec = Claude tar flere tolkningsvalg / hallusinerer mer. En stram spec = du dirigerer på hver beat. **Dette er der mesteparten av den kreative tenkningen skal skje.**
- **Byggefasen:** agenten leser spec'en + dokumentasjonen den peker på (style guide: visuelt språk, fargepaletter, animasjons-timing) + et **component registry** (gjenbrukbare biter fra tidligere videoer: tekstanimasjoner, bakgrunner, overganger, datavisualiseringer). Hver scene er en React-komponent; Remotion rendrer dem ramme for ramme. Johnny Burger (Remotion-skaper): «en video er en funksjon av bilder over tid — fortell React hvordan frame 47 ser ut, gjenta for hver frame». Alt som virker i en nettleser (CSS, SVG, canvas, JS-biblioteker) kan være i animasjonen.
- **Iterasjonsløkka:** gi Claude spec'en → pek på dokumentasjonen → si hvilken scene → den skriver kode → forhåndsvis i Remotion Studio → beskriv på naturlig språk hva som må endres → gjenta til scenen matcher. Eksporter (Remotion eller OBS) → CapCut for voiceover, klipping, musikk. «Å nudge en overgang til å lande på et ord er raskere i en videoeditor enn å beskrive det i spec'en.»
- **Separations of concerns:** spec adskilt fra implementasjon, komponenter gjenbrukbare, style guide koder beslutninger så du slipper å ta dem hver gang. «Break complex things into smaller pieces that can be understood and changed independently.»
- **Historisk mønster:** GarageBand (2004, demokratiserte musikk — Steve Lacy lagde Kendrick-spor på en cracked iPhone), Canva (Melanie Perkins avvist av 100+ investorer, nå 200M brukere/mnd). Alltid en rotete «ransom note»-periode først (desktop publishing: 15 fonter på én side), så hever gulvet seg.
- **Constraints muliggjør kreativitet** (omvendt-U mellom begrensning og kreativ output): Dr. Seuss skrev *Green Eggs and Ham* på et $50-veddemål om 50 ord (200M solgte); Spielberg skjulte haien i *Jaws* fordi mekanikken ikke virket (haien vises først etter 80 min). Spec + style guide + component registry er ikke begrensninger man jobber rundt — de er grensene som gjør output bedre. **Nå er det Claude som er den begrensede parten** — den kan reglene og fokuserer på utførelse.

**Relevans for oss:** dette er `rooms/production/` sin script→spec→build→render-pipeline i detalj (jf. Playbooks 1.3). «Spec'en er der den kreative tenkningen bor» + «tight brief» = `operations/DISPATCH.md` Mission Brief + `/plan`. Component registry = et gjenbruks-katalog for produksjonsrommet. «Constraints enable creativity» + «Claude er den begrensede parten» = hele poenget med `agent.md` Constraints-feltet og `CLAUDE.md`-reglene.

**Kategori:** Abstraction Series
