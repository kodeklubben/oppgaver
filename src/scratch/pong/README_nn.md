---
title: Lærarrettleiing - Pong
level: 4
language: nn
author: Stein Olav Romslo, Vegard Tuset
---


# Om oppgåva {.activity}

I denne oppgåva skal elevane lage ein versjon av spelet Pong. Det er eitt av dei
aller fyrste dataspela som vart laga, og det fyrste som vart ein kommersiell
suksess. Sjølve spelet er ein forenkla variant av tennis der to spelarar slår
ein ball fram og tilbake. Viss ein av spelarane ikkje klarar å returnere ballen
før den andre spelaren poeng.

![Illustrasjon av eit ferdig Pong-spel](pong.png)

## Oppgåva passar til: {.check}

__Fag__: Kunst og handverk, matematikk, programmering.

__Anbefalte trinn__: 3.-10. trinn.

__Tema__: Geometriske grunnformer, koordinatsystem, løkker, brukarinteraksjon.

__Tidsbruk__: Dobbelttime eller meir.

## Kompetansemål {.challenge}

- [ ] __Kunst og handverk, 2. trinn__: eksperimentere med form, farge, rytme og
      kontrast

- [ ] __Kunst og handverk, 7. trinn__: bruke programmering til å skape
      interaktivitet og visuelle uttrykk

- [ ] __Matematikk, 3. trinn__: eksperimentere med og forklare plasseringar i
      koordinatsystemet

- [ ] __Matematikk, 6. trinn__: utforske og beskrive symmetri og mønster og
      utføre kongurensavbildinger med og utan koordinatsystem

- [ ] __Matematikk, 6. trinn__: bruke variablar, løkker, vilkår og funksjonar i
      programmering til å utforske geometriske figurar og mønster

- [ ] __Programmering, 10. trinn__: bruke grunnleggande prinsipp i
      programmering, slik som variablar, løkker, vilkår og funksjonar, og
      reflektere over bruken av desse

## Forslag til læringsmål {.challenge}

- [ ] Elevane kan lage rektanglar som representerer rekkertar, og ein ball, og
  bruke dei i eit spel.

- [ ] Elevane kan plassere element i bestemte posisjonar ved hjelp av eit
  koordinatsystem.

- [ ] Elevane kan beskrive spegling av vinklar ved hjelp av kode.

- [ ] Elevane kan få ein ball til å bevege seg i eit koordinatsystem ved hjelp
  av retning og hastigheit.

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
  to saman, slik at dei får testa spelet med kvarandre.

## Framgangsmåte

Her finn du tips, erfaringar og utfordringar til dei ulike stega i oppgåva.
[Klikk her for å sjå oppgåveteksten.](../pong/pong_nn.html){target=_blank}


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

- [ ] Elevane kan lage ein variabel som tel poeng, og sjekke kva spelar som får
  poenget.

- [ ] Elevane kan la hastigheita auke utover i spelet, til dåmes kvar gong
  ballen treff ein av rekkertane.

- [ ] Elevane kan justere koden for å sikre at ballen alltid beveger seg mot
  høgre eller venstre (med koden i oppgåva kan ein risikere at den berre går
  rett opp og ned).

- [ ] Elevane kan lage ein funksjon som gir ulik sprett avhengig av kor på
  rekkerten ballen treff.

- [ ] Elevane kan leggje inn moglegheita for å bevege racketane sidelengs.

- [ ] Elevane kan lage power-ups som spelaren kan få i løpet av spelet.

- [ ] Elevane kan lage moglegheita for å spele åleine, og at datamaskina styrer
  den andre rekkerten.

## Eksterne ressursar {.challenge}

- [ ] Sjå [www.ponggame.org](http://www.ponggame.org/) for inspirasjon til ulike
  variantar.
