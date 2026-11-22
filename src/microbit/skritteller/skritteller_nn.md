---
title: Skritteljar
author: Erik Sagatun
translator: Claude
language: nn
---
# Introduksjon {.intro}

Visste du at mobilen din kan telje skritta dine? Han brukar ein sensor som heiter **akselerometer**, som merkar når han blir rista eller flytta på. micro:biten har akkurat den same sensoren! I denne oppgåva skal vi lage ein skritteljar som du kan feste på skoen eller ha i lomma.

Når du er ferdig, kan du gå ein runde i skulegarden og sjå kor mange skritt du har teke.

# Steg 1: Tel skritt {.activity}

Kvar gong du tek eit skritt, blir micro:biten rista litt. Det brukar vi til å telje.

## Sjekkliste {.check}

- [ ] Opne [MakeCode for micro:bit](https://makecode.microbit.org){target=_blank} og lag eit nytt prosjekt som heiter `Skritteljar`.

- [ ] Gå til `Variablar`{.microbitvariables} og lag ein variabel som heiter `skritt`.

- [ ] Hent blokka `når risting`{.microbitinput} frå `Inndata`{.microbitinput}.

- [ ] Inni ho legg du `endre skritt med 1`{.microbitvariables} og `vis tal`{.microbitbasic}, slik:

```microbit
let skritt = 0
input.onGesture(Gesture.Shake, function () {
    skritt += 1
    basic.showNumber(skritt)
})
```

## Test prosjektet {.flag}

**Last ned koden til micro:biten, eller test i simulatoren ved å klikke på RIST-knappen.**

- [ ] Går talet opp med 1 kvar gong du ristar micro:biten?

- [ ] Kva skjer når talet blir større enn 9? Ser du at det tek lengre tid å vise det?

# Steg 2: Vis talet berre når du vil {.activity}

Når talet blir stort, brukar micro:biten lang tid på å rulle det over skjermen. Medan han gjer det, kan han gå glepp av skritt! Vi lèt han heller blinke kort for kvart skritt, og viser talet først når du trykkjer på knapp A.

## Sjekkliste {.check}

- [ ] Fjern `vis tal`{.microbitbasic} frå `når risting`{.microbitinput}.

- [ ] Legg inn `tenn`{.microbitled}, ein kort `pause`{.microbitbasic} og `sløkk`{.microbitled} i staden. Bruk x = 2 og y = 2, som er lampa i midten.

- [ ] Lag ei ny blokk `når knapp A blir trykt`{.microbitinput} som viser kor mange skritt du har teke:

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

- [ ] Blinkar lampa i midten for kvart skritt?

- [ ] Viser micro:biten rett tal på skritt når du trykkjer A?

# Steg 3: Nullstill teljaren {.activity}

Før ein ny tur er det lurt å starte på null igjen.

## Sjekkliste {.check}

- [ ] Legg til `når knapp B blir trykt`{.microbitinput}.

- [ ] Inni ho brukar du `set skritt til 0`{.microbitvariables} og viser eit ikon, så du ser at det verka:

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

- [ ] Rist nokre gonger, trykk B, og trykk så A. Viser han 0?

# Steg 4: Set deg eit mål {.activity}

No skal skritteljaren feire når du når eit mål, til dømes 100 skritt.

## Sjekkliste {.check}

- [ ] Lag ein ny variabel som heiter `mål`, og set han til 100 i `ved start`{.microbitbasic}.

- [ ] I `når risting`{.microbitinput} brukar du `viss`{.microbitlogic} for å sjekke om `skritt` er lik `mål`.

- [ ] Spel ein melodi med `start melodi`{.microbitmusic} og vis eit glad fjes:

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

- [ ] Endre `mål` til 5 medan du testar, så slepp du å riste 100 gonger.

- [ ] Spelar micro:biten ein melodi og viser eit glad fjes når du når målet?

- [ ] Fest micro:biten og batteripakken på skoen og gå nøyaktig 20 skritt. Kor mange skritt viser han?

## Utfordring {.challenge}

Kan du få skritteljaren til å vise kor langt du har gått i meter? Eit skritt er om lag 0,6 meter for ein elev på mellomtrinnet. Klarer du òg å bruke `radio`{.microbitradio} til å sende skritta dine til ein annan micro:bit, slik at de kan ha skrittkonkurranse i klassen?

## Tips {.protip}

Tel micro:biten for mange eller for få skritt? Prøv `akselerasjon (mg)`{.microbitinput} i staden for `når risting`{.microbitinput}, og tel berre når verdien er større enn ei grense du vel sjølv, til dømes 1500.

## Lagre prosjektet {.save}

Bra jobba! Du har laga din eigen skritteljar. Hugs å lagre prosjektet i MakeCode. Fest micro:biten på skoen eller ha han i lomma, og sjå kor mange skritt du tek i løpet av eit friminutt!
