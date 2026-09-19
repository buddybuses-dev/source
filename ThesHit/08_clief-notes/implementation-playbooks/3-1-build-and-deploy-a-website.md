# 3.1 Build and Deploy a Website

Kilde: https://www.skool.com/cliefnotes/classroom/d3907117?md=f9b95ae2f7d9448787d27a3639ed9ef3

**Full gjennomgang (29:22 video): bygg og deploy en ekte nettside med Claude Code, gratis på GitHub Pages — fra et eksisterende nettsted som referanse til en live URL. Totalt <10 prompts.** Leksjon 3.2 og 3.3 går dypere på delene som går fort her.

**Prosessen i korte trekk:**
1. Analyser referanse-nettstedet i Claude chat (ikke Code).
2. Generer et markdown-briefing-dokument for Claude Code.
3. Sett opp en workspace-mappe på desktop.
4. Skriv første prompt med struktur, scope og «alignment»-spørsmål.
5. Svar på Claudes spørsmål, be om en PRD.
6. La Claude Code bygge v1.
7. Gjennomgå, gi design-tilbakemelding.
8. Push til GitHub, deploy på Pages.
9. Fiks pathing/deploy-problemer.
10. Bekreft at live-siten virker.

Nøkkelpoeng fra videoen: bygget starter i nettleseren, ikke terminalen — Claude chat utforsker referanse-nettstedet, klikker gjennom sider, og trekker ut struktur/stil før én linje kode skrives.

## Fra videoen (transkribert)

- **Steg 1 — forstå referansen i Claude *chat* (ikke Code):** lim inn URL-en, «klikk gjennom undersidene». Hvis den sliter: ta screenshot av hver side. Så: «gi meg en markdown-fil som beskriver strukturen og byggingen — **for Claude Code å lese, ikke for meg**». Den trakk ut slugs, form-IDer, content-typer, brand voice, visual identity, tech stack (Beehiiv), og la til uoppfordret «notes for rebuilding» («content is the product», «subscribe CTA = primary conversion»).
- **Steg 2 — workspace-mappe på desktop**, dra markdown-fila inn, åpne i Claude Code / VS Code.
- **Steg 3 — første prompt (der token-sparingen skjer):** be om en mappestruktur med **én `CLAUDE.md` for routing** + små markdown-filer per mappe (brand voice osv.); si eksplisitt «**deploy på GitHub Pages**» *nå* så Claude ikke sløser tokens på deployment-vurderinger; si «**det trenger ikke bygges ferdig i dag** — ingen brukerkontoer, manuelle submissions er OK, vi lager et template for senere»; avslutt med «**still meg tre spørsmål**» for å aligne før noe skrives.
- **Steg 4 — PRD:** «bruk **UI/UX Pro-skillen**, lag en PRD-fil» (skillen kjører Python-scripts internt for å spare tokens). Fortsatt ingen kode implementert — «få skjelettene rette, så sier jeg 'rip it'». Totalt ~4 prompts inn, men mye tenkning per prompt.
- **Auto-minne:** Claude skrev en `memory-index` til prosjekt-fila i den *installerte* Claude (`~/.claude/projects/...`) — «folk bygger enorme YAML/Obsidian-minnesystemer; Anthropic gjør det allerede automatisk». Bygget ble Astro/TypeScript.
- **Deploy på GitHub Pages:** enkel rute — repo → last opp `index.html` → Settings → Pages → «Deploy from branch: main» → få en live-lenke. Kompleks rute (Astro) — Claude installerte **GitHub CLI**, fikk device-login, opprettet filer inkl. **`.gitignore`** («så viktig — `.env` med API-nøkler MÅ stå her, ellers pusher `git` hele mappa; du kan også legge `*.md` her hvis brand voice ikke skal ut; en offentlig repo gjør det lettere å se hvordan siten er bygd = sikkerhetshensyn»). Første deploy feilet på CSS-*paths* → «hey, file talking [paths] er feil» → Claude fikset og pushet på nytt. **Poenget med Git:** rediger lokalt → test → push → lenka er allerede koblet; ingen re-upload, ingen Wix.

**Relevans for oss:** «markdown-briefing FOR Claude Code, ikke for meg» + «still tre spørsmål før du bygger» + «si deploy-mål nå for å spare tokens» = presise regler for `operations/DISPATCH.md` og `/plan`. `.gitignore`-avsnittet speiler vår eksisterende `.gitignore` (`*.env`, `**/*secret*`, embedded repos) og CLAUDE.md-regelen «aldri commit hemmeligheter». Auto-minne i `~/.claude/projects/` = samme sted som `memory/first-system-project.md` ligger. GitHub Pages = gratis-alternativ til `operations/vps-deploy.md`.

**Kategori:** Playbooks — Nettsider
