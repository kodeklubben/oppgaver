---
title: "PXT: Husket du å lukke kjøleskapsdøren?"
author: Julie Christina Revdahl
language: nb
---


# Introduksjon {.intro}
Av og til er det lett å glemme å lukke kjøleskapsdøren, noe som gjør at lyset
blir stående på og kjøleskapet blir varmt. Vi skal nå programmere micro:biten
slik at den varsler oss dersom lyset i kjøleskapet blir stående på for lenge.


# Steg 1: Vi finner "gjenta for alltid"-klossen {.activity}

## Sjekkliste {.check}

- [ ] For å gjøre denne oppgaven trenger vi litt utstyr. Vi trenger 1 buzzer og
2 krokodilleklyper. Spør veilederne om hjelp dersom du ikke finner dette.

- [ ] Start et nytt PXT-prosjekt, for eksempel ved å gå til
  [makecode.microbit.org](https://makecode.microbit.org/?lang=no){target=blank}.

- [ ] Finn en `gjenta for alltid`{.microbitbasic}-kloss. Den ligger nok allerede
i kodefeltet ditt, eller så kan du finne den i menyen under `Basis`{.microbitbasic}.
Koden vi skal legge inne i `gjenta for alltid`{.microbitbasic}-klossen vil gjentas
så lenge micro:biten er koblet til strøm.


# Steg 2: Opprette en variabel {.activity}

## Sjekkliste {.check}

- [ ] Først må vi opprette en `variabel`{.microbitvariables}. Denne skal
inneholde verdien til lysstyrken. Sett variabelen din til å inneholde `lysnivå`{.microbitinput}
fra `Inndata`{.microbitinput}-kategorien.

- [ ] Verdien til `lysnivå`{.microbitinput} går fra 0 til 255. Når verdien er 0
er det helt mørkt, og når verdien er 255 er det veldig sterkt lys. Micro:biten
er noe unøyaktig, så vi må prøve oss litt fram. Vi ser derfor for oss at dersom
verdien er mindre enn 80, så er det mørkt, og kjøleskapsdøren er mest sannsynlig
lukket.


# Steg 3: Når skal alarmen slå ut? {.activity}

## Sjekkliste {.check}

- [ ] Bruk en `hvis`{.microbitlogic}-kloss til å sjekke om lysstyrken er større
enn 80.

- [ ] Vi må så bestemme hvor lenge det skal være lov å holde kjøleskapsdøren åpen.
Denne verdien kan vi justere senere, så vi prøver oss fram med 20 sekunder til å
begynne med.

- [ ] Inne i `hvis`{.microbitlogic}-klossen legger vi derfor en `pause`{.microbitbasic}-kloss
på 20 sekunder. *Husk:pause-klossen tar verdier i millisekunder.*

- [ ] Etter at vi har ventet i 20 sekunder, må vi sjekke om døren har blitt
lukket eller om den fortsatt er åpen. Vi setter derfor variabelen for `lysstyrke`{.microbitvariables}
på nytt!

- [ ] Dersom lysstyrken fortsatt er større enn 80, må vi varsle om at døren ikke
er blitt lukket på en stund. Lag derfor en ny `hvis`{.microbitlogic}-kloss med
samme krav som tidligere.

- [ ] Inne i denne klossen skal vi nå lage en kode for hva som skal skje dersom
døren fortsatt er åpen etter 20 sekunder. Her kan du velge akkurat hva du vil,
men vi går i denne oppgaven for en kombinasjon av bilde og lyd!

- [ ] Bruk klosser under kategorien `Musikk`{.microbitmusic} til å lage en alarm,
for å advare den som har holdt på i kjøleskapet. Her har vi valgt å spille av
melodien *plingpling*.

- [ ] Legg så til et bilde som skal vises på skjermen mens alarmen går. Det kan
være et kryss, et surfjes, hva som helst.

- [ ] Her er det uendelig antall muligheter, og det er bare å prøve seg fram.
Vi har valgt å spille av *plingpling* tre ganger mens alle de røde ledlysene på
micro:biten blinker.

- [ ] Koden vår ser nå slik ut:
```microbit
let lysstyrke = 0
basic.forever(function () {
    lysstyrke = input.lightLevel()
    if (lysstyrke > 80) {
        basic.pause(20000)
        lysstyrke = input.lightLevel()
        if (lysstyrke > 80) {
            music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.Once)
            basic.showLeds(`
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                `)
            basic.clearScreen()
            basic.pause(500)
            music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.Once)
            basic.showLeds(`
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                `)
            basic.clearScreen()
            basic.pause(500)
            music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.Once)
            basic.showLeds(`
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                `)
            basic.clearScreen()
        }
    }
})
```

## Test prosjektet {.flag}

- [ ] Test først programmet ditt i simulatoren. Oppe i venstre hjørne på micro:biten
dukker det opp en sirkel som et halvt sort, halvt gul. Dette er lyssensoren. Ved
å dra i enten den gule eller den sorte delen, kan du justere lysnivået. Prøv med
ulike verdier over og under 80 for å se at koden din fungerer som den skal.

- [ ] Du kan nå laste ned programmet på micro:biten din. For å laste ned
koden må du først ha koblet micro:biten til datamaskinen med en USB-kabel. Klikk
deretter på knappen `Last ned` nede til venstre på skjermen. Det lastes nå ned
en fil som heter `microbit-Uten-navn.hex` til datamaskinen din. Samtidig dukker
det opp et vindu som sier at du må flytte denne filen til MICROBIT-disken på
datamaskinen din.

- [ ] Koble til buzzer og krokodilleklyper som vist på micro:bit-simulatoren.
Spør en veileder om du trenger hjelp!

- [ ] Dersom du ikke har et kjøleskap tilgjengelig mens du arbeider med oppgaven
kan du prøve å dekke til sensoren med hendene.


## Utfordring {.challenge}

- [ ] Greier du å få til akkurat det samme ved å bruke `kjøretid`{.microbitinput}-klossen
i stedet for en `pause`{.microbitbasic}-kloss? *Tips: Du må sette en starttid og
en sluttid, før du sammenligner om dette overskrider 20 sekunder.*
