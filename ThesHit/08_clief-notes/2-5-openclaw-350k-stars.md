# 2.5 OpenClaw Has 350K+ Stars

Kilde: https://www.skool.com/cliefnotes/classroom/036893d9?md=190cdff0f6ed40d8b479ea675e37509a

**Orkestrering vs. intelligens — og hvor verdien faktisk sitter i et AI-system.** Pitchen:
én assistent overalt du allerede er (WhatsApp, Telegram, Slack, kalender, filer, nettleser),
350 000+ GitHub-stjerner, 3 500 PR-er, 2 000 bidragsytere, noen kaller det AGI. Men åpner du
kodebasen (~50 000 linjer) er det meste vanlig kode: API-er, async-programmering, parsing,
statistikk. **De fleste produksjons-AI-systemer er ~90 % tradisjonell kode og ~10 % AI.**
Lær å se på et hvilket som helst AI-verktøy og finne hvor den reelle verdien ligger (som
regel i plumbingen, ikke i modellen). = METHOD.md steg 5: tung/deterministisk logikk i
`scripts/`, LLM bare til vurdering.

## Fra videoen (transkribert)

- **Orkestrering forklart:** en dirigent spiller ikke et instrument og lager ingen lyd — jobben er å koordinere *hvem som spiller når, hvor høyt, i hvilken rekkefølge*. Bytt musikere med AI-modeller, verktøy og meldingsplattformer, så har du orkestreringslaget. Uten et orkestreringslag må hver melding manuelt finne AI-en, som finner verktøyet, som svarer tilbake, som finner tilbake til appen — kaos. Med et sentralt hub-lag flyter alt gjennom én intelligent router.
- **Begrepene ryddet:** *AI-modell* = selve intelligensen (GPT/Claude/Llama). *Wrapper* = tynt lag rundt et API, minimal verdi. *Agent* = AI som tar handlinger autonomt. *Orkestreringslag* = koordinerer AI + verktøy + kanaler + kontekst. Verktøyet er «motorveisystemet — du må ha med din egen bil» (API-nøkkel).
- **60/30/10-regelen (Jakes arkitektur-tommelfingerregel):** bygg AI-verktøy med ~**60 % tradisjonell kode** (plattform-integrasjoner, nettverk, filhåndtering — ingenting med AI å gjøre), ~**30 % regelbasert logikk** (routing, sesjonsstyring, sikkerhetsregler — smart kode, men ikke modeller), og bare ~**10 % faktiske AI-kall**. I dette verktøyet er de 10 % til og med skjøvet eksternt (API-kall til andres AI). «The AI is a component, not the whole thing. The value is in everything around the AI.»
- **Lag-arkitekturen:** kanal-lag (WhatsApp via Baileys, Telegram via grammY, Discord via discord.js, Signal via signal-cli) → gateway (lokal websocket-server: routing, sesjoner, autentisering) → verktøy (browser-automasjon, bash, filoperasjoner, cron, webhooks) + AI-modeller (bare tomme hooks — bring egen nøkkel).
- **«Getting sherlocked»:** når en plattform legger til en funksjon som gjør hele produktet ditt overflødig. Hvis Anthropic slipper «Claude everywhere» (native WhatsApp/Slack/Discord, ingen config), hvorfor trenge et mellomledd? Motargumentet: modell-agnostisk + self-hosted + open-source = ingen vendor lock-in, data på egen maskin. «The Switzerland of AI systems.»

**Relevans for oss:** 60/30/10 er en konkret målestokk for `platform/jarvis-local/` og `scripts/` — sjekk at vi ikke lener oss på LLM der deterministisk kode holder (jf. METHOD.md steg 5, `check_system_sync.py`, `autoplan.py` = «30 %»-laget). Lag-arkitekturen (kanal → gateway → verktøy+modell) er en god mal for hvordan `operations/` innboks-/varsel-jobben bør struktureres. «Getting sherlocked» = hvorfor vi bygger på struktur/dømmekraft, ikke på en enkelt integrasjon.

**Kategori:** Abstraction Series
