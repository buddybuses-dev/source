# Servere og hosting — lærerike notater

Skrevet ut fra det vi faktisk gjorde da vi satte ThesHit-kurset opp som en 24/7 side du når fra mobilen. Alt her henger sammen med de stegene.

---

## 1. Hva en «server» egentlig er

En server er ikke en spesiell maskin. Det er bare **et program som venter på forespørsler og svarer på dem**.

- **Klient** = den som spør (nettleseren på mobilen din).
- **Server** = programmet som svarer (Python-programmet på PC-en).
- De snakker sammen med protokollen **HTTP**.

Når du åpner `http://localhost:8080/_site/` skjer dette:
1. Nettleseren sender en HTTP-forespørsel: `GET /_site/index.html`
2. Serveren finner fila på disk, leser den, og sender innholdet tilbake.
3. Nettleseren tegner opp siden.

Samme PC kan være både klient og server samtidig. «Server» er en rolle, ikke en ting.

---

## 2. Hva `python -m http.server 8080` gjør

Python har en innebygd mini-webserver. Kommandoen betyr:

| Del | Betydning |
|---|---|
| `python -m http.server` | kjør Python sin innebygde HTTP-server-modul |
| `8080` | lytt på port 8080 |
| `--bind 0.0.0.0` | ta imot forespørsler fra **alle** nettverkskort, ikke bare fra PC-en selv |

Den gjør én enkel ting: **hvilken som helst fil i mappa den startes fra, blir tilgjengelig over HTTP.** Vi startet den i `C:\Users\Mizgin2\ThesHit`, så `study-guide.mp3` inne i en modulmappe blir til URL-en `/02_the-mastery/.../study-guide.mp3`.

Dette kalles en **statisk filserver**. Den kjører ingen kode per forespørsel — den bare leverer filer som allerede finnes. Derfor er den rask, trygg og aldri «nede» av seg selv.

---

## 3. IP-adresser du møtte

En IP-adresse er «postadressen» til en maskin på et nettverk.

| Adresse | Hva det er | Hvem når den |
|---|---|---|
| `127.0.0.1` (aka `localhost`) | «meg selv» — går aldri ut på nettverket | kun PC-en selv |
| `10.0.0.30` | PC-ens adresse på ditt **hjemmenettverk (LAN)** | enheter på samme wifi |
| `0.0.0.0` | ikke en ekte adresse — betyr «lytt på alle mine adresser» | brukes bare når serveren *starter* |
| `100.x.x.x` | adressen Tailscale gir PC-en i ditt private VPN | dine egne Tailscale-enheter, hvor som helst |

Da serveren var bundet til `127.0.0.1` kunne **bare PC-en** åpne siden. Vi endret til `0.0.0.0` for at mobilen skulle slippe til.

---

## 4. Porter — hvorfor `:8080`

En IP-adresse tar deg til riktig maskin. En **port** tar deg til riktig *program* på den maskinen. Tenk på det som leilighetsnummer i en blokk.

- Port 80 = vanlig `http://` (nettleseren antar denne hvis du ikke skriver noe)
- Port 443 = `https://`
- Port 8080 = tradisjonell «test-webserver»-port, valgt fordi 80 ofte krever admin og kan være opptatt

`http://10.0.0.30:8080` betyr: maskin `10.0.0.30`, snakk med programmet som lytter på dør `8080`.

Bare **ett** program kan eie en port om gangen. Prøver du å starte serveren to ganger, feiler den andre med «address already in use».

---

## 5. Hvorfor mobilen på 4G ikke bare når hjem-PC-en

Hjemmenettverket ditt er gjemt bak ruteren med noe som heter **NAT** (Network Address Translation).

- Alle enhetene hjemme deler **én** offentlig IP-adresse utad (den ruteren fikk av internettleverandøren).
- Innenfor har hver enhet en privat adresse (`10.0.0.x`), som ikke betyr noe ute på internett.
- Trafikk som *du* starter innenfra slipper ut og tilbake. Men trafikk som kommer **utenfra og inn** blir stoppet av ruteren, fordi den ikke vet hvilken intern enhet den skal gå til.

