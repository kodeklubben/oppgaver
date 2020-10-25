---
title: "PXT: Manuell håndteller"
author: Julie Christina Revdahl
language: nb
---


# Introduksjon {.intro}

I denne oppgaven skal vi programmere micro:biten slik at den kan hjelpe oss å telle.
Det kan for eksempel være at vi vil telle hvor mange som er på en buss til en
hver tid. Da må vi kunne legge til og fjerne passasjerer når de går på og av.


# Steg 1: Å lagre antall passasjerer {.activity}

## Sjekkliste {.check}

- [ ] Start et nytt PXT-prosjekt, for eksempel ved å gå til
  [makecode.microbit.org](https://makecode.microbit.org/?lang=no){target=blank}.

- [ ] For å kunne ha oversikt over antall passasjerer til enhver tid, må vi lagre
  denne informasjonen på en slik måte at den kan endres på uten å overskrive all
  informasjon. En enkel måte å gjøre dette på, er å opprette en liste som kan
  legge til elementer og slette elementer når passasjerer kommer og går. Du kan
  opprette en liste under kategorien `Avansert -> Lister`{.microbitarrays}. Til
  å begynne med bør denne lista være tom.


# Steg 2: Legge til en passasjer {.activity}

## Sjekkliste {.check}

- [ ] Vi kan på forhånd bestemme oss for at et trykk på knapp A legger til en
  passasjer i listen, mens et trykk på knapp B fjerner en passasjer fra listen.
  Under `Avansert -> Lister`{.microbitarrays} finner du klosser du kan bruke til
  å gjøre dette.

- [ ] For å legge til en passasjer, kan man legge til et element i listen,
for eksempel bakerst. Hva elementet inneholder, er ikke så viktig i denne oppgaven
ettersom vi kun ønsker å telle. Men vi kunne for eksempel ha lagret navnet på alle
passasjerene om vi ønsket det. Her legger vi bare til tallet 1, som da representerer
1 passasjer. Hvor i listen du legger til passasjeren, er opp til deg. Se om du
finner riktig blokk på egenhånd!

- [ ] Antall passasjerer på bussen blir dermed det samme som antall elementer i
 listen. Print gjerne antall passasjerer på skjermen slik at du enklere kan se
 om det stemmer.
Koden din kan for eksempel se ut som dette:

  ```microbit
  let passasjerer: string[] = []
  input.onButtonPressed(Button.A, function () {
    passasjerer.push("1")
    basic.showNumber(passasjerer.length)
  })
  ```

## Test prosjektet {.flag}

- [ ] Test koden enkelt og greit ved å bruke simulatoren. Hver gang du trykker
    knapp A, skal tallet som vises på skjermen øke med __1__.


# Steg 3: Fjerne en passasjer {.activity}

## Sjekkliste {.check}

- [ ] Nå ønsker vi å fjerne én passasjer, eller et element fra listen, hver gang
  vi trykker på knapp B.

- [ ] For å fjerne en passasjer, kan man bruke funksjonen for å hente og fjerne
  elementer i en liste. Denne klossen finnes også under `Avansert -> Lister`{.microbitarrays},
  Ettersom denne funksjonen henter ut den siste variabelen, må vi opprette en ny
  variabel hvor denne skal lagres, før den blir slettet. På denne måten kunne vi
  brukt variabelen om igjen dersom vi hadde hatt behov for det.

  Koden din kan for eksempel se ut som dette:

  ```microbit
  let avstigning = ""
  let passasjerer: string[] = []
  input.onButtonPressed(Button.B, function () {
    avstigning = passasjerer.pop()
    basic.showNumber(passasjerer.length)
  })
  ```

## Test prosjektet {.flag}

- [ ] Test koden enkelt og greit ved å bruke simulatoren. Hver gang du trykker
  knapp A, skal tallet som vises på skjermen øke med __1__, og når du trykker på
  knapp B skal tallet minke med __1__.


# Steg 4: Resette telleren {.activity}

## Sjekkliste {.check}

- [ ] Det kan også være kjekt å legge inn en funksjon som resetter telleren, for
  slik at den kan brukes på nytt! Dette kan gjøres ved trykk på knapp A+B eller
  ved at micro:biten ristes. Du kan resette ved å tømme listen.

- [ ] Sånn! Nå er koden vår ferdig og vi kan gå videre til å teste den ferdige
  håndtelleren.

## Test prosjektet {.flag}

Det er to forskjellige måter vi kan teste micro:bit-programmer på:

- [ ] Du kan teste koden i simulatoren og se at tallet øker og minker ved
  knappetrykk. Se også til at håndtelleren resettes som du ønsker.

- [ ] Enda morsommere er det å teste programmet på micro:biten din! Koble
  micro:biten din til datamaskinen med en USB-kabel. Klikk deretter på knappen
  `Last ned` nede til venstre på skjermen.

  Det lastes nå ned en fil som heter `microbit-Uten-navn.hex` til datamaskinen
  din. Samtidig dukker det opp et vindu som sier at du må flytte denne filen til
  MICROBIT-disken på datamaskinen din.

## Utfordring  {.challenge}

- [ ] Man kan også løse oppgaven med å lagre antall passasjerer til en variabel
i stedet for en liste. Se om du greier å få det til!
