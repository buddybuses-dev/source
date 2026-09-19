# 2.2 One Line of Python Triggers 12k Lines of Code

Kilde: https://www.skool.com/cliefnotes/classroom/036893d9?md=18fb23fa6b084725937e8d47606f376a

**Hele abstraksjons-stacken fra én linje Python ned til elektroner — og hvorfor det betyr
noe for AI.** `print("Hello, World!")` (22 tegn) utløser ~12 000 linjer kode over sju lag:
Python-AST → bytecode → C-interpreter → assembly → maskinkode → mikro-operasjoner → elektroner
(som er fundamentalt probabilistiske). Historisk bue: Jacquard-veven (1804, hullkort), Ada
Lovelace, moth-i-relé (1947 → «debugging»), Pentium FDIV-bugen (1994, $475M recall), kosmisk
stråling som flipper bits (valgmaskin i Belgia 2003: nøyaktig +4096 = 2¹² stemmer; Mario 64
speedrun 2013). **Poeng: hvert lag startet upålitelig og ble pålitelig gjennom arkitektur,
redundans, feilhåndtering og verifikasjon.** AI er bare det nyeste laget — «hallusinasjon»
er dagens «moth i relé». Løsningen er den samme: struktur rundt et probabilistisk system +
menneskelig sjekkpunkt på rett sted. Mappestrukturen og prompt-rammeverket ER slik
ingeniørkunst. = METHOD.md + VERIFICATION.md sitt eksistensgrunnlag.

## Fra videoen (bekreftet + tillegg)

- De sju lagene er egentlig *templates som fylles inn i andre templates* (Python-AST → C-kode med slots → assembly → maskinkode). Hvert lag har egen feilhåndtering (`if call == null …`) — «error handlers built on error handlers all the way down to the quantum floor».
- Kvante-poenget: elektroner *har ikke* definert posisjon før måling (ikke instrument-upresisjon — fundamentalt). Ved små nok transistorer blir quantum tunneling et problem. Vi ingeniørte oss rundt det med toleranser, nok elektroner til statistisk forutsigbarhet, ECC-minne, checksums, paritetsbits, redundans.
- Avslutningen (Ada Lovelace-rammen): «The loom weaves the patterns. The engine weaves the algebra. The computer weaves the logic. And now AI weaves the language. Same pattern, different layer.» Vi er «i moths-in-relays-æraen» for AI.
- Kritikken «AI er bare probabilistisk» bommer fordi kritikerne ikke ser hele stacken — alt under føttene deres er også probabilistisk; vi har bare gjort ingeniørarbeidet allerede.

**Kategori:** Abstraction Series