Derfor virker `10.0.0.30:8080` på wifi hjemme, men ikke på 4G. Tre vanlige måter å løse det:

1. **Port-videresending** i ruteren — åpner et hull inn til PC-en fra hele internett. Enkelt å sette opp, men eksponerer serveren for alle, og hjemme-IP-en din endres ofte.
2. **Tunnel** (f.eks. Cloudflare Tunnel) — PC-en ringer *ut* til en tjeneste som gir deg en offentlig nettadresse. Ingen ruter-endringer, men siden blir offentlig.
3. **Privat VPN-mesh (Tailscale)** — dine enheter får sitt eget lille private nettverk oppå internett. Bare *du* når PC-en. Dette valgte vi.

---

## 6. Brannmuren — hva regelen gjorde

Windows har en innebygd brannmur som **blokkerer innkommende tilkoblinger** som standard. Det er en sikkerhetsting: selv om et program lytter på en port, slipper ikke fremmed trafikk inn med mindre du sier ja.

Kommandoen:
```
netsh advfirewall firewall add rule name="ThesHit 8080" dir=in action=allow protocol=TCP localport=8080
```
betyr: *lag en regel som slipper inn (`dir=in`) TCP-trafikk til port 8080.*

Uten den ville Python lytte, men mobilen fikk «connection timed out». Merk: dette åpner porten på **alle** nettverkskort, inkludert Tailscale-kortet — derfor trengs den også for VPN-tilgangen.

---

## 7. Tailscale — hva det faktisk er

Tailscale bygger et **privat, kryptert nettverk mellom bare dine egne enheter**, uansett hvor de er.

- Hver enhet du logger inn med samme konto får en fast `100.x.x.x`-adresse.
- Trafikk mellom dem er kryptert (WireGuard-protokollen) og går som regel direkte enhet-til-enhet.
- Ingenting blir offentlig. En fremmed kan ikke «finne» PC-en din — de er ikke i nettverket ditt.
- Det krever bare at appen kjører på begge sider.

Så på mobilen skriver du `http://100.x.x.x:8080/_site/` i stedet for LAN-adressen, og det virker på wifi, 4G, hotellnett, hva som helst — så lenge Tailscale-bryteren er på.

Dette er «VPN» brukt riktig: ikke for å skjule hvor du er, men for å knytte dine egne maskiner sammen som om de sto i samme rom.

---

## 8. Autostart — «hvordan holde den kjørende»

Et program som kjører i et terminalvindu dør når vinduet lukkes, du logger ut, eller PC-en starter på nytt. For at noe skal være «alltid på» trenger du en av disse:

| Mekanisme | Hva det er |
|---|---|
| **Oppgaveplanlegger** (Task Scheduler) | Windows sin «kjør dette programmet ved hendelse X». Vi brukte `SC ONLOGON` = start ved pålogging. |
| **Windows-tjeneste (service)** | Kjører før noen logger inn, i bakgrunnen. Kraftigere, men mer oppsett (f.eks. verktøyet NSSM). |
| **Oppstartsmappe** | Enkleste variant: en snarvei i `shell:startup`. Kjører ved pålogging, men viser et vindu. |

På Linux/servere heter det samme konseptet en **daemon**, styrt av `systemd`. «-d» på slutten av programnavn (som `httpd`, `sshd`) står for daemon.

Vi la også inn `serve_silent.vbs` — et bittelite skript som starter serveren **uten synlig vindu**, så den ikke roter til skjermen.

---

## 9. Strøm og dvale

«24/7» krever at maskinen faktisk er våken 24/7.

- **Dvale/sleep** = PC-en fryser alt og kutter nesten strømmen. Serveren svarer ikke.
- **Skjerm av** = helt greit, serveren kjører videre.
- Derfor: sett dvale til **Aldri** (når tilkoblet strøm). Skjermen kan gjerne slå seg av.
- En bærbar i lokket vil ofte sove uansett — da må du endre «hva skjer når jeg lukker lokket» til «gjør ingenting».

---

## 10. Statisk vs. dynamisk nettside

