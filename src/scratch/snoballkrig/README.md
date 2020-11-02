---
title: Lærerveiledning - Snøballkrig
author: Stein Olav Romslo, Vegard Tuset
level: 4
language: nb
---


# Om oppgaven {.activity}

I dette spillet vil vi kontrollere snøballkaster som prøver å jage bort slemme
gutter ved å kaste snøball etter dem.

![Illustrasjon av et ferdig snøballkrig spill](snoballkrig.png)

## Oppgaven passer til: {.check}

__Fag__: Kunst og håndtverk, matematikk, programmering.

__Anbefalte trinn__: 5.-10. trinn.

__Tema__: Digitalt bildebehandlingsprogram, koordinatsystem, variabler.

__Tidsbruk__: Dobbelttime eller mer.

## Kompetansemål {.challenge}

- [ ] __Kunst og håndtverk, 10. trinn__: visualisere form ved hjelp av
      frihåndstegninger, arbeidstegninger, modeller og digitale verktøy

- [ ] __Matematikk, 3. trinn__: eksperimentere med og forklare plasseringer i
      koordinatsystemet

- [ ] __Matematikk fordypning, 10. trinn__: diskutere, planlegge, lage og
      vurdere spilldesign og egne spill

- [ ] __Programmering, 10. trinn__: bruke grunnleggende prinsipper i
      programmering, slik som variabler, løkker, vilkår og funksjoner, og
      reflektere over bruken av disse

- [ ] __Programmering, 10. trinn__: planlegge og skape et digitalt produkt og
      vurdere dette med tanke på brukervennlighet

## Forslag til læringsmål {.challenge}

- [ ] Elevene kan lage bakgrunn og elementer i digitalt bildebehandlingsprogram,
      og bruke dem i et spill.

- [ ] Elevene kan plassere elementer på bestemte posisjoner i et
      koordinatsystem.

- [ ] Elevene kan få elementer til å bevege seg i en bestemt retning i et
      koordinatsystem.

- [ ] Elevene kan lage hensiktsmessige kommentarer for å dokumentere koden sin.

- [ ] Elevene kan bruke variabler til å telle poeng.

- [ ] Elevene kan bruke kode til å lage et spill med brukerinteraksjon.

## Forslag til vurderingskriterier {.challenge}

- [ ] Eleven viser middels måloppnåelse ved å fullføre oppgaven.

- [ ] Eleven viser høy måloppnåelse ved å videreutvikle egen kode basert på
      oppgaven.

## Forutsetninger og utstyr {.challenge}

- [ ] __Forutsetninger__: Elevene må ha god kunnskap i Scratch. De bør ha gjort
      flere prosjekter på erfaren-nivået før de begynner med denne oppgaven.

- [ ] __Utstyr__: Datamaskiner med Scratch installert. Eventuelt kan elevene
      bruke Scratch i nettleseren dersom de har en bruker (eller registrerer
      seg) på [scratch.mit.edu/](http://scratch.mit.edu/){target=_blank}.

## Fremgangsmåte

[Klikk her for å se oppgaveteksten.](../snoballkrig/snoballkrig.html){target=_blank}

_Det kan være en utfordring for mange elever å lage koden. Under følger et
eksempel på hvordan koden kan se ut under de forskjellige elementene._


# Scene {.activity}

```blocks
  når grønt flagg klikkes
  bytt bakgrunn til [Meny v]

  når [s v] trykkes
  send melding [start v]

  når jeg mottar [start v]
  sett [Poeng v] til [0]
  bytt bakgrunn til [Spill v]
  gjenta for alltid
    sett [Nivå v] til ((1) + ([gulv v] av ([kvadratrot v] av ((Poeng) / (3)))))
  slutt

  når jeg mottar [slutt v]
  stopp [other scripts in stage v]
  bytt bakgrunn til [Slutt v]
```


# Helten {.activity}

```blocks
  når grønt flagg klikkes
  skjul
  sett størrelse til (75) %
  begrens rotasjon [vend sideveis v]
  sett [hastighet v] til [5]

  når jeg mottar [start v]
  gå til x: (0) y: (-75)
  vis
  gjenta for alltid
    hvis <tast [pil høyre v] trykket?>
      pek i retning (90 v)
      neste drakt
      gå (hastighet) steg
    slutt
    hvis <tast [pil venstre v] trykket?>
      pek i retning (-90 v)
      neste drakt
      gå (hastighet) steg
    slutt
    hvis <tast [mellomrom v] trykket?>
      vent til <ikke <tast [mellomrom v] trykket?>>
      send melding [kast v]
    slutt
  slutt

  når jeg mottar [slutt v]
  skjul
  stopp [andre skript i figuren v]
```


# Snøball {.activity}

```blocks
  når grønt flagg klikkes
  skjul
  sett størrelse til (40) %

  når jeg mottar [kast v]
  lag klon av [meg v]

  når jeg starter som klon
  gå til [Helten v]
  pek i retning ([retning v] av [Helten v])
  endre y med (15)
  gå (30) steg
  vis
  gjenta til <<berører [Skumling v]?> eller <berører [kant v]?>>
    gå (hastighet) steg
  slutt
  hvis <berører [Skumling v]?>
    vent (0.02) sekunder
  slutt
  slett denne klonen

  når jeg mottar [slutt v]
  slett denne klonen
```


# Skumling {.activity}

```blocks
  når grønt flagg klikkes
  skjul
  gå til x: (0) y: (-70)
  begrens rotasjon [vend sideveis v]
  sett størrelse til (30) %
  sett [hastighet v] til [3]

  når jeg mottar [start v]
  gjenta for alltid
    hvis <(tilfeldig tall fra (0) til (1)) = [0]>
      pek i retning (90 v)
      sett x til (-250)
    ellers
      pek i retning (-90 v)
      sett x til (250)
    slutt
    lag klon av [meg v]
    vent (tilfeldig tall fra (2) til (4)) sekunder
  slutt

  når jeg starter som klon
  sett [Slem v] til (tilfeldig tall fra (1) til (Nivå))
  sett [Liv v] til (Slem)
  endre [hastighet v] med (Slem)
  endre [farge v] effekt med ((10) * (Slem))
  endre størrelse med ((5) * (Slem))
  vis
  gjenta for alltid
    gå (hastighet) steg
    vent (0.1) sekunder
  slutt

  når jeg starter som klon
  gjenta for alltid
    hvis <berører [Helten v]?>
      send melding [slutt v]
    slutt
    hvis <berører [Snøball v]?>
      endre [Liv v] med (-1)
      hvis <(Liv) = [0]>
        endre [Poeng v] med (Slem)
        slett denne klonen
      slutt
    slutt
  slutt

  når jeg mottar [slutt v]
  slett denne klonen
```

## Variasjoner {.challenge}

- [ ] _Vi har dessverre ikke noen variasjoner tilknyttet denne oppgaven enda._

## Eksterne ressurser {.challenge}

- [ ] Foreløpig ingen eksterne ressurser...
