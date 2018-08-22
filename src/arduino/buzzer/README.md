---
title: Lærerveiledning - Buzzer
author: Adrian Helle
language: nb
---


# Informasjon til veiledere

## Læringsmål

Oppgaven «Buzzer» introduserer følgende konsepter:

+ Bruke en buzzer for å spille lyd.

+ Lysfølsom motstand.

+ `tone`, `analogRead` og `map`.


# Forklaringer

## Lysfølsom motstand

En lysfølsom motstand endrer motstanden sin basert på lyset den får inn. Jo
høyere lysstyrke den leser, jo lavere motstand yter den. Når vi bruker
`INPUT_PULLUP` setter vi en positiv spenning ut fra pinnen. Jo høyere motstand i
kretsen, jo høyere vil tallet vi leser ut være.

Dvs. at jo mer lys det er i rommet, jo lavere tall leser vi ut.

## PWM

PWM står for "Pulse With Modulation". PWM gjør at vi kan sende et "analogt"
signal på en digital pin. På en ikke-PWM pin vil en sende enten HIGH eller LOW
kontinuerlig, som vil si å enten sende 5v eller 0v, til en velger å sende det
motsatte. Det PWM gjør er å sende 5v i deler av en periode, for så å slå av
strømmen resten av perioden. Jo høyere verdi en setter utgangen til, jo større
del av perioden vil vi sende 5v.

Du kan lese mer om PWM på [Arduino sine
sider](https://www.arduino.cc/en/Tutorial/PWM).

## `analogWrite`

`analogWrite` bruker PWM for å kunne sende "analoge" signaler over en pin. Dette
lar oss blant annet styre lysstyrken på en lysdiode, hastigheten på en motor,
eller fargeintensiteten på en RGB diode.

En verdi på 0 vil sende 0v ut, en verdi på 255 vil sende 5v hele perioden.

## `analogRead`

`analogRead` er en digital utlesning av den analoge spenningen på en pinne.

## `tone`

`tone` spiller av en frekvens en PWM kapabel pin. Du kan få den til å spille av
en frekvens kontinuerlig med `tone(pin, frekvens)`, som så kan stoppes med
`noTone(pin)`. Du kan også generere en tone for en gitt tid med `tone(pin,
frekvens, millisekunder)`, som vil sende en tone i gitt antall millisekunder.
