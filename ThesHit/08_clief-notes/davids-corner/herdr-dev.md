# ATTN: Keyboard Warriors, Introducing Herdr.dev

Kilde: https://www.skool.com/cliefnotes/classroom/c7f102c7?md=b1ab2923b4c54a17b29249a018c27704

**Verktøy-review.** `herdr.dev` — en agent-bevisst runtime bygget i Rust som behandler kode-agentene dine som førsteklasses borgere. Problemet den løser: folk kjører fortsatt AI-kode-agenter «som om det er 2015» — spawner en Zellij/tmux-sesjon, fyrer opp én agent i én rute, en annen i neste (pi.dev, Kilo Code, OpenCode, Codex), og holder pusten i håp om at SSH-koblingen ikke dropper og sletter hele konteksten. Herdr er ikke enda en terminal-multiplexer: «one terminal, the whole herd» — kjør alle agentene fra én terminal på hvilken som helst boks eller over ssh, se locked/working/done på et blikk, reattach fra telefonen. Forfatterens bakgrunn: nonprofit på null budsjett, «cheapest possible stack, maximum outcome».

**Relevans for oss:** relevant for hvordan flere samtidige Claude-sesjoner mot `first system project` koordineres (jf. METHOD.md-regelen om å ikke committe andres halvferdige kode). Sammenlign med Claude Code Remote Control (Building Your Stack 2.2) — samme «reattach fra telefon»-behov. Merk: uavklart om åpen kildekode; vurder mot OpenCode-anbefalingen i `rooms/learning/tools.md` før bruk.

**Kategori:** David's Corner — Reviews: Tools, Models, Methods
