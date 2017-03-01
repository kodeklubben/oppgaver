---
title: Monster - Tentakler
indexed: false
logo: ../../assets/img/ccuk_logo.png
author: Oversatt fra [Code Club UK](//codeclub.org.uk)
translator: Lars-Erik Wollan
license: "[Code Club World Limited Terms of Service](https://github.com/CodeClub/scratch-curriculum/blob/master/LICENSE.md)"
---

## Sjekkliste {.check}

+ For å få en tentakel til å bevege seg, kan vi **rotere** den og
  **endre størrelse** ved å bruke `tilfeldig tall`{.blockgreen} med en
  lav verdi i en variabel, for så å vente et øyeblikk før vi
  gjenoppretter den originale størrelsen.

  ```blocks
  sett [tentakelRotasjon v] til (tilfeldig tall fra (1) til (10))
  sett [tentakelStørrelse v] til (tilfeldig tall fra (1) til (10))
  endre størrelse med (tentakelStørrelse)
  vend venstre (tentakelRotasjon) grader
  vent (0.5) sekunder
  endre størrelse med ((tentakelStørrelse) * (-1))
  vend høyre (tentakelRotasjon) grader
  ```

  Merk at vi multipliserer `tentakelStørrelse`{.blockdata} med -1
  for å få en negativ verdi.
