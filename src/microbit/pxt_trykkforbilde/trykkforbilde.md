---
title: "PXT: Trykk A for bilde"
author: Julie Christina Revdahl
language: nb
---


# Introduksjon {.intro}

I denne oppgaven skal vi lage et program som viser et bilde når vi trykker på
knapp A.


# Steg 1: Finne klossen for når knapp A trykkes {.activity}

## Sjekkliste {.check}

- [ ] Start et nytt PXT-prosjekt, for eksempel ved å gå til
[makecode.microbit.org](https://makecode.microbit.org/?lang=no){target=blank}.

- [ ] Klossen `når knapp A trykkes`{.microbitinput} ligger under kategorien `Inndata`{.microbitinput}
i menyen til venstre. Alt vi legger inne i klossen, som danner en blokk, vil
skje etter at knapp A trykkes. Vi kan også endre til at ting skal skje når vi
trykker på knapp B eller knapp A+B ved å trykke på den lille pila på klossen.
Klossen for `når knapp A trykkes`{.microbitinput} ser slik ut:

  ```microbit
  input.onButtonPressed(Button.A, function () {

  })
  ```

# Steg 2: Legge til et bilde {.activity}

## Sjekkliste {.check}

- [ ] Nå vil vi legge til et bilde som skal vises på micro:biten vår. Vi
går først inn i kategorien `Basis`{.microbitbasic}. Der finner vi klossen `vis skjerm`{.microbitbasic},
som lar oss tegne et bilde på egenhånd, ved å velge hvilke leds som skal tennes.
Vi kan også bruke klossen `vis ikon`{.microbitbasic}, men der er bildene allerede
tegnet for oss.

- [ ] Legg nå klossen du har valgt inne i `når knapp A trykkes`{.microbitinput}-klossen.
Tegn i vei dersom du valgt `vis skjerm`{.microbitbasic}-klossen! Om du valgte
`vis ikon`{.microbitbasic}-klossen, kan du bruke den lille pila til å velge blant
mange forskjellige bilder. Vi har valgt å bruke et forhåndslagd bilde, så vår
kode ser ut som dette:

  ```microbit
  input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Angry)
  })
  ```


# Steg 3: Legge til flere bilder {.activity}

## Sjekkliste {.check}

- [ ] Nå kan du legge til flere bilder dersom du ønsker det. Da legger du bare
den nye klossen med `vis skjerm`{.microbitbasic} eller `vis ikon`{.microbitbasic}
under den forrige.

- [ ] Sånn! Nå er koden vår ferdig og vi kan gå videre til å teste den.

## Test prosjektet {.flag}

Det er to forskjellige måter vi kan teste micro:bit-programmer på:

- [ ] Til venstre på skjermen er det et bilde av en micro:bit. Dette er faktisk
  en simulator som kan kjøre programmet vi nettopp laget. Siden koden vår kjører
  med en gang kan det hende du må starte simuleringen på nytt med knappen til
  venstre under bildet av micro:biten.

- [ ] Enda morsommere er det å teste programmet på micro:biten din! Koble
  micro:biten din til datamaskinen med en USB-kabel. Klikk deretter på knappen
  `Last ned` nede til venstre på skjermen.

  Det lastes nå ned en fil som heter `microbit-Uten-navn.hex` til datamaskinen
  din. Samtidig dukker det opp et vindu som sier at du må flytte denne filen til
  MICROBIT-disken på datamaskinen din.

## Utfordring  {.challenge}

- [ ] Synes du bildene skifter litt for fort? Prøv å legge inn en `pause`{.microbitbasic}-kloss
mellom hvert av bildene. Denne klossen finner du under `Basis`{.microbitbasic} i menyen.

- [ ] Hva med å legge til et eget bilde for når vi trykker på knapp B? Får du
det til på egenhånd?
