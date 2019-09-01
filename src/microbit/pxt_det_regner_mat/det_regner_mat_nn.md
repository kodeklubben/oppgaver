---
title: "PXT: Det regnar mat!"
author: Helene Isnes
translator: Stein Olav Romslo
language: nn
---


# Introduksjon {.intro}

"Det regnar mat!" er eit spel som går ut på å fange flest mogleg matbitar. Det
fungerer slik at matbitar fell ned på skjermen og spelaren som står på botnen
skal prøve å fange maten. Spelaren skal bevege seg med knappane A og B. Ein
mistar liv når spelaren ikkje klarar å få tak i maten. Spelaren har til saman
tre liv før spelet er over.


# Steg 1: Grunnlag {.activity}

*Det fyrste me skal gjere er å kode grunnlaget for spelet. Me skal lage mat, ein
 spelar og setje antal liv. Me må også starte noko som kan halde styr på
 poenga.*

## Sjekkliste {.check}

- [ ] Lag tre variablar `spelar`{.microbitvariables}, `mat`{.microbitvariables}
  og `liv`{.microbitvariables} med `Lag ein variabel...`{.microbitvariables} i
  kategorien `Variablar`{.microbitvariables}.

Skjermen vår har 5x5 ledlys. Desse kan me skru av og på med litt kode. I denne
oppgåva brukar me klossar frå `Spel`{.microbitgame}-kategorien til å setje og
endre kor lysa skal vere. Posisjonen til lysa blir gitt ved ein __x__- og ein
__y__-posisjon, som i eit rutenett. Verdien til __x__ gir plassen til lyset
bortover (vassrett) og verdien til __y__ gir plassen nedover (loddrett), som du
ser på biletet under. Hjørnet øvst til venstre er __(0, 0)__ og hjørnet nedst
til høgre er __(4, 4)__.

![Bilete som viser korleis x og y gir posisjonen til ledlysa](ved_start_skjerm.png)

Spelaren skal bevege seg til høgre og venstre nedst på skjermen. Me vil at
`spelar`{.microbitvariables} skal starte på midten av skjermen når me startar,
 (__x = 2__ og __y = 4__).

- [ ] Legg til koden under i `ved start`{.microbitbasic}-klossen som allereie er
  i kodefeltet ditt (eller i `Basis`{.microbitbasic}-kategorien).

```microbit
let spiller: game.LedSprite = null
spiller = game.createSprite(2, 4)
```

- [ ] Gjer det same med variabelen `mat`{.microbitvariables} som du gjorde med
  variabelen `spelar`{.microbitvariables} i punktet over. Me set `mat`{.microbitvariables}
  til __x = 2__ og __y = 2__.

## {.tip}

Du finn `Set spelar til`{.microbitvariables}-klossen i `Variablar`{.microbitvariables}.
`Create sprite at x: 2 y: 4`{.microbitgame}-klossen finn du i kategorien `Spel`{.microbitgame}
i __Avansert__.

## {.tip}

Det er eigentleg ikkje så viktig kor me plasserer `mat`{.microbitvariables} ved
starten, sidan den skal flytte på seg i neste steg. Det som er viktig er at `mat`{.microbitvariables}
er på spelebrettet når me startar, slik at det går an å bruke variabelen seinare.

##

- [ ] Set variabelen `liv`{.microbitvariables} til __3__. Klossen du skal bruke
  finn du i `Variablar`{.microbitvariables}.

- [ ] Ved start skal poengsummen vere __0__. settes til 0. Du finn ein kloss som
  gjer dette i `Spel`{.microbitgame}-kategorien.

- [ ] Viss du har gjort alt rett skal koden din sjå slik ut:

```microbit
let spiller = game.createSprite(2, 4)
let mat = game.createSprite(2, 2)
let liv = 3
game.setScore(0)
```

## {.tip}

Både `mat`{.microbitvariables} og `spelar`{.microbitvariables} blir eit ledlys
kvar på micro:bit-en. Viss du vil skilje dei meir frå kvarandre kan du få maten
til å lyse litt mindre enn spelaren. Det gjer du ved å setje `sprite angir x til 0`{.microbitgame}-klossen
etter `set poengsum til 0`{.microbitgame}. Bytt ut `sprite`{.microbitvariables}
med `mat`{.microbitvariables} og __x__ med `lysstyrke`{.microbitled}.
Simulatoren og micro:bit-en opplever lysstyrke på litt ulike måtar, så i
simulatoren kan du ha lysstyrke __100__, men når du lastar det ned bør du ha
endra lysstyrken til __30__.


# Steg 2: Mat regnar {.activity}

*I dette steget skal me få maten til å regne ned. Maten skal starte på ein
 tilfeldig stad på øvste rad kvar runde.*

## Sjekkliste {.check}

- [ ] I `gjenta for alltid`{.microbitbasic}-klossen (denne har du allereie i
  kodefeltet ditt, eller du finn den i `Basis`{.microbitbasic}), set inn
  `sprite angir x til 0`{.microbitgame}-klossen som du finn i `Spel`{.microbitgame}.
  Bytt ut `sprite`{.microbitvariables} med variabelen `mat`{.microbitvariables}.
  Så byttar du ut __0__ med `velg tilfeldig 0 til 4`{.microbitmath}-klossen
  som du finn i kategorien `Matematikk`{.microbitmath}.

- [ ] Set inn endå ein `sprite angir x til 0`{.microbitgame} -kloss under den
  førre og bytt ut __x__ med __y__.

