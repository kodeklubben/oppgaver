---
title: 'Fyrverkeri'
level: 2
author: 'Omsett frå [Code Club UK](//codeclub.org.uk)'
translator: 'Stein Olav Romslo'
language: nn
---

# Introduksjon {.intro}

I dette prosjektet skal me skyte opp fyrverkeri over ein by.

![Bilete av ein rakett over ein by](fyrverkeri.png)

# Førebuingar: last ned biletefiler {.activity}

Du kan godt få hjelp frå ein vaksen til å gjere den fyrste delen.

## Sjekkliste {.check}

- [ ] Last ned zip-fila [fyrverkeri_lydogbilder.zip](fyrverkeri_lydogbilder.zip)
  og legg den på skrivebordet på datamaskina di eller ein annan plass der du
  finn ho att.

- [ ] Pakk ut zip-fila ved å høgreklikke på ho og velje `Extract All`,
  `Pakk ut filer` eller noko liknande.

# Steg 1: Lag ein rakett som flyg mot musepeikaren {.activity}

*Me startar med å importere bilete me skal bruke i spelet.*

## Sjekkliste {.check}

- [ ] Lag eit nytt Scratch-prosjekt. Fjern katten ved å høgreklikke på den og
  vel `slett`.

- [ ] Bytt bakgrunnsbilete til til dømes `utendørs/city-with-water`.

- [ ] Klikk på *Ny figur: Last opp figur frå fil* for å leggje til ein
  rakettfigur i prosjektet, `fyrverkeri_lydogbilder/rocket.png`.

- [ ] Me vil at raketten skal skjulast når du klikkar på det grøne flagget.

  ```blocks
  når @greenFlag vert trykt på
  gøym
  ```

No vil me gjerne at raketten skal bevege seg mot musepeikaren når du trykkar
på mellomromtasten.

- [ ] Legg til ein kloss `når mellomrom vert trykt`{.blockevents}. Så lagar me
  to klossar som gjer raketten synleg og let den bevege seg mot musepeikaren.

  ```blocks
  når [mellomrom v] vert trykt
  vis
  gli (1) sekund til x: (mus x) y: (mus y)
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Set musepeikaren over scena og trykk mellomromtasten.

- [ ] Ser du raketten og beveger den seg mot musepeikaren?

- [ ] Kva skjer om du flyttar på musepeikaren og trykkar mellomrom att?

## Sjekkliste {.check}

Fyrverkeri brukar ikkje å fly frå side til side, så du ber gjere det slik at
raketten alltid flyg mot musepeikaren frå botnen av skjermen.

- [ ] Før du fyrar opp raketten: bruk klossen `gå til`{.blockmotion} for å
  få raketten til å flytte seg til botnen av skjermen, men slik at den er same
  stad horisontalt.

  ```blocks
  når @greenFlag vert trykt på
  gøym

  når [mellomrom v] vert trykt
  gå til x: (mus x) y: (-200)
  vis
  gli (1) sekund til x: (mus x) y: (mus y)
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Trykk mellomromtasten.

- [ ] Flyg raketten mot musepeikaren fra botnen av skjermen?

- [ ] Kva skjer om du flyttar på musa og trykkar mellomrom att?

## Sjekkliste {.check}

- [ ] Prøv å få til det det same ved å bruke museknappen i staden for
  mellomromtasten. For å gjere det kan me pakke skriptet vårt inn i
  `gjenta for alltid`{.blockcontrol}- og `viss museknappen er
  trykt`{.blockcontrol}-klossar.

- [ ] Flytt skriptet frå `når mellomrom vert trykt`{.blockevents} til `når
  @greenFlag vert trykt på`{.blockevents}, så det ser slik ut:

  ```blocks
  når @greenFlag vert trykt på
  gøym
  gjenta for alltid
      viss <museknappen er trykt?>
          gå til x: (mus x) y: (-200)
          vis
          gli (1) sekund til x: (mus x) y: (mus y)
      slutt
  slutt
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Set musepeikaren over scena og klikk. Klikk igjen ein annan stad.

- [ ] Kjem det rakettar flygande?

## Utfordringar {.challenge}

- [ ] Prøv å få nokre rakettar til å bevege seg litt seinare eller raskare
  enn andre.

- [ ] Prøv å endre korleis raketten flyg mot musepeikaren. Til dømes kan du
  få den til å gå i ei boge.

# Steg 2: Få raketten til å eksplodere {.activity}

*No skal me få raketten til å eksplodere med eit digert smell!*

## Sjekkliste {.check}

- [ ] Fyrste steg for å få raketten til å eksplodere er å spele av eit smell
  før den startar å bevege seg, og så å gøyme seg når den når musepeikaren.
  For å importere ein lyd kan du gå til fana `Lydar`{.blocklightgrey} og klikke
  *Last opp lyd fra fil*. Last opp lyden `fyrverkeri_lydogbilder/bang.wav`.

  ```blocks
  når @greenFlag vert trykt på
  gøym
  gjenta for alltid
      viss <museknappen er trykt?>
          gå til x: (mus x) y: (-200)
          start lyden [bang v]
          vis
          gli (1) sekund til x: (mus x) y: (mus y)
          gøym
      slutt
  slutt
  ```

- [ ] Neste steg er å få raketten til å sende ei melding til reisten av spelet
  når den eksploderer. Me skal lytte etter meldinga seinare. Lag ei ny melding
  som heiter `Eksploder`.

  ```blocks
  når @greenFlag vert trykt på
  gøym
  gjenta for alltid
      viss <museknappen er trykt?>
          gå til x: (mus x) y: (-200)
          start lyden [bang v]
          vis
          gli (1) sekund til x: (mus x) y: (mus y)
          gøym
          send meldinga [Eksploder v]
      slutt
  slutt
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Syt for at raketten speler av lyden og gøymer seg når den når
  musepeikaren.

