# 4.1 Install and First Use

Kilde: https://www.skool.com/cliefnotes/classroom/036893d9?md=fd76648c16ad429fb6e828b01bfa9177

**Modul 4, leksjon 1 (24:33 video): installere de tre Claude-grensesnittene og kjøre første oppgave på egne filer.** «Alle sesjonene er bygget rundt Claude, men konseptene spenner over alle modeller og verktøy innen rimelighetens grenser.» Du sitter igjen med: alle tre grensesnitt (Desktop, VS Code, Terminal) installert og fungerende på maskinen, en klar følelse av *når* du bruker hvilket, og din første ekte oppgave kjørt på dine egne filer.

## Fra videoen (transkribert)

- **Én modell, tre grensesnitt** (ikke tre AI-er): Desktop = *samtalelag* (planlegging, tenking, rask utblåsing, minne-oppslag; kan ikke se filer, kjøre kode eller redigere — alt via kopier/lim/opplasting). VS Code + Claude Code-utvidelse = *editor-lag* (ser prosjektet, redigerer filer inline, kjører kommandoer, ingen kopiering). Terminal (`claude`) = *kommandolinje-lag* (samme motor; best når arbeidet ikke bor i et kode-prosjekt — behandle en mappe med dokumenter, rydde downloads). «Same brain behind all three — the difference is what each interface lets that brain see and do.»
- **Det viktigste på sammenligningstabellen er «iterate on output»:** i chat må du lese svaret, finne ut hva som er galt, kopiere, starte på nytt. I Claude Code sier du «det er feil, fiks dette», og flytter det til en egen mappe — du delegerer og bryter ned prosessen underveis i stedet for runder med kopier/lim i én chat. «Your interface is playing the middleman stopping you from working as well.»
- Cursor / Windsurf / Copilot / Google Anti-Gravity er *egne produkter bygget på VS Code* — noen bruker Claude, noen ikke, noen blander modeller. Denne modulen dekker kun Anthropics egne verktøy. Jake foretrekker rå VS Code («no bloat»).
- **Installasjon:** Claude Desktop → last fra Anthropic, velg Windows/Mac/ARM64 (sjekk *Settings → System → About → system type*: «64-bit … x64-based» = vanlig). Claude Code krever **Node.js**; deretter `npm`-kommando fra Anthropics store, eller la Claude Desktop installere det for deg. Logg inn med *abonnement* (ikke API-nøkkel — billigere) via nettleser-autorisering. VS Code-utvidelse: Extensions (Ctrl+Shift+X) → «Claude code for VS Code» → Install. Max-konto gir også «Claude Cowork» (Claude Code som jobber gjennom mapper inne i appen).
- **Hjemmelekse:** ta én ting fra ditt eget arbeid, legg i en mappe, få Claude Code til å oppsummere den, prøv i Desktop, prøv i VS Code-utvidelsen — og *tenk på workflowen*, ikke bare outputen. «This isn't about using an AI model, it's about designing your workflow to get a lot out of it.»
- Session 5 nevnes som «kanskje det mest verdifulle» — en dypere fil-arkitektur Jake kaller **Model Workspace Protocol** (eget kurs).

**Relevans for oss:** vi kjører alt via Claude Code allerede. «Iterate on output i Code, ikke i chat» = hvorfor `/verify`/`/redteam` er egne steg. «Design workflowen, ikke bare bruk modellen» = `goal/GOAL.md` + `operations/`. Node.js-notatet er relevant for `smart-app-control-blocks-venv-trampolines`-minnet (venv/uv-oppsett på denne maskinen).

**Kategori:** AI Coding Tools
