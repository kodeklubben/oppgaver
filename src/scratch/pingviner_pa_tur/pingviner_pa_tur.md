---
title: 'Pingviner på tur'
level: 1
author: 'Geir Arne Hjelle'
language: nb
---

# Introduksjon {.intro}

Velkommen til Scratch. Vi skal sammen lage et enkelt spill hvor pingvinene har
rømt fra akvariet i Bergen, og det er din jobb å hjelpe dem hjem igjen.

![](pingviner_pa_tur.png)

# Velkommen til Scratch {.activity}

_Om du allerede kjenner Scratch og har en Scratchbruker kan du gå videre til
[Steg 1](#steg-1-en-pingvin-pa-tur)._

[Scratch](https://scratch.mit.edu/) er et programeringsspråk laget spesielt for
at det skal være raskt å komme i gang med, og for at man raskt skal kunne lage
sine egne spill og animasjoner. Scratch kjører i nettleseren og er helt gratis å
bruke. Før du begynner å programmere er det lurt å lage seg en Scratchbruker
fordi dette gjør det enklere å lagre spillene dine og dele dem med andre.

## Lag en Scratchbruker {.check}

- [ ] Gå til nettsiden [scratch.mit.edu](https://scratch.mit.edu/) i en nettleser.

- [ ] Om siden er på engelsk kan du endre språk til norsk (bokmål eller nynorsk) i
  nedtrekksmenyen nederst på siden.

- [ ] Klikk __Bli Scratch-bruker__ øverst til høyre, og fyll ut skjemaet som dukker
  opp.

- [ ] Etter at du har blitt Scratchbruker kan du klikke __Programmering__ øverst til
  venstre for å begynne å programmere.

    Videre gir vi deg en oppskrift på hvordan du kan lage et enkelt spill hvor
    du skal hjelpe pingvinene å finne veien tilbake til akvariet i Bergen.

# Steg 1: En pingvin på tur {.activity}

_Vi begynner med å se på hvordan vi kan lage en figur og få denne til å bevege seg._

## Sjekkliste {.check}

- [ ] Når du starter et nytt Scratch-prosjekt ser du en kattefigur. I dette spillet
  skal vi ikke bruke denne. Vi begynner derfor med å slette kattefiguren:

    Klikk på ![Slett](../bilder/slett.png) øverst i menyen, og klikk deretter på
    kattefiguren for å slette denne.

- [ ] Vi skal nå legge til en pingvinfigur. Klikk på
  ![Velg figur fra biblioteket](../bilder/hent-fra-bibliotek.png) ved siden av
  __Ny figur:__ omtrent midt på skjermen. Skroll nedover skjermen til du finner
  en pingvinfigur (det er flere å velge mellom). Klikk en av dem, og deretter
  __OK__.

- [ ] Du har nå fått en pingvin inn i spillet ditt. La oss programmere den!

    Midt på skjermen ser du mange fargede klosser, for eksempel `gå (10)
    steg`{.b}. Disse er kommandoer vi kan gi til figurene våre. For å skrive et
    program pusler vi sammen flere klosser ved å dra dem over til høyre delen av
    skjermen.

- [ ] Pusle sammen denne koden for pingvinen din:

  ```blocks
  når grønt flagg klikkes
  for alltid
      gå (10) steg
      sprett tilbake ved kanten
  slutt
  ```

    Legg merke til at fargene på klossene samsvarer med kategoriene øverst på
    siden. For eksempel finner du `når grønt flagg klikkes`{.b} i
    `Hendelser`{.blockevents}-kategorien.

## Test prosjektet {.flag}

__Klikk på det grønne flagget øverst midt på skjermen for å prøve spillet ditt.__

- [ ] Pingvinen skal nå begynne å flytte seg frem og tilbake over skjermen.

- [ ] Du merker kanskje at pingvinen snur seg på hodet når den går mot venstre? Det
  er fordi scratchfigurer i utgangspunktet roterer når de skifter retning. Vi
  kan forbedre dette ved å legge til klossen `begrens rotasjon
  [vend sideveis v]`{.b} rett under `når grønt flagg klikkes`{.b}-klossen i
  programmet vårt.

Du kan bruke den røde knappen ved siden av det grønne flagget om du ønsker at
pingvinen skal slutte å bevege seg. Etterhvert som du lager mer kode bør du
klikke på det grønne flagget for å se hva som skjer.

## Lagre prosjektet {.save}

Du har nå laget et lite program! Scratch lagrer alt du gjør automatisk med jevne
mellomrom. Det kan likevel være lurt å lagre selv også innimellom.

- [ ] Over scenen er det et tekstfelt hvor du kan gi navn til prosjektet ditt. Kall
  det for eksempel `Pingviner på tur`.

- [ ] I menyen __Fil__ kan du velge __Lagre nå__ for å lagre prosjektet.

# Steg 2: På kryss og tvers {.activity}

_La oss se hvordan vi kan kontrollere hvordan pingvinen beveger seg._

## Sjekkliste {.check}

- [ ] Se nærmere på koden du har laget. Vi har fortalt pingvinen at den _for alltid_
  skal _gå_ og _sprette tilbake ved kanten_. Ser du hvordan pingvinen gjør
  akkurat som den har blitt fortalt?

    Vi kan gjøre forandringer i koden vår. For eksempel sier tallet `10` i `gå
    (10) steg`{.b}-klossen noe om hvor fort pingvinen skal bevege seg. Prøv å
    forandre dette tallet!

- [ ] Vi kan også endre størrelsen på pingvinen. Endre koden din slik at den nå ser
  slik ut:

  ```blocks
  når grønt flagg klikkes
  sett størrelse til (40) %
  begrens rotasjon [vend sideveis v]
  for alltid
      gå (4) steg
      sprett tilbake ved kanten
  slutt
  ```

- [ ] Til slutt skal vi la pingvinen gå _tilfeldig_ på kryss og tvers på
  skjermen. Legg til flere klosser slik at koden nå ser slik ut:

  ```blocks
  når grønt flagg klikkes
  sett størrelse til (40) %
  begrens rotasjon [vend sideveis v]
  gå til [tilfeldig sted v]
  pek i retning (tilfeldig tall fra (1) til (360))
  for alltid
      gå (4) steg
      sprett tilbake ved kanten
  slutt
  ```

    For å lage `pek i retning (tilfeldig tall fra (1) til (360))`{.b} må du
    først legge til `pek i retning (90 v)`{.b}-klossen og deretter pusle
    `tilfeldig tall fra (1) til (10)`{.b}-klossen inn i denne og forandre `10`
    til `360`.

## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

- [ ] Går pingvinen mer på kryss og tvers?

- [ ] Starter pingvinen forskjellige steder på skjermen om du klikker på det grønne
  flagget flere ganger?

# Steg 3: Bergen {.activity}

_Pingvinen har rømt fra akvariet i Bergen, så da burde den jo springe rundt i Bergens gater._

## Sjekkliste {.check}

- [ ] Vi skal nå legge til en bakgrunn på spillet vårt som viser et kart over
  Bergen. Last ned filen [bergen.png](bergen.png) til datamaskinen din.

    Alternativt kan du [lage ditt eget kart](../kart/kart.html) ved å gå til
    [denne siden](../kart/kart.html).

- [ ] For å legge til en ny bakgrunn klikker du på
  ![Last opp bakgrunn fra fil](../bilder/hent-fra-fil.png) under __Ny bakgrunn__
  helt til venstre på siden. Velg deretter filen du nettopp lastet ned.

- [ ] La oss nå markere Akvariet i Bergen på kartet. Hent en ny figur ved å klikke
  på ![Velg figur fra biblioteket](../bilder/hent-fra-bibliotek.png). Velg
  figuren `Button5`, og plasser denne ytterst på Nordnes for å vise hvor
  Akvariet er.

    ![](nordnes.png)

- [ ] Vi vil nå endre navn på akvariefiguren slik at vi enklere husker hva den
  er. Klikk på `i`{.blockmotion} øverst til venstre på akvariefiguren i
  figurlisten. Endre navnet fra `Button5` til `Akvariet`.

# Steg 4: Hjelp pingvinen hjem {.activity}

_Vi skal prøve å kontrollere pingvinen slik at vi kan hjelpe den tilbake til
Akvariet._

## Sjekkliste {.check}

I dette spillet skal vi kontrollere pingvinen ved å klikke på kartet. Pingvinen
skal da snu seg vekk fra der vi holder musepekeren før den går videre.

- [ ] Klikk på __Scene__ nede til venstre på skjermen. Dette gir oss muligheten til
  å skrive kode som gjelder for bakgrunnen og ikke for pingvinen.

- [ ] Lag den følgende nye koden på Scenen:

  ```blocks
  når scenen klikkes :: hat events
  send melding [snu retning v]
  trommeslag (1 v) som varer (0.25) takter
  ```

    En slik _melding_ er en beskjed programmet ditt sender til alle figurene. Du
    vil ikke se disse meldingene, men figurene dine kan reagere på dem. Her vil
    vi fortelle pingvinen at den skal snu når vi klikker på kartet (scenen).

- [ ] Klikk på pingvinen. Vi skal nå skrive et nytt skript. Lag denne koden ved
  siden av koden du skrev tidligere:

  ```blocks
  når jeg mottar [snu retning v]
  pek mot [musepeker v]
  vend venstre (180) grader
  ```

## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

- [ ] Snur pingvinen seg vekk fra musepekeren om du klikker på kartet?

# Steg 5: Pingvinen kommer hjem! {.activity}

_Vi skal til slutt se hvordan pingvinen kan oppdage at den har kommet hjem!_

## Sjekkliste {.check}

- [ ] Klossen `berører [ v]`{.b} kan brukes for å oppdage om to figurer berører
  hverandre. Legg til en `hvis`{.blockcontrol}-test i koden som flytter
  pingvinen:

  ```blocks
  når grønt flagg klikkes
  sett størrelse til (40) %
  begrens rotasjon [vend sideveis v]
  gå til [tilfeldig sted v]
  pek i retning (tilfeldig tall fra (1) til (360))
  for alltid
      gå (4) steg
      sprett tilbake ved kanten
      hvis <berører [Akvariet v] ?>
          si [Hurra!] i (7) sekunder
          gå til [tilfeldig sted v]
      slutt
  slutt
  ```

## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

- [ ] Hva skjer når pingvinen kommer til Akvariet?

- [ ] Etter at pingvinen har vært hjemme i 7 sekunder tar den seg en ny tur. Dukker
  den opp på et nytt tilfeldig sted?

## Prøv selv {.challenge}

Vi har nå laget et lite spill sammen, men prøv gjerne å utvikle det videre. Her
er noen ideer:

- [ ] Legg til flere pingviner! Dette er ganske enkelt. Klikk
  ![Lag en kopi](../bilder/lag-en-kopi.png) og deretter på pingvinfiguren for å
  lage en kopi av den.

- [ ] Kan du lage en test for om alle pingvinene har kommet hjem? Denne lager du
  enklest på akvariefiguren. Du bør bruke en `for alltid`{.blockcontrol}-løkke,
  en `hvis`{.blockcontrol}-test samt `< > og < >`{.b}- og `berører
  [ v]`{.b}-klosser.

- [ ] Kanskje vi kan telle poeng hver gang en pingvin finner veien til Akvariet? Til
  dette trenger du noe som heter variabler. Disse finner du under
  `Data`{.blockdata}. Prøv selv om du får til noe!
