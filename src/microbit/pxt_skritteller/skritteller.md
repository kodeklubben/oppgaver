---
title: "PXT: Skritteller"
author: Julie Christina Revdahl
language: nb
---


# Introduksjon {.intro}

I denne oppgaven skal vi se hvor enkelt vi kan lage en skritteller med micro:biten vår!


# Steg 1: Lage variabler {.activity}

## Sjekkliste {.check}

- [ ] Start et nytt PXT-prosjekt, for eksempel ved å gå til
  [makecode.microbit.org](https://makecode.microbit.org/?lang=no){target=blank}.

- [ ] Først vil vi lage en ny variabel. Dette gjør vi ved å gå inn i `Variabler`
i sidemenyen. Deretter trykker vi på `Lag en variabel` som vi kaller `skritt`.
I denne variabelen skal vi lagre alle skrittene vi går.

- [ ] Når vi skrur på micro:biten vil vi at antall skritt skal være 0. Under
`Variabler` i menyen finner vi klossen `Sett variabel til 0`.

Nå bør koden din se ut som dette:

  ```microbit
  let skritt = 0
  ```

# Steg 2: Vise antall skritt på skjermen {.activity}

## Sjekkliste {.check}

- [ ] Nå vil vi at antall skritt vi har gått skal vises på skjermen. Det skal
ikke bare vises med en gang vi starter, men hele tiden. Vi trenger derfor klossen
`Gjenta for alltid` som vi finner under kategorien `Basis`. Hadde vi brukt klossen
`ved start` istedet, hadde vi visst at vi hadde _0_ skritt når vi startet å gå,
men vi ville ikke sett de nye skrittene underveis.

- [ ] Ved å bruke klossen `Vis tall` fra `Basis`-kategorien kan vi vise
variabelen `skritt` på skjermen. Se om du finner disse klossene på egenhånd!

Nå ligner nok koden din på dette:

  ```microbit
  basic.forever(function () {
    basic.showNumber(skritt)
  })
  ```  


# Steg 3: Telle antall skritt {.activity}

## Sjekkliste {.check}

- [ ] Nå må vi telle antallet skritt vi går. Vi ser for oss at vi fester
micro:biten på én fot. For hver gang micro:biten ristes har vi dermed tatt
 _to_ skritt! Vi trenger derfor en kloss som gjør noe når micro:biten ristes.
 Denne finnes under kategorien `Inndata`. I tillegg trenger du en kloss som
 endrer variabelen `skritt` med 2. Denne finnes under `Variabler`. Greier du å
 sette sammen disse klossene selv?

 Koden for å telle antall skritt bør se slik ut:
```microbit
input.onGesture(Gesture.Shake, function () {
    skritt += 2
})
```

## Test prosjektet {.flag}

Det er to forskjellige måter vi kan teste micro:bit-programmer på:

- [ ] Til venstre på skjermen er det et bilde av en micro:bit. Dette er faktisk
  en simulator som kan kjøre programmet vi nettopp laget:

  Siden vår kode skal reagere når man rister på micro:biten kan du simulere
  dette ved å klikke på den hvite prikken til venstre for teksten `SHAKE` på
  micro:bit-simulatoren.

- [ ] Enda morsommere er det å teste programmet på micro:biten din! Koble
  micro:biten din til datamaskinen med en USB-kabel. Klikk deretter på knappen
  `Last ned` nede til venstre på skjermen.

  Det lastes nå ned en fil som heter `microbit-Uten-navn.hex` til datamaskinen
  din. Samtidig dukker det opp et vindu som sier at du må flytte denne filen til
  MICROBIT-disken på datamaskinen din. Fest micro:biten på foten din før du går
  litt rundt. Teller micro:biten riktig antall skritt?


## Utfordring : Regne ut hvor langt du har gått {.challenge}

- [ ] Greier du å få micro:biten til å regne ut hvor langt du har gått ved å
først måle hvor langt ett av dine skritt er?
