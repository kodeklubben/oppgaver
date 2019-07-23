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

- [ ] Gå til `Løkker` i menyen. Som du ser finst det fleire typer, men i denne
  oppgåva skal me bruke den som ser slik ut:

	![Bilete som viser `gjenta for indeks frå 0 til 4`-klossen](gjenta_for_kloss.png)

Dette er ein mykje brukt løkketype som er kjent som ei for-løkke.

# Steg 2: Start å telje {.activity}

## Sjekkliste {.check}

- [ ] Lag koden som du ser under. Du finn klossane `ved start` og `vis tal` i
  `Basis`, medan `indeks` ligg i `Variablar` etter at du legg ut løkka. Hugs å
  endre talet i løkka frå 4 til 5!

	![Bilete som illustrerer korleis ein kan få micro:bit-en til å telje fra 0 til 5](ved_start_1.png)

- [ ] Simulatoren til venstre skal no telle frå 0 til 5 når du startar
  programmet.

## {.tip}

Ei løkke køyrer koden som står inni fleire gonger. Det som gjer for-løkka nyttig
er at variabelen `indeks` får ein ny verdi kvar gong. Den fyrste løkka som vert
køyrt har `indeks` lik `0`. Når den viser talet som heiter `indeks` viser den
altså talet `0`. Så køyrer den løkka ein gong til, men no er verdien endra til
`1`, så den viser talet `1` i staden. Slik fortset den å køyre løkka for `indeks
= 2`, `indeks = 3`, `indeks = 4` og `indeks = 5`. Då stoppar den, sidan me har
sagt at den berre skal gjenta seg sjølv for indeksverdiar frå `0` til `5`.

##

- [ ] Kan du endre koden så løkka tel frå `0` til `9` i staden?


# Steg 3: Endre indeks {.activity}

`Indeks` startar på `0`, men viss me viser talet `indeks + 1` i staden, vil det
fyrste talet som visast vere `1`.

## Sjekkliste {.check}

- [ ] Finn ![Bilete av pluss-klossen](pluss_kloss.png)-klossen i
  `Matematikk`-kategorien og set den inn i `vis tal`-klossen.

- [ ] Fiks på koden din til den ser slik ut:

	![Bilete av program som tel frå 1 til 10](ved_start_2.png)

- [ ] Frå kva tal til kva tal tel løkka no? Når `indeks` er lik `9`, kva blir
  `indeks + 1`?


# Steg 4: Telje nedover {.activity}

`Indeks` aukar med 1 for kvar runde i løkka, men med matematikk kan me få koden
til å telje nedover likevel.

- [ ] Gjer `+`-klossen om til ein `-`-kloss ved å velje `-` i nedtrekkslista
  (klikk på pila ved sidan av `+`).

- [ ] Endre reisten av koden slik at den ser slik ut:

	![Bilete av program som tel nedover frå 9 til 0](ved_start_3.png)

- [ ] Tel programmet nedover som det skal?

## Utfordringar {.challenge}

- [ ] Programmet tel veldig fort. Bruk ![Bilete av pause-kloss](pause_kloss.png)
  med eit tall du synest passar (100 ms er eit tidels sekund, 1000 ms er 1
  sekund) for å telje saktare.

- [ ] Klarar du å lage eit program som tel ned frå `3` (`3`, `2`, `1`) og så
  viser eit bilete?
