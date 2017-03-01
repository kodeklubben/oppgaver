---
title: Monster - Hengslede armer
indexed: false
logo: ../../assets/img/ccuk_logo.png
author: Oversatt fra [Code Club UK](//codeclub.org.uk)
translator: Lars-Erik Wollan
license: "[Code Club World Limited Terms of Service](https://github.com/CodeClub/scratch-curriculum/blob/master/LICENSE.md)"
---

## Sjekkliste {.check}

+ En arm lages av to figurer, og de kan være ganske vanskelige å
  bygge, siden de to armene må vite om hverandre, slik at de ikke
  skilles og det blir seende rart ut. Dette kan gjøres med matematiske
  beregninger som kalles **trigonometri**, noe som regelmessig brukes
  i produksjon av dataspill, roboter og andre kule teknologier. Armens
  første figur er overarmen, som ikke er så vanskelig, da den ganske
  enkelt vil rotere ved skulderen og flytte seg med kroppen og de
  andre kroppsdelene. En ting vi må legge til er å sette retningen
  `retning`{.blockmotion} til armen i en variabel (mer om det
  seinere).

  ```blocks
  når [mellomrom v] trykkes
  vend venstre (15) grader
  sett [venstre arm v] til (retning)
  send melding [flyttet v]
  endre x med (hastighet)
  ```

+ Den neste beregningen brukes for å kontrollere **underarmen**. Her
  bruker vi trigonometri for å beregne hvor underarmen bør plasseres
  (Det kan godt være at du trenger å be om hjelp når du skal gjøre
  dette).

  ```blocks
  når jeg mottar [flyttet v]
  gå til [Sprite3 v]
  gå til x: ((x-posisjon) + ((45) * ([sin v] av (venstre arm)))) y: ((y-position) + ((45) * ([cos v] av (venstre arm))))
  ```

+ Først oppdaterer armen seg, når meldingen `flyttet`{.blockbrown}
  blir sendt, men du kan bruke hvilken som helst melding, så lenge
  overarmen sender den eller flytter seg til samme medling som
  underarmen.

+ Så flytter underarmen seg selv til **senterpunktet** av overarmen,
  dette er punktet hvor toppen av overarmen er festet til
  skulderen. Vi vil så flytte underarmen slik at den møter
  overarmen. Tenk deg at vi tegner en sirkel mens overarmen roterer
  rundt skulderen, hva er så radius på den sirkelen? Armen i dette
  eksempelet er circa **45 pixler** lang. Vi trenger å finne ut hva
  punktet i den andre enden av armen er, og posisjonerer underarmen
  vår der. Man kan bruke trigonometri formelen over for å
  reposisjonere underarmen og lage en albue.
