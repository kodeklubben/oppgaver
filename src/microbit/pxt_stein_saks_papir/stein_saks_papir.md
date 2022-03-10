---
title: "PXT: Stein, saks, papir"
author: Bjørn Hamre, Julie Christina Revdahl
language: nb
---


# Introduksjon {.intro}

Her skal du lære å programmere micro:biten slik at du kan spille stein, saks,
papir med den eller mot den.


# Steg 1: Velge et tilfeldig tall {.activity}

I første del av oppgaven skal vi få micro:biten til å velge et tilfeldig tall
når den ristes. For at du senere skal kunne bruke dette tallet, må tallet lagres
i en variabel.

## Sjekkliste {.check}

- [ ] Start et nytt PXT-prosjekt, for eksempel ved å gå til
  [makecode.microbit.org](https://makecode.microbit.org/?lang=no){target=blank}.

- [ ] Micro:biten skal velge et tilfeldig tall når du rister på den. Til dette
  skal du bruke `når ristes`{.microbitinput}-klossen som finnes i kategorien
  `Inndata`{.microbitinput}.

- [ ] Deretter trenger du en variabel som skal lagre det tilfeldige tallet i.
  Klikk på `Variabler`{.microbitvariables}-kategorien og deretter på knappen
  `Lag en variabel`{.microbitvariables}.Den nye variabelen kan hete hva som helst,
   men her velger vi å kalle den `bildenummer`{.microbitvariables} og klikk `OK`{.microbitvariables}.
   Vi velger å kalle den bildenummer, fordi vi senere vil at tallet som velges
   skal representere et bilde: enten stein, saks eller papir. Du vil se at det
   dukker opp en kloss som heter `bildenummer`{.microbitvariables} i
  `Variabler`{.microbitvariables}-kategorien.

- [ ] Nå vil vi at den nye variabelen vi opprettet skal få en tilfeldig verdi.
  Plasser `sett variabel til 0`{.microbitvariables}-klossen fra `Variabler`{.microbitvariables}-kategorien
  inne i `når ristes`{.microbitinput}-klossen vi fant tidligere. Trykk på den
  lille pilen bak `variabel`{.microbitvariables} og  endre til den nye variabelen
   du lagde - `bildenummer`{.microbitvariables}.

- [ ] For å få micro:biten til å velge et tilfeldig tall hver gang vi spiller,
  kan vi bruke klossen `velg tilfeldig 0 og 4`{.microbitmath} fra `Matematikk`{.microbitmath}-kategorien.
  Koble denne til `sett bildenummer til 0`{.microbitvariables}-klossen i stedet
  for tallet `0`{.microbitvariables}.

- [ ] For å vise hvilket tall som ble valgt kan du sette sammen klossen
`vis tall 0`{.microbitbasic}fra `Basis`{.microbitbasic}-kategorien, og erstatte
`0`{.microbitbasic} med den nye variabelen `bildenummer`{.microbitvariables}.
Denne settes sammen med med de andre klossene slik at programmet ditt ser slik ut:

  ```microbit
  let bildenummer = 0
  input.onGesture(Gesture.Shake, function () {
    bildenummer = Math.randomRange(0, 4)
    basic.showNumber(bildenummer)
  })
  ```

## Test prosjektet {.flag}

Det er to forskjellige måter du kan teste micro:bit-programmer på:

- [ ] Til venstre på skjermen er det et bilde av en micro:bit. Dette er en
  simulator som kan kjøre programmet ditt uten at du trenger å laste det og
  overføre det til din micro:bit:

  Siden din kode skal reagere når du rister på micro:biten kan du simulere dette
  ved å klikke på den hvite prikken til venstre for teksten `SHAKE` på
  micro:bit-simulatoren. Det tilfeldige tallet som ble valgt skal vises på
  skjermen til micro:bit-simulatoren. Prøv flere ganger og se at tallet
  forandrer seg.

- [ ] Enda morsommere er det å teste programmet på micro:biten din! Koble
  micro:biten din til datamaskinen med en USB-kabel. Gi prosjektet ditt et navn,
  for eksempel `stein-saks-papir` i feltet til høyre for `Last ned`-knappen
  nede i venstre hjørne av skjermen. Trykk på `Last ned`-knappen for å laste ned
  programmet.

  Det lastes nå ned en fil som heter `stein-saks-papir.hex` til datamaskinen
  din. Samtidig dukker det opp et vindu som sier at du må flytte denne filen til
  MICROBIT-disken. Dersom du trenger hjelp til dette så spør en av veilederne.


# Steg 2: Vise tallet som ble tilfeldig valgt {.activity}

*Micro:biten skal vise om det er stein, saks eller papir som ble valgt.*

## Sjekkliste {.check}

- [ ] Du har bare tre mulige trekk å velge mellom: stein, saks eller papir. Siden
klossen som velger et tilfeldig tall starter å telle på null, må vi endre den
slik at den enten velger 0, 1 eller 2. Klossen som velger tilfeldig tall, må
derfor velge et tall mellom 0 og 2.

- [ ] Variabelen `bildenummer`{.microbitvariables} skal nå inneholde en av verdiene
0, 1 eller 2. La 0 være stein, 1 være saks og 2 være papir.

- [ ] Vi vil nå vise forskjellige bilder på skjermen, avhengig av hvilket tall
som ble valgt. Vi trenger derfor en `hvis-sann`{.microbitlogic}-kloss fra
kategorien `Logikk`{.microbitlogic}. Vi plasserer denne nederst i blokken fra Steg 1.

- [ ] Den nye `hvis-sann`{.microbitlogic}-klossen skal brukes til å sammenligne
det tilfeldige tallet med 0, 1 og 2 for å kunne vise riktig bilde på skjermen.
Vi vil derfor bytte ut `sann`{.microbitlogic} med en ny kloss. Dette er `0 = 0`{.microbitlogic}-klossen
fra `Logikk`{.microbitlogic}-kategorien.

- [ ] Du skal sammenligne og se om variabelen `bildenummer`{.microbitvariables}
er lik 0. For å få til dette henter vi ut en ny kloss med `bildenummer`{.microbitvariables}
fra kategorien `Variabler`{.microbitvariables}, slik at vi nå har en blokk som
sier `hvis- bildenummer = 0`{.microbitlogic}.

- [ ] Dersom variablen `bildenummer`{.microbitvariables} innholder verdien 0
ønsker vi å vise et bilde av en stein, som bestemt over. Velg klossen `vis ikon`{.microbitbasic}
fra `Basis`{.microbitbasic}-kategorien og velg et bilde som skal representere en
stein. Eventuelt kan du lage bildet selv med `vis skjerm`{.microbitbasic}-klossen.
Plasser klossen inne i `hvis-bildenummer = 0`{.microbitlogic}-blokken

  ```microbit
  input.onGesture(Gesture.Shake, function () {
    bildenummer = Math.randomRange(0, 2)
    basic.showNumber(bildenummer)
    if (bildenummer == 0) {
        basic.showLeds(`
            . . # . .
            . # # # .
            # # # # #
            . # # # .
            . . # . .
            `)
    }
  })
  ```

## Test prosjektet {.flag}

Nå skal du teste programmet ditt ved å trykke på den hvite `SHAKE`-knappen.

- [ ] Hvis tallet `0` velges, vises `0` en kort stund før det erstattes av
  bildet tegnet av en stein.

- [ ] Hvis tallet `1` eller `2` velges, vises kun det valgte tallet. Resten av
  programmet skal du lage nå.


# Steg 3: Vise saks {.activity}

*Tegne saks når tallet 1 blir valgt.*

## Sjekkliste {.check}

- [ ] Du trenger en ny `hvis`{.microbitlogic}-kloss for å tegne en saks når
tallet 1 er valgt. Denne plasseres rett under den forrige `hvis`{.microbitlogic}-klossen.

- [ ] På samme måte som du gjorde med stein, skal du bruke en `0 = 0`{.microbitlogic}-kloss,
men erstatte det venstre `0`{.microbitlogic}-tallet med variabelen `bildenummer`{.microbitvariables}.

- [ ] Du skal vise en saks når variablen `bildenummer`{.microbitvariables}
inneholder tallet 1, så nå må det høyre `0`{.microbitlogic}-tallet erstattes
med et `1`{.microbitlogic}-tall. Programmet ser nå slik ut:

  ```microbit
  input.onGesture(Gesture.Shake, function () {
      bildenummer = Math.randomRange(0, 2)
      basic.showNumber(bildenummer)
      if (bildenummer == 0) {
          basic.showLeds(`
              . . # . .
              . # # # .
              # # # # #
              . # # # .
              . . # . .
              `)
      }
      if (bildenummer == 1) {

      }
  })
  ```

- [ ] Det finnes et ferdig bilde av en saks som du kan bruke. Gå til kategorien
`Basis`{.microbitbasic} for å finne `vis ikon`{.microbitbasic}-klossen. Ved å
trykke på den lille pila, kan du endre hvilket ikon som skal vises.

  ```microbit
  basic.showIcon(IconNames.Scissors)
  ```
## Test prosjektet {.flag}

Før du går videre er det på tide å teste programmet igjen. Det skal vise bildet
av stein hvis `0` blir valgt og saks hvis tallet er `1`. Når tallet `2` blir
valgt vil det ikke vises noe bilde ennå.


# Steg 4: Vise papir {.activity}

*Å Tegne papir når variabelen* `bildenummer`{.microbitvariables} *har verdien 2
blir veldig likt steg 1 du gjorde tidligere.*

## Sjekkliste {.check}

- [ ] Fremgangsmåten for å lage en `hvis`{.microbitlogic}-blokk for når tallet 2
velges, er akkurat den samme som får både stein og saks. Prøv å lage denne selv.
*Husk: Du må bytte ut begge* `0`{.microbitlogic}*-ene i denne blokken også.*

- [ ] Det ferdige programmet skal nå se slik ut:
  ```microbit
  let bildenummer = 0
  input.onGesture(Gesture.Shake, function () {
    bildenummer = Math.randomRange(0, 2)
    basic.showNumber(bildenummer)
    if (bildenummer == 0) {
        basic.showLeds(`
            . . # . .
            . # # # .
            # # # # #
            . # # # .
            . . # . .
            `)
    }
    if (bildenummer == 1) {
        basic.showIcon(IconNames.Scissors)
    }
    if (bildenummer == 2) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    }
  })
  ```


## Test prosjektet {.flag}

Nå kan du teste programmet ditt. Det skal nå vise enten stein, saks eller papir
avhengig av hvilket tall som blir valgt når du trykker på `SHAKE`-knappen.

- [ ] Dersom du laster ned programmet på micro:biten din, bør du koble til en
  strømkilde (spør veilederne) slik at du ikke er uheldig og river ned noe mens du
  rister på den.


# Steg 5: Tømme skjermen mellom hvert spill {.activity}

*Når micro:biten skal velge et tilfeldig tall, kan det samme tallet blir valgt
to ganger på rad. Det kan derfor være vanskelig å vite om det samme tallet ble
valgt igjen, eller om du ikke ristet hardt nok. For å gjøre det enkelt å se, vil
vi tømme skjermen mellom hvert spill.*

## Sjekkliste {.check}

- [ ] Gå til kategorien `Inndata`{.microbitinput} og velg klossen `når knapp A trykkes`{.microbitinput},
og plasser den for seg selv. Den skal ikke henge sammen med den andre kodeblokken.

- [ ] Inne i `når knapp A trykkes`{.microbitinput}-klossen legger du klossen
`tøm skjerm`{.microbitbasic}. Når `A`{.microbitinput}-knappen trykkes skal
micro:biten slå av alle lysene slik at den er klar til nytt spill.

- [ ] Den nye programblokken ser da slik ut:
  ```microbit
  input.onButtonPressed(Button.A, function () {
      basic.clearScreen()
  })
  ```

## Test prosjektet {.flag}

  Nå kan du teste programmet ditt. Det skal nå vise enten stein, saks eller papir
  avhengig av hvilket tall som blir valgt når du trykker på `SHAKE`-knappen.

  - [ ] Dersom du laster ned programmet på micro:biten din, bør du koble til en
    strømkilde (spør veilederne) slik at du ikke er uheldig og river ned noe mens du
    rister på den.

## Utfordring {.challenge}

- [ ] Dersom du ikke ønsker å se tallet på skjermen før bildet tegnes, kan du
  fjerne `vis tall 'bildenummer'`{.microbitbasic}-blokken vi la inn i steg 1.

- [ ] Greier du å slå sammen de tre `hvis`{.microbitlogic}-klossene til bare én?

- [ ] I denne oppgaven har vi brukt at et trykk på knapp A nullstiller skjermen
  til et nytt spill. Greier du å legge all koden inn i samme blokk ved å bruke
  for eksempel en `pause`{.microbitbasic}-kloss og en `tøm skjerm`{.microbitbasic}-kloss?
  Her er det ingen fasit, det er bare å prøve seg fram.

- [ ] Hva med å la micro:biten vise de forskjellige bildene av stein, saks og
  papir før den stopper på den det ble? *Tips: Bruk klossen* `gjenta for bildenummer
  0 til 2`{.microbitloops} *til å først vise alle én gang. Bruk den samme blokken
  igjen for å vise bildenummer fra 0 og opp til bildenummeret som ble valgt
  (vi lagret det i variabelen* `bildenummer`{.microbitvariables}*). I tillegg
  trenger du en  kloss som viser bildene på skjermen som du gjorde i steg 2, 3 og 4!*
