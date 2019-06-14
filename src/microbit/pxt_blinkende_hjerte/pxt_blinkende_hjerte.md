---
title: "PXT: Blinkende hjerte"
author: Helene Isnes
language: nb
---


# Introduksjon {.intro}
I denne opggaven skal vi få et hjerte til å blinke i ulike hastigheter. 


# Steg 1: Vi finner "gjenta for alltid"-klossen {.activity}

## Sjekkliste {.check}

- [ ] Finn en `gjenta for alltid`-kloss. Den ligger nok allerede i kodefeltet ditt, eller så kan du finne den i menyen under `Basis`. 

![Bilde for å vise gjenta for alltid klossen](gjenta_for_alltid.png)

Koden som er inni en `gjenta for alltid`-kloss vil gjenta seg så lenge micro:biten er koblet til strøm (batteri eller PC).


# Steg 2: Hjerte som blinker {.activity}

## Sjekkliste {.check}

- [ ] Gå til `Basis` og finn `vis ikon`-klossen. Legg den inni `gjenta for alltid`. Simulatoren til venstre skal nå vise et hjerte. 

- [ ] Nå skal vi få hjertet til å blinke. Vi gjør dette ved å fjerne bildet fra skjermen med `tøm skjermen`-klossen. Den finner du ved å trykke på `Basis` og så på `more` (mer) som står rett under. 

![Bilde for å vise koden for blinkende hjerte](blinkende_hjerte.png)

Kan du se at hjertet blinker? Det skjer ganske fort, for bildet vises og slettes så raskt som programmet klarer. 

# Steg 3: Endre hastighet på blinkingen {.activity}

## Sjekkliste {.check}

For å kontrollere hvor lenge bildet skal vises, og hvor lenge skjermen skal være blank, legger vi inn pauser. 

- [ ] Du finner `pause`-klossen i `Basis`. Legg til to `pause`-klosser i koden din.

- [ ] Koden din burde nå se slik ut:

![Bilde for å vise koden for blinkende hjerte med pauser](blinkende_hjerte_med_pauser.png)


## {.tip}

Hvis du skal bruke samme kloss flere ganger kan du høyreklikke på den og trykke på lag kopi. 

## Test prosjektet {.flag}

- [ ] Nå er programmet klart til å lastes ned på micro:biten. For å laste ned koden må du først ha koblet micro:biten til datamaskinen med en USB-kabel. Klikk deretter på knappen `Last ned` nede til venstre på skjermen. Det lastes nå ned en fil som heter `microbit-Uten-navn.hex` til datamaskinen din. Samtidig dukker det opp et vindu som sier at du må flytte denne filen til MICROBIT-disken på datamaskinen din.


## Utfordring {.challenge}

- [ ] Hva skjer dersom du endrer tallet i `pause`-klossene til 200? Hva med 1000? 5000? Test det ut! Gjerne prøv med flere tall enn disse. 

- [ ] Kan du klare å få hjertet til å blinke i samme tempo som pulsen din?
