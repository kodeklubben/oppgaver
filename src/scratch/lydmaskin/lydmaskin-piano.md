---
title: Lydmaskin - Piano
indexed: false
logo: ../../assets/img/ccuk_logo.png
author: Oversatt fra [Code Club UK](//codeclub.org.uk)
translator: Lars-Erik Wollan
license: "[Code Club World Limited Terms of Service](https://github.com/CodeClub/scratch-curriculum/blob/master/LICENSE.md)"
---

## Sjekkliste {.check}

+ Tegn et piano ved å lage svarte og hvite rektangler.

  ![costume1](piano-costume-1.png)

+ Lag et skript som spiller en note når `A` trykkes.

  ```blocks
  når [a v] trykkes
  send melding [piano-1 v]

  når jeg mottar [piano-1 v]
  spill tone (60 v) i (0.5) takter
  ```

+ Lag to noter til for når man trykker `S` eller `D` på tastaturet.

  ```blocks
  når [a v] trykkes
  send melding [piano-1 v]

  når [s v] trykkes
  send melding [piano-2 v]

  når [d v] trykkes
  send melding [piano-3 v]

  når jeg mottar [piano-1 v]
  spill tone (60 v) i (0.5) takter

  når jeg mottar [piano-2 v]
  spill tone (64 v) i (0.5) takter

  når jeg mottar [piano-3 v]
  spill tone (67 v) i (0.5) takter
  ```

+ Kopier drakten 3 ganger og fyll ulike tangenter.

  ![](piano-costume-3.png)

+ Sørg for at hver note bytter til en annen drakt og tilbake til
  `drakt1` slik at det ser ut som tangenten blir trykket på.

  ```blocks
  når jeg mottar [piano-1 v]
  bytt drakt til [costume2 v]
  spill tone (60 v) i (0.5) takter
  bytt drakt til [costume1 v]

  når jeg mottar [piano-2 v]
  bytt drakt til [costume3 v]
  spill tone (60 v) i (0.5) takter
  bytt drakt til [costume1 v]

  når jeg mottar [piano-3 v]
  bytt drakt til [costume4 v]
  spill tone (60 v) i (0.5) takter
  bytt drakt til [costume1 v]
  ```

## Utfordring {.challenge}

En måte å endre hvilket instrument som spilles.

```blocks
når [pil opp v] trykkes
velg instrument (tilfeldig tall fra (1) til (99))
```
