---
title: "BallongBattle"
author: "Sigurd Schaathun" 
language: "nb"
---


# Introduksjon {.intro}

I super:bitpakken er Bit:Bot, en bil som vi kan programmere med micro:bit. I denne oppgaven skal vi lage en fjernstyring til den slik at vi kan ha battle.


# Steg 1: Radiokommunikasjon {.activity}

I de første oppgavene med Bit:Bot, er alt forhåndsprogrammert på en micro:bit som festes på bit:bot. Vi vil fjernstyre bit:bot og da trenger vi to micro:bit som snakker sammen.

## Sjekkliste {.check}

- [ ] I seksjonen Radio finner du alle kodeblokkene for å bruke radiofunksjonene.

- [ ] I kodeblokken __ved start må du fortelle micro:biten hvilken radiokanal som skal brukes. Sett inn `radio sett gruppe`{.microbitradio} og velg f. eks. 42. Alle micro:bit som skal snakke sammen må ha samme kanal. Er du i kodeklubben eller på skolen vil instruktøren eller læreren gi deg en kode.
```microbit

 {

    radio.setGroup(42)

})
````


- [ ] Når du trykker på A skal micro:bit sende et tall.

- [ ] Når micro:biten mottar et tall, skal tallet vises.

```microbit

input.onButtonPressed(Button.A, function () {
   radio.sendNumber(5)
})

