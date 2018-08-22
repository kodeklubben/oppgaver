---
title: Lærerveiledning - RGB-lysdiode
author: "Morten Minde Neergaard & Martin Ertsås"
language: nb
---


# Informasjon til veiledere

## Læringsmål

+ `for`- og `while`-løkker

+ Styre en RGB-lysdiode


# Løsningsforslag for fargekombinasjonssykling {.activity}

```cpp
const auto roed_pinne = 9;
const auto groenn_pinne = 10;
const auto blaa_pinne = 11;

const auto roed_styrke = 255 * 0.7;
const auto groenn_styrke = 255 * 0.85;
const auto blaa_styrke = 255;

void setup() {
  for (auto led = 9; led <= 11; ++led) {
    pinMode(led, OUTPUT);
    digitalWrite(led, LOW);
  }
}

void loop() {
  for (auto roed = 0; roed <= 1; ++roed) {
    analogWrite(roed_pinne, roed * roed_styrke);

    for (auto groenn = 0; groenn <= 1; ++groenn) {
      analogWrite(groenn_pinne, groenn * groenn_styrke);

      for (auto blaa = 0; blaa <= 1; ++blaa) {
        analogWrite(blaa_pinne, blaa * blaa_styrke);
        delay(1000);
      }
    }
  }
}
```

## Kommentar {.protip}

Vi har testet dette med RGB-lysdioden som er med i kodegenet sin pakke. For å
kunne se blå og grønn mens rød hadde full intensitet måtte vi skalere
intensiteten til rød med 0.7. Det er også grunnen til at vi har skalert grønn
med 0.85, denne gangen for å kunne se blå.

Skaleringsfaktorene kan variere mellom lysdioder, så hvis disse faktorene ikke
fungerer må en prøve seg frem.
