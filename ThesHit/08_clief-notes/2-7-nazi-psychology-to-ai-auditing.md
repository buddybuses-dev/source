# 2.7 From Nazi Psychology to AI Auditing

Kilde: https://www.skool.com/cliefnotes/classroom/036893d9?md=3ef5bfe338ad4031beaa655312d66a8b

**Siste leksjon i abstraksjons-serien — et ekte AI-system tatt fra hverandre bit for bit.**
Forfatteren tok psykometriske tester som opprinnelig målte autoritære tendenser på 1950-tallet
og rettet dem mot AI-modeller, og bygde en data-pipeline som kan administrere mange
personlighetstester på tvers av flere modeller samtidig (moral foundations, autoritarisme-skalaer
m.m.). Det man finner inni er ikke magi: API-er, async, parsing, statistikk. **AI er ~10 % av
systemet; de andre 90 % er ingeniørkunst som har eksistert i tiår.** Full artikkel: arXiv
2510.11742 «The Ethics Engine: A Modular Pipeline for Accessible Psychometric …». Binder hele
serien sammen.

## Fra videoen (transkribert)

- **«Agent» — språket løper foran ingeniørkunsten.** Det vi kaller en AI-agent er i de aller fleste tilfeller *ikke* én entitet som tar autonome beslutninger. Det er en samling prompts strukturert og sekvensert av *tradisjonell kode* som får modellen til å oppføre seg forskjellig på ulike stadier. Orkestreringslaget (vanlig software) vurderer modellens output og bestemmer neste prompt basert på betingelser en menneskelig ingeniør definerte. Analogi: forskjellen på et **funksjonskall** (input → output, bestemmer ikke hva som skjer videre) og en **kjørende prosess** (som tar den beslutningen). Hvert modell-kall er et funksjonskall; det agentiske oppstår fra orkestrerings-koden rundt.
- **API = en kontrakt.** To programmer blir på forhånd enige om formen på samtalen (hvordan request/response ser ut, hva som er lov). Ingen av sidene trenger å forstå den andres innmat. Ethics engine → Claude = en HTTP-request med JSON (prompt + modellnavn + parametere) til Anthropics endpoint → JSON tilbake. Alt scoring/analyse skjer *lokalt i tradisjonell kode*.
- **N×M-problemet og standardisering:** hvis systemet må snakke med 20 tjenester og hver kobling er custom, vokser antall integrasjoner som (apper × verktøy) — uholdbart. Historisk løst med standardiserte grensesnitt: USB (før: hver periferienhet sin kontakt), HTTP (før: hver app sin protokoll), Language Server Protocol (før: hver editor × hvert språk). **MCP (Model Context Protocol)** er den moderne versjonen — introdusert av Anthropic sent 2024, eksplisitt inspirert av LSP. Tre deler: *host* (AI-appen), *client* (håndterer koblingen), *server* (wrapper verktøyet, snakker MCP). Modellen kaller ikke API-er direkte.
- **Språk → tall-broen:** modellen svarer med en streng (probabilistisk språk); scoring-systemet trenger et tall. Broen er *parsing / pattern matching / regex* — tekstverktøy som er tiår gamle. Så: reverse-scoring, subskala-aggregering (basisaritmetikk, men peer-reviewed), reliabilitet (Cronbachs alfa, test-retest via scipy/numpy — eldre enn modellene de evaluerer).
- **Den bekreftede ratioen:** AI-kall ~**10 %** av systemvolumet, orkestrering (async, rate-limiting, retry, kø) ~**30 %**, dataprosessering (prompts, personas, parsing, scoring, analyse, reliabilitet) ~**60 %**. «All the bad systems ignore this ratio.» = 60/30/10 fra 2.5.
- **Syntesen av hele serien:** AI *utvider* det vi alltid har gjort — legger til et lag der naturlig språk er grensesnittet og kontekst er programmet — men det laget hviler på samme ingeniørtradisjon (API-er, protokoller, statistikk). Det semantiske laget (operere på *mening* i stedet for *syntaks*) er genuint nytt, men erstatter ikke lagene under; det er avhengig av dem. Når ekte agentisk atferd (autonome løkker) kommer, blir ingeniørens jobb ikke å gjøre AI-en smartere, men å bygge infrastrukturen rundt: pålitelighetsmønstre, feilhåndtering, protokoller for trygg autonom drift.

**Relevans for oss:** «en agent er en samling prompts sekvensert av kode» = presist hva `agents/*/agent.md` + `operations/DISPATCH.md` + coordinator-agent er. MCP-avsnittet = hvorfor `.claude/` MCP-serverne (codebase-memory, m.fl.) er riktig mønster, ikke custom integrasjoner. 60/30/10 + «bad systems ignore the ratio» = målestokk for `platform/jarvis-local/` og `scripts/`. «Funksjonskall vs. prosess» = hvorfor `/verify` og `/redteam` er egne steg, ikke noe modellen «bare gjør».

**Kategori:** Abstraction Series
