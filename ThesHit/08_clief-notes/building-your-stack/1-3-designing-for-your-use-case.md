# 1.3 Designing for Your Use Case

Kilde: https://www.skool.com/cliefnotes/classroom/2a86a1d1?md=fdb1ae130aec49d28eba9142efb5762f

**Innsiden av en ekte build-økt: hvordan Claude Code jobber seg gjennom en PRD, bruker plan
mode og sub-agents, og noen ganger tar bedre valg enn det du ba om.** Mindre forelesning, mer
livestream — du ser forfatteren jobbe. Oppsett: jobber inne i «Animation Studio»-workspace,
front-end-mappe opprettet, PRD droppet inn. **PRD-en beskriver:** hva som bygges (en
kontrollflate for arbeidsflyten), hvilke repoer det hentes fra, hva som skal kuttes fra dem,
panel-layout (workflow map, file editor, Claude chat), faser og steg. Claude Code leser alt
dette. «NO API FEES.» = malen for `platform/jarvis-local/`.

## Fra videoen (transkribert — «live stream»-stil)

- **Målet, formulert presist:** «det abstrakte målet er ikke et penere Claude-front-end. Det er en **control surface** der jeg flytende kan bytte mellom at *jeg kjører* og at *Claude kjører*.» Noen ganger vil han redigere hver enkelt fil; noen ganger automatisere alt — men stole på at det automatiseres slik han vil.
- **Repoene nevnt:** Claude CLI, Claude Code Web, opcode — «de gjør lignende ting, men ikke alt jeg ville ha; jeg vibet ikke med front-endene deres». Plan: klon / hent selektivt, strip vekk det han ikke liker, gjør det modulært senere. «Don't reinvent the wheel — make a better wheel, make it yours.»
- **Ønsket: en workflow-map (node/web-map)** til venstre der du kan *redigere mappene* visuelt (script-lab → animation-studio → spec → build → render), file editor i midten, Claude Code til høyre med flere kollapsbare chats. Bygget på Claude Codes infrastruktur — «ikke en separat app».
- **Pipeline-definisjoner som JavaScript** (kunne like gjerne vært flat markdown: «for å skrive et script, gå til denne mappa»). «Alle programmeringsspråk er omtrent like: en *definisjon* + en *beskrivelse*, paret med andre — samme som en mappe med en `CONTEXT.md` og filer inni.»
- **Stateless vs. stateful prompt:** en prompt sendt i en chat er *stateless* — borte når samtalen slutter. En markdown-fil gjør prompten *permanent* — kan refereres, redigeres, restartes raskt. Markdown tar færre tokens enn PDF/doc og modellene er godt trent på det; last opp til Google Docs og formateringen rendrer.
- **Plan mode vs. execution mode:** Claude velger selv, men du kan tvinge det (`/model` bytter modell). Med 4.6/default lager den **sub-agents** for å spare tokens — sender en agent for å studere workspacet, en annen for å hente ting; hoved-Claude er «manager». Kjørte `bash`/`find`/web-fetch — og hentet **individuelle filer fra repoene i stedet for å klone hele** (bedre enn det Jake ba om).
- **Hvorfor kjøre i selve workspacet, ikke en separat mappe:** så den kan hente kontekst fra den faktiske arbeidsflyten — «men bare når jeg ber om det, ikke 'les alt her'».

**Relevans for oss:** «control surface — bytte mellom jeg kjører og Claude kjører» er en perfekt formulering for `platform/jarvis-local/` sitt formål og for CLAUDE.md-permission-modellen (3-tier). «Stateless prompt vs. permanent markdown-fil» = hele begrunnelsen for `rooms/*/ROOM.md`, `agents/*/agent.md`, `.claude/commands/`. «Sub-agents for å spare tokens, hoved-Claude som manager» = `agents/coordinator-agent/` + `operations/DISPATCH.md`. «Kjør i workspacet, hent kontekst bare på forespørsel» = ICM kontekst-scoping (Foundation 3.3 feil 4).

**Kategori:** Building Your Stack — Custom UI
