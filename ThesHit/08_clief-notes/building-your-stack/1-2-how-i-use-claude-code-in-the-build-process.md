# 1.2 How I Use Claude Code in the Build Process

Kilde: https://www.skool.com/cliefnotes/classroom/2a86a1d1?md=789abc7e897742f7807ebee7d066e385

**Research- og planleggingsfasen for et custom build: finne eksisterende repoer, lage en PRD,
sette opp workspace så Claude har kontekst fra start.** Bakgrunn: «David» ville ha et
front-end-UI for å styre og overvåke Claude — naturlig neste steg når man er komfortabel med
Claude Code i VS Code. **API-kostnadsproblemet:** Claude Code via abonnement koster ikke ekstra
per melding, men et custom front-end via Anthropic-API-et koster per token → poenget er å bygge
det UTEN å brenne API-kreditter (dvs. drive Claude Code, ikke rå-API-et). Dette er nøyaktig
prinsippet bak `platform/jarvis-local/`.

## Fra videoen (transkribert)

- **Davids spørsmål:** han bygde egne animasjoner etter Jakes video, men ville ha et front-end for å *overvåke/observere* hvordan agentene jobber — noe bedre enn bare VS Code.
- **Løsning: ikke reinvent hjulet.** Jake fikk Claude til å grave frem open-source-repoer som allerede styrer Claude Code via et nedlastbart front-end (ett sporer også forbruk; ett kjører via mobil). «La oss se på hver repo, ta det vi liker, kutt resten.»
- **Jobb baklengs:** vanligvis gir Jake Claude en markdown-fil med filstrukturen *før* bruk. Her gir han i stedet sin egen struktur (animasjons-workflow: scripts → animasjoner) og spør «hva om vi lager et front-end rundt akkurat *dette* mappesystemet?».
- **Ikke bygg i desktop — lag en PRD.** «Make a PRD markdown of this **for Claude Code** (den vil lese den) som beskriver hva vi prøver å gjøre og bryter det i steg fra tidlig fase til sen fase» — så det ikke bygges alt på én gang. PRD-en beskriver stacks, integrasjoner, targeting. Du leser og redigerer den; eller **mater den inn i en annen Claude som fungerer som auditor** og skriver den om. Så: drop PRD-en i workspace, ny Claude Code-instans, «les PRD-en for front-end».

**Relevans for oss:** «lag en PRD for Claude Code, ikke for meg» + «bruk en annen Claude som auditor på PRD-en» = presist mønster for `operations/DISPATCH.md` + `/plan` + `/redteam`. «Ikke reinvent hjulet — hent fra open-source, kutt det du ikke liker» = `rooms/learning/tools.md` sin holdning (OpenCode framfor claw-code). Front-end-som-driver-Claude-Code-ikke-API = `platform/jarvis-local/server.py`.

**Kategori:** Building Your Stack — Custom UI
