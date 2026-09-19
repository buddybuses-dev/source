# Claude Design: Folder Structure as a Design System

Kilde: https://www.skool.com/cliefnotes/classroom/d3907117?md=90dccec7e9c248389b858bebe56e80ee

**Modul 1.5 (42:29 video). Claude Design er Anthropics verktøy for å bygge design-systemer,
slide-decks, prototyper og animert innhold — under grensesnittet er det Claude [Code].**
Kjerneidé: **mappestruktur ER et design-system.** Forutsetninger: Foundation-leksjon 2
(mappestruktur = riktig abstraksjon for AI — «prinsippene der er hvorfor Claude Design virker
i det hele tatt»), Foundation 4 (Claude Code + VS Code-oppsett for å kjøre eksporterte
design-systemer), og Playbook Modul 1 (animasjons-bygge-flyten som Claude Design nå delvis
automatiserer). I dette prosjektet: samme tanke som `rooms/marketing/design-system/` +
`design`-skillet.

## Fra videoen (transkribert)

- **Claude Design brenner credits fort:** topp Max-plan → 83 % av Claude Design-kvoten på én dag med lett testing. Videoen handler mye om hvordan slippe unna det.
- **Hovedverdien:** importer eksisterende assets — fra **GitHub**, **Figma-filer**, eller en desktop-mappe — og la Claude bygge et **design system** (mapper + skills + komponenter) du kan generere «nesten hva som helst» fra i et kontrollert miljø. «En designer bruker Claude Design bedre enn nesten alle andre.»
- **Wireframe** (få tokens, se hvordan noe *kan* se ut) vs. **high fidelity** (bygger faktisk, bedre/raskere output, mange flere tokens). Prosjektet har en mappe med skills (interactive prototype, high-fi design, design system) — alle bare markdown; du kan legge til flere (Anthropics egen skills-GitHub, front-end-design-skill).
- **Generering-flyten:** peker på GitHub → leser README, navigerer *hver fil dypt* (derav token-forbruket), tar notater, bestemmer hvilke filer som er viktige/skal ignoreres, lager style sheets + **egne skill-dokumenter** (med routing, non-negotiables, hovedfarger) + tar **screenshots for å verifisere seg selv**. Deretter *reviewer du*: «er dette READMEen? er dette fargene våre?» → «looks good» / «needs work». «Forfin start-dataen så du aldri må forfine den igjen.»
- **Eksport:** last ned som zip → pakk ut lokalt → **du trenger ikke Claude lenger**. Åpne mappa i Claude Code / VS Code / Codex, kjør `/initiate`, den lager en `CLAUDE.md`, og du genererer slide-decks/PowerPoints lokalt med *langt* færre tokens. Kan også eksportere til PowerPoint/HTML/Canva som briefing-dokument til andre designere.
- **Lokale modeller funker** så lenge modellen kan lese filer + navigere mappe: **Qwen 3 Coder (Next-edition — 80B params, laster kun noen om gangen → mindre GPU)**, **Code Gemma** (Google DeepMind), **Mistral Devstral**, **DeepSeek** (V2/«B2» — men omdiskutert i US-statlig arbeid pga. tracking-påstander). «Forstår du mappestrukturen kan du fjerne behovet for å bare bruke Claude — jeg traff limiten, byttet bare modell.»
- **Kjerneprognose:** de neste 5 årene kommer flere verktøy som Claude Design; mindre og mindre trenger du å *bygge* agenter som navigerer mapper — mer og mer må du *kondensere* strukturene dine til noe én god kode-agent kan lese og gjøre tool calls mot. «Build systems that grow with time, not get replaced with time.»
- Sitat verdt å notere: **«productionize your opinion»** — når du er i topp-10 % av design/kode/matte, blir *meningen din* det verdifulle; alle kan få «decent enough» output.

**Relevans for oss:** «mappestruktur ER design-systemet» + «eksporter zip, kjør lokalt med færre tokens» = direkte modell for `rooms/marketing/ui-ux-pro-max/` og `rooms/production/`. `/initiate`-mønsteret ligner våre `.claude/commands/`. Lokal-modell-listen (Qwen 3 Coder Next, Code Gemma, Devstral) → inn i `operations/ROUTING.md` som fallback-kandidater (jf. `smart-app-control`-minnet + `Nous-kreditter tomme`-hendelsen). «Productionize your opinion» = hvorfor `goal/GOAL.md` og agent-personligheter betyr noe. Merk: bruk Claude Design sparsomt (egen kvote).

**Kategori:** Playbooks — Claude Design
