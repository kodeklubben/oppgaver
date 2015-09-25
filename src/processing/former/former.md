---
title: Former
level: 1
logo: ../../assets/img/ccuk_logo.png
author: Sigmund Hansen
license: "[Code Club World Limited Terms of Service](https://github.com/CodeClub/scratch-curriculum/blob/master/LICENSE.md)"
---

# Introduksjon: {.intro}

I denne modulen skal vi lære et programmeringsspråk og verktøy som
heter Processing. Det ble laget for å gjøre programmering lett for
designere og andre som ikke har programmert før, sånn at de kan lage
multimedieprogrammer, spill og liknende. Mange liker Processing fordi
det går fort å lage programmer som vanligvis krever mye arbeid.

# Steg 1: Vindu {.activity}

Nå skal vi begynne helt enkelt med å lage et vindu og fylle det med en
bakgrunnsfarge. Dette vil bli grunnlaget for nesten alle programmer
som du lager med Processing, så det er et fint sted å starte.

## Sjekkliste {.check}

+ Start Processing og skriv dette:

  ```processing
  void setup() {
    size(640, 480);
  }

  void draw() {
    background(0);
  }
  ```
+ Kjør programmet ved å trykke på **Ctrl+R**, knappen med en pil
  eller **Sketch --> Run** i menyen.
+ Lagre programmet som Former ved å trykke på **Ctrl+S** eller
  velg **File --> Save** i menyen.
+ Det anbefales at man utforsker mulighetene litt selv, hva skjer hvis du:
  + Bytter ut det første tallet i size(640, 480);?
  + Bytter ut det andre tallet?
  + Hva om du bruker et annet tall i background(0);?
  + Hva skjer hvis tallet er høyere enn 255?
  + Hva skjer hvis tallet er lavere enn 0?
+ Før du går videre kan det være lurt å fjerne endringene som ble gjort i
  utforskningen med andre tallverdier.

### Tips {.protip}

TODO: Sett inn tabell med oversikt over hvordan man skriver
forskjellige parenteser og spesieltegn på Windows-maskiner og Mac.

Selv om du har utforsket size og background litt, lurer du sikkert på
hva resten av koden gjør eller er godt for. Før vi går videre, skal vi
derfor ta en liten titt på hva all koden gjør.

TODO: Skriv en kort forklaring av setup, draw, size og background.

## Steg 2: Sirkel {.activity}

