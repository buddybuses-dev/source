# 4.5 Where This Goes

Kilde: https://www.skool.com/cliefnotes/classroom/036893d9?md=dd5a0adc38a440f29b48354a3a9da667

**Modul 4-avslutning (video «Coming Soon» — companion-tekst er kjøttet): hvordan `CLAUDE.md` skalerer fra ett prosjekt til en full workspace-arkitektur.** Så langt: tre grensesnitt (Desktop, VS Code, Terminal), ekte oppgaver på egne filer, Desktop til tenkning + Code til bygging, og en `CLAUDE.md` som gir Claude prosjekt-nivå kontekst. «Men hva om...» du har 10 prosjekter, eller en kompleks workflow med ulike oppgavetyper, eller et team som trenger samme kvalitet på tvers. Én `CLAUDE.md` per prosjekt funker fortsatt — men det finnes et nivå over: **task routing**, der ulike oppgaver laster ulik kontekst automatisk («skriv et script» → laster kun voice-docs; osv.). Du setter opp to scoped-kontekster og ser Claude oppføre seg forskjellig i hver.

**Relevans for oss:** «task routing — ulike oppgaver laster ulik kontekst automatisk» ER `CLAUDE.md`-routeren + `rooms/*/ROOM.md` + `operations/ROUTING.md` i vårt system. Vi er allerede på nivået «over én `CLAUDE.md` per prosjekt» — 15 scoped rom. Bekreftelse på at arkitekturen vår er riktig retning.

**Kategori:** AI Coding Tools
