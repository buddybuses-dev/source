# 2.1 Setting Up Claude in Chrome (5 Min)

Kilde: https://www.skool.com/cliefnotes/classroom/d3907117?md=bbabe44d36eb414c8f6189077c3f6185

**Installer Claude-utvidelsen i nettleseren så den kan interagere med enhver side du besøker.**
Krav: betalt Claude-plan (Pro/Max/Team/Enterprise) + **Google Chrome eller Microsoft Edge**.
**Brave, Arc og andre Chromium-nettlesere virker ikke ennå — bruk Chrome eller Edge.**
Steg: (1) installer fra Chrome Web Store (Anthropic publisher-side), (2) restart Chrome helt
(lar native messaging-host initialisere — hopper du over dette får du connection errors),
(3) pin utvidelsen (puslebrikke-ikon → pin), (4) logg inn i sidebar-en.

## Fra videoen (transkribert — kort promo-klipp, 192 ord)

Anthropics egen demo: «Claude for Chrome bringer Sonnet 4.5 (state-of-the-art for computer use) rett inn i nettleseren.» Eksempel — en oppussing der budsjettet ligger spredt over et planleggingsdokument og flere e-poster med håndverkere: på prompt samler Claude konteksten (finner relevante e-poster og kvitteringer), jobber aktivt i regnearket (sporer opp manglende tall, oppdaterer budsjettet i sanntid), og lager til slutt et e-postutkast for å dele planen med partneren — **du gjør de siste redigeringene før sending**. Sikkerhet bygget inn: granular tillatelser for hvilke handlinger Claude får ta, beskyttelse mot **prompt injection**, restriksjoner på hvilke nettsteder Claude kan bruke, og den **spør alltid før sensitive handlinger** som kjøp.

**Relevans for oss:** dette er `platform/claude-in-chrome`-verktøyene + `operations/`-innboks-jobben — «samle kontekst → jobb i et regneark → lag utkast, mennesket sender». Sikkerhetsmodellen (granular tillatelser, prompt-injection-vern, spør før kjøp) matcher vår `security/APP-SECURITY-CHECKLIST.md` og CLAUDE.md-permission-modellen.

**Kategori:** Playbooks — Browser Flow
