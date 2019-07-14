---
title: "PXT: Tikkande bombe"
author: Kolbjørn Engeland
translator: Stein Olav Romslo
language: nn
---


# Introduksjon {.intro}

Kjenner du "Tikkande bombe"-spelet? Spelarane kastar ei leikebombe mellom seg
medan ei klokke tel ned, og personen som heldt den når tida er ute tapar. Det er
veldig morosamt!

I dette prosjektet skal me byggje eit liknande spel, men i staden brukar me ei
virituell bombe og micro:bit-radio. Den virituelle bomba er ein tal-variabel som
tel ned til `0`, og me skal sende dette talet mellom fleire micro:bit-ar. Den
som har den virituelle bomba når me kjem til `0` tapar. Me kan sende tal ved
hjelp av radioklossane.

![Bilete av ein micro:bit som viser ei bombe](bombe.png)

# Steg 1: Me startar spelet {.activity}

_Me startar med å vise eit tal når me ristar på micro:bit-en._

## Sjekkliste {.check}

- [ ] Start eit nytt PXT-prosjekt, til dømes ved å gå til
  [makecode.microbit.org](https://makecode.microbit.org/?lang=no){target=_blank}.

Kva tyder det å ha eit tal som representerer ei bombe? Me kan lage ei
bombe-klokke som er eit tal som vert sendt mellom micro:bit-ane ved hjelp av
radioen. Bombeklokka skal telje ned, og når den blir `0` skal den ringe.

Me startar med å kode interaksjonen mellom micro:bit-en og spelarane. Då vil me
at spelet skal starte, og den fyrste bomba vert sendt ved å trykke på
`A+B`-knappen. Når ei bombe er motteke, viser skjermen eit bilete av bomba, og
når spelaren ristar på micro:bit-en sendast den vidare til neste spelar.

- [ ] Lag ein variabel `bombe` og set den til `-1` inne i `ved start`-klossen.

- [ ] For at micro:bit-en skal vite kven den skal sende til og få tal frå, må de
  lage ein felles radiokanal. Dette kan du gjere ved å velje `radio set gruppe`
  frå `Radio`-kategorien. Du kan velje eit tal frå `0` til `255`, og dei som
  skal spele saman må velje same tal.

![Bilete av "set bombe til"- og "radio set gruppe"-klossene](bombeskript_1.png)

- [ ] For å starte spelet trykkar me på `A+B`-knappen, og gir eit positivt tall
  til `bombe`-variabelen. For å gjere spelet mindre føreseieleg brukar me `plukk
  tilfeldig`-klossen frå `Matematikk`-kategorien for å gi `bombe`-variabelen ein
  verdi mellom `10` og `20`:

![Bilete av "når A+B trykkes" der bombe vert sett til eit tilfeldig tal mellom 10 og 20](bombeskript_2.png)

- [ ] For å sende ei bombe kan me riste micro:bit-en. Viss `bombe`-variabelen er
  positiv, har me bomba og me kan sende den. Etter å ha sendt den vert
  `bombe`-variabelen sett til `-1` sidan me ikkje har den lengre.

![Bilete av "når ristast" der verdien for bombe-variabelen vert sendt og sett til 0](bombeskript_3.png)

- [ ] Me registrerer at bomba er motteke med ein `når radio mottek`-kloss.
  `recievedNumber` representerer bomba og vert lagra i `bombe`-variabelen.

![Bilete av "når radio mottar"-kloss der verdien for bombe-variabelen vert sett til RecievedNumber](bombeskript_4.png)

No kan me gå i gang med å kode nedteljinga til `0`. Dette gjer me ved å bruke
ein `gjenta for alltid`-kloss der `bombe`-variabelen tel ned til `0`. Inne i
denne klossen må me sjekke kva verdi `bombe`-variabelen har, slik at me viser
bombe-ikonet og tel ned når me har bomba (altså at `bombe` er positiv), og
stoppar nedteljinga og viser ein hovudskalle når me kjem til `0`.

- [ ] Me kan leggjet til ei klokke med `gjenta for alltid`-klossen.

- [ ] Viss `bombe`-variabelen er lik `0`: KABOOM! Du tapte, og me viser ein
  hovudskalle!

- [ ] Viss `bombe`-variabelen er negativ (`bombe` < `0`) har me ikkje bomba, så
  me tømmer skjermen.

- [ ] Viss `bombe`-variabelen er positiv (`bombe` > `0`) viser me eit bombe-ikon
  og reduserer variabelen med `1`.

![Bilete av "for alltid"-kloss der ein viser bilete avhengig av verdien til bombe-variabelen](bombeskript_5.png)

## Test prosjektet {.flag}

Det er to ulike måtar me kan teste micro:bit-program på:

- [ ] Til venstre på skjermen er det eit bilete av ein micro:bit. Starter du å
  teste her vil du få opp to bilete av micro:bit, og du kan prøve å sende bomba
  mellom desse.

- [ ] Du og ein venn kan laste opp koden på kvar dykkar micro:bit. Den som
  startar spelet trykkar på `A+B` og rister på micro:bit-en for å sende bomba
  vidare. Kven tapar? Kva skjer viss fleire spelarar er på same kanal?
