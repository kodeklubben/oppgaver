---
title: "PXT: Rakettoppskyting"
author: Helene Isnes
translator: Stein Olav Romslo
language: nn
---


# Introduksjon {.intro}

Her skal me fyrst telje ned frå fem, og så lage ein animasjon av ein rakett som
flyg av garde.


# Steg 1: Nedteljing {.activity}

Fyrst skal me lage nedteljinga. Du vil få talet __5__ til å visast i eitt sekund,
så __4__, __3__, osv. Dette kan du få til ved å bruke ein kombinasjon av klossane
`vis tal`{.microbitbasic} og `pause`{.microbitbasic} frå `Basis`{.microbitbasic}-kategorien.

## Sjekkliste {.check}

- [ ] Få micro:bit-en til å telje ned frå 5. *Hugs at 1000 ms er det same som 1
  sekund*

- [ ] Koden burde sjå slik ut:

```microbit
basic.showNumber(5)
basic.pause(1000)
basic.showNumber(4)
basic.pause(1000)
basic.showNumber(3)
basic.pause(1000)
basic.showNumber(2)
basic.pause(1000)
basic.showNumber(1)
basic.pause(1000)
```


# Steg 2: Raketten {.activity}

No som me har fått til nedteljinga treng me ein rakett. Raketten min ser slik
ut:

```microbit
basic.showLeds(`
    . . # . .
    . # # # .
    . # # # .
    # # # # #
    . # # # .
    `)
```

Du kan designe raketten din akkurat slik du vil.

## Sjekkliste {.check}

- [ ] For å skape inntrykket av at raketten blir skote opp teiknar me nye bilete
  på skjermen slik at det ser ut som raketten flyttar seg litt og litt. Bileta
  du teiknar legg du etter koden frå steg 1.

Døme på bilete du kan bruke:

```microbit
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . # . .
    `)
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . # . .
    . # # # .
    `)
basic.showLeds(`
    . . . . .
    . . . . .
    . . # . .
    . # # # .
    . # # # .
    `)
basic.showLeds(`
    . . . . .
    . . # . .
    . # # # .
    . # # # .
    # # # # #
    `)
basic.showLeds(`
    . . # . .
    . # # # .
    . # # # .
    # # # # #
    . # # # .
    `)
basic.showLeds(`
    . # # # .
    . # # # .
    # # # # #
    . # # # .
    . . . . .
    `)
basic.showLeds(`
    . # # # .
    # # # # #
    . # # # .
    . . . . .
    . . . . .
    `)
basic.showLeds(`
    # # # # #
    . # # # .
    . . . . .
    . . . . .
    . . . . .
    `)
basic.showLeds(`
    . # # # .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)
```

# Vidare arbeid {.activity}

- [ ] Synest du noko går for fort? Legg til eit par `pause`{.microbitbasic}-klossar
  då vel!

- [ ] Kanskje raketten treng nokre flammer etter seg? Kanskje den fell ned att?
  Eller skal det kome ei ny oppskyting kvar gong du trykkar A? Her er det berre
  fantasien som set grenser, og hugs at det er lov å leike seg!

## Utfordring {.challenge}

- [ ] Kan du løyse nedteljinga med løkker? Korleis?
