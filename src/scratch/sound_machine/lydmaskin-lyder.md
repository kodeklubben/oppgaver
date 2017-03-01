---
title: Lydmaskin - Lyder
indexed: false
logo: ../../assets/img/ccuk_logo.png
author: Oversatt fra [Code Club UK](//codeclub.org.uk)
translator: Lars-Erik Wollan
license: "[Code Club World Limited Terms of Service](https://github.com/CodeClub/scratch-curriculum/blob/master/LICENSE.md)"
---

## Sjekkliste {.check}

+ Lag en ny figur og se om du klarer å få den til å se ut som den
  lyden du vil lage.

+ I fanen `Lyder`, lag et nytt opptak eller importer en lydfil.

  ![Lyder](sound-sample.png)

+ Trykk på figuren og lag et skript som sender en melding til figuren
  når man trykker på den:

  ```blocks
  når denne figuren klikkes
  send melding [katt v]
  ```

+ Nå må vi spille lyden når den får den rette meldingen.

  ```blocks
  når jeg mottar [katt v]
  spill lyden [meow v]
  ```

+ Til slutt endrer vi utseende når lyden spilles.

  ```blocks
  når jeg mottar [katt v]
  spill lyden [moew v]
  sett størrelse til (110) %
  vent (0.1) sekunder
  sett størrelse til (100) %
  ```
