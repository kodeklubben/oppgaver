---
title: testMicrobit
author: Erik Sagatun
language: nb
---
# Introduksjon {.intro}

Vi skal i denne opggaven lage et program som får et lys på micro:biten til å
blinke!


# Steg 1: Tenn et lys {.activity}

*Klossen* `tenn`{.microbitled} *kan bli brukt til å slå på et lys på micro:biten
og klossen* `slukk`{.microbitled} *kan bli bruk til å slå av et lys som er på.
Begge klossene kan du finne i* `Skjerm`{.microbitled}*-kategorien.*

## Sjekkliste {.check}

- [ ] Prøv å se hva som skjer når `tenn`{.microbitled}-klossen brukes inne i en
`ved start`{.microbitbasic}-kloss.

```microbit
led.plot(0, 0)
```

For at lyset skal slå seg av igjen må vi legge til en `slukk`{.microbitled}
blokk. Men vi har jo lyst til å se at lyset faktisk lyser litt først, og da kan
vi legge inn en `pause`{.microbitbasic}-kloss.

- [ ] Legg en `pause`{.microbitbasic}-kloss under `tenn`{.microbitled}-klossen
  og en `slukk`{.microbitled}-kloss under `pause`{.microbitbasic}-klossen.
  `pause`{.microbitbasic}-klossen kan du finne i `Basis`{.microbitbasic}.

- [ ] Sett tallet inne i `pause`{.microbitbasic}-klossen til 1000 (1 sekund).

```microbit
led.plot(0, 0)
basic.pause(1000)
led.unplot(0, 0)
```

## Test prosjektet {.flag}

__Prøv koden i simulatoren for å teste koden så langt.__

- [ ] Hva skjer når du endrer tallene i `tenn`{.microbitled}-klossen og `slukk`{.microbitled}-klossen?
  *Hint: prøv med et tall mellom 0 og 4*

- [ ] Hva skjer når tallene i `tenn`{.microbitled}-klossen er ulike de tallene
  som er i `slukk`{.microbitled}-klossen?


# Steg 2: La det blinke {.activity}

*Det vi har laget til nå blinker lyset en gang, men vi vil jo gjerne at det skal
blinke flere ganger.*

## Sjekkliste {.check}

- [ ] Prøv å få lyset til å blinke mange ganger ved å bruke en løkke. Du må
  kanskje legge til en ekstra pause også.

- [ ] Koden din kan for eksempel se slik ut:

```microbit
basic.forever(function () {
    led.plot(0, 0)
    basic.pause(1000)
    led.unplot(0, 0)
    basic.pause(1000)
})
```

## Test prosjektet {.flag}

- [ ] Last ned programmet til micro:biten og se at lyset slår seg av og på

## Utfordringer {.challenge}

- [ ] Legg til kode slik at flere lys blinker samtidig

- [ ] Få flere lys til å blinke, men med forskjellige hastigheter.
  *Prøv med forskjellige tall i* `pause`{.microbitbasic}*-klossene.*