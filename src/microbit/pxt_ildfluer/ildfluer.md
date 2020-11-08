---
title: "PXT: Ildfluer"
author: 'Oversatt fra [makecode.microbit.org](https://makecode.microbit.org/projects/fireflies)'
translator: 'Kolbjørn Engeland'
language: nb
---


# Introduksjon {.intro}

Ildfluer blinker i mørket om natta. Noen ildfluer er spesielle ved at de kan
blinke nesten i takt. Hvordan er dette mulig? Forskere har funnet ut at hver
ildlfue har sin egen interne klokke og blinker med jevne mellomrom. I tillegg
ser hver ildflue når naboen blinker, og da endrer de litt på på sin egen klokke.
Til slutt kan da hele svermer av ildlfluer blinke i takt. Du kan lese mer om
ildlfuer og synkronisert blinking på
[denne nettsiden](http://ncase.me/fireflies/){target=_blank}.

I denne oppgaven skal vi kode micro:bitene slik at de fungere som en sverm med blinkende
ildfluer.


# Steg 1: Vi lager en ensom ildflue {.activity}

Det første vi skal gjøre er å lage en ensom ildflue som ikke kommuniserer med de andre.
Det gjør vi ved å lage en intern klokke som teller langsomt oppver.
Hver gang den når verdien __8__
bruker en `endre poengsum`{.microbitgame}-kloss fra `Spill`{.microbitgame}-menyen for å vise en liten animasjon.


## Sjekkliste {.check}

- [ ] Lag en variabel som heter `klokke`{.microbitvariables}

- [ ] Bruk `gjenta for alltid`{.microbitbasic}-klossen og legg inn en `hvis-ellers`{.microbitlogic}-kloss
fra `Logikk`{.microbitlogic}-kategorien.

- [ ] Test for om variabelen `klokke`{.microbitvariables} er større eller lik __8__ øverst i
`hvis-ellers`{.microbitlogic}-klossen.

- [ ] I den øverset åpningen i `hvis ellers`{.microbitlogic}-klossen, legg inn en
`endre poengsum med 1`{.microbitgame}-kloss fra `Spill`{.microbitgame}-kategorien, legg inn en
`pause`{.microbitbasic}-kloss og ta en pause på `200 ms`{.microbitbasic}. Sett så variabelen
`klokke`{.microbitvariables} til __0__.

- [ ] I den nederste åpningen i `hvis-ellers`{.microbitlogic}-klossen legg inn en
`pause`{.microbitbasic}-kloss og ta en pause på `100 ms`{.microbitbasic}. Legg så til en
`endre klokke med 1`{.microbitvariables}-kloss fra `Variabler`{.microbitvariables}-kategorien.

```microbit
basic.forever(function () {
    if (klokke >= 8) {
        game.addScore(1)
        basic.pause(200)
        klokke = 0
    } else {
        basic.pause(100)
        klokke += 1
    }
})
```

## Test prosjektet {.flag}

*Nå kan dere teste om micro:biten blinker med jevne mellomrom*

- [ ] Last ned prosjektet til micro:biten.

- [ ] Har dere flere micro:biter i gruppa/klassen? Blinker de i takt?


# Steg 2: Ildfluene kommuniserer {.activity}

Vi kan nå få micro:bitene til å kommunisere ved å be de sende ut et radiosignal
hver gang de blinker. Vi vil også la alle micro:bitene motta radiosignal fra
naboene og endre klokka når signalet mottas.


## Sjekkliste {.check}

- [ ] Alle micro:bitene må bruke samme radiokanal. Dette gjør vi ved å
legge inn en `radio send serienummer`{.microbitradio}-kloss fra `Radio`{.microbitradio}-kategorien inne i `ved start`{.microbitbasic}-klossen.

```microbit
radio.setGroup(1)
```

- [ ] Nå må vi endre på koden fra Steg 1 ved å legge inn en `radio send tall`{.microbitradio}-kloss i den
øverste åpningen i `hvis-ellers`{.microbitlogic}-klossen. Nå sender micro:biten ut et radiosignal hver gang
den blinker.

```microbit
basic.forever(function () {
    if (klokke >= 8) {
        radio.sendNumber(0)
        game.addScore(1)
        basic.pause(200)
        klokke = 0
    } else {
        basic.pause(100)
        klokke += 1
    }
})
```

- [ ] Nå må vi få micro:biten til å motta radio-signal fra andre. Legg inn en
`når mottar recievedNumber`{.microbitradio}-kloss fra `Radio`{.microbitradio}-kategorien. Inne i denne endres klokke med 1.

```microbit
radio.onReceivedNumber(function (receivedNumber) {
    klokke += 1
})
```

## Test prosjektet {.flag}

*Nå kan dere teste om micro:biten blinker med jevne mellomrom*

- [ ] Last ned prosjektet til micro:biten.

- [ ] Har dere flere micro:biter. Blinker de mer i takt?


## Noen utfordringer {.challenge}

*Noen forslag til endringer og utvidelser, men prøv selv dine ideer!*

Nedenfor er noen
ideer til videreutvikling, men finn gjerne på noe helt eget!

- [ ] Kan du la ildfluen din ha sitt helt eget bilde eller animasjon?

- [ ] Hva skjer hvis fluene har ulik klokke?
