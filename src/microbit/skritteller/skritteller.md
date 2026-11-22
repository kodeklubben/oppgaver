---
title: Skritteller
author: Erik Sagatun
language: nb
---
# Introduksjon {.intro}

Visste du at mobilen din kan telle skrittene dine? Den bruker en sensor som heter **akselerometer**, som merker når den blir ristet eller beveget. micro:biten har akkurat den samme sensoren! I denne oppgaven skal vi lage en skritteller som du kan feste på skoen eller ha i lomma.

Når du er ferdig, kan du gå en runde i skolegården og se hvor mange skritt du har tatt.

# Steg 1: Tell skritt {.activity}

Hver gang du tar et skritt, blir micro:biten ristet litt. Det bruker vi til å telle.

## Sjekkliste {.check}

- [ ] Åpne [MakeCode for micro:bit](https://makecode.microbit.org){target=_blank} og lag et nytt prosjekt som heter `Skritteller`.

- [ ] Gå til `Variabler`{.microbitvariables} og lag en variabel som heter `skritt`.

- [ ] Hent blokken `når ristes`{.microbitinput} fra `Inndata`{.microbitinput}.

- [ ] Inni den legger du `endre skritt med 1`{.microbitvariables} og `vis tall`{.microbitbasic}, slik:

```microbit
let skritt = 0
input.onGesture(Gesture.Shake, function () {
    skritt += 1
    basic.showNumber(skritt)
})
```

## Test prosjektet {.flag}

**Last ned koden til micro:biten, eller test i simulatoren ved å klikke på RIST-knappen.**

- [ ] Går tallet opp med 1 hver gang du rister micro:biten?

- [ ] Hva skjer når tallet blir større enn 9? Ser du at det tar lengre tid å vise det?

# Steg 2: Vis tallet bare når du vil {.activity}

Når tallet blir stort, bruker micro:biten lang tid på å rulle det over skjermen. Mens den gjør det, kan den gå glipp av skritt! Vi lar den heller blinke kort for hvert skritt, og viser tallet først når du trykker på knapp A.

## Sjekkliste {.check}

- [ ] Fjern `vis tall`{.microbitbasic} fra `når ristes`{.microbitinput}.

- [ ] Legg inn `tenn`{.microbitled}, en kort `pause`{.microbitbasic} og `slukk`{.microbitled} i stedet. Bruk x = 2 og y = 2, som er lampen i midten.

- [ ] Lag en ny blokk `når knapp A trykkes`{.microbitinput} som viser antall skritt:

```microbit
let skritt = 0
input.onGesture(Gesture.Shake, function () {
    skritt += 1
    led.plot(2, 2)
    basic.pause(50)
    led.unplot(2, 2)
})
input.onButtonPressed(Button.A, function () {
    basic.showNumber(skritt)
})
```

## Test prosjektet {.flag}

- [ ] Blinker lampen i midten for hvert skritt?

- [ ] Viser micro:biten riktig antall skritt når du trykker A?

# Steg 3: Nullstill telleren {.activity}

Før en ny tur er det lurt å starte på null igjen.

## Sjekkliste {.check}

- [ ] Legg til `når knapp B trykkes`{.microbitinput}.

- [ ] Inni den bruker du `sett skritt til 0`{.microbitvariables} og viser et ikon, så du ser at det virket:

```microbit
let skritt = 0
input.onButtonPressed(Button.B, function () {
    skritt = 0
    basic.showIcon(IconNames.Yes)
    basic.pause(500)
    basic.clearScreen()
})
```

## Test prosjektet {.flag}

- [ ] Rist noen ganger, trykk B, og trykk så A. Viser den 0?

# Steg 4: Sett deg et mål {.activity}

Nå skal skrittelleren feire når du når et mål, for eksempel 100 skritt.

## Sjekkliste {.check}

- [ ] Lag en ny variabel som heter `mål`, og sett den til 100 i `ved start`{.microbitbasic}.

- [ ] I `når ristes`{.microbitinput} bruker du `hvis`{.microbitlogic} for å sjekke om `skritt` er lik `mål`.

- [ ] Spill en melodi med `start melodi`{.microbitmusic} og vis et glad fjes:

```microbit
let skritt = 0
let mål = 100
input.onGesture(Gesture.Shake, function () {
    skritt += 1
    led.plot(2, 2)
    basic.pause(50)
    led.unplot(2, 2)
    if (skritt == mål) {
        music.startMelody(music.builtInMelody(Melodies.PowerUp), MelodyOptions.Once)
        basic.showIcon(IconNames.Happy)
        basic.pause(1000)
        basic.clearScreen()
    }
})
```

## Test prosjektet {.flag}

- [ ] Endre `mål` til 5 mens du tester, så slipper du å riste 100 ganger.

- [ ] Spiller micro:biten en melodi og viser et glad fjes når du når målet?

- [ ] Fest micro:biten og batteripakken på skoen og gå nøyaktig 20 skritt. Hvor mange skritt viser den?

## Utfordring {.challenge}

Kan du få skrittelleren til å vise hvor langt du har gått i meter? Et skritt er omtrent 0,6 meter for en elev på mellomtrinnet. Klarer du også å bruke `radio`{.microbitradio} til å sende skrittene dine til en annen micro:bit, slik at dere kan ha skrittkonkurranse i klassen?

## Tips {.protip}

Teller micro:biten for mange eller for få skritt? Prøv `akselerasjon (mg)`{.microbitinput} i stedet for `når ristes`{.microbitinput}, og tell bare når verdien er større enn en grense du velger selv, for eksempel 1500.

## Lagre prosjektet {.save}

Bra jobbet! Du har laget din egen skritteller. Husk å lagre prosjektet i MakeCode. Fest micro:biten på skoen eller ha den i lomma, og se hvor mange skritt du tar i løpet av et friminutt!