- [ ] PRøv å endre talet i `gli`{.blockmotion}-klossen slik at raketten blir
  gøymt samstundes som det smell.

## Sjekkliste {.check}

- [ ] Last opp ein ny figur fra fil, `fyrverkeri_lydogbilder/firework1.png`.

- [ ] Når denne figuren får meldinga `Eksploder` passar me på at den er gøymt,
  flyttar den til raketten med klossen `gå til`{.blockmotion}, viser den og
  skjuler den att eitt sekund seinare.

  ```blocks
  når eg får meldinga [Eksploder v]
  gøym
  gå til x: ([x-posisjon v] av [rocket v]) y: ([y-posisjon v] av [rocket v])
  vis
  vent (1) sekund
  gøym
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Blir raketten erstatta av eit eksplosjonsbilete når den eksploderer?

- [ ] Kva skjer viss du heldt museknappen nede medan du flyttar musepeikaren?
  (Ta det med ro, me skal fikse det seinare.)

# Steg 3: Gjer kvar eksplosjon unik {.activity}

*No skal me lage variantar slik at ikkje alle eksplosjonane ser like ut.*

## Sjekkliste {.check}

- [ ] For å gjere kvar eksplosjon unik brukar me klossen `sett
  fargeeffekt`{.blocklooks} og vel ei tilfeldig farge før eksplosjonen blir
  vist.

  ```blocks
  når eg får meldinga [Eksploder v]
  gøym
  set [farge v]-effekt til (tilfeldig tal frå (1) til (200))
  gå til x: ([x-posisjon v] av [rocket v]) y: ([y-posisjon v] av [rocket v])
  vis
  vent (1) sekund
  gøym
  ```

- [ ] Legg til fleire bilete av eksplosjonar som drakter ved å velje
  `Drakter`{.blocklightgrey}-fana til `firework1`. Ved å klikke *Last
  opp drakt frå fil* kan du leggje til `firework2.png`, `firework3.png` og
  `firework4.png` frå `fyrverkeri_lydogbilder`.

- [ ] Klarar du å få eksplosjonane til å bruke ulike drakter? (Hint: Du kan
  til dømes bruke `neste drakt`{.blocklooks} ein passande stad i skriptet
  til Firework1.)

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Har eksplosjonane ulike farger?

- [ ] Ser kvar eksplosjon ulik ut?

## Sjekkliste {.check}

- [ ] Til slutt skal eksplosjonen bli større etter at raketten eksploderer!
  I staden for å vente i eitt eksund kan du setje storleiken til figuren til
  5 % før den blir vist, og så aukar du storleiken med fem 20 gonger ved å
  bruke klossen `gjenta`{.blockcontrol}.

  ```blocks
  når eg får meldinga [Eksploder v]
  gøym
  neste drakt
  set [farge v]-effekt til (tilfeldig tal frå (1) til (200))
  gå til x: ([x-posisjon v] av [rocket v]) y: ([y-posisjon v] av [rocket v])
  set storleik til (5) %
  vis
  gjenta (20) gongar
      endra storleik med (5)
  slutt
  vent (1) sekund
  gøym
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Spreier eksplosjonen seg ut frå midten av raketten?

- [ ] Veks eksplosjonen gradvis?

## Utfordringar {.challenge}

Prøv å gjere kvar eksplosjon endå meir unik. Endre storleiken og
kor raskt eksplosjonen veks.

# Steg 4: Fiks "send melding"-feilen {.activity}

Hugsar du at me har eit problem dersom me heldt museknappen nede?

Problemet skjer fordi raketten sender meldinga si om eksplosjonen og gjentek
`viss`{.blockcontrol}-løkka med ein gong. Dermed blir eksplosjonsmeldinga sendt
før den førre er ferdig med animasjonen sin.

I programmeringsverda kallar me denne typen problem for *bugs* fordi i gamle
dagar var datamaskinene så mykje større at ein kunne få problem med at
innsekt vart fanga inne i datamaskina og øydela programmet.

## Sjekkliste {.check}

- [ ] For å fikse problemet kan du erstatte klossen `send melding`{.blockevents}
  med `send meldinga og vent`{.blockevents}. Då vil ikkje løkka gjenta seg før
  den førre eksplosjonen er ferdig. Gå tilbake til `rocket` og
  endre skriptet:

  ```blocks
  når @greenFlag vert trykt på
  gøym
  gjenta for alltid
      viss <museknappen er trykt?>
          gå til x: (mus x) y: (-200)
          start lyden [bang v]
          vis
          gli (1.5) sekund til x: (mus x) y: (mus y)
          gøym
          send meldinga [Eksploder v] og vent
      slutt
  slutt
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Dukkar eksplosjonen opp på riktig stad og til riktig tid?

## Lagre prosjektet {.save}

__Gratulerer, du er ferdig! No kan du kose deg med spelet!__

Ikkje gløym å dele spelet ditt med venene og familien din! Klikk på `Legg ut`
i menylinja.
