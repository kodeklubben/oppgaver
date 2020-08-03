---
title: Parkeringsplass
author: "Oversatt fra [Espen Clausen nettside](https://espenec.files.wordpress.com/2015/09/lego-mindstorms-del-3-4.pdf)"
translator: Øistein Søvik
language: nb
---


# Parkeringsplass {.intro}

De aller fleste moderne biler, har en fantastisk nyvinning som kalles
ryggesensor. Ryggesensoren er en ultralydsensor plassert flere steder bak på
bilen. De piper når de nærmer seg andre objekter som vegger, gjerder og andre
biler. Jo nærmere bilen kommer andre objekter, jo oftere piper den.

Vi har konstruert en liten parkeringsplass til roboten. Den ligner litt på en
garasje, fordi det er høye vegger rundt den. Alt du skal gjøre er å parkere
roboten på parkeringsplassen. Du må konstruere og programmere roboten slik at
den ved hjelp av ultralydsensor er i stand til å parkere roboten på
parkeringsplassen.

Roboten skal starte fra en gitt strek, gjerne så langt som 5 meter unna, og
kjøre bort til parkeringsplassen, snu, og deretter rygge inn på plass.

## Fremgangsmåte {.check}

- [ ] Konstruer roboten slik at ultralydsensoren står bak på roboten. Pass på
  ultralydsensoren slik at den ikke står veien for andre deler på roboten, og
  med en høyde som gjør at den oppdager hindrene.

- [ ] Koble til Ultralydsensoren til EV3 roboten ved hjelp av en kabel. Kabelen
  skal kobles til en av portene merket med 1-4.

- [ ] Programmer roboten til å kjøre fram 1 sekund. Mål deretter hvor langt den
  kjører.

- [ ] Lag en tabell, der du skriver inn hvor langt den kjører på 1,2 og 4
  sekund.

| Tid       | 1 sekund | 2 sekund | 4 sekund |
| :-------- | -------: | -------: | -------: |
| Strekning |       cm |       cm |       cm |
|           |          |          |          |

- [ ] Regn ut hvor mange sekunder roboten bruker på å kjøre fra start til
  punktet hvor den må snu.

- [ ] Programmer roboten til å snu, slik at den er i stand til å rygge på plass.
  Det er flere muligheter å løse dette på, og det er ikke sikkert første innfall
  er det enkleste og beste.

- [ ] Roboten skal rygge inn på parkeringsplassen. Ryggesensoren skal
  kontrollere ryggingen, og stoppe roboten 2 cm fra veggen bak i garasjen.
