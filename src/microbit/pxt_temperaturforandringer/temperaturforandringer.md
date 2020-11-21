---
title: "PXT: Temperaturforandringer"
author: Julie Christina Revdahl
language: nb
---


# Introduksjon {.intro}

Micro:biten vår kan brukes som et termometer til å måle temperatur. I denne
oppgaven skal vi måle temperaturer på ulike steder og lagre de i en liste, slik
at vi senere kan se på hvordan temperaturen forandret seg fra sted til sted.


# Steg 1: Opprette en liste {.activity}

*Vi begynner med å opprette en liste som skal inneholde alle temperaturene vi
måler.*

## Sjekkliste {.check}

- [ ] Start et nytt PXT-prosjekt, for eksempel ved å gå til
  [makecode.microbit.org](https://makecode.microbit.org/?lang=no){target=blank}.

- [ ] Opprett en `variabel`{.microbitvariables} med et passende navn. Dette blir navnet på listen som
skal inneholde de ulike temperaturene vi måler.

- [ ] Ved start skal denne variabelen settes til en `tom liste`{.microbitarrays}, da vi ikke har
gjort noen målinger ennå.


# Steg 2: Måle temperaturen {.activity}

*Vi vil måle temperaturen i rommet der vi er. Hvordan gjør vi det på en
 micro:bit?*

## Sjekkliste {.check}

- [ ] For å måle flere temperaturer, må vi fortelle micro:biten nøyaktig når
den skal lagre en temperaturmåling. Dette kan gjøres ved å for eksempel trykke
på knapp A, knapp B, eller riste på micro:biten. Vi velger å bruke `knapp A`{.microbitinput},
men du kan velge helt selv hva du ønsker å bruke.

- [ ] Opprett en `variabel`{.microbitvariables} som skal inneholde én enkelt
temperaturmåling. Sett denne til å være `temperatur (°C)`{.microbitinput}.

- [ ] Lag koden for å vise temperaturen på skjermen.

- [ ] Målingen vi har tatt må så legges til i listen. Den kan legges til hvor
som helst, men for enkelhetsskyld kan det være greit å legge den bakerst, slik
at målingene du har gjort kommer i rikitg rekkefølge. Du finner klossen til dette
under kategorien `Lister`{.microbitarrays}. Verdien vi nå skal legge til i listen,
er den verdien vi lagret i variabelen vi akkurat opprettet. Prøv å gjøre dette
steget på egen hånd uten å lurkikke på koden.

- [ ] Koden din kan nå ligne på denne:
```microbit
input.onButtonPressed(Button.A, function () {

  let temperaturforandringer: number[] = []

    temperatur = input.temperature()
    basic.showNumber(temperatur)
    temperaturforandringer.push(temperatur)
})
```


# Steg 3: Vise temperaturforandringene vi har målt {.activity}

*Nå vil vi vise alle målingene på skjermen slik at vi kan se hvordan de varierte.*

## Sjekkliste {.check}

- [ ] For å vise alle temperaturene på skjermen, må vi gå gjennom hele listen
hvor alle temperaturene er lagret. Til å gjøre dette kan vi bruke en såkalt
loop eller løkke. Under kategorien `Løkker`{.microbitloops} finner du en kloss
som går gjennom alle verdiene i listen. Se om du finner riktig kloss!

- [ ] Vi kan endre `verdi`{.microbitvariables} til å ha samme navn som variabelen
vi lagret én og én temperatur i. Da blir det lettere å forstå at for hver runde
så ser vi på én temperaturmåling i listen hvor vi lagret alle temperaturene. Vi
ser først på den første målingen vi tok, så måling nummer 2, måling nummer 3 og
så videre.

- [ ] Inne i denne loopen skal vi nå lage koden for å vise tallet på skjermen.
*Obs: Valgte vi å gå gjennom hver `verdi`{.microbitvariables} i listen, må vi vise
`verdi`{.microbitvariables} på skjermen.*

- [ ] For å få et klarere skille mellom hver gang en temperatur skrives på
skjermen, kan det være greit å vise et ikon mellom hver gang. Det er helt opp til
deg hva du vil vise. Vi bruker ikonet for et termometer.

- [ ] Tøm så skjermen slik at vi er klare til å vise neste tall.

- [ ] Koden din kan nå ligne på denne:
```microbit
input.onButtonPressed(Button.B, function () {
    for (let temperatur of temperaturforandringer) {
        basic.showNumber(temperatur)
        basic.showIcon(IconNames.Sword)
        basic.clearScreen()
    }
}
```


## Test prosjektet {.flag}

  Det er to forskjellige måter vi kan teste micro:bit-programmer på:

  - [ ] Til venstre på skjermen er det et bilde av en micro:bit. Dette er faktisk
    en simulator som kan kjøre programmet vi nettopp laget. Gjør koden din det
    du vil at den skal gjøre?

  - [ ] Enda morsommere er det å teste programmet på micro:biten din! Koble
    micro:biten din til datamaskinen med en USB-kabel. Klikk deretter på knappen
    `Last ned` nede til venstre på skjermen.

    Det lastes nå ned en fil som heter `microbit-Uten-navn.hex` til datamaskinen
    din. Samtidig dukker det opp et vindu som sier at du må flytte denne filen til
    MICROBIT-disken. Dersom du trenger hjelp til dette så spør en av veilederne.

## Utfordringer {.challenge}

- [ ] Koble micro:biten til et batteri og mål temperaturer i forskjellige rom,
og kanskje også utendørs.

- [ ] Lag regler for hvilke temperaturer som er for varme og for kalde. Koble til
en buzzer og spill én lyd når temperaturen er akkurat passe, én når det er for
varmt, og en annen lyd når det er for kaldt.
