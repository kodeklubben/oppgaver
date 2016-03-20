---
title: Donkey Kong
level: 4
author: Geir Arne Hjelle
---

# Introduksjon {.intro}

Donkey Kong var det første virkelig plattform-spillet da det ble gitt
ut i 1981. I tillegg til Donkey Kong var det også her vi første gang
ble kjent med Super Mario (som het Jumpman den gang). I spillet styrer
vi Super Mario mens han prøver å redde kjæresten sin fra Donkey Kong,
og må passe seg for tønner og ildkuler mens han hopper mellom
plattformer.

![](donkey_kong.png)

# Oversikt over prosjektet {.activity}

*Mesteparten av kodingen av Donkey Kong skal du gjøre selv. Underveis
 vil du lære hvordan du lager et enkelt plattform-spill i Scratch.*

## Plan {.check}

+ Hvordan styre en plattform-helt som kan hoppe?

+ Plattformer

+ Donkey Kong og rullende ildkuler

+ .. og andre utfordringer

# Steg 1: En hoppende helt {.activity}

*Den viktigste delen av et godt plattform-spill er å ha en helt man
 kan styre rundt og hoppe fra plattform til plattform med.*

I denne delen skal vi konsentrere oss om hvordan vi kan styre
heltefiguren, og spesielt hvordan vi får den til å hoppe og falle på
en troverdig måte.

## Sjekkliste {.check}

+ Start et nytt prosjekt.

+ For å kunne teste at heltefiguren oppfører seg som vi vil trenger vi
  en enkel plattform. Tegn en ny bakgrunn. Velg å tegne med
  `Vektorgrafikk`. Tegn en smal, lang boks nederst på skjermen. Fyll
  den med en farge forskjellig fra linjefargen.

  ![](plattform.png)

+ Velg eller lag deg en figur du ønsker å bruke som den hoppende
  helten du skal styre. Om du ikke bruker Scratch-katten så slett
  denne. Kall figuren `SuperMario`. Sannsynligvis vil vi gjøre figuren
  mindre slik at vi får plass til flere plattformer på sjermen. Dette
  kan du gjøre med kode som kun kjører i det du starter spillet, for
  eksempel:

  ```blocks
      når grønt flagg klikkes
      sett størrelse til (40) %
  ```

+ Vi trenger to variabler som vi skal bruke til å kontrollere
  bevegelsen til `SuperMario`. Lag to variabler, `(fartX)`{.b} og
  `(fartY)`{.b}. Pass på at begge gjelder kun _for denne figuren_.

+ I hovedløkken som styrer `SuperMario` vil vi først endre litt på
  disse `fart`{.blockdata}-variablene, og til slutt flytte selve
  figuren basert på dem.

  Dersom ingenting påvirker figuren vår vil vi at `(fartX)`{.b} skal
  gå mot 0 (farten bremses), mens vi vil at `(fartY)`{.b} skal bli et
  stadig større negativt tall (figuren faller). Men om figuren står på
  plattformen skal `(fartY)`{.b} være 0 (figuren står i ro). Dette kan
  vi kode omtrent som følger:

  ```blocks
      når jeg mottar [nytt spill v]
      gå til x: (-150) y: (-100)
      for alltid
          sett [fartX v] til ((0.8) * (fartX))  // farten bremses
          endre [fartY v] med (-0.5)  // gravitasjon, figuren faller
          hvis (berører fargen [#0000ff])  // figuren står på plattformen
              sett [fartY v] til [0]
          slutt
          endre x med (fartX)  // flytt selve figuren
          endre y med (fartY)
      slutt
  ```

+ Om du prøver spillet ditt så langt (husk å legge til et skript på
  bakgrunnen som sender en `nytt spill`-melding når det grønne flagget
  klikkes), vil du se at figuren din faller ned til plattformen. Men
  du kan ikke kontrollere den.

+ For å styre `SuperMario` legger vi flere
  `hvis`{.blockcontrol}-tester inn i hovedløkken. For eksempel kan du
  få figuren til å bevege seg mot venstre ved å legge til dette rett
  før `endre x med (fartX)`{.b}:

  ```blocks
      hvis (tast [pil venstre v] trykket?)
          pek i retning (-90 v)
          sett [fartX v] til [-5]
          neste drakt
      slutt
  ```

  Lag også en tilsvarende blokk for å flytte figuren mot høyre.

+ Vi vil også at `SuperMario` hopper når vi trykker på `pil
  opp`-tasten. Her må vi være litt forsiktig, siden vi bare vil at
  figuren kan hoppe hvis den står på en plattform (ikke når den
  allerede hopper). En enkel måte å få til dette på er å legge `pil
  opp`-testen inne i testen for om figuren står på plattformen:

  ```blocks
      hvis (berører fargen [#0000ff])  // gammel kode: figuren står på plattformen
          sett [fartY v] til [0]
          hvis (tast [pil opp v] trykket?)  // ny kode: figuren hopper
              sett [fartY v] til [5]
          slutt
      slutt
  ```

Vi har nå et bra utgangspunkt for et plattformspill. Nemlig en figur
som vi kan styre rundt, og som kan hoppe når vi vil det. Lek litt med
`SuperMario` og tallene vi har brukt i `sett [fart_ v] til
[]`{.b}-klossene slik at du får en bevegelse du synes virker naturlig.

+ Du har kanskje oppdaget at `SuperMario` av og til tilsynelatende
  faller delvis _gjennom_ plattformen? Hvis ikke, prøv å slipp ham fra
  toppen av skjermen. Den følgende testen fikser dette ganske greit:

  ```blocks
      hvis (berører fargen [#009900])
          endre y med (2)
      slutt
  ```

  Dette var også grunnen til at vi fylte plattformen med en annen
  farge enn linjefargen.

# Steg 2: Plattformer og stiger {.activity}


# Steg 3: Donkey Kong og rullende ildkuler {.activity}


# Steg 4: Videreutvikling av spillet {.activity}

*Du har nå laget en enkel variant av Donkey Kong. Men prøv å gjøre
 spillet morsommere ved å videreutvikle det. Du bestemmer selv hvordan
 du vil jobbe videre, men nedenfor er noen ideer som kanskje kan være
 til inspirasjon?*

## Ideer til videreutvikling {.check}

