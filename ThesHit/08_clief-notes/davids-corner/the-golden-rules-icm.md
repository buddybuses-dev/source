# The Golden Rules — ICM (Interpreted Context Methodology)

Kilde: https://www.skool.com/cliefnotes/classroom/c7f102c7?md=470128e36994482695f3d770411455ac

**Den kanoniske versjonen av hele metoden — «ICM: Jake's Interpreted Context Methodology.
Minimize token usage. Start owning your stack. Filesystem-first system.»**

**5-lags kontekst-hierarki** (last aldri hele workspacet):
- **L0** `CLAUDE.md` (~400 tokens) — prosjekt-orientering, høynivå-ruting
- **L1** rot-`context.md` (lean)
- **L2** stage-`context.md` (~200–500 tokens) — «start contract» for et steg
- **L3** `_config`, referanser, skills — brand voice, stabil kunnskap (selektivt lastet)
- **L4** working artifacts (scoped) — run-spesifikke inputs/outputs

**7 gyldne regler for token-effektivitet:**
1. Lag konteksten din kompromissløst i lag — aldri last hele workspacet
2. Ett steg, én jobb — ingen monolittiske prompts; eksplisitte «inputs»-tabeller
3. Skriv tydelige stage contracts (inputs → process → outputs)
4. Konfigurer «fabrikken» — brand voice, maler, skills, `_config`
5. Bruk menneskelige review-gates
6. Hold det globale lean, det stegvise presist
7. Iterér selve strukturen — rename, reorder, refine

«ICM cuts token waste by layering context through numbered folders and stage contracts —
load only what each step needs.» **= nøyaktig `first system project` sin arkitektur + METHOD.md
+ DISPATCH.md + `/verify`-gatene.**

**Kategori:** David's Corner — Must Have Resources
