---
title: Monster - Hjul
indexed: false
logo: ../../assets/img/ccuk_logo.png
author: Oversatt fra [Code Club UK](//codeclub.org.uk)
translator: Lars-Erik Wollan
license: "[Code Club World Limited Terms of Service](https://github.com/CodeClub/scratch-curriculum/blob/master/LICENSE.md)"
---

## Sjekkliste {.check}

+ For å få et hjul til å bevege seg, kan vi **rotere** det litt av
  gangen og flytte det når vi mottar en **flyttet melding**.

  ```blocks
  når jeg mottar [flyttet venstre v]
  endre x med ((hastighet) * (-1))
  vend høyre (15) grader

  når jeg mottar [flyttet høyre v]
  endre x med (hastighet)
  vend venstre (15) grader
  ```

+ Hvis du vil, kan du erstatte verdiene med variabler som
  `hastighet`{.blockdata}, slik at du kan kontrollere hastigheten i
  alle retninger fra ett sted.

**(Merk at vi har multiplisert `hastighet`{.blockdata} med -1 for å få
  negativ verdi, og bevege hjulet i motsatt retning)**
