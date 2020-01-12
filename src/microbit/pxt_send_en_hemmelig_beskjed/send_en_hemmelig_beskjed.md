---
title: "PXT: Send en hemmelig beskjed"
author: Helene Isnes
language: nb
---


# Introduksjon {.intro}

I denne oppgaven skal du sende og motta hemmelige beskjeder til/fra en annen sin
micro:bit ved å bruke radiosignaler. Du trenger derfor noen å utveksle hemmelige
beskjeder med! Finn noen som har lyst til å gjøre denne oppgaven samtidig med
deg.


# Steg 1: Sett opp en radiogruppe {.activity}

## Sjekkliste {.check}

- [ ] Finn en `ved start`{.microbitbasic}-kloss (den ligger allerede i
  kodefeltet eller du finner den nederst i `Basis`{.microbitbasic}).

- [ ] Gå til `Radio`{.microbitradio} og klikk på `radio sett gruppe`{.microbitradio}-klossen.

- [ ] Velg dere et gruppenummer mellom 0 og 255 som dere tror ingen andre har.
  Alle micro:biter som er i samme gruppe kan kommunisere, og du vil ikke at noen
  andre skal høre den hemmelige beskjeden!

```microbit
radio.setGroup(42)
```


# Steg 2: Send en hemmelig beskjed {.activity}

## Sjekkliste {.check}

- [ ] Gå til `Inndata`{.microbitinput} og finn klossen `når knapp A trykkes`{.microbitinput}.
  Vi bruker denne fordi vi vil sende den hemmelige beskjeden når vi trykker på
  A.

- [ ] Finn klossen `radio send tekst`{.microbitradio} i `Radio`{.microbitradio}.
  Legg den inn i `når knapp A trykkes`{.microbitinput} og skriv inn den
  hemmelige beskjeden du vil sende.

```microbit
input.onButtonPressed(Button.A, function () {
    radio.sendString("Hemmelig beskjed")
})
```


### OBS! {.protip}

Micro:biten klarer ikke å vise Æ, Ø eller Å. Bruk heller AE, OE og AA.

Beskjeden burde heller ikke være for lang siden micro:biten bare klarer å sende
noen få ord av gangen.


# Steg 3: Lag sender og mottaker {.activity}

Du er nå klar til å sende hemmelige beskjeder. Men før du gjør det trenger vi å
skrive kode slik at de hemmelige beskjedene kan bli mottatt og lest.

- [ ] Gå til `Radio`{.microbitradio} igjen og finn `når radio mottar recievedString`{.microbitradio}-klossen:

```microbit
radio.onReceivedString(function (receivedString) {

})
```


"RecievedString" betyr "Mottatt tekst" på norsk, og beskjeden som mottas blir
lagret i klossen som heter dette.

- [ ] Legg til en `vis tekst`{.microbitbasic}-kloss (fra `Basis`{.microbitbasic})
  og `recievedString`{.microbitvariables}-kloss. Du finner denne ved å trykke på
  `recievedString`{.microbitvariables} i klossen du allerede har funnet og dra
  den dit du vil ha den. Legg dem slik at koden din for å motta beskjeder ser
  slik ut:

```microbit
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
```


## Test prosjektet {.flag}

Nå er vi klare til å både sende og motta beskjeder!

- [ ] Last ned koden til micro:biten og send de hemmelige beskjedene til
  hverandre ved å trykke på A.

## {.tip}

For å laste ned koden må du først ha koblet micro:biten til datamaskinen med en
USB-kabel. Klikk deretter på knappen `Last ned` nede til venstre på skjermen.
Det lastes nå ned en fil som heter `microbit-Uten-navn.hex` til datamaskinen
din. Samtidig dukker det opp et vindu som sier at du må flytte denne filen til
MICROBIT-disken på datamaskinen din.


# Ekstra testing {.activity}

Det er mulig å justere styrken på senderen til micro:biten ved å bruke klossen
`radio sett sendereffekt`{.microbitradio} som du finner hvis du trykker på
`Radio`{.microbitradio} og så `more`{.microbitradio} (mer) rett under. Den
høyeste styrken senderen kan ha er 7. Prøv flere ulike styrker når du går
gjennom punktene under.

## Sjekkliste {.check}

- [ ] Test hvor langt unna hverandre dere kan stå og fremdeles klare og motta
  beskjeder.

- [ ] Klarer dere å sende beskjeder gjennom et pledd?

- [ ] Hva med vegger?
