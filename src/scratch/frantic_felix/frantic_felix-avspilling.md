---
title: Frantic Felix - Avspilling
indexed: false
logo: ../../assets/img/ccuk_logo.png
author: Oversatt fra [Code Club UK](//codeclub.org.uk)
translator: Lars-Erik Wollan
license: "[Code Club World Limited Terms of Service](https://github.com/CodeClub/scratch-curriculum/blob/master/LICENSE.md)"
---

## Sjekkliste {.check}

1.  Klar!

  Trykk Lag en Variabel for å lage en index variabel

  ![](variabel.png)


2.  Prøv denne koden

  Få figuren til å følge stien som ble tatt opp.

  ```scratch
  når jeg mottar [replay v]
      sett [index v] til [1]
      gjenta (length of [xs v]) ganger
          sett x til (element (index) av [xs v])
          sett y til (element (index) av [ys v])
          endre [index v] med (1)
          vent (0.1) sekunder
     slutt

  ```
