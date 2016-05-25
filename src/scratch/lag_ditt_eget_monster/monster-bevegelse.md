---
title: Monster - Bevegelse
indexed: false
logo: ../../assets/img/ccuk_logo.png
author: Oversatt fra [Code Club UK](//codeclub.org.uk)
translator: Lars-Erik Wollan
license: "[Code Club World Limited Terms of Service](https://github.com/CodeClub/scratch-curriculum/blob/master/LICENSE.md)"
---

## Sjekkliste {.check}

+ Etterhvert vil monsteret ditt bestå av en mengde figurer og det vil
  bli nødvendig å sørge for at alle figurene flyttes sammen. I stedet
  for å legge til flyttkommandoer på alle figurer, kan du rett og
  slett legge til kontroller på kroppsfiguren og bruke en `send
  melding`{.blockevents} for å kontrollere andre figurer.  Når vår
  tentakkelfigur (eller en hvilken som helst annen figur!) mottar en
  `flyttet høyre`-melding, kan vi flytte den også til høyre.

  ```blocks
  // på spøkelseskroppen
  når [pil høyre v] trykkes
  endre x med (hastighet)
  send melding [flyttet høyre v]

  når [pil venstre v] trykkes
  endre x med ((hastighet) * (-1))
  send melding [flyttet venstre v]

  // på tentakkelen
  når jeg mottar [flyttet høyre v]
  endre x med (hastighet)

  når jeg mottar [flyttet venstre v]
  endre x med ((hastighet) * (-1))
  ```

+ Ved å bruke en `send melding`{.blockevents} kan vi også endre
  hvordan bevegelseskommandoen virker, ved å bare endre et
  skript. **Ta en titt på dette eksempelet:**

  ```blocks
  // på spøkelseskroppen
  når [pil høyre v] trykkes
  endre x med (hastighet)
  pek i retning (90 v)
  sprett tilbake ved kanten
  hvis <ikke <berører [kant v]?>>
      send melding [flyttet høyre v]
      send melding [flyttet v]
  slutt

  når [pil venstre v] trykkes
  endre x med ((hastiget) * (-1))
  pek i retning (-90 v)
  sprett tilbake ved kanten
  hvis <ikke <berører [kant v]?>>
      send melding [flyttet venstre v]
      send melding [flyttet v]
  slutt
  ```

+ Her forteller vi at kroppen skal gå i den retningen den beveger seg
  i (husk å sette figur orienteringen til **“venstre-høyre”**) og for
  å stoppe og at den snur hvis den kolliderer med
  skjermkanten. Kanskje har du også lagt merke til at vi har lagt
  meldingen i en `hvis`{.blockcontrol}-kloss, vi vil bare at de andre
  kroppsdelene skal bevege seg hvis kroppen ikke er i kanten av
  skjermen. **Hvis du bestemmer deg for å legge til animasjon på
  bevegelsen, må du huske på at tilhørende bevegelser vil ta like lang
  tid. f. eks hvis å bevege et bein til venstre tar 1 sekund, må alle
  andre venstrebevegelser ta et sekund også (bruk en
  `vent`{.blockcontrol}-kloss for å sørge at de er i samme steg).**

+ Du kan også animere kroppsfiguren ved å bruke `neste
  drakt`{.blocklooks}, som kan aktiveres hver gang en
  bevegelsesmelding mottas.

  ```blocks
  når jeg mottar [flyttet høyre v]
  neste drakt
  ```
