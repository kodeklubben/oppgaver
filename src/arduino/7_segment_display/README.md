---
title: Lærerveiledning - 7-Segment Display
author: "Martin Ertsås & Morten Minde Neergaard"
language: nb
---


# Informasjon til veiledere

## Læringsmål

Oppgaven «7-Segment Display» introduserer flere konsepter:

+ En teknikk for å utforske ukjente komponenter

+ 7-Segment Display

+ Funksjoner og funksjonskall

+ Switch statements

## Merk

Denne oppgaven krever at elevene holder styr på en god del ledninger, og
sluttresultatet vil se noe kaotisk ut.

![kaotisk](kaotisk.jpg)


# Løsningsforslag

## Display som teller opp og ned med to knapper

Kobling:

![Kobling](toknappkrets.jpg)

Kode:

```cpp
void blank() {
  for (int led = 6; led <= 13; led++) {
    digitalWrite(led, LOW);
  }
}

void tegn_0() {
  blank();
  digitalWrite(7, HIGH);
  digitalWrite(8, HIGH);
  digitalWrite(9, HIGH);
  digitalWrite(12, HIGH);
  digitalWrite(11, HIGH);
  digitalWrite(10, HIGH);
}

void tegn_1() {
  blank();
  digitalWrite(9, HIGH);
  digitalWrite(12, HIGH);
}

void tegn_2() {
  blank();
  digitalWrite(8, HIGH);
  digitalWrite(9, HIGH);
  digitalWrite(6, HIGH);
  digitalWrite(10, HIGH);
  digitalWrite(11, HIGH);
}

void tegn_3() {
  blank();
  digitalWrite(8, HIGH);
  digitalWrite(9, HIGH);
  digitalWrite(6, HIGH);
  digitalWrite(12, HIGH);
  digitalWrite(11, HIGH);
}

void tegn_4() {
  blank();
  digitalWrite(7, HIGH);
  digitalWrite(6, HIGH);
  digitalWrite(9, HIGH);
  digitalWrite(12, HIGH);
}

void tegn_5() {
  blank();
  digitalWrite(8, HIGH);
  digitalWrite(7, HIGH);
  digitalWrite(6, HIGH);
  digitalWrite(12, HIGH);
  digitalWrite(11, HIGH);
}

void tegn_6() {
  blank();
  digitalWrite(8, HIGH);
  digitalWrite(7, HIGH);
  digitalWrite(10, HIGH);
  digitalWrite(11, HIGH);
  digitalWrite(12, HIGH);
  digitalWrite(6, HIGH);
}

void tegn_7() {
  blank();
  digitalWrite(8, HIGH);
  digitalWrite(9, HIGH);
  digitalWrite(12, HIGH);
}

void tegn_8() {
  blank();
  digitalWrite(8, HIGH);
  digitalWrite(7, HIGH);
  digitalWrite(6, HIGH);
  digitalWrite(12, HIGH);
  digitalWrite(10, HIGH);
  digitalWrite(11, HIGH);
  digitalWrite(9, HIGH);
}

void tegn_9() {
  blank();
  digitalWrite(8, HIGH);
  digitalWrite(7, HIGH);
  digitalWrite(6, HIGH);
  digitalWrite(9, HIGH);
  digitalWrite(12, HIGH);
}

int minus = 5;
int pluss = 4;
int tall = 0;

void setup() {
  for (int led = 6; led <= 13; led++) {
    pinMode(led, OUTPUT);
  }
  pinMode(pluss, INPUT_PULLUP);
  pinMode(minus, INPUT_PULLUP);
  tegn_0();
}

void oppdater() {
  switch (tall) {
    case 1:
      tegn_1();
      break;
    case 2:
      tegn_2();
      break;
    case 3:
      tegn_3();
      break;
    case 4:
      tegn_4();
      break;
    case 5:
      tegn_5();
      break;
    case 6:
      tegn_6();
      break;
    case 7:
      tegn_7();
      break;
    case 8:
      tegn_8();
      break;
    case 9:
      tegn_9();
      break;
    case 10:
      tall = 9;
      break;
    default:
      tegn_0();
      tall = 0;
      break;
  }
  digitalWrite(13, HIGH);
  delay(150);
  digitalWrite(13, LOW);
  delay(150);
}

void loop() {
  if (digitalRead(pluss) == LOW) {
    tall += 1;
    oppdater();
  }
  if (digitalRead(minus) == LOW) {
    tall -= 1;
    oppdater();
  }
}
```
