---
title: "PXT: Frustrasjon"
author: "Oversatt fra [Code Club UK](https://codeclubprojects.org/en-GB/microbit/frustration/)"
translator: dagfs
language: nb
---


# Introduksjon {.intro}

Dette er et enkelt kordinasjonspill som går ut på å lede en stav med en løkke
langs en bøyd ståltråd. Hvis spilleren kommer borti ståltråden vil en buzzer gi
lyd og såilleren får et poeng. Spilleren med færrest poeng vinner!

Til dette prosjektet trengs det et par ekstra ting:

- Ståltråd

- Krokkodilleklyper

- Treklosser med hull til å stikke ståltråden i.

- Buzzer


# Steg 1: Lagre poeng {.activity}

## Sjekkliste {.check}

- [ ] Start et nytt PXT-prosjekt, for eksempel ved å gå til
  [makecode.microbit.org](https://makecode.microbit.org/?lang=no){target=blank}.

- [ ] Slett de eksisterende blokkende.

![Bilde av start og for alltid blokker som kastes](slett_standard_blokker.png)

- [ ] Vi ønsker å starte et nytt spill når spilleren trykker på knapp A. Til
  dette kan vi bruke `når knapp A trykkes`{.microbitinput}-klossen som finnes i kategorien
  `Inndata`{.microbitinput}.

  ```microbit
    input.onButtonPressed(Button.A, function () {

  })
  ```

  - [ ] Vi må opprette en *variabel* til å ta vare på hvor mange ganger
    spilleren berører ståltråden i løpet av spillet. Vi oppretter variabelen
    `beroering`{.microbitvariables} til dette. Husk det er lurt å unngå *æøå* fordi det fungerer
    ikke i alle tilfeller.

    ![Bilde av hvordan lage en ny variabel](lag_variabel_beroeringer.png)

    ![Bilde av hvordan sette variabelnavn](lag_variabel_beroeringer2.png)

```microbit
    let beroeringer = 0
    input.onButtonPressed(Button.A, function () {
        beroeringer = 0
    })
  ```

  - [ ] Legg til at antall `beroeringer`{.microbitvariables} vises etter at `knapp a`{.microbitinput} er trykket.

```microbit
  let beroeringer = 0
  input.onButtonPressed(Button.A, function () {
      beroeringer = 0
      basic.showNumber(beroeringer)
  })
```


# Steg 2: Oppdatere berøringene {.activity}

## Sjekkliste {.check}

- [ ] Du skal legge til 1 til variabelen `beroeringer`{.microbitvariables} hver gang kontakt P0
  trykkes.

```microbit
  input.onPinPressed(TouchPin.P0, function () {

  })
```

- [ ] Videre skal vi vise et kryss for 1 sekund hver gang kontakt P1 trykkes.

```microbit
input.onPinPressed(TouchPin.P1, function () {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
})
```

```microbit
  input.onPinPressed(TouchPin.P1, function () {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
    music.playTone(262, music.beat(BeatFraction.Whole))
})
```

```microbit
input.onPinPressed(TouchPin.P1, function () {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
    music.playTone(262, music.beat(BeatFraction.Whole))
    basic.pause(500)
})
```

- [ ] Så må du endre verdien til `beroeringer`{.microbitvariables} med 1.

```microbit
input.onPinPressed(TouchPin.P1, function () {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
    music.playTone(262, music.beat(BeatFraction.Whole))
    basic.pause(500)
    beroeringer += 1
})
```

- [ ] Så må vi vise hvor mange ganger vi har berørt.

```microbit
input.onPinPressed(TouchPin.P1, function () {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
    music.playTone(262, music.beat(BeatFraction.Whole))
    basic.pause(500)
    beroeringer += 1
    basic.showNumber(beroeringer)
})
```


# Steg 3: Bygg spillet {.activity}

## Sjekkliste {.check}

- [ ] Ta en bit ståltråd og lag en løkke i den ene enden.

- [ ] Tre løkken i en annen bit ståltråd som du setter i to treklosser med hull
  i.

- [ ] Fest en kabel med ktrokkodilleklyper i P0 på Microbiten til det ene
  beinet på buzzeren og en annen kabel fra GND på Microbiten til det andre
  beinet på buzzeren. *Det har ikke noe å si hvilket bein på buzzeren som
  kobles til hvilken kabel på buzzeren*

![Bilde av to krokodilleklemmer og en buzzer](buzzer.png)

- [ ] Fest en kabel med krokkodilleklyper til P1 på Microbiten og til
  ståltråden med løkke. Fest en kabel til ståltråden som er festet til
  treklossene og til GND på Microbiten.

![Bilde av en buzzwire](buzzwire.png)

![Bilde av en microbit med klemmer på 1, 2 og 2 på GND](microbit.png)

## Utfordring : Legge til egne melodier {.challenge}

- [ ] Klarer du å endre spillet slik at en starter med 3 liv og for hver gang en
  kommer borte i ståltråden reduseres liv med 1? Tips: Det er mulig å bruke
  blokken `game over`{.microbitgame} i kategorien `Spill`{.microbitgame} for å vise en Game over annimasjon
  når spilleren mister det siste livet.
