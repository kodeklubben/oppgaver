---
title: "PXT: Blinkende hjerte"
author: Helene Isnes
language: nb
---


# Introduksjon {.intro}
I denne oppgaven skal vi få et hjerte til å blinke i ulike hastigheter.

# Steg 1: Vi finner "gjenta for alltid"-klossen {.activity}

## Sjekkliste {.check}

- [ ] Trykk på denne lenken for å komme til MakeCode:
      [MakeCode](https://makecode.microbit.org/){target=_blank}.

- [ ] Trykk på nytt prosjekt.

- [ ] Finn en `gjenta for alltid`{.microbitbasic}-kloss. Den ligger nok allerede
i kodefeltet ditt, eller så kan du finne den i menyen under `Basis`{.microbitbasic}.

```microbit
basic.forever(function () {

})
```

Koden som er inni en `gjenta for alltid`{.microbitbasic}-kloss vil gjenta seg så
lenge micro:biten er koblet til strøm (batteri eller PC).


# Steg 2: Hjerte som blinker {.activity}

## Sjekkliste {.check}

- [ ] Gå til `Basis`{.microbitbasic} og finn `vis ikon`{.microbitbasic}-klossen.
  Legg den inni `gjenta for alltid`{.microbitbasic}. Simulatoren til venstre
  skal nå vise et hjerte.

- [ ] Nå skal vi få hjertet til å blinke. Vi gjør dette ved å fjerne bildet fra
  skjermen med `tøm skjermen`{.microbitbasic}-klossen. Den finner du ved å
  trykke på `Basis`{.microbitbasic} og så på `more`{.microbitbasic} (mer) som
  står rett under.

```microbit
basic.forever(function () {
    basic.showIcon(IconNames.Heart)
    basic.clearScreen()
})
```

Kan du se at hjertet blinker? Det skjer ganske fort, for bildet vises og slettes
så raskt som programmet klarer.

# Steg 3: Endre hastighet på blinkingen {.activity}

## Sjekkliste {.check}

For å kontrollere hvor lenge bildet skal vises, og hvor lenge skjermen skal være
blank, legger vi inn pauser.

- [ ] Du finner `pause`{.microbitbasic}-klossen i `Basis`{.microbitbasic}. Legg
  til to `pause`{.microbitbasic}-klosser i koden din.

- [ ] Koden din burde nå se slik ut:

```microbit
basic.forever(function () {
    basic.showIcon(IconNames.Heart)
    basic.pause(100)
    basic.clearScreen()
    basic.pause(100)
})
```

## {.tip}

Hvis du skal bruke samme kloss flere ganger kan du høyreklikke på den og trykke
på __lag kopi__.

## Test prosjektet {.flag}

- [ ] Nå er programmet klart til å lastes ned på micro:biten. For å laste ned
  koden må du først ha koblet micro:biten til datamaskinen med en USB-kabel.
  Klikk deretter på knappen `Last ned` nede til venstre på skjermen. Det lastes
  nå ned en fil som heter `microbit-Uten-navn.hex` til datamaskinen din.
  Samtidig dukker det opp et vindu som sier at du må flytte denne filen til
  MICROBIT-disken på datamaskinen din.


## Utfordring {.challenge}

- [ ] Hva skjer dersom du endrer tallet i `pause`{.microbitbasic}-klossene til
  200? Hva med 1000? 5000? Test det ut! Gjerne prøv med flere tall enn disse.

- [ ] Kan du klare å få hjertet til å blinke i samme tempo som pulsen din?
