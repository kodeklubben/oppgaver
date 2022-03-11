---
title: "PXT: Temperatur"
author: Kolbjørn Engeland, Julie Revdahl
language: nb
---


# Introduksjon {.intro}

Kan micro:biten vår brukes som et termometer? Ja, den har faktisk en
temperatursensor!

![Bilde av en microbit som viser bilde av et termometer](temperatur.png)


# Steg 1: Vi rister løs {.activity}

*Vi begynner med å vise et tall når vi rister på micro:biten.*

## Sjekkliste {.check}

- [ ] Start et nytt PXT-prosjekt, for eksempel ved å gå til
  [makecode.microbit.org](https://makecode.microbit.org/?lang=no){target=blank}.

- [ ] Vi vil at noe skal skje når vi rister på micro:biten. Til dette kan vi
  bruke `når ristes`{.microbitinput}-klossen som finnes i kategorien `Inndata`{.microbitinput}.

- [ ] Aller først vil vi bare se at vi får til å vise tallet __1__. For å vise
  et tall bruker vi `vis tall`{.microbitbasic}-klossen fra `Basis`{.microbitbasic}-kategorien.

- [ ] Sett sammen disse to klossene slik at skriptet ditt ser slik ut:
```microbit
input.onGesture(Gesture.Shake, function () {
    basic.showNumber(1)
})
```

## Test prosjektet {.flag}

Det er to forskjellige måter vi kan teste micro:bit-programmer på:

- [ ] Til venstre på skjermen er det et bilde av en micro:bit. Dette er faktisk
  en simulator som kan kjøre programmet vi nettopp laget:

  Siden vår kode skal reagere når man rister på micro:biten kan du simulere
  dette ved å klikke på den hvite prikken til venstre for teksten `SHAKE` på
  micro:bit-simulatoren. Tallet `1` skal vises på skjermen til
  micro:bit-simulatoren.

- [ ] Enda morsommere er det å teste programmet på micro:biten din! Koble
  micro:biten din til datamaskinen med en USB-kabel. Klikk deretter på knappen
  `Last ned` nede til venstre på skjermen.

  Det lastes nå ned en fil som heter `microbit-Uten-navn.hex` til datamaskinen
  din. Samtidig dukker det opp et vindu som sier at du må flytte denne filen til
  MICROBIT-disken. Dersom du trenger hjelp til dette så spør en av veilederne.


# Steg 2: Mål temperaturen {.activity}

*Vi vil vise temperaturen i rommet der vi er. Hvordan gjør vi det på en
 micro:bit?*

## Sjekkliste {.check}

- [ ] Micro:bit har en innebygd temperatursensor som gir temperaturen i °C.
  Dette betyr grader målt i Celcius, og er den enheten vi vanligvis bruker når
  vi snakker om temperatur i Norge. Den kan du få tak i ved å bruke klossen
  `Temperatur (°C)`{.microbitinput} fra `Inndata`{.microbitinput}-kategorien.

- [ ] Prøv selv å legge `Temperatur (°C)`{.microbitinput}-klossen inn i koden
din, slik at den målte temperaturen vises i stedet for __1__ som tidligere.

- [ ] Bruk simulatoren eller last koden til micro:biten din for å teste som
  tidligere. Når du rister på micro:biten (eller klikker på `SHAKE`) skal
  temperaturen måles på nytt. Hvilken temperatur vises? Hva er temperaturen i et
  annet rom eller ute ?


# Steg 3: Temperaturen huskes og vis værtegn {.activity}

*Hva om vi vil bruke temperaturmålingen senere? Da må vi huske hva vi målte!*

## Sjekkliste {.check}

- [ ] Når vi programmerer bruker vi `variabler`{.microbitvariables} til å huske
  ting for oss. La oss lage en variabel som kan huske den målte temperaturen:

  Klikk på `Variabler`{.microbitvariables}-kategorien og deretter på knappen
  `Lag en variabel`{.microbitvariables}. Gi den nye variabelen navnet `temperatur`{.microbitvariables}.
  Du vil se at det dukker opp en ny kloss som heter `temperatur`{.microbitvariables}
  i `Variabler`{.microbitvariables}-kategorien.

  ![Bilde av hvordan lage en ny variabel](variabel_temperatur.png)

- [ ] For å bruke denne nye variabelen kan vi bestemme hva den skal huske med
  `sett variabel til 0`{.microbitvariables}-klossen. La oss endre skriptet vårt
  slik at `temperatur`{.microbitvariables} husker målt temperatur. Legg til og
  flytt på klossene slik at skriptet ditt ser slik ut:

  ```microbit
    let temperatur = 0
    input.onGesture(Gesture.Shake, function () {
        temperatur = input.temperature()
        basic.showNumber(temperatur)
      })
  ```
Om du tester prosjektet ditt nå skal det oppføre seg helt likt som før! Men
denne endringen gir oss nye muligheter! Siden vi nå vet resultatet av
temperaturmålingen kan vi for eksempel vise en sol hver gang vi måler over 20
°C, en paraply hver gang vi måler under 20 °C.

- [ ] Med klossen `vis skjerm`{.microbitbasic} som du finner i `Basis`{.microbitbasic}-kategorien
  kan vi selv bestemme bildet som vises på skjermen til micro:biten. Prøv selv å
  tegne en sol og en paraply på hver sin bilde-kloss (eller andre bilder du
  heller vil bruke). Du kan også bruke en `vis ikon`{.microbitbasic}-kloss med
  ferdiglagde bilder.

- [ ] For å sammenligne to ting bruker vi klosser fra `Logikk`{.microbitlogic}-kategorien.
  Her vil vi sammenligne resultatet av temperaturmålingen med tallet 20. Vi kan
  si at `hvis temperatur > 20`{.microbitlogic} skal vi vise sol-bildet, ellers
  skal vi vise paraply-bildet.

  Prøv å pusle sammen klosser fra `Logikk`{.microbitlogic}- og `Variabler`{.microbitvariables}-kategoriene
  som sier `hvis temperatur > 20`{.microbitlogic}.

- [ ] Vi vil sjekke om temperaturen ble større enn 20 °C. Det betyr at vi må
  legge en `hvis - ellers`{.microbitlogic}-kloss etter løkken vi laget tidligere.
  Programmet ditt vil til slutt se ut omtrent som dette:

```microbit
  let temperatur = 0
  input.onGesture(Gesture.Shake, function () {
      temperatur = input.temperature()
      basic.showNumber(temperatur)
      if (temperatur > 20) {
          basic.showLeds(`
            # . # . #
            . # # # .
            # # # # #
            . # # # .
            # . # . #
            `)
          } else {
            basic.showIcon(IconNames.Umbrella)
        }
      })
```


# Steg 4: Mer avansert termometer {.activity}

*Hva kan vi bruke temperaturmålingene våre til? Prøv selv dine ideer!*

## Flere ideer {.check}

Du har nå lært hvordan micro:biten kan måle temperatur. Men det finnes mange
måter dette kan utvikles videre på. Nedenfor er noen ideer, men finn gjerne på
noe helt eget!

- [ ] Kan man vise måleenheten (°C) etter at temperaturen er vist?

- [ ] En annen temperaturenhet er Fahreinheit, den brukes for eksempel i USA.
  Kan du regne om til Farenheit med formelen `T(°F) = T(°C) × 9/5 + 32`?