- **Statisk**: filene finnes ferdige på disk. Serveren sender dem som de er. (ThesHit-siden vår: én stor `index.html` + mp3-filer.)
- **Dynamisk**: serveren *kjører kode* per forespørsel og bygger svaret der og da — henter fra database, sjekker innlogging osv. (WordPress, nettbank, Mighty Networks).

Vi valgte statisk med vilje: ingenting kan «krasje», ingen database å vedlikeholde, ingen sikkerhetshull i egen kode, og alt virker uten internett. Hele «appen» (meny, søk, fremdrift, faner) kjører i nettleseren din som JavaScript. Fremdriften lagres i nettleserens `localStorage` — lokalt på den enheten.

---

## 11. Hvordan lyden streames

Når du trykker play på en mp3 laster ikke mobilen ned hele fila. Nettleseren sender en **Range-forespørsel**:

```
GET /.../study-guide.mp3
Range: bytes=0-65535
```

Serveren svarer med bare den biten (`206 Partial Content`). Spoler du framover, ber den om en ny bit lenger ute i fila. Python sin `http.server` støtter dette fra og med versjon 3.7, derfor virker spoling og «last inn underveis» selv på den store 24-timers samlefila.

---

## 12. Sikkerhet — hva du bør vite

Med oppsettet vårt (Tailscale, ingen port-videresending):

- Serveren er **ikke** synlig på det åpne internett. Bare enheter i ditt Tailscale-nett når den.
- Den serverer **kun lesing** av filer i kursmappa. Ingen kan skrive, slette eller kjøre noe.
- Ingen innlogging på selve siden — men det trengs ikke, siden bare dine egne enheter slipper til.

Hva du **ikke** bør gjøre:
- Ikke sett opp port-videresending i ruteren for denne. Da blir kurset ditt (og alt annet i mappa den serverer) tilgjengelig for hvem som helst som skanner IP-er.
- Ikke server fra en mappe som ligger *over* kurset (f.eks. hele `C:\Users\Mizgin2`), for da eksponerer du alt i den mappa.

---

## 13. Feilsøking — vanlige meldinger

| Melding | Betyr | Fiks |
|---|---|---|
| `address already in use` | porten er opptatt | serveren kjører allerede, eller `taskkill /F /IM python.exe` og start på nytt |
| `connection refused` | ingen server lytter på den porten/adressen | start serveren; sjekk at porten stemmer |
| `connection timed out` | noe blokkerer på veien | brannmur, feil IP, eller Tailscale er av |
| `403 / 404` | serveren svarer, men fila finnes ikke der du spør | sjekk stien; husk `/_site/` på slutten |
| `The requested operation requires elevation` | kommandoen krever admin | åpne terminal som administrator |

---

## 14. Miniordliste

- **HTTP** — språket nettlesere og webservere snakker.
- **Port** — nummerert «dør» inn til ett bestemt program på en maskin.
- **localhost / 127.0.0.1** — maskinen selv.
- **LAN** — ditt lokale nettverk (hjemme-wifi).
- **NAT** — ruteren som deler én offentlig IP på mange interne enheter; grunnen til at «utenfra og inn» er stengt.
- **Brannmur** — filter som bestemmer hvilken nettverkstrafikk som slipper inn/ut.
- **VPN** — krypterte tunneler mellom maskiner; her brukt for å binde sammen *dine egne* enheter (Tailscale).
- **Tunnel** — å la en maskin bak NAT bli nåbar ved at den kobler *ut* til en mellomtjeneste.
- **Daemon / tjeneste** — program som kjører i bakgrunnen hele tiden, uten vindu.
- **Statisk side** — ferdige filer sendes som de er; ingen kode kjøres per forespørsel.
- **Range-forespørsel** — «gi meg bare byte X til Y», grunnlaget for å streame/spole lyd og video.
- **Oppgaveplanlegger** — Windows-verktøyet som starter programmer automatisk ved hendelser (som pålogging).

---

*Kobles til: [[study-guide]] i modulene om Hosting & Deployment (Foundation lag 5), Cloud & Compute (lag 6), og Load Balancing & Scaling (lag 11).*
