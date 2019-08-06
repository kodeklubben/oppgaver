---
title: "PXT: Klokka tikker"
author: Julie Christina Revdahl
language: nb
---


# Introduksjon {.intro}
I denne opggaven skal vi lage en timer som teller ned fra 10 sekunder. Denne kan
vi bruke til å lage et morsomt spill! Ved start får spilleren en kategori, for
eksempel farger, og skal deretter komme på flest mulig farger på sine 10 sekunder.
Den som samler flest poeng vinner.


# Steg 1: Lage en variabel som teller ned tiden {.activity}

## Sjekkliste {.check}

- [ ] Først vil vi lage en variabel som skal
inneholde de ti sekundene vi vil telle ned fra. Vi oppretter derfor en variabel
vi kaller `tid`{.microbitvariables}. Dette gjøres under kategorien `Variabler`{.microbitvariables}.
Finn deretter klossen `sett tid til 0`{.microbitvariables}, og endre slik at `tid`{.microbitvariables}
settes til 10 sekunder. Dersom du ønsker lengre tid, kan du endre denne
variabelen senere.

- [ ] Vi lager nå enda en variabel, `kategorier`{.microbitvariables}, som skal
inneholde de ulike kategoriene en spiller kan få. For å få til dette, lager vi
en liste med `kategorier`{.microbitvariables}. Dette finner vi under menyen
`Lister`{.microbitarrays}. Ved å trykke på plusstegnet, kan vi legge til så
mange kategorier som vi ønsker. Disse bestemmer dere helt selv. Her har vi gått
for *farger*, *blomster* og *biler*.

- [ ] Nå vil koden for `når knapp A+B trykkes`{.microbitinput} se slik ut:

```microbit
input.onButtonPressed(Button.AB, function () {
    tid = 10
    kategorier = ["farger", "blomster", "biler"]
})
```


# Steg 2: Registrere poeng {.activity}

## Sjekkliste {.check}

- [ ] Vi vil nå lage en kode-blokk for å registrer antall poeng hver spiller får.
Dette kan vi enkelt gjøre med en `når knapp B trykkes`{.microbitinput}-kloss fra
`Inndata`{.microbitinput}-kategorien.

- [ ] Lag en ny variabel `poeng`{.microbitvariables} som skal registrer antall
poeng. Hver gang knapp B trykkes, skal `poeng`{.microbitvariables} endres med 1.
Denne klossen finner du under `Variabler`{.microbitvariables}-kategorien.

- [ ] Kode-blokken for `når knapp B trykkes`{.microbitinput} ser nå slik ut:

```microbit
input.onButtonPressed(Button.B, function () {
    poeng += 1
})
```


# Steg 3: Starte timeren {.activity}

## Sjekkliste {.check}

- [ ] Finn klossen for `når knapp A trykkes`{.microbitinput}. Vi vil starte å
telle ned timeren når denne knappen trykkes.

- [ ] Først må spilleren få utdelt en kategori. Denne må hentes og fjernes fra
listen, slik at ikke flere spillere får samme kategori. Vi finner  klossen for
å gjøre dette under kategorien `Lister`{.microbitarrays}. Denne må settes inne i
en `vis tekst`{.microbitbasic}-kloss fra `Basis`{.microbitbasic}-kategorien.

- [ ] For å enklere se at koden vår fungerer, kan vi vise `tid`{.microbitvariables}
på skjermen. Se om du finner klossen for dette under kategorien `Basis`{.microbitbasic}.

- [ ] Vi trenger nå en `gjenta hvis sann`{.microbitloops}-kloss, som vi skal
bruke til å telle ned tiden. Vi skal erstatte `sann`{.microbitloops} med at
tiden er ulik fra null. Det vil si at vi ønsker å telle ned fra ti og helt til
null. Disse klossene finner du under kategoriene `Logikk`{.microbitlogic},
`Løkker`{.microbitloops} og `Variabler`{.microbitvariables}. Du trenger en
`ulik`{.microbitlogic}-kloss og variabelen `tid`{.microbitvariables}. Sett de
sammen så de oppfyller kravene vi akkurat gikk gjennom.

- [ ] Inne i `gjenta hvis`{.microbitloops}-klossen skal vi legge selve koden for
å telle ned. Vi trenger en `pause`{.microbitbasic}-kloss som venter i 1
sekund(1000 ms) før vi teller ned. Deretter vil vi `endre tid med -1`{.microbitvariables}.
Vis deretter `tid`{.microbitvariables} på skjermen, slik at vi kan se tiden
telle nedover.

- [ ] Nå bør koden din ligne på dette:

```microbit
input.onButtonPressed(Button.A, function () {
    let kategorier: string[] = []
    basic.showString("" + kategorier.pop())
    basic.showNumber(tid)
    while (tid != 0) {
        basic.pause(1000)
        tid += -1
        basic.showNumber(tid)
    }
})
```

- [ ] Nederst i `når knapp A trykkes`{.microbitinput}-blokken skal vi legge en
`hvis`{.microbitlogic}-kloss som viser en tekst om at tiden er ute når
variabelen `tid`{.microbitvariables} har blitt null. Her vil vi også vise antall
poeng spilleren har fått. Bruk klossen `sett sammen`{.microbittext} til å sette
sammen tekst og antall poeng.

- [ ] Nå bør koden-blokken for `når knapp A trykkes`{.microbitinput} se slik ut:

```microbit
input.onButtonPressed(Button.A, function () {
    let kategorier: string[] = []
    basic.showString("" + kategorier.pop())
    basic.showNumber(tid)
    while (tid != 0) {
        basic.pause(1000)
        tid += -1
        basic.showNumber(tid)
    }
    if (tid == 0) {
        basic.showString("Tiden er ute!" + "Du fikk" + poeng + "poeng")
    }
})
```

## {.tip}

Hvis du skal bruke samme kloss flere ganger kan du høyreklikke på den og trykke på lag kopi.

## Test prosjektet {.flag}

Det er to forskjellige måter vi kan teste micro:bit-programmer på:

- [ ] Til venstre på skjermen er det et bilde av en micro:bit. Dette er faktisk
  en simulator som kan kjøre programmet vi nettopp laget.

- [ ] Enda morsommere er det å teste programmet på micro:biten din! Koble
  micro:biten din til datamaskinen med en USB-kabel. Klikk deretter på knappen
  `Last ned` nede til venstre på skjermen.

  Det lastes nå ned en fil som heter `microbit-Uten-navn.hex` til datamaskinen
  din. Samtidig dukker det opp et vindu som sier at du må flytte denne filen til
  MICROBIT-disken på datamaskinen din.


## Utfordring {.challenge}

- [ ] Finn en venn, bli enig om kategorier og spill! Hvem fikk flest poeng?
