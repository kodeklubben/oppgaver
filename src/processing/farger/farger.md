---
title: Farger
level: 1
author: Sigmund Hansen
---

# Introduksjon {.intro}

På skolen lærer vi om farger og hvordan vi kan blande dem for å få
andre farger. Slik er det med farger i datamaskinen også; vi blander
primærfarger og mengden av hver farge bestemmer hvilken farge vi
får. Det er en liten forskjell mellom fargene vi har lært om når vi
tegner og maler og fargene som vises på skjermen. Det skal vi lære om
i denne leksjonen hvor vi skal se nærmere på farger i Processing.

# Steg 1: Mer enn grått {.check}

Her skal vi raskt se litt på farger. I det første punktet viser vi
hele programmet, og i resten av punktene ser vi kun på `draw` som er
den delen av koden som skal endres. For hvert steg kan du kjøre
programmet med **Ctrl + R**, og hvis du vil, kan du lagre det med
**Ctrl + S**.

+ Vi begynner med å fylle bakgrunnen med sort:

    ```processing
    void setup() {
      size(800, 600);
    }
    
    void draw() {
      background(0);
    }
    ```

  Dette har du kanskje sett før. Når vi kaller på `background` med
  bare ett tall får vi en gråtone der `0` er sort og `255` er hvitt.

+ La oss endre på `draw` slik at vi får en rød bakgrunn:

    ```processing
    void draw() {
      background(255, 0, 0);
    }
    ```

  Dette likner på det vi hadde i det første steget, men nå bruker vi
  plutselig tre tall istedenfor ett. La oss utforske dem litt.

+ La oss endre på kallet på `background` igjen:

    ```processing
    void draw() {
      background(0, 255, 0);
    }
    ```

  Hvis du kjører programmet, får du nå en grønn bakgrunn istedenfor en
  rød.

+ La oss endre på kallet på `background` enda en gang:

    ```processing
    void draw() {
      background(0, 0, 255);
    }
    ```

  Og nå får du en blå bakgrunn istedenfor en grønn.

## Forklaring av additive farger {.protip}

Som nevnt har du sikkert lært om farger i skolen og blandet farger med
maling, fargeblyanter eller -stifter. Da lærte du nok om primærfargene
rødt, gult og blått, og at du kunne lage omtrent alle slags farger ved
å blande disse sammen. Jo flere farger du blandet, desto mørkere ble
den ferdige fargen. Dette er fordi du tegnet med fargede pigmenter som
absorberer lys. Jo flere farger i lyset som absorberes, desto færre
farger og mindre lys reflekteres og treffer øyet ditt.

I en datamaskin er det annerledes. Du har nok lagt merke til at
skjermen lyser. Derfor angir vi fargen som hvor mye lys vi skal lage
av hver farge. Siden øyet reagerer på rødt, grønt og blått lys, er
disse valgt som primærfargene i skjermer. Det er derfor de tre
verdiene i kallet på `background` ga oss henholdsvis rødt, grønt og
blått. Fordi primærfargene er rød, grønn og blå kalles dette systemet
som regel RGB. Det er også kjent som et *additivt* system, fordi man
legger sammen fargene, mens i tegning på papir jobber man med et
*subtraktivt* system der farger trekkes fra.

Vi kan også blande farger her, men det oppfører seg litt annerledes
fra du kanskje er vant til fra maling. Hvis vi blander rødt og grønt,
får vi gult. Hvis vi blander grønt og blått, får vi en slags turkis,
kalt cyan. Hvis vi blander rødt og blått, får vi en slags rosa, kalt
magenta. Når alle tre fargene er like sterke, får vi en gråtone. Med
alle tre på fullt, `255`, får vi hvitt.

![](RGB.png "Tre overlappende sirkler i rødt, grønt og blått. Der de
 overlapper blandes fargene til gul, cyan, magenta og hvitt.")

![](FargehjulRGB.png "RGB-fargehjulet med primær- og sekundærfarger.")