- [ ] Så treng me ein `pause`{.microbitbasic}-kloss (den ligg i `Basis`{.microbitbasic}).
  Endre talet til __300__.

Til no har me sett `mat`{.microbitvariables} til ein tilfeldig x-posisjon, og
sikra at den startar på øvste rad kvar runde. Vidare skal me lage kode for maten
som skal regne ned.

- [ ] Finn ein `gjenta 4 gonger`{.microbitloops}-kloss i `Løkker`{.microbitloops}
  og plasser den under `pause`{.microbitbasic}-klossen.

For å få maten til å regne nedover må me endre posisjonen til `mat`{.microbitvariables}
i __y__-retninga. Me endrar posisjonen med __1__ for kvar gong me går gjennom
løkka.

- [ ] Legg til koden under i `gjenta 4 gonger`{.microbitloops}-klossen.

## {.tip}

Viss me ikkje legg til `pause`{.microbitbasic}-klosser vil maten bevege seg for
fort til at me klarar å fange den!


# Steg 3: Få poeng og tap liv {.activity}

*No skal me lage kode som anten gir spelaren poeng viss den fangar maten, eller
 som tek bort eit liv viss spelaren ikkje klarar det.*

## Sjekkliste {.check}

- [ ] Plasser ein `viss-elles`{.microbitlogic}-kloss under `gjenta 4 gonger`{.microbitloops}-blokka.
  `Viss-elles`{.microbitlogic}-klossen finn du i `Logikk`{.microbitlogic}.

Me vil at poengsummen skal auke med __1__ viss spelaren klarar å fange maten.

- [ ] Bytt ut `sann`{.microbitlogic} med `is sprite touching`{.microbitgame}-klossen
  som du finn i `Spel`{.microbitgame}-kategorien. I staden for `sprite`{.microbitvariables}
  vil me ha variabelen `spelar`{.microbitvariables} og i den tomme boksen vil me
  ha variabelen `mat`{.microbitvariables}. *"Is* `spelar`{.microbitvariables}
  *touching* `mat`{.microbitvariables} *"
  tyder "berører* `spelar`{.microbitvariables} `mat`{.microbitvariables}*" på
  norsk.*

- [ ] Set inn klossen `endre poengsum med 1`{.microbitgame}-

## {.tip}

`Viss-elles`{.microbitlogic}-klossen fungerer slik at viss spelaren får tak i
maten, så vil programmet køyre koden som høyrer til `viss`{.microbitlogic}-delen
av klossen. Viss ikkje dette er sant (spelaren klarte ikkje å få tak i maten
denne runden), så vil programmet køyre koden som høyrer til `elles`{.microbitlogic}-delen
av klossen.

##

Når `spelar`{.microbitvariables} ikkje klarar å fange maten skal me miste eit liv.

- [ ] I `elles`{.microbitlogic}-delen av `viss-elles`{.microbitlogic}-klossen må
  du setje inn `endre liv med -1`{.microbitvariables}
  som du finn i `Variablar`{.microbitvariables}. *Hugs å endre frå* __1__ *til*
  __-1__ i klossen. Kva skjer viss du ikkje gjer det?*

Vidare må me sjekke om variabelen `liv`{.microbitvariables} er lik null, for
viss den er det har spelaren tapt.

- [ ] Set koden i biletet inn rett under `endre liv med -1`{.microbitvariables}-klossen.
  "Game over" er engelsk for at spelet er slutt, og blir ofte nytta i slike spel.  

- [ ] Sjekk at koden din frå steg 2 og 3 ser slik ut:

```microbit
basic.forever(function () {
    let spiller: game.LedSprite = null
    let mat: game.LedSprite = null
    mat.set(LedSpriteProperty.X, Math.randomRange(0, 4))
    mat.set(LedSpriteProperty.Y, 0)
    basic.pause(300)
    for (let i = 0; i < 4; i++) {
        mat.change(LedSpriteProperty.Y, 1)
        basic.pause(300)
    }
    if (spiller.isTouching(mat)) {
        game.addScore(1)
    } else {
        liv += -1
        if (liv == 0) {
            game.gameOver()
        }
    }
})
```

## Test prosjektet {.flag}

- [ ] Sjekk i simulatoren at det regnar eit ledlys ned med ulik __x__-posisjon for
  kvar runde. Eit anna ledys skal heile tida stå stille midt på nedste rad.


# Steg 4: Beveg spelaren! {.activity}

*No skal me lage siste del av koden, nemleg koden for å styre spelaren!*

## Sjekkliste {.check}

- [ ] Når knapp `A`{.microbitinput} vert trykt skal `spelar`{.microbitvariables}
  bevege seg mot venstre. Dette får me til ved å bruke ein kloss me finn i
  `Spel`{.microbitgame}-kategorien. Lag koden som er vist under.

```microbit
  input.onButtonPressed(Button.A, function () {
      let spiller: game.LedSprite = null
      spiller.change(LedSpriteProperty.X, -1)
  })
```

- [ ] Kopier koden frå førre punkt og endre den slik at når knapp `B`{.microbitinput}
  vert trykt, skal `spelar`{.microbitvariables} bevege seg til høgre.

## Test prosjektet {.flag}

*No er koden ferdig!*

- [ ] Sjekk simulatoren og sjå til at alt fungerer som det skal.

- [ ] Last ned spelet til micro:bit-en og spel i veg!

## {.tip}

Er spelet for lett eller vanskeleg? Du kan endre hastigheiten maten fell ned med
og/eller endre kor mange liv ein startar med.

## Utfordring {.challenge}

- [ ] Legg på lyd!
