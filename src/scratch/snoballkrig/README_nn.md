---
title: Lærarrettleiing - Snøballkrig
level: 4
language: nn
author: Stein Olav Romslo, Vegard Tuset
---


# Om oppgåva {.activity}

I denne oppgåva skal elevane lage eit spel der dei kontrollerer ein
snøballkastar som prøver å jage bort slemme gutar ved å kaste snøball på dei.

![Illustrasjon av eit ferdig Snøballkrig-spel](snoballkrig.png)

## Oppgåva passar til: {.check}

__Fag__: Kunst og handverk, matematikk, programmering.

__Anbefalte trinn__: 3.-10. trinn.

__Tema__: Digitalt bildehandsamingsprogram, koordinatsystem, variablar.

__Tidsbruk__: Dobbelttime eller meir.

## Kompetansemål {.challenge}

- [ ] __Kunst og handverk, 10. trinn__: visualisere form ved hjelp av
      frihandteikningar, arbeidsteikningar, modeller og digitale verktøy

- [ ] __Matematikk, 3. trinn__: eksperimentere med og forklare plasseringar i
      koordinatsystemet

- [ ] __Matematikk fordypning, 10. trinn__: diskutere, planlegge, lage og
      vurdere spilldesign og eigne spel

- [ ] __Programmering, 10. trinn__: bruke grunnleggande prinsipp i
      programmering, slik som variablar, løkker, vilkår og funksjonar, og
      reflektere over bruken av desse

- [ ] __Programmering, 10. trinn__: planlegge og skape eit digitalt produkt og
      vurdere dette med tanke på brukervennlighet

## Forslag til læringsmål {.challenge}

- [ ] Elevane kan lage bakgrunn og element i eit digitalt
  bildehandsamingsprogram, og bruke dei i eit spel.

- [ ] Elevane kan plassere element på bestemte posisjonar i eit koordinatsystem.

- [ ] Elevane kan få element til å bevege seg i ei bestemt retning i eit
  koordinatsystem.

- [ ] Elevane kan lage relevante kommentarar for å dokumentere koden sin.

- [ ] Elevane kan bruke variablar til å telje poeng.

- [ ] Elevane kan bruke kode til å lage eit spel med brukarinteraksjon.

## Forslag til vurderingskriterium {.challenge}

- [ ] Eleven syner middels måloppnåing ved å fullføre oppgåva.

- [ ] Eleven syner høg måloppnåing ved å vidareutvikle eigen kode basert på
  oppgåva, til dømes ved å gjere ein eller fleire av variasjonane under.

## Føresetnader og utstyr {.challenge}

- [ ] __Føresetnader__: Elevane må ha god kunnskap i Scratch. Dei bør ha gjort
  fleire prosjekt på erfaren-nivået før dei startar med denne oppgåva.

- [ ] __Utstyr__: Datamaskiner med Scratch installert. Eventuelt kan elevane
  bruke Scratch i nettlesaren viss dei har ein brukar (eller registrerer seg) på
  [scratch.mit.edu/](https://scratch.mit.edu/). Elevane kan gjerne jobbe to og
  to saman.

## Framgangsmåte

Her finn du tips, erfaringar og utfordringar til dei ulike stega i oppgåva.
[Klikk her for å sjå
oppgåveteksten.](../snoballkrig/snoballkrig_nn.html){target=_blank}

_Det kan vere ei utfordring for mange elevar å lage koden. Under følgjer eit døme på korleis koden kan sjå ut under dei ulike elementa._


# Scene {.activity}

```blocks
  når @greenFlag vert trykt på
  byt bakgrunn til [Meny v]

  når [s v] vert trykt
  send meldinga [start v]

  når eg får meldinga [start v]
  set [Poeng v] til [0]
  byt bakgrunn til [Spill v]
  gjenta for alltid
    set [Nivå v] til ((1) + ([golv v] av ([kvadratrot v] av ((Poeng) / (3)))))
  slutt

  når eg får meldinga [slutt v]
  stopp [andre skript på scena v]
  byt bakgrunn til [Slutt v]
```


# Helten {.activity}

```blocks
  når @greenFlag vert trykt på
  gøym
  set storleik til (75) %
  bruk roteringstypen [vend sidevegs v]
  set [hastigheit v] til [5]

  når eg får meldinga [start v]
  gå til x: (0) y: (-75)
  vis
  gjenta for alltid
    viss <tasten [pil høgre v] er trykt?>
      peik i retning (90 v)
      neste drakt
      gå (hastigheit) steg
    slutt
    viss <tasten [pil venstre v] er trykt?>
      peik i retning (-90 v)
      neste drakt
      gå (hastigheit) steg
    slutt
    viss <tasten [mellomrom v] er trykt?>
      vent til <ikkje <tasten [mellomrom v] er trykt?>>
      send meldinga [kast v]
    slutt
  slutt

  når eg får meldinga [slutt v]
  gøym
  stopp [andre skript i figuren v]
```


# Snøball {.activity}

```blocks
  når @greenFlag vert trykt på
  gøym
  set storleik til (40) %

  når eg får meldinga [kast v]
  lag klon av [meg v]

  når eg startar som klon
  gå til [Helten v]
  peik i retning ([retning v] av [Helten v])
  endre y med (15)
  gå (30) steg
  vis
  gjenta til <<rører [Skumling v]?> eller <rører [kant v]?>>
    gå (hastigheit) steg
  slutt
  viss <rører [Skumling v]?>
    vent (0.02) sekund
  slutt
  slett denne klonen

  når eg får meldinga [slutt v]
  slett denne klonen
```


# Skumling {.activity}

```blocks
  når @greenFlag vert trykt på
  gøym
  gå til x: (0) y: (-70)
  bruk roteringstypen [vend sidevegs v]
  set storleik til (30) %
  set [hastigheit v] til [3]

  når eg får meldinga [start v]
  gjenta for alltid
    viss <(tilfeldig tal frå (0) til (1)) = [0]>
      peik i retning (90 v)
      set x til (-250)
    ellers
      peik i retning (-90 v)
      set x til (250)
    slutt
    lag klon av [meg v]
    vent (tilfeldig tal frå (2) til (4)) sekund
  slutt

  når eg startar som klon
  set [Slem v] til (tilfeldig tal frå (1) til (Nivå))
  set [Liv v] til (Slem)
  endre [hastigheit v] med (Slem)
  endre [farge v]-effekt med ((10) * (Slem))
  endre storleik med ((5) * (Slem))
  vis
  gjenta for alltid
    gå (hastigheit) steg
    vent (0.1) sekund
  slutt

  når eg startar som klon
  gjenta for alltid
    viss <rører [Helten v]?>
      send meldinga [slutt v]
    slutt
    viss <rører [Snøball v]?>
      endre [Liv v] med (-1)
      viss <(Liv) = [0]>
        endre [Poeng v] med (Slem)
        slett denne klonen
      slutt
    slutt
  slutt

  når eg får meldinga [slutt v]
  slett denne klonen
```

## Variasjonar {.challenge}

- [ ] _Me har diverre ikkje nokre variasjonar knytta til denne oppgåva endå._

## Eksterne ressursar {.challenge}

- [ ] Førebels ingen eksterne ressursar...
