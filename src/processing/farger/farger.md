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

  Hvis du kjører programmet, får du nå en blå bakgrunn istedenfor en
  grønn.

