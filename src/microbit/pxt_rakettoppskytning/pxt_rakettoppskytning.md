---
title: "PXT: Rakettoppskytning"
author: Helene Isnes
language: nb
---


# Introduksjon {.intro}
Her skal vi først telle ned fra fem, og så lage en animasjon av en rakett som
flyr av gårde.


# Steg 1: Nedtelling {.activity}

Først skal vi lage nedtelleren. Du vil at tallet 5 skal vises i ett sekund, så
4, så 3 osv. Dette kan du få til ved å bruke en kombinasjon av blokkene
`vis tall`{.microbitbasic} og `pause`{.microbitbasic} fra `Basis`{.microbitbasic}-kategorien.


## Sjekkliste {.check}

- [ ] Få micro:biten til å telle ned fra 5. *Husk at 1000 ms er det samme som 1 sekund*

- [ ] Koden burde nå se slik ut:

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

Nå som vi har fått til nedtellingen trenger vi en rakett. Min rakett ser slik ut:

```microbit
basic.showLeds(`
    . . # . .
    . # # # .
    . # # # .
    # # # # #
    . # # # .
    `)
```

Du kan designe raketten din akkurat som du vil. Denne skal også legges inne i
`ved start`{.microbitbasic}-klossen etter selve nedtellinge.


## Sjekkliste {.check}

- [ ] For å skape et inntrykk av at raketten skytes opp, tegner du nye bilder på
skjermen hele tiden slik at det ser ut som om raketten flytter seg litt og litt.
Bildene du tegner legger du etter koden i steg 1.

Eksempel på bilder du kan ende opp med:

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


# Videre arbeid {.activity}

- [ ] Synes du noe går for fort? Legg til et par `pause`{.microbitbasic}-klosser
  da vel!

- [ ] Kanskje raketten trenger noen flammer etter seg? Kanskje den faller ned
  igjen? Eller kanskje det skal komme en ny rakettoppskytning hver gang du
  trykker A? Her er det bare fantasien som setter grenser, og husk at det er lov
  å leke seg!


## Utfordring {.challenge}

- [ ] Kan man løse nedtellingen med løkker? Hvordan?
