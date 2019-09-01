---
title: "PXT: Send ein hemmeleg beskjed"
author: Helene Isnes
translator: Stein Olav Romslo
language: nn
---


# Introduksjon {.intro}

I denne oppgåva skal du sende og motta hemmelege beskjedar til/frå ein annan
micro:bit ved å bruke radiosignal. Du treng nokon å utveksle hemmelege beskjedar
med! Finn nokon som har lyst å gjere denne oppgåva saman med deg.


# Steg 1: Set opp ei radiogruppe {.activity}

## Sjekkliste {.check}

- [ ] Finn ein `ved start`{.microbitbasic}-kloss (den ligg allereie i kodefeltet,
  elles finn du den nedst i `Basis`{.microbitbasic}).

- [ ] Gå til `Radio`{.microbitradio} og klikk på `radio sett gruppe`{.microbitradio}-klossen.

- [ ] Vel eit gruppenummer mellom __0__ og __255__ som de trur ingen andre her.
  Alle micro:bit-ar i same gruppe kan kommunisere, og du vil ikkje at nokon andre
  skal høyre den hemmelege beskjeden!

  ```microbit
  radio.setGroup(42)
  ```


# Steg 2: Send ein hemmeleg beskjed {.activity}

## Sjekkliste {.check}

- [ ] Gå til `Inndata`{.microbitinput} og finn klossen `når knapp A vert trykt`{.microbitinput}.
  Me brukar denne fordi me vil sende den hemmelege beskjeden når me trykkar på A.

- [ ] Finn klossen `radio send tekst`{.microbitradio} i `Radio`{.microbitradio}.
  Legg den inni `når knapp A vert trykt`{.microbitinput} og skriv inn den
  hemmelege beskjeden du vil sende.

```microbit
input.onButtonPressed(Button.A, function () {
    radio.sendString("Hemmelig beskjed")
})
```

### OBS! {.protip}

Micro:bit-en klarar ikkje å vise Æ, Ø eller Å. Bruk heller AE, OE og AA.

Beskjeden burde heller ikke vere for lang sidan micro:bit-en berre klarar å
sende nokre få ord kvar gong.


# Steg 3: Lag sendar og mottakar {.activity}

No er du klar til å sende hemmelege beskjedar. Men fyrst må me skrive kode slik
at dei hemmelege beskjedane kan bli motteke og lese.

- [ ] Gå til `Radio`{.microbitradio} att og finn `når radio mottek recievedString`{.microbitradio}-klossen:

```microbit
radio.onReceivedString(function (receivedString) {

})
```

"RecievedString" tyder "Motteke tekst" på norsk, og beskjeden som blir motteke
blir lagra i klossen som heiter dette.

- [ ] Legg til ein `vis tekst`{.microbitbasic}-kloss (frå `Basis`{.microbitbasic})
  og `recievedString`{.microbitvariables}-kloss (frå `Variablar`{.microbitvariables}).
  Legg dei slik at koden din for å motta beskjedar ser slik ut:

```microbit
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
```

## Test prosjektet {.flag}

No er me klare til å både sende og motta beskjedar!

- [ ] Last ned koden til micro:bit-en og send dei hemmelege beskjedane til
  kvarandre ved å trykke på A.

## {.tip}

For å laste ned koden må du fyrst ha kopla micro:bit-en til datamaskina med ein
USB-kabel. Klikk på knappen `Last ned` nede til venstre på skjermen. No blir det
lasta ned ei fil som heiter `microbit-Uten-navn.hex` til datamaskina di.
Samstundes dukkar det opp eit vindauge som seier at du må flytte denne fila til
MICROBIT-disken på datamaskina di.


# Ekstra testing {.activity}

Det er mogleg å justere styrken på sendaren til micro:bit-en ved å bruke klossen
`radio sett sendareffekt`{.microbitradio} som du finn viss du trykkar på `Radio`{.microbitradio}
og så `more`{.microbitradio}(meir) rett under. Den høgste styrken sendaren kan
ha er 7. Prøv fleire ulike styrkar når du går gjennom punkta under.

## Sjekkliste {.check}

- [ ] Test kor langt unna kvarandre de kan stå og framleis klare å motta
  beskjedar.

- [ ] Klarar de å sende beskjedar gjennom eit pledd?

- [ ] Kva med veggar?
