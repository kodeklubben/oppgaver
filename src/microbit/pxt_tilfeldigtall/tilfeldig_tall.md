---
title: "PXT: Vis et tilfeldig tall"
author: Julie Christina Revdahl
language: nb
---


# Introduksjon {.intro}

I denne oppgaven er målet å få micro:biten vår til å vise et tilfeldig tall hver
 gang vi trykker på knappen A.


# Steg 1: Finne klossen som registrerer at knapp A trykkes {.activity}

## Sjekkliste {.check}

- [ ] Start et nytt PXT-prosjekt, for eksempel ved å gå til
  [makecode.microbit.org](https://makecode.microbit.org/?lang=no){target=blank}.

- [ ] For at vi skal få noe til å skje, må vi ha en blokk som gjør noe når knapp
 A trykkes inn. Denne klossen finner vi ved å gå i kategorien `Inndata` i menyen
  på venstre side. Klikk på riktig kloss slik at den havner i vinduet du
  programmerer i.

Nå bør koden din se ut som dette:
  ```microbit
  input.onButtonPressed(Button.A, function () {})
  ```

# Steg 2: Lage en variabel {.activity}

## Sjekkliste {.check}

- [ ] Nå vil vi opprette en variabel. I denne variabelen skal vi lagre det
tilfeldige tallet som velges. For å lage en ny variabel må vi inn i kategorien
`Variabler` og så trykke på knappen `Lag en variabel`. Vi kan kalle variabelen vår
hva som helst, men det er best å kalle den noe som forteller oss hva den brukes
 til. Vi vil lagre tilfeldige tall i den, og kaller den derfor `Tall`.


# Steg 3: Sette en variabel til et tilfeldig tall {.activity}

## Sjekkliste {.check}

- [ ] Nå har vi allerede opprettet variabelen `Tall`. Nå vil vi sette denne til
et tilfeldig tall. Dette kan vi gjøre ved å sette sammen klossen `Sett variabel til 0`
fra kategorien `Variabler` med klossen `Velg tilfeldig 0 til 4` fra kategorien
`Matematikk`.


# Steg 4: Sette sammen til en blokk {.activity}

## Sjekkliste {.check}

- [ ] Nå vil vi sette sammen alle klossene fra Steg 1 og Steg 2 til én blokk.
Vi vil at når knapp A trykkes inn, så skal variabelen `Tall` få et tilfeldig
tall. Dette gjør vi ved å sette koden fra Steg 2 inn i klossen vi fant i Steg 1.

 Sett sammen klossene til en blokk som dette:
```microbit
let Tall = 0
input.onButtonPressed(Button.A, function () {
    Tall = Math.randomRange(0, 4)
})
```

# Steg 5: Vise tallet på skjermen {.activity}

## Sjekkliste {.check}

- [ ] Til slutt vil vi at det tilfeldige tallet skal vises på skjermen. Dette
kan enkelt gjøres ved å sette sammen klossen `Vis tall 0` fra kategorien `Basis`
med klossen `Tall` som du finner igjen under `Variabler`. Sett sammen dette med
resten koden din!

Til slutt blir kodeblokken din seende ut som dette:
```microbit
let Tall = 0
input.onButtonPressed(Button.A, function () {
    Tall = Math.randomRange(0, 4)
    basic.showNumber(Tall)
})
```

## Test prosjektet {.flag}

Det er to forskjellige måter vi kan teste micro:bit-programmer på:

- [ ] Til venstre på skjermen er det et bilde av en micro:bit. Dette er faktisk
  en simulator som kan kjøre programmet vi nettopp laget:

  Siden vår kode skal reagere når man trykker på  knapp A på micro:biten kan du
  simulere dette ved å klikke på selve knappen på micro:bit-simulatoren.

- [ ] Enda morsommere er det å teste programmet på micro:biten din! Koble
  micro:biten din til datamaskinen med en USB-kabel. Klikk deretter på knappen
  `Last ned` nede til venstre på skjermen.

  Det lastes nå ned en fil som heter `microbit-Uten-navn.hex` til datamaskinen
  din. Samtidig dukker det opp et vindu som sier at du må flytte denne filen til
  MICROBIT-disken på datamaskinen din.

## Utfordring {.challenge}

- [ ] Greier du å få større variasjon på tallene som velges? Prøv å endre
firetallet i klossen `Velg tilfeldig 0 til 4`. Hva skjer da?

- [ ] Greier du å legge til en lignende kode slik at det samme gjøres når du
trykker på knapp B?

- [ ] Om du har greid utfordringen og fått laget tilfeldig tall når knapp B
trykkes: Greier du å lage en kalkulator som multipliserer de to tilfeldige tallene?
*Tips: Bruk klossen* `0 x 0` *fra kategorien Matematikk og sett inn variablene
du lagret de tilfeldige tallene i.*

- [ ] Man kan også gjøre det om til en lek: Finn en venn og gjett hvilket tilfeldig
tall som dukker opp. Vinneren er den som kommer nærmest.
