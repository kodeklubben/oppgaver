---
title: Lærarrettleiing - Labyrint
level: 1
language: nn
author: Stein Olav Romslo, Vegard Tuset
---


# Om oppgåva {.activity}

I denne oppgåva skal elevane lage eit enkelt spel der ein kontrollerer ein liten
utforskar som leitar etter skatten gøymt inne i ein labyrint.

![Bilete av labyrinten, froskekongen, utforskaren og skatten](labyrint.png)

## Oppgåva passar til: {.check}

__Fag__: Programmering, matematikk.

__Anbefalte trinn__: 3.-10. trinn.

__Tema__: Løkker, testar, variablar, tilfeldigheit.

__Tidsbruk__: Dobbelttime eller meir.

## Kompetansemål {.challenge}

- [ ] __Matematikk, 5. årstrinn__: lage og programmere algoritmar med bruk av
      variablar, vilkår og løkker

- [ ] __Matematikk, 6. årstrinn__: bruke variablar, løkker, vilkår og
      funksjonar i programmering til å utforska geometriske figurar og mønster

- [ ] __Programmering, valgfag__: bruke grunnleggande prinsipp i programmering
      , slik som variablar, løkker, vilkår og funksjonar, og reflektere over
      bruken av desse

- [ ] __Programmering, valgfag__: analysere problem, gjere dei om til
      delproblem og gjere reie for korleis nokon av delproblema kan løysast med programmering

## Forslag til læringsmål {.challenge}

- [ ] Elevane kan forklare korleis løkker, testar og variablar fungerer, og
  kvifor det er verdifullt å bruke desse i denne oppgåva.

- [ ] Eleven kan forklare korleis brukaren kan styre figuren med piltastane, og
  korleis figuren interagerer med labyrinten.

- [ ] Eleven kan forklare korleis tilfeldigheitsgeneratoren fungerer.

## Forslag til vurderingskriterium {.challenge}

- [ ] Eleven syner middels måloppnåing ved å fullføre oppgåva slik det er
  beskrive.

- [ ] Eleven syner høg måloppnåing ved å leggje til fleire moment, og utvikle
  ein meir utfordrande labyrint.

- [ ] Dette er ei oppgåve der elevane fint kan pråve kvarandre sine labyrintar
  og vurdere kvarandre.

## Føresetnader og utstyr {.challenge}

- [ ] __Føresetnader__: Ingen, fin introduksjon til Scratch.

