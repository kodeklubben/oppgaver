---
title: 'Pingviner på tur'
level: 1
author: 'Geir Arne Hjelle'
translator: 'Stein Olav Romslo'
language: nn
---


# Introduksjon {.intro}

I denne oppgåva skal me lage eit enkelt spel der pingvinane har rømt frå
akvariet i Bergen. Det er din (spelaren) sin jobb å hjelpe dei heim att.

![Bilete av pingvinar på rømmen](pingviner_pa_tur.png)


# Velkommen til Scratch {.activity}

_Viss du allereie kjenner Scratch og har ein Scratchbrukar kan du gå vidare til
[steg 1](#steg-1-ein-pingvin-pa-tur)._

[Scratch](https://scratch.mit.edu/) er eit programmeringsspråk som er laga
spesielt for å vere enkelt å kome i gang med og raskt kunne lage sine eigne spel
og animasjonar. Scratch køyrer i nettlesaren og er heilt gratis å bruke. Før du
startar å programmere er det lurt å lage ein brukar, sidan det gjer det enklare
å lagre det du lagar og dele det med andre.

## Lag ein Scratchbrukar {.check}

- [ ] Gå til nettsida [scratch.mit.edu](https://scratch.mit.edu/) i ein
  nettlesar.

- [ ] Viss sida er på engelsk kan du endre språk til norsk (både nynorsk og
  bokmål er tilgjengeleg) i nedtrekksmenyen nedst på sida.

- [ ] Klikk __Bli Scratch-brukar__ øvst til høgre, og fyll ut skjemaet som
  dukkar opp.

- [ ] Etter at du har blitt Scratchbrukar kan du klikke __Programmering__ øvst
  til venstre for å kome i gang med programmeringa.

    Vidare skal me gå gjennom ei oppskrift på korleis du kan lage eit enkelt
    spel der målet er å hjelpe pingvinane å finne vegen heim til akvariet i
    Bergen.


# Steg 1: Ein pingvin på tur {.activity}

_Me startar med å sjå på korleis me kan lage ein figur og få denne til å bevege
seg._

## Sjekkliste {.check}

- [ ] Når du startar eit nytt Scratch-prosjekt ser du ein kattefigur. I dette
  spelet skal me ikkje bruke katten. Difor startar me med å slette kattefiguren:

    Klikk på ![Slett](../bilder/slett.png) øvst i menyen, og så klikkar du på
    kattefiguren for å slette den.

- [ ] I staden skal me leggje til ein pingvinfigur. Klikk på  ![Vel figur frå
  biblioteket](../bilder/hent-fra-bibliotek.png) ved sidan av  __Ny figur:__
  omlag midt på skjermen. Rull nedover skjermen til du finn ein pingvinfigur
  (det er fleire å velje mellom). Klikk på ein av dei, og så __OK__.

- [ ] No har du ein pingvin i spelet ditt! La oss programmere den!

    Midt på skjermen ser du mange farga klossar, til dømes `gå (10) steg`{.b}.
    Desse er kommandoar me kan gi til figurane våre. For å skrive eit program
    puslar me samen fleire klossar ved å dra dei over til høgre del av skjermen.

- [ ] Pusle saman denne koden for pingvinen din:

  ```blocks
  når @greenFlag vert trykt på
  gjenta for alltid
      gå (10) steg
      viss ved kant, sprett
  slutt
  ```

    Legg merke til at farga på klossane samsvarar med kategoriane øvst på sida.
    Til dømes finn du `når @greenFlag vert trykt på`{.b} i
    `Hendingar`{.blockevents}-kategorien.

## Test prosjektet {.flag}

__Klikk på det grøne flagget øvst midt på skjermen for å prøve spelet ditt.__

- [ ] No skal pingvinen starte å flytte seg fram og attende over skjermen.

- [ ] Legg du merke til at pingvinen snur seg på hovudet når den går mot
  venstre? Det er fordi scratchfigurar i utgangspunktet roterer når dei skiftar
  retning. Dette kan du justere ved å leggje til klossen `bruk roteringstypen
  [vend sidevegs v]`{.b} rett under `når @greenFlag vert trykt på`{.b}-klossen i
  programmet vårt.

Du kan bruke den raude knappen ved sidan av det grøne flagget for å stoppe
pingvinen att. Etter kvart som du lagar meir kode bør du trykkje på det grøne
flagget for å sjå kva som skjer.

## Lagre prosjektet {.save}

No har du laga eit lite program! Scratch lagrar alt du gjer automatisk med jamne
mellomrom. Likevel er det lurt å leggje til seg vanen om å lagre sjølv
innimellom.

- [ ] Over scena er det eit tekstfelt der du kan gi namn til prosjektet ditt.
  Du kan til dømes kalle det `Pingvinar på tur`.

- [ ] I menyen __Fil__ kan du velje __Lagre no__ for å lagre prosjektet.


# Steg 2: På kryss og tvers {.activity}

_No vil me få pingvinen til å bevege seg på kryss og tvers._

## Sjekkliste {.check}

- [ ] Sjå meir på koden du har laga. Me har sagt til pingvinen at den _for
  alltid_ skal _gå_ og _sprette tilbake ved kanten_. Ser du korleis pingvinen
  gjer akkurat det me har sagt til den at den skal gjere?

    Me kan gjere endringar i koden vår. Til dømes seier talet `10` i `gå (10)
    steg`{.b}-klossen noko om kor fort pingvinen skal bevege seg. Prøv å endre
    talet!

- [ ] Me kan endre storleiken på pingvinen. Endre koden din slik at den ser slik
  ut:

  ```blocks
  når @greenFlag vert trykt på
  set storleik til (40) %
  avgrens rotering til [venstre-høgre v]
  gjenta for alltid
      gå (4) steg
      viss ved kant, sprett
  slutt
  ```

- [ ] Til slutt skal me la pingvinen gå _tilfeldig_ på kryss og tvers på
  skjermen. Legg til fleire klossar slik at koden ser slik ut:

  ```blocks
  når @greenFlag vert trykt på
  set storleik til (40) %
  avgrens rotering til [venstre-høgre v]
  gå til [tilfeldig stad v]
  peik i retning (tilfeldig tal frå (1) til (360))
  gjenta for alltid
      gå (4) steg
      viss ved kant, sprett
  slutt
  ```

    For å lage `peik i retning (tilfeldig tal frå (1) til (360))`{.b} må du
    fyrst leggje til `peik i retning (90 v)`{.b}-klossen og så pusle `tilfeldig
    tal frå (1) til (10)`{.b}-klossen inn i den og forandre `10` til `360`.

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Går pingvinen meir på kryss og tvers?

- [ ] Startar pingvinen ulike stader på skjermen viss du klikkar på det grøne
  flagget fleire gonger?


# Steg 3: Bergen {.activity}

_Pingvinen har rømt frå akvariet i Bergen, så den burde jo springe rundt i
gatene i Bergen._

## Sjekkliste {.check}

- [ ] No skal me leggje til ein bakgrunn på spelet vårt som viser eit kart over
  Bergen. Last ned fila [bergen.png](bergen.png) til datamaskina di.

    Alternativt kan du lage ditt eige kart ved å gå til
    [denne sida](../kart/kart.html).

- [ ] For å leggje til ein ny bakgrunn klikkar du på ![Last opp bakgrunn frå
  fil](../bilder/hent-fra-fil.png) under __Ny bakgrunn__ heilt til venstre på
  sida. Så vel du fila du akkurat lasta ned.

- [ ] No skal me markere Akvariet i Bergen på kartet. Hent ein ny figur ved å
  klikke på ![Vel figur frå biblioteket](../bilder/hent-fra-bibliotek.png). Vel
  figuren `Button5`, og plasser den ytst på Nordnes for å vise kor akvariet er.

    ![Bilete av Nordnes i Bergen med kryss på akvariet](nordnes.png)

- [ ] No vil me endre namn på akvariefiguren slik at me enklare kan hugse kva
  den er. Klikk på `i`{.blockmotion} øvst til venstre på akvariefiguren i
  figurlista. Endre namnet frå `Button5` til `Akvariet`.


# Steg 4: Hjelp pingvinen heim {.activity}

_No skal me prøve å kontrollere pingvinen slik at me kan hjelpe den heim til
akvariet._

## Sjekkliste {.check}

I dette spelet kontrollerer me pingvinen ved å klikke på kartet. Pingvinen skal
snu seg vekk frå der me heldt musepeikaren før den går vidare.

- [ ] Klikk på __Scene__ nede til høyre på skjermen. Då får me moglegheit til
  å skrive kode som gjeld for bakgrunnen, ikkje for pingvinen.

- [ ] Lag den følgjande nye koden på scena:

  ```blocks
  når scena vert trykt på :: hat events
  send meldinga[snu retning v]
  trommeslag (1 v) som varer (0.25) takter
  ```

    Ei slik _melding_ er ein beskjed programmet ditt sender til alle figurane.
    Du får ikkje sjå meldingane, men figurane dine kan reagere på dei. Her vil
    me at pingvinen skal snu når den får melding om at me har klikka på kartet
    (scena).

- [ ] Klikk på pingvinen. No skal me skrive eit nytt skript. Lag denne koden ved
  sidan av koden du skreiv tidlegare:

  ```blocks
  når eg får meldinga [snu retning v]
  peik mot [musepeikar v]
  snu @turnLeft (180) gradar
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Snur pingvinen seg vekk frå musepeikaren viss du klikkar på kartet?


# Steg 5: Pingvinen kjem heim! {.activity}

_Til slutt skal me få pingvinen til å oppdage at den har kome heim!_

## Sjekkliste {.check}

- [ ] Me kan bruke klossen `rører [ v]`{.b} for å oppdage om to figurar er
  borti kvarandre. Legg til ein `viss`{.blockcontrol}-test i koden som flyttar
  pingvinen:

  ```blocks
  når @greenFlag vert trykt på
  set storleik til (40) %
  avgrens rotering til [venstre-høgre v]
  gå til [tilfeldig stad v]
  peik i retning (tilfeldig tal frå (1) til (360))
  gjenta for alltid
      gå (4) steg
      viss ved kant, sprett
      viss <rører [Akvariet v] ?>
          sei [Hurra!] i (7) sekund
          gå til [tilfeldig stad v]
      slutt
  slutt
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Kva skjer når pingvinen kjem til akvariet?

- [ ] Etter at pingvinen har vore heime i 7 sekund tek den seg ein ny tur.
  Dukkar den opp på ein ny tilfeldig stad?

## Prøv sjølv {.challenge}

No har me laga eit lite spel saman, men du kan gjerne utvikle det vidare. Her er
nokre idear:

- [ ] Legg til fleire pingvinar! Dette er ganske enkelt. Klikk ![Lag ein
  kopi](../bilder/lag-en-kopi.png) og så på pingvinfiguren for å lage ein kopi
  av den.

- [ ] Kan du lage ein test for om _alle_ pingvinane har kome heim? Den er
  enklast å lage på akvariefiguren. Du bør bruke ei `gjenta for
  alltid`{.blockcontrol}-løkke, ein `viss`{.blockcontrol}-test samt
  `< > og < >`{.b}- og `rører [ v]`{.b}-klossar.

- [ ] Kanskje me kan telje poeng kvar gong ein pingvin finn vegen til akvariet?
  Til det treng du noko som heiter variablar. Desse finn du under
  `Data`{.blockdata}. Prøv sjølv om du får til noko!
