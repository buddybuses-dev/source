# Building Agents With Cognitive Functions

Kilde: https://www.skool.com/cliefnotes/classroom/c7f102c7?md=01cf4ecf9cf24b5cba00a65445db49a3

**Brooke Hays (The Lens Series) — del 2, praktisk.** Fra «Bullhorns and Bullseyes»-podcasten: å «type» AI-agenter kan være svært nyttig. Agenter har ikke personlighet, følelser eller preferanser — men de kan instrueres til å prioritere ulike måter å prosessere informasjon på. Å type en agent er ikke å gi den personlighet, men å velge en **resonneringsstrategi** som vektlegger visse styrker og godtar visse tradeoffs. Tenk mindre på *hva* agenten gjør og mer på *hvordan* du vil at den skal angripe oppgaven. Eksempel — en research-agent kan: samle mest mulig konkret data (Se), sammenligne mot eksisterende info (Si), generere mange mulige tolkninger (Ne), eller syntetisere til ett underliggende mønster (Ni).

## Fra videoen (transkribert — «Watering Hole»-podcast, ~1 time; Curtis Hays, Tom, Brooke Hays)

- **De 8 kognitive funksjonene (Jung → Myers-Briggs):** to *perseiverende* — **Sensing** (konkret, håndfast, 5 sanser) og **iNtuition** (implisitt, mønstre, muligheter, mening); to *dømmende* — **Thinking** (logikk, «gir dette mening?») og **Feeling** (verdier, menneskelig påvirkning, «hva betyr mest her?»). Hver har en *attitude*: **e**kstern eller **i**ntern.
  - **Se** — utforsker håndfaste detaljer uten å legge til mening («eplet er rødt, blankt, knasende»).
  - **Si** — sammenligner mot tidligere erfaring/data («dette eplet minner om epleplukking med far; noe er *off*»).
  - **Ne** — spretter ut mange abstrakte muligheter fra ett detalj (firework-mønster).
  - **Ni** — tar mye ekstern info og koker det ned til *én* konklusjon/implikasjon.
  - **Te** — gyldig/ugyldig etter tommelfingerregler, prioriterer effektivitet («hva må gjøres *nå*»).
  - **Ti** — gyldig/ugyldig etter *intern* logisk konsistens, prioriterer nøyaktighet over tid.
  - **Fe** — moralsk rett/galt etter normer («folk vil normalt ha støtte, så jeg validerer»).
  - **Fi** — moralsk rett/galt etter *personlige* verdier («da jeg var lei meg ville jeg ha råd, så jeg gir det»).
- **Funksjoner kommer i par:** Se↔Ni, Si↔Ne, Te↔Fi, Ti↔Fe. Stack: **hero** (mest naturlig, default under stress) → **parent** (guide, motsatt perseiv/døm) → **child** (balanserer parent) → **inferior** (svakhet / vekstpunkt). 4-bokstavskoden (INTJ osv.) *utledes fra* de to sterkeste funksjonene — «du trenger bare de to første».
- **Eksperimentet (Brooke, gratis ChatGPT-konto, 30 min):** to «projects» (= spesialiserte agenter) med **identiske instruksjoner + identisk prompt — eneste forskjell er de kognitive funksjonene** (gitt som fire bokstaver til en «cognitive-functions-ekspert»-agent som ekspanderte dem). Oppgave: analysér forretningsdata og finn underliggende årsaker.
  - *Lira* (**Ne + Ti**): stilte oppfølgingsspørsmål uoppfordret, ga 5 hypoteser med styrkegrad, ba om mer info — «den irriterende ansatte som kommer tilbake med tusen spørsmål».
  - *Malachi* (**Ni + Te**): én setning om hva som skjer, så steg-for-steg, implikasjoner, og *nøyaktig hva du skal gjøre nå*.
- **Curtis' produksjonsoppsett (i Claude Code):** et **folder system** med spesialiserte agenter (Cash the copywriter, Cassidy graphic designer, Hank sales/proposals, Wayne complex-issues, Cody WordPress/IT …) + en **orchestrator** på toppen som laster rett agent + kontekst basert på spørsmålet — «så den ikke bare bruker gjennomsnittet av internett». 18 agenter typet på én kveld med Brooke; Cash fikk samme funksjoner som Tom (INFJ: Ni + Fe — «underliggende budskap i brandingen, så trekk i publikums hjertestrenger»); Pike fikk Se + Fi («hva sier målgruppa ordrett online, ingen mening lagt til, men matchet mot org-verdiene»).
- **Orchestrator rerouter selv:** «be Radley skrive social posts» → «Radley gjør ikke det — reruter til Cash». «I barely need to think anymore.»
- **Verdiene ligger *over* personligheten:** organisasjonens/individets verdier er non-negotiables — «ting vi *nekter* å gjøre» — imprinted på topp-nivå; agenten resonnerer *ut fra* dem. «Skal du outsource til en AI-agent, sørg for at den har et *hode, et bryst og en mage*» (C.S. Lewis-referanse) — ellers tar du all menneskeligheten ut av arbeidet og sitter igjen med «gjennomsnittet av internett».

**Relevans for oss:** dette er en ferdig oppskrift for `agents/` + `agents/coordinator-agent/` + `operations/DISPATCH.md`:
1. Gi hver agent en **funksjons-profil** (to bokstaver) i `agent.md` «Identitet»/«Context» — f.eks. coordinator = **Ni+Te** (syntese → konkret handling), red-team/`/redteam` = **Ne+Ti** (mange tolkninger, intern logikk-sjekk), production/research = **Se+Fi**, marketing/writing = **Ni+Fe** («window not mirror» = Fe).
2. **Orchestrator-mønsteret** (last rett agent + kontekst per spørsmål, reroute ved feil match) = nøyaktig coordinator-agentens rolle + `CLAUDE.md`-routeren.
3. **Verdier over personlighet, med non-negotiables** = `goal/GOAL.md` + `SOUL`-tanken fra [`do-you-have-a-soul`](do-you-have-a-soul.md) + CLAUDE.md 3-tier-permission.
4. «To bokstaver er nok» = hold profilen kort (Foundation 3.3 feil 4: kontekst om *arbeidet*, ikke lange personlighetsavsnitt).

**Kategori:** David's Corner — Brooke Hays: The Lens Series
