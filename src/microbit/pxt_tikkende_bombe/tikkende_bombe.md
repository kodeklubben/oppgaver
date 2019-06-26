---
title: "PXT: Tikkende bombe"
author: Kolbjørn Engeland
language: nb
---


# Introduksjon {.intro}

Kjenner du "Tikkende-bombe" -spillet? Du kaster rundt en leke-bombe mens en klokke teller ned og personen som holder
den når tiden er ute, taper... Det er veldig morsomt.
I dette prosjektet vil vi bygge en lignende type spill, men i stedet bruker vi en virtuell bombe og micro:bit radio.

I stedet for å sende en ekte bombe rundt mens en ekte klokke teller ned, skal vi sende et tall mellom micro:biter. 
Vi kan gjøre det ved hjelp av radioblokkene. De bruker antennen på micro:bit for å sende data over
radiofrekvenssignaler, akkurat som telefoner eller dingser rundt deg.

Hva betyr det å ha et tall som representerer en bombe? Vi kan lage en bombe-klokke som er et tall som sendes
mellom micro:bitene ved hjelp av radioen. Bombeklokka skal telle ned, og når den blir 0, skal den ringe.

For å holde oversikt over ting, la oss få en variabel som heter potet:
* Hvis verdien av bombe er positiv, har spilleren bomben og bombe-variabelen representerer gjenværende tid.
* Hvis verdien av bombe når 0, er spillet over.
* Hvis verdien av bombe er negativ, betyr dette at spilleren ikke har bomben i hånden.

Nå som vi vet hva bombe er, må vi komme opp med brukerinteraksjonene. Slik spiller brukeren spillet:
* Trykk på A + B-knappen for å starte spillet og sende den første bomben
* Når en bombe er mottatt, viser skjermen et bilde
* Når spilleren rister på micro:bit, sender den bomben til andre spillere

![Bilde av en microbit som viser en bombe](bombe.PNG)



# Steg 1: Vi starter spillet {.activity}

*Vi begynner med å vise et tall når vi rister på micro:biten.*

## Sjekkliste {.check}

- [ ] Start et nytt PXT-prosjekt, for eksempel ved å gå til
  [makecode.microbit.org](https://makecode.microbit.org/?lang=no).

- [ ] Lag en variabel `bombe` og sette den til -1 inne i 'ved start' -blokken.

- [ ] For at micro:biten skal vite hvem den skal sende og få tall fra må dere lage en felles radiokanal.
Dette kan du gjøre ved å velge `radio sett gruppe` fra `Radio`-kategorien. 
Du kan velge et tall fra 0 til 255, og de som skal spille sammen må velge samme tall.

    ![Bilde av "sett bombe til" og "radio sett gruppe" klossene](bombeskript_1.PNG)

- [ ] For å starte spillet, bruker vi på A + B-knappen, og gir et positivt tall til bombe-variabelen. For å gjøre
spillet mindre forutsigbart, bruker vi  `plukk tilfeldig `- blokk fra `Matematikk`-kategorien for å lage en verdi mellom 10 og 20.:

    ![Bilde av "når A+B trykkes" der bombe settes til tilfeldig tall mellom 20 og 20](bombeskript_2.PNG)

- [ ] For å sende en potet kan vi riste micro:bit. Hvis bombe-variabelen er positiv, har vi bomben og vi kan
sende den. Etter å ha sendt den, setter vi bombe-variabelen til -1 siden vi ikke har den lenger.

   ![Bilde av "når ristes" der verdien for bombe-variabelen sendes og settes til 0](bombeskript_3.PNG)

- [ ] Mottak av bombe gjøres med en ‘når radio mottar’-blokk. recievedNumber representerer bombe og
lagres i bombe-variabelen.

   ![Bilde av "når radio mottar-blokk" der verdien for bombe-variabelen settes til RecievedNumber](bombeskript_4.PNG)

- [ ] Vi kan legge til en klokke med ‘gjenta for alltid’ blokken
* Hvis bombe er lik 0 (bombe = 0), KABOOM! du tapte, og vi viser en hodskalle!
* Hvis bombe-variabelen er negativ (bombe <0), har vi ikke bomben, så vi tømmer skjermen.
* Hvis bombe-variabelen er positiv (bombe > 0), viser vi et bombe-bilde og reduserer variabelen med 1

  ![Bilde av "for alltid blokk" der man viser bilde avhengig av verdien til bombe-variabelen](bombeskript_5.PNG)


## Test prosjektet {.flag}

Det er to forskjellige måter vi kan teste micro:bit-programmer på:

- [ ] Til venstre på skjermen er det et bilde av en micro:bit. Starter du å teste her vil du få opp to bilder av 
micro:bit og kan teste ut med å sende bomben mellom disse to.


- [ ] Du og en venn kan laste opp koden på hver deres micro:bit. Den som starter spillet trykker på 'A+B' 
og rister på micro:biten for å sende den videre. Hvem taper? Hva skjer hvis flere spillere er på samme kanal?

