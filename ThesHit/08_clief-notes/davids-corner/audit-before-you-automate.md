# Stop automating your frustration. Audit it first.

Kilde: https://www.skool.com/cliefnotes/classroom/c7f102c7?md=a6e956b765044372a3f425339dedfdfe

**Kjernemetodikk — workflow-audit (inspirert av Laura L.'s «AI Workflow Audits»).** De fleste automatiserings-fiaskoer følger samme mønster: du velger workflowen du hater mest, prøver full ende-til-ende-automatisering, den feiler på et dyrt punkt, og du klandrer modellen. Fiksen er ikke en bedre prompt — det er en **audit før du bygger.** En deterministisk, etterprøvbar skill for ICM-workspacet ditt tvinger deg til å score hver workflow på to akser — **Impact** og **Risk** — før en eneste agent kjører. Resultatet plasserer workflowen i en 2×2: høy impact / lav risiko → **AUTOMATE**; høy risiko → **HYBRID** (menneskelig gate); lav impact / høy risiko → **MANUAL**. Stegmapper: `01_research`, `02_draft`, `03_review_gate`, `04_execute`.

**Relevans for oss:** dette er nøyaktig `skill-audit` / `obliteratus`-tanken vi allerede refererer i `security/tools.md`, satt i system. Impact/Risk-scoringen bør inn i `operations/DISPATCH.md` sin Mission Brief Builder, og `03_review_gate` = METHOD.md steg 5 + «human review gates» (ICM golden rule).

**Kategori:** David's Corner — Learning for Everyone
