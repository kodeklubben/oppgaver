---
title: Lydmaskin - Tromme
indexed: false
logo: ../../assets/img/ccuk_logo.png
author: Oversatt fra [Code Club UK](//codeclub.org.uk)
translator: Lars-Erik Wollan
license: "[Code Club World Limited Terms of Service](https://github.com/CodeClub/scratch-curriculum/blob/master/LICENSE.md)"
---

## Sjekkliste {.check}

+ Importer en ny figur ved å velge `Ting/Drum1`. Gi den navnet `Tromme`.

+ Vi vil at trommen skal lage lyd når vi klikker på den eller trykker
  på `mellomromstasten`.

  ```blocks
  når denne figuren klikkes
  send melding [tromme v]

  når [mellomrom v] trykkes
  send melding [tromme v]
  ```

+ Nå må vi lage lyd når den mottar `tromme`. Ved å endre tallet, kan
  du endre lyden trommen lager.

  ```blocks
  når jeg mottar [tromme v]
  trommeslag (48 v) som varer (0.2) takter
  ```

+ Prøv å endre utseende slik at man ser hvilket instrument som
  spiller.

  ```blocks
  når jeg mottar [tromme v]
  trommeslag (48 v) som varer (0.2) takter
  sett størrelse til (110) %
  vent (0.1) sekunder
  sett størrelse til (100) %
  ```
