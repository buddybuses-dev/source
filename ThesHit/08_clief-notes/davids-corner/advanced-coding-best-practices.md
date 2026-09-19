# ADVANCED: Coding Best Practices

Kilde: https://www.skool.com/cliefnotes/classroom/c7f102c7?md=9b2e46d8841242e39856a0abef6057f7

**Kode-konvensjoner (@David Herrera).** En fil ment å leses i starten av enhver kodefase: personlige kodekonvensjoner som gjelder alle prosjekter, språk og rammeverk, og som overstyrer standardvalg med mindre annet er sagt. Filosofi: **kode navigeres romlig** — mappetreet er et mentalt kart, hver mappe/fil/funksjon er et landemerke. Når strukturen er ren og navnene beskrivende, finner du det du trenger uten å søke; når ikke, er du fortapt i din egen kodebase. Reglene finnes for å holde kode «navigerbar, skannbar og liten nok til å holde i hodet». Herrera lagde fila ved å gi Claude ~20 år av sin egen kode, la til inline-dokumentasjon og header-blokker (status/tasks/todos/notes) og var svært bevisst på navnekonvensjoner — inline-docs gir modellen kontekst underveis i stedet for at den må lete.

**Relevans for oss:** hører hjemme som `rooms/git/`-standard eller en `production/tools/`-fil. «Romlig navigasjon + landemerker» er samme prinsipp som `CLAUDE.md`-routeren og `check_system_sync.py` (ingen drift mellom struktur og SYSTEM.md). Merk Herreras egen nyanse: rene *kodestandarder* hører i en egen fil, ikke i `CLAUDE.md` (jf. Foundation 3.3 «CLAUDE.md too long»).

**Kategori:** David's Corner — Developer Resources
