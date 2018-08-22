---
title: Lærarrettleiing - Snake
level: 4
language: nn
author: Stein Olav Romslo
---


# Om oppgåva {.activity}

I denne oppgåva skal elevane lage ein versjon av spelet Snake. Ein eller annan
variant av dette spelet har eksistert på nesten alle personlege datamaskiner
heilt sidan slutten av 1970-talet. Spelet vart ekstra populært då det dukka opp
på Nokia sine mobiltelefonar i 1997, og har seinare blitt innlemma i New York
Museum of Modern Art si samling.

Spelet går ut på å styre ein slange rundt på skjermen, og slangen må unngå å
krasje i kanten av skjermen eller seg sjølv. Slangen veks ved å ete eple som
dukkar opp tilfeldige stader på skjermen. Spelet kan vidareutviklast på mange
måtar, anten ved å lage ekstra hindringar på skjermen, ulike typar bonuseple,
eller til dømes ved at to slangar konkurrerer om å ete epla og om å stenge
kvarandre inne.

![Illustrasjon av eit ferdig Snake-spel](snake.png)

## Oppgåva passar til: {.check}

__Fag__: Kunst og handverk, matematikk, programmering.

__Anbefalte trinn__: 3.-10. trinn.

__Tema__: Grunnleggjande geometriske former, koordinatsystem, variablar.

__Tidsbruk__: Dobbelttime eller meir.

## Kompetansemål {.challenge}

- [ ] __Kunst og handverk, 4. trinn__: bruke enkle funksjonar i digitale
  bildehandsamingsprogram

- [ ] __Kunst og handverk, 4. trinn__: eksperimentere med enkle geometriske
  former i konstruksjon og som dekorative formelement

- [ ] __Matematikk, 4. trinn__: lese av, plassere og beskrive posisjonar i
  rutenett, på kart og i koordinatsystem, både med og utan digitale verktøy

- [ ] __Matematikk, 7. trinn__: beskrive plassering og flytting i rutenett, på
  kart og i koordinatsystem, med og utan digitale hjelpemiddel, og bruke
  koordinatar til å berekne avstandar parallelt med aksane i eit koordinatsystem

- [ ] __Programmering, 10. trinn__: bruke grunnleggjande prinsipp i
  programmering, slik som løkker, testar, variablar, funksjonar og enkel
  brukarinteraksjon

## Forslag til læringsmål {.challenge}

- [ ] Elevane kan lage enkle figurar som representerer ein slangekropp og eple,
  og bruke dei i eit spel.

- [ ] Elevane kan plassere element i bestemte posisjonar ved hjelp av eit
  koordinatsystem.

- [ ] Elevane kan få ein figur til å bevege seg i eit koordinatsystem ved hjelp
  av retning og hastigheit, og at tilhøyrande figurar følgjer etter.

- [ ] Elevane kan lage eit spel med kontinuerleg brukarinteraksjon.

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
[Klikk her for å sjå oppgåveteksten.](../snake/snake_nn.html){target=_blank}


# Når eg får meldinga [nytt spel] {.activity}

I dei meir avanserte Scratch-oppgåvene brukar me kodeblokka

```blocks
når eg får meldinga [Nytt spel v]
```

i staden for

```blocks
når @greenFlag vert trykt på
```

Det blir introdusert litt subtilt i kvar oppgåve, så dei fleste elevane får det
ikkje med seg når dei programmerer. Å bruke ei slik melding har fleire fordelar,
mellom anna at det går an å starte spelet på nytt utan å måtte trykke på det
grøne flagget (til dømes kan meldinga `Nytt spel` sendast ut når ein bestemt
tast på tastaturet blir trykt). Gjerne diskuter fordelar og ulemper ved dette
med elevane for å gjere eit poeng av det.

## Variasjonar {.challenge}

- [ ] Elevane kan lage ein variabel som tel poeng.

- [ ] Elevane kan lage ein funksjon som aukar hastigheita i spelet. Merk at å
  auke antal steg slangen går ikkje vil fungere direkte, fordi alle ledda i
  kroppen òg må henge med.

- [ ] Elevane kan lage eple med ulike effektar, til dømes at slangekroppen aukar
  med to ledd i staden for eitt.

- [ ] Elevane kan la fleire eple vere synlege samstundes.

- [ ] Elevane kan la epla flytte seg viss det går for lang tid før dei blir
  etne.

- [ ] Elevane kan lage ein to-spelar-versjon, der spelarane både konkurrerer om
  å ete eple og å låse kvarandre inne.

- [ ] Elevane kan lage ei framside og ei menyside for spelet.

## Eksterne ressursar {.challenge}

- [ ] Førebels ingen eksterne ressursar...
