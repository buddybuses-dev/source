# 3.3 Common Mistakes and How to Fix Them

Kilde: https://www.skool.com/cliefnotes/classroom/036893d9?md=7b1919bbe3af42aa859b6060e4e7513f

**De sju vanligste feilene folk gjør når de setter opp mappe-arkitekturen — alle hentet fra ekte community-medlemmer som postet oppsettene sine og gikk på veggen.** Les dette før du ferdigstiller strukturen fra 3.2, så slipper du unna de fleste.

1. **`CLAUDE.md` blir for lang.** Den er en *rutefil* — ikke en prosjekt-brief, stilguide eller hjernedump. For lang → Claude brenner tokens på irrelevant info, og rute-instruksjonene drukner i bakgrunnsstøy. **Fiks:** hold den til én skjerm — identitet, mappestruktur, rutetabell, konvensjoner.
2. **Hoppe over rutetabellen.** Uten den må Claude gjette hvilke filer den skal lese; output blir inkonsistent uten at du skjønner hvorfor. **Fiks:** tre kolonner — *oppgave · hvor · hva som skal leses* — én rad per type arbeid.
3. **For mange workspaces.** Åtte rom for et prosjekt med to–tre arbeidsmoduser; vedlikeholdet blir større enn arbeidet, kontekstfiler blir utdaterte. **Fiks:** start med to–tre. Spørsmålet: «skifter jeg mental modus mellom disse oppgavene?» Skrive vs. bygge = to rom. Utkast vs. redigering = ett rom med en prosess inni.
4. **Kontekstfiler som beskriver hva AI-en skal *være* i stedet for hva *arbeidet* er.** 30 linjer om personlighet, to linjer om prosjektet. Claude responderer langt mer på kontekst om arbeidet («publikum er mid-market HR-direktører som har prøvd tre andre verktøy og er skeptiske») enn om seg selv. **Fiks:** flipp forholdet — 80 % om arbeidet (hva prosjektet er, publikum, hva som er gjort, hva god output ser ut som, hva man skal unngå), ≤20 % atferds-instruksjon.
5. **Aldri oppdatere kontekstfilene.** Prosjektet utvikler seg, filene sier fortsatt det de sa dag én, output «driver» — folk tror Claude «ble verre». **Fiks:** behandl dem som arbeidsnotater; rediger når prosjektet endrer seg (30 sek per edit — systemets høyest-leverage vane). En «Sist oppdatert»-linje øverst hjelper.
6. **Alt i én flat mappe og håpe `CLAUDE.md` sorterer det.** 50 filer, ingen undermapper, ruting kun på filnavn → Claude leser hele listen og velger ofte feil. **Fiks:** har du mer enn 8–10 filer på samme nivå, trenger du undermapper. Grupper etter workspace, så etter stadium/type. Mappestrukturen *er* arkitekturen.
7. **Bygge hele systemet før du bruker det.** Bygde fabrikken uten å lage et produkt en eneste gang; halvparten av beslutningene matcher ikke hvordan du faktisk jobber. **Fiks:** bygg minimum (én `CLAUDE.md`, ett–to rom, én `CONTEXT.md` hver), begynn å jobbe, legg til det som mangler etter noen dager, fiks det som er galt etter en uke. De beste oppsettene i communityet ble alle bygget inkrementelt.

**Handling for oss:** kjør denne som sjekkliste mot `first system project`. Vår `CLAUDE.md` = ruting + 3-tier-permission (OK, feil 1/2). Feil 3: vi har mange rom — verifiser at hvert er en reell egen arbeidsmodus (jf. `check_system_sync.py`). Feil 4: revider `ROOM.md`/`agent.md` for 80/20-forholdet arbeid vs. atferd. Feil 5: «Sist oppdatert»-linje i alle `ROOM.md`/`CONTEXT`-filer + `autoplan` som sjekker alder. Feil 7: den løpende «bygg bedre for hver dag» ER inkrementell bygging.

**Kategori:** Folder Architecture
