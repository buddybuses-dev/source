# 3.1 The Full Walkthrough (23 Min Video)

Kilde: https://www.skool.com/cliefnotes/classroom/036893d9?md=2b4a8ab7461c4f6d828e21c0eb196a6a

**Kjernen i «The Full Method» — et fungerende mappe-system som forteller Claude hvor den er,
hva den skal gjøre, og hvor arbeidet skal legges. Tre lag. Ren tekst. Ingen kode, ingen
rammeverk, ingen agenter.** Problemet det løser: folk åpner Claude/ChatGPT, skriver noe, får
svar, starter på nytt — brenner tokens på ting som ikke betyr noe, kan ikke redigere det AI
produserer underveis, og hver samtale begynner fra null. De tre lagene: en topp-nivå
identitetsfil (`CLAUDE.md`) som ruter alt, workspace-nivå kontekstfiler, og skills/tools som
plugges inn der de trengs. Video-eksempelet bruker et fiktivt prosjekt med et
community-workspace, et production-workspace og et writing-room — **nesten identisk med
rom-strukturen i `first system project`.** Dekker også navnekonvensjoner og research bak.

## Fra videoen (transkribert — kjerne-gjennomgangen)

- **«Workspace blueprint»:** tre workspaces i eksempelet (community / production / writing room), hvert håndterer *en type arbeid*. Poenget er å hindre at AI-en ser alt: du dirigerer den bare til det du vil.
- **Token-forklaringen:** en token ≈ ¾ ord («hamburger» = ham-bur-ger). Begrepet fra NLP-forskning på 90-tallet, lånt fra lingvistikk, fra gammelengelsk *tācen* (tegn/symbol). Kontekstvinduet er endelig — dumper du alt i én fil, leser en AI som skriver blogg også videoprod-notatene dine og brenner tokens på irrelevant stoff.
- **Markdown:** John Gruber, 2004 — ordspill på «markup»; skriv noe lesbart som ren tekst som *også* kan rendres formatert. Claude skriver alt i markdown allerede (fet skrift, lister). «Ingenting knekker når du redigerer den — det er bare engelsk.»
- **De tre lagene, konkret:**
  - **Lag 1 = kartet / plantegningen** (`CLAUDE.md`): lastes automatisk i enhver mappe. Mappestruktur, navnekonvensjoner, hvor filer går. «Du går inn i et rom, plantegningen henger på veggen.»
  - **Lag 2 = rommene plantegningen sender deg til**: workspace-nivå `CONTEXT.md` — hva er oppgaven, gå hit, les *dette*, hopp over *det*, du trenger kanskje *disse* skills. «Det viktigste mønsteret i hele systemet er en enkel tabell: for denne oppgaven, les disse filene, hopp over de, du trenger kanskje disse skills.»
  - **Lag 3 = selve arbeidsområdet**: hvor filene faktisk legges. `production/` har sin egen pipeline i fire stadier — **brief → spec → build → output** — der ulike docs (tech standards, design system, component library) lastes på ulike stadier.
- **Én Claude *blir* agenten du trenger** når du jobber i et workspace — du slipper å bygge en egen agent per rom. To Claude Code-instanser samtidig: én i writing room, én i production. «Ta scriptet fra writing room og lag en animasjon i production» — den flytter fila; finner den ikke et script, sløser den ikke tokens, den sier bare «vi må skrive et script først».
- **Ingen database:** navnekonvensjoner i `CLAUDE.md` (f.eks. `off-api-guide-draft-v2.md`, `2026-03-launch-week.md`) lar AI-en finne og flytte filer uten SQL/vektor-DB/Postgres. «The folder becomes your app. This is your UI. What simpler UI than a folder?»
- **Skills vs. system:** en skill er bare en prosess noen andre pakket i mapper/markdown (+ evt. Python). Forskjellen mellom «bare skills» og «et system» er at du *plasserer skills inne i MD-tankeprosessen* — ruter dem inn der de trengs (front-end design, web-app-testing, PDF), eller lar Claude slå opp / lage en ny. 15–100 skills kan wires inn per workspace, men lastes bare når de trengs.
- **Dette er tradisjonell function-calling / software-routing** — eksisterer i tiår — men nå på naturlig språk. «This isn't a prompt trick, this isn't crazy infrastructure. It's folders and markdown files with the understanding of advanced software engineering.» Jake skriver et paper om programmeringens regler (transparency, composition) fra 1972 og fremover, med en **5-lags arkitektur** — men de fleste trenger bare de tre.
- **Gjør det til ditt:** writing room → script lab, production → edit bay, community → distribution hub. «Én Claude Code-abonnement, generer 100 'apper' som bare er mapper.» «Neste steg, innen 6 måneder: du snakker bare til mappe-oppsettet ditt.»

**Relevans for oss:** dette ER `first system project` — `CLAUDE.md`-router (lag 1) + `rooms/*/ROOM.md` (lag 2) + `rooms/*/SKILL.md` + `.claude/` MCP (lag 3). «Rute-tabellen er det viktigste mønsteret» → sjekk at `CLAUDE.md` faktisk har en task→hvor→les-tabell (jf. Foundation 3.3 feil 2). `production/` brief→spec→build→output = Playbooks 1.3 + `operations/DISPATCH.md`. Navnekonvensjoner-i-stedet-for-DB = allerede hvordan vi jobber. «Snakk til mappa» = `platform/jarvis-local/` + Remote Control.

**Kategori:** Folder Architecture