- [ ] __Utstyr__: Datamaskiner med Scratch installert. Eventuelt kan elevane
  bruke Scratch i nettlesaren viss dei har ein brukar (eller registrerer seg) på
  [scratch.mit.edu/](https://scratch.mit.edu/). Elevane kan gjerne jobbe to og
  to saman.

## Framgangsmåte

Her finn du tips, erfaringar og utfordringar til dei ulike stega i oppgåva.
[Klikk her for å sjå
oppgåveteksten.](../labyrint/labyrint_nn.html){target=_blank}


# Steg 3: Utforskaren kan ikkje gå gjennom veggen {.activity}

- [ ] Eit vanleg problem her er at __utforskaren kan gå rett gjennom veggen__.
  Typisk vil det vere fordi ein ikkje har rett farge i XXX-klossen. Eventuelt at
  ein har brukt fleire fargar på veggane i labyrinten. Det er viktig at alle
  veggane er teikna med same farge.

  Ein kan òg oppleve at utforskaren går rett gjennom veggen viss
  `hastigheit`{.blockvariable} er for høg. Det er fordi utforskaren *hoppar*
  `hastigheit`{.blockvariable} steg kvar gong ein trykkar ein piltast, og då kan
  den hoppe over ein vegg.

- [ ] Eit anna problem er at __utforskaren hoppar gjennom veggar når den snur__.
  Alle figurane har eit definert senterpunkt som dei roterer rundt (sjå steg 2 i
  prosjektet [Soloball](../soloball/soloball_nn.html) for eit godt døme på
  korleis dette virkar). Viss dette senterpunktet ikkje er midt på
  `Utforskar`-figuren vil det sjå ut som den hoppar rundt når den snur. For å
  setje senterpunktet riktig kan de trykkje på `Drakter`-fana og så på ![Bilete
  av senterpunkt-knappen](../bilder/velg_senterpunkt.png). Korset viser kor
  senterpunktet er, og det kan bli dratt slik at det er midt på figuren.

- [ ] Det kan skje at __det er vanskeleg å bevege seg i labyrinten__. Viss
  gangane er for smale eller veggane for skrå blir det vanskeleg for utforskaren
  og froskekongen å bevege seg.


# Steg 5: Froskekongen voktar i gangane {.activity}

- [ ] Eit vanleg problem her kan vere at __utforskaren eller froskekongen set
  seg fast i veggen__. I denne oppgåva har me prøvd å halde koden så enkel som
  mogleg. Spesielt er koden som passar på at figurane ikkje gør gjennom veggane
  litt *for enkel*. Nokre enkle tips for å motverke problemet er presentert i
  tipsboksen nedst i steg 5 i oppgåva.


# Stopp alle {.activity}

Me brukar klossen `stopp alle`{.b} for å stoppe alle skripta i programmet når
froskekongen tek utforskaren. Det stoppar alle skripta som starta då me trykka
på det grøne flagget, men det hindrar ikkje nye skript å starte. Difor kan
framleis utforskaren bli flytta rundt med piltastane etterpå.

Sidan oppgåva er eit introduksjonsprosjekt er det ikkje gjort noko med dette.
For elevar som har lyst å prøve seg på ei løysing kan du foreslå det følgjande:

- [ ] Lag ein `game_over`-variabel som er sett til `false` eller `0` når spelet
  pågår, som blir sjekka kvar gong spelaren trykkjer ein piltast, før
  utforskaren flyttar seg. Set variabelen til `true` eller `1` når spelet er
  over.

- [ ] Ei meir vanleg (og betre) løysing er å bruke ei `for alltid`-løkke med
  `viss ... er trykt?`-klossar. Desse blir stoppa av `stopp alle`-klossen.

## Variasjonar {.challenge}

- [ ] Dette er eit introduksjonsprosjekt, så elevane blir ført ganske detaljert
  gjennom korleis spelet skal programmerast. Det er framleis rom for ein del
  kreativitet. Elevane kan gjerne bli oppfordra til å

  - [ ] __velje sine eigne figurar__. Dei kan fritt velje figurane som blir
    brukt for `Utforskar`, `Skatt` og `Froskekonge` utan at det har nokon effekt
    på programmeringa.

  - [ ] __teikne sin heilt eigne labyrint__. I oppgåva finn de eit dåme (eller
    to om ein ser på teikninga fyrst i oppgåva) på ein labyrint, men elevane kan
    gjerne teikne ein annan. Pass på at du ber elevane tenke på at det skal vere
    enkelt for utforskaren og froskekongen å bevege seg rundt, så labyrinten bør
    ha rette veggar og breie nok gonger.

  - [ ] __eksperimentere med hastigheit__. I steg 1 i oppgåva blir det vist
    korleis ein kan endre kor raskt ein figur flyttar seg ved å bruke ein
    `hastigheit`-variabel. La elevane eksperimentere med denne for utforskaren
    og froskekongen, og spør dei korleis det forandrar vanskegraden i spelet.

- [ ] Viss elevane allereie er komfortable med Scratch kan du nytte anledninga
  til å prate om korleis teikneverktøyet i Scratch fungerer og gi dei nokre tips
  til kolreis dei kan bruke det effektivt.

- [ ] For dei meir avanserte elevane kan du vise fram kode som gjer ein betre
  sjekk av kollisjon med veggen.

## Eksterne ressursar {.challenge}

- [ ] Førebels ingen eksterne ressursar...
