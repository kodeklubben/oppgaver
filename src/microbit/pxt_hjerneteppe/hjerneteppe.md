---
title: "PXT: Hjerneteppe!"
author: Helene Isnes og Julie Revdahl
language: nb
---


# Introduksjon {.intro}

"Hjerneteppe!" er en huskelek hvor du skal huske stadig lengre rekker med
bokstaver!

I denne oppgaven skal vi bruke noe som kalles for en funksjon. En funksjon er et
sett med flere kodelinjer (klosser) som til sammen utfører en oppgave. Å lage
funksjoner er lurt dersom man skal gjøre oppgaven flere ganger underveis i
programmet. Det kan også være lurt for å dele opp programmet i mindre deler.  


# Steg 1: Velg fasit {.activity}

*Det første vi skal kode er en funksjon som skal inneholde de forskjellige
bokstavkombinasjonene man kan få som en oppgave. Funksjonen skal også ha med en
variabel* `Fasit`{.microbitvariables} *som skal velge hvilken oppgave som er
den gjeldende.*

## Sjekkliste {.check}

- [ ] Lag en ny funksjon som du kaller `Velg fasit`{.microbitfunctions}. Du lager
  en ny funksjon med `Lag en funksjon...`{.microbitfunctions}-knappen i kategorien
  `Funksjoner`{.microbitfunctions} i __Avansert__.

- [ ] Sett en variabel kalt `Oppgaver`{.microbitvariables} til en liste med tre
  eller flere tekstsstrenger med ulike variasjoner på rekkefølge på bokstavene A,
  B og C. Du kan få bruk for klossen `sett text list til array of...`{.microbitvariables}.
  Koden settes inn i `Velg fasit`{.microbitfunctions}.

## {.tip}
Forslag til tre ulike teksstrenger er: ABCCBABA, ACCBACBC og CBACCBAB
##

- [ ] En variabel `Fasit`{.microbitvariables} skal settes til `Oppgaver`{.microbitvariables}
  som får en verdi mellom 0 og __antall oppgaver - 1__. `Sett Fasit til`{.microbitvariables}-klossen
  finner du i `Variabler`{.microbitvariables}, `list får en verdi ved 0`{.microbitarrays}
  finner du i `Lister`{.microbitarrays} og `velg tilfeldig 0 til 4`{.microbitmath}
  finner du i `Matematikk`{.microbitmath}.

## OBS! {.tip}
Hvis du endrer antall oppgaver i listen, må du også endre makstallet for det
tilfeldige tallet du plukker. Makstallet skal være __antall oppgaver - 1__.


# Steg 2: Vis fasit {.activity}

*I dette steget skal vi lage en til funksjon. Denne skal holde styr på nivået vi
er på og vise bokstavene til skjermen på micro:biten.*

## Sjekkliste

- [ ] Lag en ny funskjon kalt `Vis fasit`{.microbitfunctions} og sett den inn i
  kodefeltet ditt.  

- [ ] Lag en ny variabel `Gjetning`{.microbitvariables}. Denne skal inneholde
  gjetningen av bokstaver til spilleren.

- [ ] Sett den nye variabelen til en tom teksstreng i `Vis fasit`{.microbitfunctions}-funksjonen.
  `Vis tekst`{.microbitbasic}-klossen finner du i kategorien `Tekst`{.microbitbasic}.

- [ ] Lag en ny variabel `Kan gjette`{.microbitvariables}. Denne variabelen skal
  holde styr på om personen som spiller kan gjette, eller om den må vente. *Senere
  skal vi kode at spilleren bare kan gjette hvis et spørsmålstegn vises på
  skjermen til micro:biten.*

- [ ] Sett `Kan gjette`{.microbitvariables} til `usann`{.microbitlogic}.`usann`{.microbitlogic}-klossen
  finner du i `Logikk`{.microbitlogic}.

Nivået vi er på tilsvarer antall bokstaver vi må huske. Det vi nå skal kode er
bokstavene som skal vises på skjermen til nivået vi er på.