radio.onReceivedNumber(function (receivedNumber) {
        basic.showNumber(receivedNumber))
})
```


## Test prosjektet {.flag}

**Last inn programmet på 2 micro:biter.** 

- [ ] Mottar den andre micro:biten når du sender ved å trykke på A?

- [ ] Hvor langt unna kan man være og likevel motta?



# Steg 2: Fjernkontrollprogrammet {.activity}

Nå skal vi sette opp et enkelt fjernstyringsprogram. Micro:biten skal sende tall for å få bit:boten til å gjøre ulike ting. Foreksempel kan 0 være stopp, 1 være å kjøre fremover, 2 sving venstre og 3 sving høyre.

## Sjekkliste {.check}

- [ ] Når micro:bit ristes, skal den sende 0.

- [ ] Når vi trykker på A og B, skal den sende 1.

- [ ] Når vi trykker på A, skal den sende 2.

- [ ] Når vi trykker på B, skal den sende 3.

```microbit
input.onGesture(Gesture.Shake, function () {
    radio.sendNumber(0)
})
input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(1)
})
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(2)
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(3)
})
```

## Test prosjektet {.flag}

**Last inn programmet på den ene micro:biten.**

- [ ] Prøv å trykke på knappene og riste. Mottar den andre micro:biten kommandoene?

- [ ] Ser du noe som mangler i programmet? Hvordan kan vi gi beskjed om å kjøre bakover?

## Tips {.protip}

Micro:bit har en gyro som kan registrere om den holdes vannrett eller tipper oppover eller nedover ved å bruke blokken `helningsvinkel tonehøyde`{.microbitinput} under Inndata-mer. Her er oversettelsen litt dårlig pitch er oversatt med tonehøyde. Det kan vi bruke for å bestemme om den skal kjøre fremover eller bakover.
I tillegg kan vi bruke en `hvis`{.microbitlogic}-løkke og sjekke hvordan knappene er trykket inn.

## Sjekkliste {.check}

- [ ] Legg inn en `hvis`{.microbitlogic}-løkke i `for alltid`{.microbitbasic} kodeblokken.

- [ ] Når `helningsvinkel tonehøyde`{.microbitinput} er mindre enn 0, skal vi ha en ny hvis-løkke.

- [ ] Hvis `knapp A+B trykkes`{.microbitinput}, skal den `send tall 1`{.microbitradio},

- [ ] Hvis ingenting trykkes, skal den `send tall 0`{.microbitradio}.

- [ ] Legg til de øvrige kommandoene den skal sende kommandoer for å kjøre bakover.

```microbit
basic.forever(function () {
    if (input.rotation(Rotation.Pitch) < 0) {
        if (input.buttonIsPressed(Button.AB)) {
            radio.sendNumber(1)
        } else if (input.buttonIsPressed(Button.A)) {
            radio.sendNumber(2)
        } else if (input.buttonIsPressed(Button.B)) {
            radio.sendNumber(3)
        } else {
            radio.sendNumber(0)
        }
    } else {
        if (input.buttonIsPressed(Button.AB)) {
            radio.sendNumber(4)
        } else if (input.buttonIsPressed(Button.A)) {
            radio.sendNumber(5)
        } else if (input.buttonIsPressed(Button.B)) {
            radio.sendNumber(6)
        } else {
            radio.sendNumber(0)
        }
    }
})
```

## Test prosjektet {.flag}

**Last inn programmet på den ene micro:biten.**

- [ ] Prøv å sende kommandoene. Mottar den andre micro:biten kommandoene riktig?

- [ ] Hvorfor sender den 0 når ingen knapper er trykket?

# Steg 3: Kjøre bilen {.activity}

Nå må vi lage programmet på bit:boten. Den skal oversette tallene til bevegelse. Her er det to måter å gjøre det på. Du kan legge til egne bit:bot-koder. Da går du nederst under avansert og velger utvidelser. Der velger du bit:bot og får opp en egen fane som heter bit:bot. Den andre måten er å hardkode - med å bruke `skriv digital`{.microbitpins} eller `skriv analog`{.microbitpins}. Da må du finne ut hvilken pinne som gjør hva.

## Sjekkliste {.check}

- [ ] Her trenger du `Når radio mottar`{.microbitradio} -blokken. Inni den legger du en `hvis`{.microbitlogic}- løkke. Den skal sjekke hvilket kommandotall du mottar.

- [ ] For hvert tall, legg inn den funksjonen du ønsker, enten med bit:bot-kommandoer:

```microbit
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 0) {
        bitbot.stop(BBStopMode.Coast)
    } else if (receivedNumber == 1) {
        bitbot.go(BBDirection.Forward, 100)
    }
})
```
- [ ] Eller bruk hardkoding. Da må du finne ut hvilke pinner som gjør hva, og legge inn:

```microbit
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 0) {
        pins.digitalWritePin(DigitalPin.P16, 0)
        pins.digitalWritePin(DigitalPin.P14, 0)
        pins.digitalWritePin(DigitalPin.P12, 0)
        pins.digitalWritePin(DigitalPin.P8, 0)
    } else if (receivedNumber == 1) {
        pins.digitalWritePin(DigitalPin.P16, 1)
        pins.digitalWritePin(DigitalPin.P14, 1)
        pins.digitalWritePin(DigitalPin.P12, 0)
        pins.digitalWritePin(DigitalPin.P8, 0)
    }
})
```
## Tips {.protip}

`skriv digital`{.microbitpins} er enten 0 eller 1. Hvis du vil kjøre med redusert fart, kan du bruke `skriv analog`{.microbitpins}. Da kan du justere kraften mellom 0 og 1023. Dette må vi bruke for å kunne svinge mens vi rygger.

På undersiden av bit:bot, står det hvilke pinner motoren er koblet til. Når det står P14/P8, er det en pinne for å kjøre fremover og en for å kjøre bakover. Hvis du setter strøm på begge samtidig, vil ikke motoren gå. 

## Test prosjektet {.flag}

**Last inn programmet på micro:biten du setter i bit:boten.**

- [ ] Får du bilen til å bevege seg?

- [ ] Lystrer den fjernstyringen?

- [ ] Hvordan er den å styre?

## Utfordring {.challenge}

- [ ] På Bit:boten er det masse ledlys. Kan du få det til å blinke eller lyse når du kjører?

- [ ] Kan bit:boten få ansikt (bruk `vis bilde`{.microbitbasic}).

- [ ] Hva skjer hvis vi dekker til en micro:bit med aluminiumsfolie? Hvorfor?

## BallongBattle {.flag}

Da er det å blåse opp en ballong og dytte den nedi pennefestet på bit:boten, og feste en knappenål med tape foran på festet. Da kan dere prøve å sprekke ballongene til de andre, mens du beskytter din egen ballong.