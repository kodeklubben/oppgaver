---
title: Rotasjon rundt egen akse
level: 1
author: Carl A. Myrland
---

# Læringsmål {.tips}
+ beskrive og gjennomføre spegling, rotasjon og parallellforskyving
+ beskrive plassering og flytting i rutenett, på kart og i koordinatsystem, med og utan digitale hjelpemiddel, og bruke koordinatar til å berekne avstandar parallelt med aksane i eit koordinatsystem

# Introduksjon {.intro}
I denne oppgaven skal vi importere en geometrisk figur og deretter `rotere`{.blockmotion} den.

![](Geometri.png)

# Steg 1: Vi roterer en likebeint trekant {.activity}

*For å gjøre det enkelt å komme i gang, henter vi inn en ferdig figur fra biblioteket til Scratch.
Denne figuren er tilnærmet lik en likebeint trekant*

## Sjekkliste {.check}

+ Start et nytt prosjekt.
+ Slett kattefiguren ved å høyreklikke på den og velge `slett`.
+ Legg til en ny figur. Klikk på ![Velg figur fra biblioteket](../bilder/hent-fra-bibliotek.png)-knappen og velg trollmannshatten. Vi har brukt `Ting/Wizard Hat`-figuren.
+ Gi den nye figuren navnet `Hattulf` ved å klikke på `i`.
+ Før vi begynner med selve oppgaven, skal vi legge inn en liten hjelpefunksjon om noe uventet skulle skje:

  ```blocks
  når [n v] trykkes
  vis
  pek i retning [90 v]
  gå til x: (0) y: (0)
  ```
+ Skulle noe uventet skje nå, trenger du bare å trykke på tasten N på tastaturet, så vil Hattulf gå tilbake til utgangspunktet, slik at du kan prøve på nytt.

Vi skal nå gi Scratch beskjed om å `rotere`{.blockmotion} hatten 90 grader.

+ Legg til følgende skript på `Hattulf`-figuren din.

  ```blocks
  når grønt flagg klikkes
  vend høyre (90) grader
  ```

## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

+ Hva skjer når du trykker på det grønne flagget?
+ Roterer hatten som forventet?
+ Hva tror du skjer om du trykker på det grønne flagget en gang til? I hvilken retning vil toppen av hatten peke?
+ Hvor mange ganger må du be hatten om å rotere før den er tilbake til utgangspunktet?

## Sjekkliste {.check}

Rotasjon er jo gøy! Men at ting roterer med 90 grader av gangen er jo litt kjedelig, og litt unaturlig.

+ Halver antall grader hatten skal rotere per gang:

  ```blocks
  når grønt flagg klikkes
  vend høyre (45) grader
  ```

## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

+ Hvor mange ganger må du trykke på hatten for at den skal rotere hele veien rundt nå?
+ Fortsett å halvere antall grader hatten skal rotere. Prøv å finne en sammenheng mellom hvor mange grader den roteres, og hvor mange ganger du må trykke på det grønne flagget for at den skal roteres helt rundt.

Du oppdager kanskje at det begynner å bli veldig mange klikk etterhvert?

# Steg 2: A little more action, please! {.activity}

Heldigvis kan vi ved hjelp av litt programmeringsmagi få datamaskinen til å gjøre jobben for oss!

## Sjekkliste {.check}

+ Vi legger til en `styring`{.blockcontrol}-kloss som ber hatten om å rotere et bestemt antall ganger:

  ```blocks
  når grønt flagg klikkes
  gjenta (8) ganger
  vend høyre (45) grader
  ```

+ Tips: For hver gang du halverer vinkelen, må du doble antall repetisjoner for at hatten skal snurre like langt.

# Steg 3: The final countdown {.activity}

+ Du vet kanskje at vi vanligvis omtaler en sirkel som 360 grader. Hvis du fortsetter å halvere antall grader forbi 1,40625, vil du oppdage at gradene blir mindre enn 1, og vi må gjenta roteringen 512 ganger. Selv om dette selvfølgelig er mulig, og absolutt nødvendig i enkelte sammenhenger, er det ikke nøvendig for oss nå.
  Vi tar derfor en snarvei her, og røper at Hattulf skal rotere 1 grad 360 ganger.

  ```blocks
  når grønt flagg klikkes
  gjenta (360) ganger
  vend høyre (1) grader
  ```

## Test prosjektet {.flag}

__Klikk på det grønnet flagget.__

+ Roterer hatten hele veien rundt seg selv når du trykker på grønt flagg?
+ Ved å sette antall grader du roterer pr gang til 1, hvor mange ganger må du rotere `Hattulf` for at han skal gjøre to fulle roteringer? Hva med tre og en halv rotasjon? Ser disse tallene kjent ut?

## Avslutning

+ Lagre prosjektet ved å gi det et navn, for eksempel "Geometri 1"
