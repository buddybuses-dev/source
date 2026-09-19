# 2.4 Session Persistence Across Devices

Kilde: https://www.skool.com/cliefnotes/classroom/2a86a1d1?md=fa6dced1aed94c4792602cf121a0168a

**To slags persistens.** (1) Remote Control gir persistens *innad i en økt* — alt synkes
mellom enheter, samtalen er kontinuerlig. (2) Men økter tar slutt (terminalen lukkes,
token-grenser, laptop restarter) → Claude husker ikke den gamle økten. Denne leksjonen handler
om den andre typen: **sørg for at DU ikke mister kontekst selv når Claude gjør det.** Problemet:
å re-forklare er tregt og du mister detaljer. Løsningen: **legg konteksten i filer**
(mappestruktur / `CLAUDE.md` / notater) som en ny økt kan lese. = nøyaktig `memory/`-laget +
`/session-start` + `/pickup` i `first system project`.

**Kategori:** Building Your Stack — Remote Access
