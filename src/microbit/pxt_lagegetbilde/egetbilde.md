---
title: "PXT: Lag ditt eget bilde"
author: Julie Christina Revdahl
language: nb
---


# Introduksjon {.intro}

I denne oppgaven skal vi se hvor enkelt vi kan lage ett eller flere bilder og
vise dem på micro:biten vår!


# Steg 1: Ved start-klossen {.activity}

## Sjekkliste {.check}

- [ ] Start et nytt PXT-prosjekt, for eksempel ved å gå til
  [makecode.microbit.org](https://makecode.microbit.org/?lang=no){target=blank}.

- [ ] Klossen `ved start`{.microbitbasic} ligger i kodefeltet når vi starter et
nytt prosjekt. Dersom du ikke finner den der, ligger den under kategorien `Basis`{.microbitbasic}.
Alt vi legger inne i klossen `ved start`{.microbitbasic} vil skje med en gang
programmet vårt lastes over på micro:biten vår.


# Steg 2: Vis bilde-klossen {.activity}

## Sjekkliste {.check}

- [ ] Nå vil vi legge til et bilde vi vil at skal vises på micro:biten vår. Vi
går først inn i kategorien `Basis`{.microbitbasic}. Der finner vi klossen
`vis skjerm`{.microbitbasic}, som lar tegne et bilde på egenhånd, ved å velge
hvilke lys som skal tennes. Vi kan også bruke klossen `vis ikon`{.microbitbasic},
men der er bildene allerede tegnet for oss.

- [ ] Legg nå klossen du har valgt inne i `ved start`{.microbitbasic}-klossen.
Tegn i vei dersom du valgt `vis skjerm`{.microbitbasic}-klossen! Om du valgte `vis ikon`{.microbitbasic}-klossen,
kan du bruke den lille pila til å velge blant mange andre bilder.

Vi har valgt å tegne vårt eget bilde, så vår kode ser ut som dette:

  ```microbit
  basic.showLeds(`
    # . # . #
    . # # # .
    # # # # #
    . # # # .
    # . # . #
    `)
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
mellom hvert av bildene. Denne klossen finner du under `Basis`{.microbitbasic}
i menyen.

- [ ] Greier du å få et bilde til å blinke i rytmen til en sang du kan ved å
legge `vis ikon`{.microbitbasic}-klosser og `pause`{.microbitbasic}-klosser
annenhver gang? *Tips: Bruk ulik lengde på pausene mellom* `vis ikon`{.microbitbasic}
*-klossene.*  

- [ ] Nå brukte vi `ved start`{.microbitbasic}-klossen i koden vår, slik at kom
på skjermen med en gang vi lastet over koden. Prøv å bytte ut `ved start`{.microbitbasic}-klossen
med en `gjenta for alltid`{.microbitbasic}-kloss. Hva skjer da?
