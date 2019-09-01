---
title: "PXT: Blinkande lys"
author: Helene Isnes
translator: Stein Olav Romslo
language: nn
---


# Introduksjon {.intro}

I denne oppgåva skal me lage eit program som får eit lys på micro:bit-en til å
blinke!


# Steg 1: Tenn eit lys {.activity}

*Me kan bruke klossen* `tenn`{.microbitled} *til å slå på eit lys på micro:biten
og klossen* `slukk`{.microbitled} *til å slå av eit lys som er på. Du finn begge
klossane i* `Skjerm`{.microbitled}*-kategorien.*

## Sjekkliste {.check}

- [ ] Sjå kva som skjer når `tenn`{.microbitled}-klossen ligg inne i ein
  `ved start`{.microbitbasic}-kloss.

```microbit
led.plot(0, 0)
```

For at lyset skal slå seg av att må me leggje til ein `slukk`{.microbitled}-kloss.
Men me vil sjå at lyset er på fyrst, så me legg inn ei `pause`{.microbitbasic}.

- [ ] Legg ein `pause`{.microbitbasic}-kloss under `tenn`{.microbitled}-klossen
  og ein `slukk`{.microbitled}-kloss under `pause`{.microbitbasic}-klossen. Du
  finn `pause`{.microbitbasic}-klossen i `Basis`{.microbitbasic}.

- [ ] Set talet inne i `pause`{.microbitbasic}-klossen til 1000
(1000 millisekund = 1 sekund).

```microbit
led.plot(0, 0)
basic.pause(1000)
led.unplot(0, 0)
```

## Test prosjektet {.flag}

__Prøv koden i simulatoren for å teste koden så langt.__

- [ ] Kva skjer når du endrar tala i `tenn`{.microbitled}-klossen og `slukk`{.microbitled}-klossen?
  *Hint: prøv med eit tal mellom 0 og 4*

- [ ] Kva skjer når tala i `tenn`{.microbitled}-klossen er ulike dei tala som er
  i `slukk`{.microbitled}-klossen?


# Steg 2: La det blinke {.activity}

*Til no får me lyset til å blinke éin gong. Men me vil gjerne at det skal blinke
 fleire gonger.*

## Sjekkliste {.check}

- [ ] Prøv å få lyset til å blinke mange gonger ved å bruke ei løkke. Du må
  kanskje legge til ei ekstra pause.

- [ ] No kan koden din til dømes sjå slik ut:

```microbit
basic.forever(function () {
    led.plot(0, 0)
    basic.pause(1000)
    led.unplot(0, 0)
    basic.pause(1000)
})
```

## Test prosjektet {.flag}

- [ ] Last ned programmet til micro:bit-en og sjå at lyset slår seg av og på.

## Utfordringar {.challenge}

- [ ] Legg til kode slik at fleire lys blinkar samstundes.

- [ ] Få fleire lys til å blinke, men med ulike hastigheiter. *Prøv med ulike
  tal i* `pause`{.microbitbasic}*-klossane.*
