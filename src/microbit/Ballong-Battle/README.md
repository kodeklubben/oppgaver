---
title: "PXT: BallongBattle"
author: "Sigurd Schaathun"
language: "nb"
---


# Om oppgaven {.activity}

I denne oppgaven skal vi lage fjernstyring til Bit:Bot som kommer i Super:bit-pakken. Til slutt skal elevene kjøre BallongBattle der poenget er å sprekke andres ballonger mens de beskytter sin egen. Ballongene festes på Bit:Bot - det holder som regel å dytte den nedi pennehullet, og en knappenål limes fast på fronten av bit:bot med tape.

## Oppgaven passer til: {.check}

 **Fag**: Matematikk, Naturfag

**Anbefalte trinn**: 5.- 10.

**Tema**: Fjernstyring, motorer

**Tidsbruk**: 45 - 90 minutter

## Kompetansemål {.challenge}

- [ ] **Matematikk, 5. trinn**:  lage og programmere algoritmar med bruk av variablar, vilkår og lykkjer

- [ ] **Naturfag, 7. trinn**:  utforske, lage og programmere teknologiske systemer som består av deler som virker sammen

- [ ] **Naturfag, 10. trinn**:  utforske, forstå og lage teknologiske systemer som består av en sender og en mottaker


## Forslag til læringsmål {.challenge}

- [ ] Elevene kan lage program og fjernstyre en Bit:Bot med Micro:Bit.

## Forslag til vurderingskriterier {.challenge}

Det er mange ulike måter man kan vurdere et programmeringsprosjekt, og her må en
selv vurdere hva som er den beste måten ut ifra hvilket fag man jobber i,
hvilken aldergruppe og hviklet nivå elevene er på, hva man ønsker å teste og
hvor mye tid man har til rådighet til å jobbe med prosjektet. I vårt
[lærerdokument](https://github.com/kodeklubben/oppgaver/wiki/Hvordan-undervise-i-og-vurdere-programmering){target=_blank} har vi blant
annet beskrevet ulike måter dette kan gjøres på, tillegg til en del andre
nyttige tips til hvordan man underviser i programmering.

## Forutsetninger og utstyr {.challenge}

- [ ] **Forutsetninger**: Elevene må ha programmert noe før. Det er best for en mindre gruppe, for å ha en bit:bot til hver.

- [ ] **Utstyr**: Super:Bit (20 microbit, 10 Bit:Bot), ballonger, knappenåler, tape

## Fremgangsmåte

Her kommer tips, erfaring og utfordringer til de ulike stegene i den faktiske
oppgaven.

# Steg 1: Radiokommunikasjon {.activity}

- [ ] Her må lærer/instruktør tildele radiogrupper til hver. Radiogrupper bestemmer hvilke micro:bit som skal kommunisere med hverandre. Det er 256 grupper, nummerert fra 0 til 255.

- [ ] Begge micro:bitene (fjernkontroll og bit:bot) må være på samme gruppe - husk dette til senere.

# Steg 2: Fjernkontroll {.activity}

- [ ] Her er det først to måter, en enkel, men med begrensete muligheter, før en mer elegant, men litt mer kompleks måte.

- [ ] Pass på at `hvis`{.microbitlogic}-løkken sjekker knapp A+B før den sjekker A eller B. Når hendelsen A+B er sann, er også hendelsene A og B sanne. Derfor vil den aldri oppdage A+B hvis A og/eller B sjekkes først.

# Steg 3: Kjøre bilen {.activity}

- [ ] Det er enklere å sette opp med å bruke bit:bot kodeblokkene, men du har mer presis styring med å bruke direkte styring med `skriv digital`{.microbitpins} eller `skriv digital`{.microbitpins}.

- [ ] Finn ut hvilken pinne som gjør hva. Det står på undersiden av bit:boten. Når det er oppført to pinner på en motor, er det en pinne for å kjøre fremover, og en pinne for å kjøre bakover. Settes strøm på begge, vil bit:boten stå i ro.

## Variasjoner {.challenge}

- [ ]  Elevene kan gjerne bruke lysfunksjonene i bit:bot hvis de har ekstra tid.
