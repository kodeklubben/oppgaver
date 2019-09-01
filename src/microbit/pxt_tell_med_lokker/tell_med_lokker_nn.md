---
title: "PXT: Tel med løkker"
author: Helene Isnes
translator: Stein Olav Romslo
language: nn
---


# Introduksjon {.intro}

I denne oppgåva skal me få micro:bit-en til å telje både oppover og nedover med
løkker.


# Steg 1: Lag ei løkke {.activity}

## Sjekkliste {.check}

- [ ] Gå til `Løkker`{.microbitloops} i menyen. Som du ser finst det fleire
  typer, men i denn  oppgåva skal me bruke `gjenta for indeks frå 0 til 4`{.microbitloops}.
  Dette er ein mykje brukt løkketype som er kjent som ei for-løkke.

# Steg 2: Start å telje {.activity}

## Sjekkliste {.check}

- [ ] Lag koden som du ser under. Du finn klossane `ved start`{.microbitbasic}
  og `vis tal`{.microbitbasic} i `Basis`{.microbitbasic}, medan `indeks`{.microbitvariables}
  ligg i `Variablar`{.microbitvariables} etter at du legg ut løkka. Hugs å endre
  talet i løkka frå 4 til 5!

```microbit
for (let indeks = 0; indeks <= 5; indeks++) {
    basic.showNumber(indeks)
}
```

- [ ] Simulatoren til venstre skal no telle frå 0 til 5 når du startar
  programmet.

## {.tip}

Ei løkke køyrer koden som står inni fleire gonger. Det som gjer for-løkka nyttig
er at variabelen `indeks`{.microbitvariables} får ein ny verdi kvar gong. Den
fyrste løkka som vert køyrt har `indeks`{.microbitvariables} lik __0__. Når den
viser talet som heiter `indeks`{.microbitvariables} viser den altså talet __0__.
Så køyrer den løkka ein gong til, men no er verdien endra til __1__, så den
viser talet __1__ i staden. Slik fortset den å køyre løkka for `indeks`{.microbitvariables}
= 2, `indeks`{.microbitvariables} = 3, `indeks`{.microbitvariables} = 4 og
`indeks`{.microbitvariables} = 5. Då stoppar den, sidan me har sagt at den berre
skal gjenta seg sjølv for indeksverdiar frå __0__ til __5__.
##

- [ ] Kan du endre koden så løkka tel frå __0__ til __9__ i staden?


# Steg 3: Endre indeks {.activity}

`Indeks`{.microbitvariables} startar på __0__, men viss me viser talet
`indeks`{.microbitvariables}+1 i staden, vil det fyrste talet som visast vere __1__.

## Sjekkliste {.check}

- [ ] Finn `pluss`{.microbitmath}-klossen i `Matematikk`{.microbitmath}-kategorien
  og set den inn i `vis tal`{.microbitbasic}-klossen.

- [ ] Fiks på koden din til den ser slik ut:

```microbit
for (let indeks = 0; indeks <= 9; indeks++) {
    basic.showNumber(indeks + 1)
}
```

- [ ] Frå kva tal til kva tal tel løkka no? Når `indeks`{.microbitvariables} er
  lik __9__, kva blir `indeks`{.microbitvariables}+1?


# Steg 4: Telje nedover {.activity}

`Indeks`{.microbitvariables} aukar med 1 for kvar runde i løkka, men med
matematikk kan me få koden til å telje nedover likevel.

- [ ] Gjer __pluss__-klossen om til ein __minus__-kloss ved å velje __-__ i nedtrekkslista
  (klikk på pila ved sidan av __+__).

- [ ] Endre reisten av koden slik at den ser slik ut:

```microbit
for (let indeks = 0; indeks <= 9; indeks++) {
    basic.showNumber(9 - indeks)
}
```

- [ ] Tel programmet nedover som det skal?

## Utfordringar {.challenge}

- [ ] Programmet tel veldig fort. Bruk `pause`{.microbitbasic}-klossen
  med eit tall du synest passar (100 ms er eit tidels sekund, 1000 ms er 1
  sekund) for å telje saktare.

- [ ] Klarar du å lage eit program som tel ned frå __3__ (__3__, __2__, __1__)
  og så viser eit bilete?
