---
title: "PXT: Er du rask nok?"
author: Julie Christina Revdahl
language: nb
---


# Introduksjon {.intro}
I denne opggaven skal vi lage et morsomt spill som krever at du er rask til å
reagere! På skjermen vises piler i ulike retninger, hvor hver pil har en tilhørende
knapp som gir deg poeng. Er du ikke rask nok til å trykke, eller trykker du feil,
taper du poeng.


# Steg 1: Piler og knappetrykk {.activity}

## Sjekkliste {.check}

- [ ] Først må vi ha en oversikt over hvilke knapper og piler som skal henge
sammen. Da har vi klare regler for hva koden vår skal gjøre.

| Pil 	| Knapp som skal trykkes 	| Pilnummer 	|
|:---:	|:----------------------:	|:---------:	|
|  ←  	|            A           	|     0     	|
|  →  	|            B           	|     1     	|
|  ↑  	|           A+B          	|     2     	|
|  ↓  	|       Ikke trykk       	|     3     	|


# Steg 2: Knapp A {.activity}

*Først skal vi lage koden som gir oss poeng hvis vi trykker A når pilen peker mot
venstre.*

## Sjekkliste {.check}

- [ ] Først lager vi variabelen `poeng`{.microbitvariables} hvor vi skal lagre
poengene vi samler.

- [ ] Lag også en variabel som skal inneholde pilnummeret som velges.

- [ ] Nå har vi alle variablene vi trenger, og vi starter på selve koden for hva
som skal skje når knapp A trykkes. Vi trenger derfor klossen `når knapp A trykkes`{.microbitinput}.

- [ ] Inne i denne klossen må vi lagre regler for når vi skal få poeng, og når
vi skal tape poeng: Vi skal få poeng hvis pilnummeret matcher pilen som vises.
For knapp A betyr det at vi skal få poeng dersom pilnummeret er 0. Dersom
pilnummeret ikke er null, har vi trykket feil knapp og vi vil tape poeng. Se om
du finner klosser under kategoriene `Logikk`{.microbitlogic} og `Variabler`{.microbitvariables}
til å lage koden som oppfyller disse kravene.

- [ ] Koden din bør nå ligne på dette:

```microbit
input.onButtonPressed(Button.A, function () {
    if (pilnummer == 0) {
        poeng += 1
    } else {
        poeng += -1
    }
})
```

# Steg 3: Knapp B {.activity}

*Nå skal vi lage koden som gir oss poeng hvis vi trykker B når pilen peker mot
høyre.*

## Sjekkliste {.check}

- [ ] Vi har allerede alle variablene som trengs for å lage denne kodeblokken,
både `poeng`{.microbitvariables} og `pilnummer`{.microbitvariables}.

- [ ] Vi skal lage koden på akkurat samme måte som for knapp A. Husk at vi nå
vil gi poeng dersom `pilnummer`{.microbitvariables} er 1, som vist i tabellen.

- [ ] Koden din bør nå ligne på dette:

```microbit
input.onButtonPressed(Button.B, function () {
    if (pilnummer == 1) {
        poeng += 1
    } else {
        poeng += -1
    }
})
```


# Steg 4: Knapp A+B {.activity}

*Nå trenger vi koden som gir oss poeng dersom vi trykker A+B når pilen peker
oppover.*

## Sjekkliste {.check}

- [ ] Denne kode-blokken skal bygges på akkurat samme måte som for knapp A og
knapp B. Det greier du på egen hånd! Kontroller i tabellen at du har riktig krav
for når poeng skal gis.


# Steg 5: Lage selve spillet {.activity}

## Sjekkliste {.check}

- [ ] Vi vil at spillet vårt skal kunne starte på nytt når vi rister på
micro:biten. Til det trenger vi først en `når ristes`{.microbitinput}-kloss.

- [ ] Tøm så skjermen, slik at forrige spill ikke blir stående.

- [ ] Legg inn en `pause`{.microbitbasic}-kloss, slik at spilleren rekker å
gjøre seg klar før spillet er i gang. Du kan justere lengden på denne selv, men
prøv å starte med en pause på 500ms.

- [ ] På starten av spillet skal spilleren ha 0 poeng. Sett derfor variabelen
`poeng`{.microbitvariables} til 0. Nå har vi gjort alt klart slik at et nytt
spill kan starte.

- [ ] Vi vil at spillet skal vare i 20 runder, slik at det er om å gjøre å samle
flest mulig poeng totalt. Du kan selvfølgelig justere lengden på spillet selv.
Vi bruker klossen `gjenta 4 ganger`{.microbitloops}, en såkalt loop, og endrer
koden slik at vi får __20__ runder i stedet for __4__.

- [ ] Inne i denne loopen trenger vi en `tøm skjerm`{.microbitbasic}- og en
`pause`{.microbitbasic}-kloss. `Tøm skjerm`{.microbitbasic} trenger vi for at
skjermen skal tømmes mellom hver runde i spillet, og `pause`{.microbitbasic} for
at spilleren skal rekke å se pilen før den neste kommer. Sett `pause`{.microbitbasic}-klossen
til 100ms. Du kan endre den senere dersom det blir for lett eller vanskelig.

