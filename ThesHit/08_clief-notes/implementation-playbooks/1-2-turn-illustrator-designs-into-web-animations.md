# 1.2 Turn Illustrator Designs into Web Animations

Kilde: https://www.skool.com/cliefnotes/classroom/d3907117?md=815d6b2b88d84a46a2eb96434c67bb6e

**SVG-basert workflow: ta ferdig-tegnede assets fra Illustrator/Figma og gjør dem til
animerte, redigerbare komponenter du styrer med naturlig språk.** I motsetning til 1.1
(bygg fra spec) starter du her med designs som allerede finnes. **Hvorfor SVG:** SVG-filer
er i praksis HTML — tekstfiler som beskriver former, farger, posisjoner. Claude kan lese,
redigere og animere dem direkte. PNG/JPG er flate bilder Claude ikke kan jobbe med på samme
måte. Øyne som blinker, uttrykk som skifter, elementer som animerer på signal — alt redigerbart
med ren engelsk.

## Fra videoen (transkribert)

- **Ekte case:** en kompis' Illustrator-storyboard for skolen skulle bli et nettsted med custom animerte karakterer (mikro-uttrykk, blunking, karakterer som «henger sammen»). Professoren (elsket design, ikke AI-skeptiker) trodde ikke AI kunne lage *redigerbare, itererbare* animasjoner fra originale Illustrator-filer. Jake tok det som en utfordring.
- **Forberedelse:** de re-labelte SVG-lagene (`left-iris`, `right-eye`, `eyebrow-left` …) så AI-en *vet* hva hver del er uten å måtte ta screenshot og gjette. Lastet ned hele storyboardet som én SVG.
- **To skills kreves:** Remotion-skill (React-animasjoner programmatisk) + **UI/UX Pro-skill** (får front-end/nettsted til å se profesjonelt ut, ikke «vibe-coded» — «enklere å fange den opp som skill enn å prompte Claude i hjel»).
- **Struktur:** hver scene er en React-komponent som refererer *komponenter* for karakterene (hode, farger, emotion-profiler, blunke-timing, iris-hastighet per karakter — «joy», «fear» osv.). En `project.md` (lest som `CLAUDE.md`) peker på hvilke mapper og hvor original-SVG-en ligger, så Claude ikke må lese hele kodebasen for en liten endring.
- **Poenget — refinert redigering:** «jeg liker ikke øynene på *sadness*» → Claude går bare inn i den ene komponenten, finner iris-hastigheten for den emotionen og endrer den, uten å ødelegge resten. Kontrast: bilde-genererende AI må gjøre om hele videoen/seksjoner hver gang. Ferdig scene → «kast den karakteren inn i React-front-end-nettstedet».
- Bygget på **3 timer** (uker manuelt). «Appless work is now possible» — ingen Adobe Illustrator nødvendig etter start-SVG-en; alt arbeid skjer i en mappe med naturlig språk. Men Illustrator-basen og design-nyansene *var fortsatt påkrevd*.

**Relevans for oss:** «re-label lagene så AI-en vet hva ting er» = navnekonvensjoner (Foundation 3.1). `project.md` som ruter til rett mappe = `ROOM.md`. «Refinert redigering av én komponent» = hvorfor komponent-/fil-separasjon i `rooms/production/` sparer tokens og unngår regresjon. `rooms/marketing/ui-ux-pro-max/` (gitignorert i repoet) ER denne UI/UX Pro-skillen.

**Kategori:** Playbooks — Animasjon
