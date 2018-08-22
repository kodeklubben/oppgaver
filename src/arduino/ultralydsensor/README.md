---
title: Lærerveiledning - Ultralydsensor
author: "Martin Ertsås & Morten Minde Neergaard"
language: nb
---


# Informasjon til veiledere

## Læringsmål

Oppgaven «Ultralydsensor» introduserer flere konsepter:

+ Bruk av ultralydsensor

+ Seriellkonsoll


# Koblingsskjema

Elevene skal allerede ha løst en del oppgaver før de begynner på denne, men
hittil alltid fått koblingsskjema utlevert. Denne oppgaven kan være en god
anledning til å la dem prøve å koble opp komponentene uten skjema. Det kan dog
være greit å ha et koblingsskjema eller tre i bakhånd for å dele ut:

![kobling](ultra.png)


# Hjelp til 7-segment-utfordringen

I oppgaven [7-Segment Display](../7_segment_display/7_segment_display.html) har
vi laget koden som kan vise et tall mellom 0 og 9 på et display. Koden under vil
bare skrive ut «Om du hadde hatt et display burde det vist tallet (tall)» om og
om igjen på seriellkonsollet.

```cpp
const auto ekko = 2; // Echo pin
const auto sender = 3; // Trig pin
const auto lydens_hastighet = 0.034029; // 340.29 m/s

void setup() {
  Serial.begin(9600);
  pinMode(ekko, INPUT);
  pinMode(sender, OUTPUT);

  digitalWrite(sender, LOW);
}

void loop() {
  digitalWrite(sender, HIGH);
  delayMicroseconds(5);
  digitalWrite(sender, LOW);

  auto tid = pulseIn(ekko);
  auto avstand = (tid * hastighet) / 2;

  auto syvsegment = map(avstand, 0, 127, 0, 9);
  Serial.print("Om du hadde hatt et display burde det vist tallet ");
  Serial.println(constrain(syvsegment, 0, 9));

  delay(100);
}
```

`map` vil lineært skalere `avstand` fra verdiområdet 0-127 til en verdi fra 0
til 9. En avstand på over 127 cm vil gi høyere verdier enn 9.

Tallet 127 cm er litt tilfeldig valgt som et tall som kan gi mening for å
oppdage gjenstander rundt pulten. Ultralydsensoren skal kunne «se» opp til 4
meter fremfor seg, men da må de være store og flate (f.eks. en vegg).

For formelen brukt i `map`, se referansen for hos
[arduino.cc](https://www.arduino.cc/reference/en/language/functions/math/map/).
Dette kan være relevant om man vil vinkle denne oppgaven inn mot matematikk.

`constrain` vil her gjøre at alle verdier høyere enn 9 vil bli satt til 9.