- [ ] Lag to nye variabler `indeks`{.microbitvariables} og `Nivå`{.microbitvariables}.

- [ ] Finn en passende løkke i `Løkker`{.microbitloops} som skal gjenta for
  variabelen `indeks`{.microbitvariables} fra 0 til `Nivå`{.microbitvariables}__- 1__.
  Løkken skal settes inn nederst i `Vis fasit`{.microbitfunctions}.

- [ ] Sett først inn en `tøm skjerm`{.microbitbasic}-kloss og deretter en `pause`{.microbitbasic}-kloss
  på 200 ms inn i løkken. Begge klossene kan du finne i `Basis`{.microbitbasic}-kategorien.

- [ ] Videre i løkken vil vi at en bokstav fra variabelen `Fasit`{.microbitvariables}
  skal vises, på den posisjoen (`indeks`{.microbitvariables}) vi er på i løkken.
  En `vis tekst`{.microbitbasic}-kloss finner du i `Basis`{.microbitbasic},
  klossen `tegn fra .. posisjon 0`{.microbittext} fra `Tekst`{.microbittext} kan
  også komme godt med.  

- [ ] Sett inn en `pause`{.microbitbasic}-kloss med et tall mellom 500 og 1000.

Vi går nå ut av løkken og fortsetter videre under.

- [ ] Siden vi er ferdig med å vise bokstavene spilleren skal gjette, setter vi
`Kan gjette`{.microbitvariables} til `sann`{.microbitlogic}.

- [ ] Til slutt i denne funksjonen vil vi vise et spørsmålstegn så lenge
  gjetningen ikke er like lang som det nivået vi er på. Sett inn koden som er
  vist nedenfor under forrige kloss. Klossen `lengde på`{.microbittext} finner du i
  `Tekst`{.microbittext}-kategorien.

```microbit
let Nivå = 0
let Gjetning = ""
while (Gjetning.length < Nivå) {
    basic.showString("?")
}
```
Merk at du må sette denne koden inn i funksjonen din på riktig sted, og ikke
i en `ved start`{.microbitbasic}-blokk som på bildet.


# Steg 3: Sett sammen programmet {.activity}

## Sjekkliste {.check}

- [ ] I `ved start`{.microbitbasic} skal det legges inn en kloss som heter
  `call Velg fasit`{.microbitfunctions} fra `Funksjoner`{.microbitfunctions}.
  *Denne klossen henter funksjonen* `Velg fasit`{.microbitfunctions} *og kjører
  koden der den plasseres.*

- [ ] Lag en ny variabel som du kaller `Nivå`{.microbitvariables}. Denne skal
  settes til 0.

- [ ] Legg til en `gjenta hvis sann`{.microbitloops}-kloss. I steden for `sann`{.microbitlogic}
  vil vi at løkken skal kjøre så lenge `Nivå`{.microbitvariables} er mindre enn
  lengden på `Fasit`{.microbitvariables}. `Mindre enn`{.microbitlogic}-klossen
  finner du i `Logikk`{.microbitlogic}-kategorien.

- [ ] Endre `Nivå`{.microbitvariables} med 1 inne i løkken fra forrige punkt.

- [ ] Hent ut funksjonen `Vis fasit`{.microbitfunctions}.

- [ ] Sett inn en `gjenta hvis sann`{.microbitloops}-kloss. Bytt ut `sann`{.microbitlogic}
  med koden under. *Vi skal fortsatt være inne i den første løkken.*

```microbit
let Nivå = 0
let Fasit = ""
let Gjetning = ""
while (Gjetning.compare(Fasit.substr(0, Nivå)) != 0) {

}
```
Pass på at du plasserer koden der den skal.

- [ ] Sett inn en `vis ikon`{.microbitbasic}-kloss (fra `Basis`{.microbitbasic})
  i løkken fra forrige punkt. Bildet som skal vises skal være et kryss.

- [ ] Under bildet skal `Vis fasit`{.microbitfunctions} hentes på nytt.  

Vi går nå ut av den ene løkken.

