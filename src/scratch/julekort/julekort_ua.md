---
title: Різдвяна листівка
level: 1
author: 'Еспен Клауз'
translator: 'Анатолій Пилипенко'
language: ua
---


# Introduksjon {.intro}

Vi skal lage et julekort i Scratch. Det skal ha noen enkle funksjoner
og animasjoner. Når det er ferdig vil det se omtrent slik ut.

![Eksempel på bilde av et julekort](julekort.png)

# Steg 1: Endre bakgrunn og finne figurer {.activity}

## Sjekkliste {.check}

- [ ] Start et nytt prosjekt. Når du står på startsiden til Scratch,
  trykk på navnet ditt øverst i høyre hjørne.  Trykk så "Mine ting" og
  til slutt "Nytt prosjekt". Du vil se en katt som venter på å bli
  programmert!

- [ ] Trykk på
![Velg figur fra biblioteket](../bilder/velg-bakgrunn.png) nede til
høyre for å importere en ferdig bakgrunn. Velg den bakgrunnen du
vil. Trykk så `Scene`, `Bakgrunner`, velg den tomme bakgrunnen til
venstre, og slett den ved å høyreklikke på den og velg `Slett`.

- [ ] Slett kattefiguren `Sprite1` ved å høyreklikke på ham og slette.

- [ ] Velg nye figurer fra biblioteket med dette ikonet nede til
  høyre: ![Hent fra bibliotek](../bilder/hent-fra-bibliotek.png)

   Legg til isbjørnen, snømannen og juletreet.


# Steg 2: Legge til kode {.activity}

Nå skal vi få figurene til å gjøre ting når de blir klikket på.

## Sjekkliste {.check}

- [ ] Velg isbjørnen og fanen `Skript`{.blocklightgrey} og lag denne
  koden. Når isbjørnen blir klikket på skal den si `God jul!`.
  Deretter skal den skifte utseende hvert sekund, 10 ganger.

  ```blocks
  når denne figuren klikkes
  si [God jul!] i (2) sekunder
  gjenta (10) ganger
      neste drakt
      vent (1) sekunder
  slutt
  ```

## Test prosjektet ditt {.flag}

__Klikk på isbjørnen og se om koden din virker.__

- [ ] Sier isbjørnen `God jul!`?

- [ ] Forandrer isbjørnen stilling?

## Sjekkliste {.check}

- [ ] Velg snømannen og fanen `Skript` og lag denne koden.  Snømannen skal
  spørre etter navnet ditt. Den setter svaret inn i en ny
  setning. Deretter skal den skifte farge.

  ```blocks
  når denne figuren klikkes
  spør [Hva er navnet ditt?] og vent
  si (sett sammen [God jul ] (svar)) i (2) sekunder
  gjenta for alltid
      endre [farge v] effekt med (25)
  slutt
  ```

## Test prosjektet ditt {.flag}

__Klikk på snømannen og se om koden din virker.__

- [ ] Spør snømannen om navnet ditt?

- [ ] Svarer snømannen med navnet ditt når du har skrevet det inn?

- [ ] Forandrer snømannen farge?

## Sjekkliste {.check}

- [ ] Velg juletreet og fanen `Skript`{.blocklightgrey} og lag denne
koden.  Nå skal juletreet skifte farge og utseende.

  ```blocks
  når @greenFlag klikkes
  gjenta for alltid
      vent (0.3) sekunder
      endre [farge v] effekt med (25)
      neste drakt
  slutt
  ```

## Test prosjektet ditt {.flag}

__Trykk på det grønne flagget og se om alt virker.__

- [ ] Endrer treet farge?

- [ ] Danser treet fra side til side?


# Steg 3: Har du ledig tid, sier du? {.activity}

Da har du jobbet godt! Om du fortsatt har ledig tid kan du:

## Sjekkliste {.check}

- [ ] Legge til din egen velkomsthilsen, for eksempel "God jul" eller du
kan synge din egen julesang.

  Klikk på `Scene`, og velg fanen `Lyder`{.blocklightgrey}. Flytt
  musepekeren over `Velg en lyd`-ikonet helt nede til venstre, og
  klikk `Spill inn lyd`.

  ![Bilde av fanen "Lyder" i Scratch](lyder.png)

   Ta opp din egen lyd, og gi den et navn, for
  eksempel `julehilsen`. Gå deretter inn på `Skript`{.blocklightgrey},
  og legg inn følgende kode:

  ```blocks
  når @greenFlag klikkes
  spill lyden [julehilsen v] til den er ferdig
  ```

- [ ] Kanskje finne på noen andre morsomme animasjoner? Snømannen kan
danse eller turne litt? Kan vi ha snakkende eller hoppende gale
julepresanger? Du bestemmer!


# Steg 4: Lagre og publisere {.activity}

Gi julekortet ditt et navn. Klikk `Fil`-menyen øverst til venstre, og klikk `Lagre nå` under den.

Deretter kan du publisere julekortet ditt ved å velge `Legg ut`.

![Bilde av hvordan publisere Scratch julekortet](leggut.png)