- [ ] Nå må vi sørge for at vi får forskjellige piler hver runde. For å få til
dette må vi sette `pilnummer`{.microbitvariables} til et tilfeldig tall. Klossen
`velg tilfeldig`{.microbitmath} finner du under kategorien `Matematikk`{.microbitmath}.
Ser du hvilket tall den må gå til? *Hint: Hvilke tall kan pilnummer ha?*

- [ ] Etter at `pilnummer`{.microbitvariables} har fått en verdi, må vi sette
opp hva vi vil at micro:biten skal gjøre for de ulike verdiene. Vi starter med å
finne en `hvis - ellers`{.microbitlogic}-kloss.

- [ ] I første `hvis`{.microbitlogic} er kravet at `pilnummer`{.microbitvariables}
skal være lik 0. Finn klossen `0 = 0`{.microbitlogic} under kategorien `Logikk`{.microbitlogic},
og sett sammen slik at det stemmer.

- [ ] Vi ser nå på hva vi vil at skal skje inne i denne `hvis`{.microbitlogic}-koden.
Om vi tar en titt på tabellen ser vi at når `pilnummer`{.microbitvariables} = 0,
så viser vi en pil mot venstre. Dette er det samme som en pil som peker mot Vest.
Under `Basis`{.microbitbasic} finner du en egen kloss som viser pilretninger.
Endre denne klossen slik at den peker mot Vest.

- [ ] Nå må vi ta for oss tilfellet hvor `pilnummer`{.microbitvariables} = 1. Da
skal pilen peke mot Øst. Som i stad må vi først sette opp kravet `hvis pilnummer = 1`{.microbitlogic},
og deretter fylle inn at vi vil vise en pil mot Øst.

- [ ] Gjør det samme for når `pilnummer`{.microbitvariables} = 2, og `pilnummer`{.microbitvariables}
= 3 på egen hånd. Sjekk at pilretningen stemmer med tabellen.

- [ ] Vi kan ha tilfeller hvor det samme `pilnummer`{.microbitvariables} velges
flere ganger etter hverandre. For å skille hver gang det kommer en ny pil legger
vi inn et bilde mellom hver gang. Bruk klossen `vis skjerm`{.microbitbasic} til
å lage et bilde som skal komme mellom hver pil.

- [ ] Nå har vi lagd hele spillet vårt, og når det er over vil vi gjerne vise
hvor mange poeng vi har fått. Vi legger derfor en ny loop `gjenta 4 ganger`{.microbitloops}
utenfor den første. Inne i denne legger vi en tom `vis tekst`{.microbitbasic}-kloss
etterfulgt av en `vis tall`{.microbitbasic}-kloss. Tallet som skal vises er
lagret i variabelen `poeng`{.microbitvariables}. På denne måten vil antall poeng
vi har fått blinke fire ganger når spillet er over.

- [ ] Denne kodeblokken bør nå se ut som dette:

```microbit

input.onGesture(Gesture.Shake, function () {
    basic.clearScreen()
    basic.pause(500)
    poeng = 0
    for (let i = 0; i < 20; i++) {
        basic.clearScreen()
        basic.pause(100)
        fasit = Math.randomRange(0, 3)
        if (fasit == 0) {
            basic.showArrow(ArrowNames.West)
        } else if (fasit == 1) {
            basic.showArrow(ArrowNames.East)
        } else if (fasit == 2) {
            basic.showArrow(ArrowNames.North)
        } else {
            basic.showArrow(ArrowNames.South)
        }
        basic.showLeds(`
            . . . . .
            . # # # .
            . # . # .
            . # # # .
            . . . . .
            `)
    }
    for (let i = 0; i < 4; i++) {
        basic.showString("")
        basic.showNumber(poeng)
    }
})
```
- [ ] Vi har nå lagd alle blokkene for koden vår, og den er klar til å testes!

## Test prosjektet {.flag}

Det er to måter du kan teste spillet ditt på:

- [ ] Bildet av micro:biten til venstre på skjermen din er faktisk en simulator
hvor du kan teste koden din. Gjør koden din det den skal?

- [ ] Du kan også teste spillet ved å laste det ned på micro:biten. For å laste
ned koden må du først ha koblet micro:biten til datamaskinen med en USB-kabel.
Klikk deretter på knappen `Last ned` nede til venstre på skjermen. Det lastes nå
ned en fil som heter `microbit-Uten-navn.hex` til datamaskinen din. Samtidig
dukker det opp et vindu som sier at du må flytte denne filen til MICROBIT-disken
på datamaskinen din.


## Utfordring {.challenge}

- [ ] Finn en venn og se hvem som er greier å samle flest poeng!

- [ ] Prøv å endre på pause-klossene dersom pilene endres for raskt eller sakte.

- [ ] Prøv å legge til musikk, slik at et trykk på riktig knapp gir én lyd, mens
et trykk på feil knapp gir en annen lyd. *Til dette trenger du en buzzer og to
krokodilleklyper.*
