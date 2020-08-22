---
title: "PXT: Spill en melodi"
author: Helene Isnes
language: nb
---


# Introduksjon {.intro}

I denne oppgaven skal vi koble micro:biten til hodetelefoner eller en liten
høyttaler og spille av en liten melodi.

Vi trenger litt ekstra utstyr:
- 2 ledninger med krokodilleklemmer
- Hodetelefoner eller 1 buzzer (en liten høyttaler)

Micro:biten har fem store tilkoblinger på brettet, som vi kaller porter. Disse
er koblet til store hull og er merket: 0, 1, 2, 3V og GND, på micro:biten.

![Bilde av en micro:bit og påkoblede krokodilleklemmer](kontakt.png)

GND porten blir brukt for å fullføre en krets. Hvis du holder på GND-porten med
en hånd, kan du programmere micro:biten til å oppdage at du berører 0, 1 eller 2
pinnen med den andre hånden (da bruker du kroppen din til å fullføre en elektrisk
krets). Dette kan du bruke for å få micro:biten til å gjøre eller vise ulike ting.
Du kan også få micro:biten til å sende signaler ut gjennom portene. For eksempel
kan du programmere micro:biten til å sende ut lyd, og kobler du på en høyttaler
med krokodilleklemmer, kan du høre på lyden.

Du kan lese mer om portene på micro:biten her:
[microbit.org](https://microbit.org/no/guide/hardware/pins/){target=blank}


# Steg 1: Grunnkoden {.activity}

## Sjekkliste {.check}

- [ ] Finn `ved start`{.microbitbasic}-klossen. Den ligger allerede i kodefeltet
	ditt, eller du kan finne den i `Basis`{.microbitbasic}-kategorien.

![Bilde av ved start klossen](ved_start.png)

- [ ] Finn `start melodi dadada-daa gjenta en gang`{.microbitmusic}-klossen i
	kategorien `Musikk`{.microbitmusic} og legg den inn i `ved start`{.microbitbasic}.
	Koden din skal nå se slik ut:

```microbit
music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
```

# Steg 2: Velg melodi {.activity}

## Sjekkliste {.check}

- [ ] Klikk på `dadada-daa`{.microbitmusic}. Da dukker det opp en meny med alle
	melodiene du kan velge mellom. Velg en melodi du har lyst til å spille.
	*Du må gjerne teste ut mer enn en melodi!*


# Steg 3: Gjør klart til lyd {.activity}

*Micro:biten har ikke høytalere. Derfor må vi koble til en buzzer eller
hodetelefoner. Måten vi kobler til en buzzer er litt forskjellig fra måten vi
kobler til hodetelefoner. Først kommer en sjekkliste for hvordan du kobler til
en buzzer, og etter det kommer sjekklisten for om du bruker hodetelefoner.*

## Buzzer sjekkliste {.check}

- [ ] Fest en ledning fra port 0 på micro:biten til pinnen som det står pluss
	(+) ved på buzzeren.

- [ ] Fest den andre ledningen fra der det står GND på micro:biten til den andre
	pinnen på buzzeren.

## Hodetelefoner sjekkliste {.check}

- [ ] Fest en ledning fra GND-porten på micro:biten til helt øverst på den
	metaliske delen av hodetelefonene.

- [ ] Fest den andre ledningen fra port 0 på micro:biten til helt nederst på den
	metaliske delen av hodetelefonene.

- [ ] Simulatoren viser hvordan det nå skal se ut:

![Bilde av hvordan man kobler til hodetelefoner](tilkobling_lyd.png)

## Test prosjektet {.flag}

*Nå er det tid for å se om micro:biten klarer å lage lyd!*

- [ ] Last ned prosjektet til micro:biten og lytt!
