---
title: "PXT: Tell med løkker"
author: Helene Isnes
language: nb
---


# Introduksjon {.intro}
I denne oppgaven skal vi få micro:biten til å telle både oppover og nedover med
løkker.


# Steg 1: Lag en løkke {.activity}

## Sjekkliste {.check}

- [ ] Gå til `Løkker`{.microbitloops} i menyen. Som du ser finnes det flere typer,
	men i denne	oppgaven skal vi benytte løkken `gjenta for indeks fra 0 til 4`{.microbitloops}.
	Dette er en mye brukt løkketype som er kjent som en for-løkke.

# Steg 2: Begynn å tell {.activity}

## Sjekkliste {.check}

- [ ] Lag koden som vises nedenfor. Du finner klossene `ved start`{.microbitbasic}
	og `vis tall`{.microbitbasic} i `Basis`{.microbitbasic}, mens `indeks`{.microbitvariables}
	finner du i `Variabler`{.microbitvariables} etter at du legger ut løkka. Husk
	å endre tallet i løkka fra 4 til 5!

```microbit
for (let indeks = 0; indeks <= 5; indeks++) {
    basic.showNumber(indeks)
}
```

- [ ] Simulatoren til venstre skal nå ved start av programmet telle fra 0 opp til 5.

## {.tip}
En løkke kjører koden som står inni flere ganger. Det som gjør for-løkka nyttig,
er at variabelen `indeks`{.microbitvariables} får en ny verdi hver gang. Den
første løkka som kjøres har `indeks`{.microbitvariables} lik 0. Når den viser
tallet som heter `indeks`{.microbitvariables}, viser den dermed tallet 0. Så
kjører den løkka en gang til, men nå har den endret verdien av `indeks`{.microbitvariables}
til 1, og viser tallet 1 istedenfor. Slik fortsetter den å kjøre løkka for
`indeks`{.microbitvariables} = 2, `indeks`{.microbitvariables} = 3,
`indeks`{.microbitvariables} = 4 og `indeks`{.microbitvariables} = 5. Da stopper
den, siden vi har sagt at den bare skal gjenta seg selv for indeksverdiene fra
0 til 5.
##

- [ ] Kan du endre koden så løkka teller fra 0 til 9 istedenfor?


# Steg 3: Endre indeks {.activity}

`Indeks`{.microbitvariables} begynner på null, men hvis vi viser tallet
`indeks`{.microbitvariables}+1 istedenfor, vil det første tallet som vises være 1.

## Sjekkliste {.check}

- [ ] Finn `pluss`{.microbitmath}-klossen i `Matematikk`{.microbitmath}-kategorien
	og sett den inn i `vis tall`{.microbitbasic}-klossen.

- [ ] Fiks på koden din til den ser slik ut:

```microbit
for (let indeks = 0; indeks <= 9; indeks++) {
    basic.showNumber(indeks + 1)
}
```

- [ ] Fra hvilket tall til hvilket tall teller løkka nå? Når `indeks`{.microbitvariables}
	er lik 9, hva blir `indeks`{.microbitvariables}+1?


# Steg 4: Telle nedover {.activity}

`Indeks`{.microbitvariables} øker med 1 for hver runde i løkka, men med
matematikk kan vi få koden til å telle nedover likevel.

- [ ] Gjør __pluss__-klossen om til en __minus__-kloss ved å velge __-__ i nedtrekkslista
(klikk på pila ved siden av __+__).

- [ ] Endre resten av koden slik at den ser slik ut:

```microbit
for (let indeks = 0; indeks <= 9; indeks++) {
    basic.showNumber(9 - indeks)
}
```

- [ ] Teller programmet nedover som den skal?


## Utfordringer {.challenge}

- [ ] Programmet teller nokså fort. Bruk en `pause`{.microbitbasic}-kloss med et
	tall du synes passer (100 ms = et tidels sekund, 1000 ms = 1 sekund) for å
	telle saktere.

- [ ] Klarer du å lage et program som teller ned fra 3 (3, 2, 1) og så viser et
	bilde?
