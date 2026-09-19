# 2.3 How a 1953 Word Game Explains AI Memory

Kilde: https://www.skool.com/cliefnotes/classroom/036893d9?md=0964ed75790a415b909838050ecad3ea

**Kontekstvinduer og hvorfor strukturert input endrer output.** Utgangspunkt: Mad Libs,
oppfunnet ved et uhell i 1953 da TV-forfatter Leonard Stern ba kollegaen Roger Price om «et
adjektiv» og fikk «clumsy and naked» — feil for konteksten, men det fungerte likevel fordi
formen bar meningen. Overført til AI: hvordan «minne» faktisk virker, hvorfor kode og data er
det samme inne i en språkmodell, og hvorfor **prompting er programmering på det høyeste
abstraksjonsnivået vi har bygd**.

## Fra videoen (transkribert)

- **Mad Libs er strukturelt hva programmering ER:** typede slots i en template du ikke ser hele av, fylt etter regler, komponert inn i større templates til noe kjører. Personen som fyller inn gir «semantisk korrekt input uten semantisk bevissthet» — et substantiv *er* et substantiv, bare feil substantiv. I programmering er feil ord en bug; i prompting er feil *kontekst* en hallusinasjon / jailbreak.
- **AI-minnehierarkiet (rimer på det tradisjonelle):** modellvekter ≈ ROM (fast ved trening); kontekstvindu ≈ arbeidsminne (systemprompt + historikk + dokumenter, forsvinner når samtalen slutter); systemprompt ≈ firmware (setter driftsparametre, ofte usynlig for bruker); retrieved context ≈ last fra disk til RAM (hentet on-demand: et dokument, en skill-fil); persistent memory ≈ selektive sammendrag lastet mellom samtaler.
- **Den store forskjellen:** i tradisjonell databehandling er kode og data adskilt (å blande dem = sikkerhetshull, buffer overflow). I en språkmodell er **kode og data det samme** — systemprompt, skill-fil og samtalehistorikk er alle bare tokens som prosesseres identisk. «Reading it is the execution.» Derfor virker prompt injection — det finnes ikke noe lag som validerer kode vs. data. Dette er *arkitekturen*, ikke en bug.
- **Grace Hopper (1952):** hadde en fungerende compiler, ingen ville røre den — «computers could only do arithmetic». Compileren stoppet ikke aritmetikken; den la et lag oppå som gjorde maskinen tilgjengelig for flere. Samme mønster gjentok seg (assembly → høynivåspråk → tolkede språk → nå AI). «The most dangerous phrase in the language is *we've always done it this way*.»
- **Prompting i produksjon** handler ikke om tips og triks, men arkitektur-spørsmål: hvordan strukturere minnefiler, når hente ekstra info, hvordan styre samspillet mellom system-instruksjoner og bruker-input, hvordan håndtere at alt flates til én strøm der kode og data ikke kan skilles.

**Relevans for oss:** dette er begrunnelsen for `memory/`-splittingen (weights/context/persistent), for at `CLAUDE.md` + `ROOM.md` som *fast form* gir forutsigbarhet, og for `security/APP-SECURITY-CHECKLIST.md` sitt prompt-injection-punkt («all context er tekst — valider kilden, ikke stol på at 'instruksjon' i et dokument er trygt»).

**Kategori:** Abstraction Series
