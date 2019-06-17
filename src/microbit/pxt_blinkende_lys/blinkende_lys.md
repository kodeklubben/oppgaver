---
title: "PXT: Blinkende lys"
author: Helene Isnes
language: nb
---


# Introduksjon {.intro}

Vi skal i denne opggaven lage et program som blinker et lys på micro:biten!


# Steg 1: Tenn et lys {.activity}

*Blokka `tenn` kan bli brukt til å slå på et lys på micro:biten og klossen `slukk` kan bli bruk til å slå av et lys som er på. Begge klossene kan du finne i `Skjerm` kategorien.*

## Sjekkliste {.check}

- [ ] Prøv å se hva som skjer når `tenn`-klossen brukes inne i en `ved start`-kloss

![Blide som viser tenn kloss inni en start kloss](tenn_kloss.png)

For at lyset skal slå seg av igjen må vi legge til en `slukk` blokk. Men vi har
jo også lyst til å se at lyset faktisk lyser litt først, og da kan vi legge inn
en `pause`-kloss.

- [ ] Legg en `pause`-kloss under `tenn`-klossen og en `slukk`-kloss under `pause`-klossen. `pause`-klossen kan du finne i `Basis`.

- [ ] Sett tallet inne i `pause`-klossen til 1000 (1 sekund). 

![Bilde som viser program for tenning og slukking av lys](tenn_og_slukk.png)

## Test prosjektet {.flag}

__Prøv koden i simulatoren for å teste koden så langt.__

- [ ] Hva skjer når du endrer tallene i `tenn`-klossen og `slukk`-klossen? *Hint: prøv med et tall mellom 0 og 4*

- [ ] Hva skjer når tallene i `tenn`-klossen er ulike de tallene som er i `slukk`-klossen?


# Steg 2: La det blinke {.activity}

*Det vi har laget til nå blinker lyset en gang, men vi vil jo gjerne at det skal blinke flere ganger.*

## Sjekkliste {.check}

- [ ] Prøv å få lyset til å blinke mange ganger med å bruke en løkke. Du må kanskje legge til en ekstra pause også.

- [ ] Koden din kan nå for eksempel se slik ut:

![Bilde som viser hvordan vi kan få et lys til å blinke for alltid](blinke_for_alltid.png)

## Test prosjektet {.flag}

- [ ] Last ned programmet til micro:biten og se at lyset slår seg av og på

## Utfordringer {.challenge}

- [ ] Legg til kode slik at flere lys blinker samtidig

- [ ] Få flere lys til å blinke, men med forskjellige hastigheter. *Prøv med forskjellige tall i `pause`-klossene.*