- [ ] Sett inn en `vis ikon`{.microbitbasic}-kloss under løkken. Du kan for
  eksempel bruke bildet som heter __ja__. Hvis du holder musepekeren over de
  ulike ikonene kommer navnene deres opp.

- [ ] Gå ut av den første løkken og sett inn en `vis ikon`{.microbitbasic}-kloss
  helt nederst i `ved start`{.microbitbasic}-blokken. Dette bildet skal vise at
  spillet er ferdig og at spilleren har klart alle nivåene i oppgaven. Du kan
  selv velge hvilket bilde du vil bruke.


# Steg 4: Knapper {.activity}

*Nå skal vi lage knappene som spilleren skal bruke når den gjetter på bokstavene!*

## Sjekkliste {.check}

- [ ] Plasser en `når knapp A trykkes`{.microbitinput}-kloss fra `Inndata`{.microbitinput}
  i kodefeltet ditt.

Spilleren skal bare kunne gjette hvis variabelen `Kan gjette`{.microbitvariables}
er satt til sann.

- [ ] Sett inn en `hvis`{.microbitlogic}-kloss fra `Logikk`{.microbitlogic}.
  Bytt ut `sann`{.microbitlogic} med `Kan gjette`{.microbitvariables}.

- [ ] Inne i `hvis`{.microbitlogic}-klossen, skal du sette sammen `sett gjetning til 0`{.microbitvariables}
  og `sett sammen`{.microbittext} slik at når knapp A trykkes, skal bokstaven __A__
  settes sammen med gjetningen vår.  

- [ ] Lag kode for `når knapp B trykkes`{.microbitinput} og `når knapp A+B trykkes`{.microbitinput}.
  `Når knapp A+B trykkes`{.microbitinput} skal det være en gjetning på bokstaven C.

## Test prosjektet {.flag}
*Nå er koden din ferdig!*

- [ ] Last ned koden til micro:biten og se hvor mye du klarer å huske!


# Videre arbeid: Musikk istedenfor bokstaver! {.activity}

*Hvis du vil kan du bytte til å gjette på toner i steden for bokstaver. Du vil
trenge litt ekstra utstyr:*

*- Høyttaler (buzzer) eller hodetelefoner*

*- 2 krokodilleklemmer*

- [ ] Bytt ut `Vis tekst tegn fra...`{.microbitbasic} i `Vis fasit`{.microbitfunctions}-funksjonen
  med det under:
```microbit
let indeks = 0
let Fasit = ""
if (Fasit.charAt(indeks) == "A") {
    music.playTone(262, music.beat(BeatFraction.Whole))
} else if (Fasit.charAt(indeks) == "B") {
    music.playTone(330, music.beat(BeatFraction.Whole))
} else {
    music.playTone(392, music.beat(BeatFraction.Whole))
}
```
Pass på at du plasserer koden inne i funksjonen din og ikke i `ved start`{.microbitbasic}-klossen
som på bildet.
- [ ] Utvid koden for knappene til de ser slik ut:

```microbit
input.onButtonPressed(Button.A, function () {
    let Kan_Gjette = 0
    if (Kan_Gjette) {
        music.playTone(262, music.beat(BeatFraction.Whole))
        Gjetning = "" + Gjetning + "A"
    }
})
input.onButtonPressed(Button.AB, function () {
    let Kan_Gjette = 0
    if (Kan_Gjette) {
        music.playTone(392, music.beat(BeatFraction.Whole))
        Gjetning = "" + Gjetning + "C"
    }
})
input.onButtonPressed(Button.B, function () {
    let Kan_Gjette = 0
    if (Kan_Gjette) {
        music.playTone(330, music.beat(BeatFraction.Whole))
        Gjetning = "" + Gjetning + "B"
    }
})
```

- [ ] Koble til en høyttaler (buzzer) eller hodetelefoner med krokodilleklemmer
  (hvis du er usikker på hvordan dette gjøres kan du se på en av de andre
  oppgavene som skal spille av lyd, der er alt forklart).

- [ ] Last ned koden til micro:biten og spill i vei.
