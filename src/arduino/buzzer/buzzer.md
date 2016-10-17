---
title: Buzzer
level: 1
author: Adrian Helle
---

# Introduksjon {.intro}

Nå som vi har sett litt på hvordan vi kan kontrollere en lysdiode på
forskjellige måter, kan vi gå over til å lage litt lyd!

# Steg 1: Finn frem utstyr {.activity}

Før vi kan begynne å lage kretsen og koden, er vi nødt til å finne frem alt vi trenger.
I denne oppgaven trenger vi i hovedsak en buzzer.

## Dette trenger du {.check}

+ 1 Arduino Uno
+ 1 breadboard
+ 2 ledninger
+ 1 buzzer

<figure><img src="buz.jpg" style="width: 900px"></figure>

# Steg 2: Lag kretsen {.activity}

Før vi kan begynne med programmeringen, så er vi nødt til å lage en krets.
Hvis du nå har funnet frem alt du trenger kan du følge instruksjonene og illustrasjonen
under.

<figure><img src="krets.png" style="width: 900px"></figure>


## Sjekkliste {.check}

+ Ledning fra GND på Arduinoen til den negative lederen på buzzeren.
+ Ledning fra 11~ på Arduinoen til den positive lederen på buzzeren.

## Porter merket med ~ {.protip}

Husker du hva "~" betyde? Det har seg slik at alle porter merket med "~"
har en spesiel funksjon kalt PWM. Dette står for "Pulse With Modulation"
og brukes for å lage et analogt signal. I denne oppgaven bruker vi dette
for å generer toner.

# Steg 3: Lag en tone {.activity}

*Nå skal vi lage vår første tone med Arduinoen.*

## Sjekkliste {.check}

+ Åpne Arduino-programmet om det ikke allerede er åpent.
+ Arduino-programmet starter med denne koden:

  ```cpp
  void setup(){

  }

  void loop(){

  }
  ```

+ Skriv denne koden:

  ```cpp
  int lyd = 11;

  void setup(){
    pinMode(lyd, OUTPUT);
  }

  void loop(){
    tone(lyd, 880);
  }
  ```

+ Trykk på ![](upload.png) for å laste opp koden. Denne sjekker først om koden
er riktig, og så vil programmet ditt kjøre på arduinoen.
+ Lager den lyd?

### Virker det ikke? {.protip}

Hvis det ikke virker, så kan det hende at Arduino-programmet står på feil __port__
og/eller __brett__. Da kan du sjekke disse to tingene:

+ Brett er satt riktig: __Tools -> Board -> Arduino/Genuino Uno__

+ Port er satt riktig:
	+ Windows: __Tools -> Port -> COM1__ (kan være et annet tall)
	![](port.png)
	+ Mac: __Tools -> Port ->/dev/tty.usbmodem262471__ (kan være et annet tall)

Hvis dette ikke fungerer, kan du prøve å lukke programmet og åpne det igjen.


### Utfordringer {.challenge}

+ Klarer du å finne ut hvilken tone dette er? (Hint: 880 er frekvensen til tonen.)
+ Klarer du å lage en annen tone?

# Steg 4: Bruk en fotoresistor til å styre lyden {.activity}

Vi kan bruke en lyssensor for å styre lyden også. La oss se hvordan vi kan få en
fotoresistor til å styre lyden. En fotoresistor varierer motstanden etter hvor mye
lys den får inn. Finn frem alt du trenger og koble opp slik som på diagrammet under
og følg sjekklisten!
<figure><img src="foto.jpg" style="width: 900px"></figure>
<figure><img src="ldr.png" style="width: 900px"></figure>


## Sjekkliste {.check}

+ La alle de andre komponentene være som før.
+ Ledning fra en fot på fotoresistoren til A5 på arduinoen.
+ Ledning fra fot på fotoresistor til GND.
+ Skriv  koden under:
```cpp
int lyd = 11;
int lys = A3;

void setup() {
	pinMode(lys, INPUT_PULLUP);
	pinMode(lyd, OUTPUT);
}

void loop() {
	tone(lyd, analogRead(lys)*3.2);
}
```

Se der! Nå har du lært å lage litt lyd med Arduino!

### Utfordringer {.challenge}
Her er noen nøtter du kan prøve deg på ved å endre koden.

+ Klarer du å bruke knapper for å spille forskjellige toner?
+ Kan du få en RGB lysdiode til å lyse forskjellige farger for forskjellige toner?
