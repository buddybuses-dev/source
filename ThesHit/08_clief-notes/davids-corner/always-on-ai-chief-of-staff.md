# Built always-on AI Chief of Staff that texts me

Kilde: https://www.skool.com/cliefnotes/classroom/c7f102c7?md=f2ec206026dd4182906f07874a9e3533

**Referanse-bygg (Justin Solomon).** En lokalt hostet AI-assistent («Emma») som kjører 24/7 på en gammel MacBook (2015), sender daglige briefinger via iMessage, og styrer kalender, e-post og prosjekter gjennom MCP-integrasjoner. Poeng: du kan bygge et produksjons-klart personlig AI-system på forbrukermaskinvare uten sky-avhengigheter eller kompliserte orkestrerings-rammeverk. Davids ramme: markdown-mapper i stedet for vektordatabaser, «constraint-first» — han holdt seg innenfor vanlige abonnements-grenser og gjorde det modell-agnostisk med én linjes endring. iMessage-integrasjonen alene er verdt å studere.

**Relevans for oss:** dette ER `platform/jarvis-local/` sitt endemål — lokal server, daglig briefing, MCP-styrt kalender/e-post. «Constraint-first, modell-agnostisk med én linje» = `operations/ROUTING.md`. «Daglig briefing via melding» = mønster for trading-agentens og coordinator-agentens daglige rapport (jf. `PushNotification`/SMS). Kobler til [`hermes-stack.md`](hermes-stack.md).

**Kategori:** David's Corner — David and Jake's Picks V2
