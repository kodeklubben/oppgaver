---
title: "PXT: Tikkende bombe"
author: Kolbjørn Engeland og Julie Revdahl

language: nb
---



# Introduksjon {.intro}

Kjenner du "Tikkende-bombe" -spillet? Du kaster rundt en leke-bombe mens en klokke teller ned og
personen som holder den når tiden er ute, taper... Det er veldig morsomt.

I dette prosjektet vil vi bygge et lignende type spill, men i stedet bruker vi en virtuell bombe og micro:bit radio.
Den virtuelle bomben er en tall-variabel som teller ned til __0__, og vi skal sende dette tallet mellom flere micro:biter.
Den som har den virtuelle bomben når vi kommer til __0__ taper. Vi kan sende tall ved hjelp av radioblokkene.

![Bilde av en microbit som viser en bombe](bombe.png )

# Steg 1: Vi starter spillet {.activity}

_Vi begynner med å vise et tall når vi rister på micro:biten._

## Sjekkliste {.check}

- [ ] Start et nytt PXT-prosjekt, for eksempel ved å gå til
      [makecode.microbit.org](https://makecode.microbit.org/?lang=no){target=blank}.

Hva betyr det å ha et tall som representerer en bombe? Vi kan lage en bombe-klokke som er et tall som sendes
mellom micro:bitene ved hjelp av radioen. Bombeklokka skal telle ned, og når den blir __0__, skal den ringe.

Vi starter med å kode interaksjonen mellom micro:biten og spillerne. Vi vil da at spillet starter og den første
bomben sendes ved å trykke på A+B-knappen. Når en bombe er mottatt, viser skjermen et bilde av bomben,
og når spilleren rister på micro:biten sendes bomben til den neste spilleren.

- [ ] Lag en variabel `bombe`{.microbitvariables} og sette den til __-1__ inne i `ved start`{.microbitbasic} -blokken.

- [ ] For at micro:biten skal vite hvem den skal sende til og få tall fra må dere lage en felles radiokanal.
      Dette kan du gjøre ved å velge `radio sett gruppe`{.microbitradio} fra `Radio`{.microbitradio}-kategorien.
      Du kan velge et tall fra __0__ til __255__, og de som skal spille sammen må velge samme tall.

```microbit
let bombe = -1
radio.setGroup(5)
```

- [ ] For å starte spillet, trykker vi på `A+B`{.microbitinput}-knappen, og gir et positivt tall til `bombe`{.microbitvariables}-variabelen. For å gjøre
      spillet mindre forutsigbart, bruker vi `velg tilfeldig`{.microbitmath}- kloss fra `Matematikk`{.microbitmath}-kategorien for å gi
      `bombe`{.microbitvariables}-variabelen en verdi mellom __10__ og __20__:

```microbit
input.onButtonPressed(Button.AB, function () {
    bombe = Math.randomRange(10, 20)
})
```

- [ ] For å sende en bombe kan vi riste micro:biten. Hvis `bombe`{.microbitvariables}-variabelen er positiv, har vi bomben og vi kan
      sende den. Etter å ha sendt den, setter vi `bombe`{.microbitvariables}-variabelen til __-1__ siden vi ikke har den lengre.

```microbit
input.onGesture(Gesture.Shake, function () {
    if (bombe > 0) {
      radio.sendNumber(bombe)
        bombe = -1
  }
})
```

- [ ] Mottak av bombe gjøres med en `når radio mottar`{.microbitradio} -blokk. `recievedNumber`{.microbitvariables} representerer bomben og
      lagres i `bombe`{.microbitvariables}-variabelen.

```microbit
radio.onReceivedNumber(function (receivedNumber) {
    bombe = receivedNumber
})
```

Nå kan vi gå i gang med å kode selve klokka som teller ned til __0__. Dette gjør vi ved å bruke en `gjenta for alltid`{.microbitbasic} blokk
der `bombe`{.microbitvariables}-variabelen teller ned til __0__. Inne i denne blokken må vi sjekke hvilken verdi `bombe`{.microbitvariables}-variabelen har, slik at vi
viser bombe-ikon og teller ned kun når vi har bomben (dvs `bombe`{.microbitvariables}-variabelen er positiv) og stopper nedtellingen og viser
et hodeskalle-ikon når vi kommer til __0__.

- [ ] Vi kan legge til en klokke med `gjenta for alltid`{.microbitbasic}-blokken.
- [ ] Hvis `bombe`{.microbitvariables}-variabelen er lik __0__: KABOOM! du tapte, og vi viser en hodskalle!
- [ ] Hvis `bombe`{.microbitvariables}-variabelen er negativ (`bombe`{.microbitvariables} < __0__), har vi ikke bomben, så vi tømmer skjermen.
- [ ] Hvis `bombe`{.microbitvariables}-variabelen er positiv (`bombe`{.microbitvariables} > __0__), viser vi et bombe-bilde og reduserer variabelen med __1__.

```microbit
let bombe = 0
basic.forever(function () {
    if (bombe < 0) {
        basic.clearScreen()
    }
    if (bombe == 0) {
        basic.showIcon(IconNames.Skull)
    }
    if (bombe > 0) {
        basic.showIcon(IconNames.Target)
        bombe += -1
    }
})
```

## Test prosjektet {.flag}

Det er to forskjellige måter vi kan teste micro:bit-programmer på:

- [ ] Til venstre på skjermen er det et bilde av en micro:bit. Starter du å teste her vil du få opp to bilder av
      micro:bit og kan teste ut med å sende bomben mellom disse.

- [ ] Du og en venn kan laste opp koden på hver deres micro:bit. Den som starter spillet trykker på A+B
      og rister på micro:biten for å sende den videre. Hvem taper? Hva skjer hvis flere spillere er på samme kanal?