---
title: Forskyving
level: 1
author: Carl A. Myrland
indexed: false
---

## Læringsmål {.tips}
+ beskrive og gjennomføre spegling, rotasjon og parallellforskyving
+ beskrive plassering og flytting i rutenett, på kart og i koordinatsystem, med og utan digitale hjelpemiddel, og bruke koordinatar til å berekne avstandar parallelt med aksane i eit koordinatsystem

# Introduksjon {.intro}

Denne oppgaven forutsetter at du har fullført oppgave 1 i denne oppgaveserien.

Vi skal nå se på hvordan vi kan flytte en figur rundt på skjermen uten at den endrer form, størrelse eller retning. Det kalles en forskyvning!

Aller først henter vi frem `Hattulf` fra forrige oppgave. Trykk på "mine ting" og velg å "se inni" den forrige oppgaven din.

Vi skal la rotasjonen ligge en liten stund, så vi kobler ganske enkelt "Når grønt flagg klikkes"-boksen fra resten av koden.
Ikke slett koden, vi skal bruke den igjen senere!

# Steg 1: Vi forskyver Hattulf {.activity}

Vi må huske at for en datamaskin foregår all bevegelse på skjermen i et koordinatsystem. Koordinatene for bevegelse i lengderetning, altså fra høyre til venstre, kaller vi x-koordinater.
Vil du bevege deg i høyden må vi endre på y-koordinatene.

Vi begynner med å endre på X-koordinatene

## Sjekkliste {.check}

+ Vi henter en `endre x med`-{.blockmotion} fra `Bevegelse`{.blockmotion} og kobler den til `Når grønt flagg klikkes`{.blockcontrol}
+ Du kan endre verdien med så mye som du selv ønsker.

  ```blocks
  når grønt flagg klikkes
  endre x med ()
  ```
+ Det blir litt slitsomt å holde kontroll på hvor hatten er hele tiden. Derfor legger vi til en tastekommando som får hatten tilbake til utgangspunktet, koordinatet (0,0):

  ```blocks
  når [o] trykkes
  gå til x: (0) y: (0)
  ```

## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

+ Hva skjer?
+ Husk å trykke "o" om `Hattulf` forsvinner ut av bildekanten
+ Utfordring: Ved å bruke det du kan om bevegelser på ei tallinje, kan du få `Hattulf` til å gå til venstre på skjermen ved å endre på verdien til tallet du endrer x med. Får du det til?

# Steg 2: Flytte `Hattulf` langs y-aksen. {.activity}

Du blir kanskje ikke veldig overrasket over at vi nå skal benytte oss av `endre y med ()`{.blockmotion}.

+ Nå skal kodeblokken din se slik ut:

  ```blocks
  når grønt flagg klikkes
  endre y med ()
  ```
