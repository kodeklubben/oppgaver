---
title: "Jenter og teknologi"
author: "Béatrice Bieuville" 
language: "nn"
---


# Introduksjon {.intro}

Speler det noken rolle å vera ei jenta eller ein gutt når det gjeld å velja utdanning? Er det ein kjønnsgap? I denne oppgåven skal du undersøkja det ved å laga ein programmvare som viser data i eit diagram. Data som du skal bruke vart henta på samordnaopptak.no. Du skal bruke Python, som er eit veldig godt programmeringsspråk for å handla dataset.


# Førebu koding {.activity}

Her skal du henta filene som trengs og førebu programmering i Python.

## Sjekkliste {.check}

- [ ] Åpne og last ned .csv filen på [lenkjen her](https://drive.google.com/file/d/1af07oztwUAdDiuckpxpGhjmPQYAOSoSA/view?usp=sharing){target=_blank}.

## {.tip}
.csv (for comma-separated values) er ein format for å lagra tabelldata i tekstform. Data frå ein vanleg tabell er lagra som tekst og ser slik ut:

```
Olympe de Gouges, 1791
Simone de Beauvoir, 1949
Simone Veil, 1975
```

I .csv filen er det  `,` eller `;` mellom kvar kolon.
#

- [ ] Åpne python 3 i [Trinket](https://trinket.io/python3){target=_blank}

## {.tip}
Trinket er in løysing for å skrive og køyre Python i nettlesaren -vanlegvis køyrer Python på PC-en, ikkje på nettlesaren.
#

- [ ] Last opp .csv filen ved å trykkja på "upload text file" ikonen. Vel dokumentet som du har lasta ned i "nedlastingar" mappa på PC-en din.

**[BILDE IKON]**

- [ ] No har du eit prosjekt med 2 filer (main.py og jenter-teknologi.csv) og ein slik arbeidsområde:

**[BILDE PROSJEKTET]**

#
# Bygg diagrammet i main.py {.activity}
#

No skal du laga eit diagram for å presentera data frå tabellen du har importert. Skriv koden herunder i main.py.

## Sjekkliste {.check}
#

- [ ] Import biblioteker: 
dei innheld bl.a. ferdig laga funskjonar, som gjer at når me bruker dei så slepper me å skrive koden sjølv. Meir info om [programvarebibliotek på wiki](https://nn.wikipedia.org/wiki/Programvarebibliotek)

```python
import matplotlib.pyplot as plt
import numpy as np
```

## {.tip}
Det er OK å vera litt lat av og til. Dermed tilsetter me `as np`, slik at me kan skrive `np` i staden for `numpy` i koden.
#

- [ ] Lagr data frå jenter-teknologi.csv i main.py med `np.genfromtext`. Fyrst, lag ein variabel `x1` som blir din x-axis. Han skal innhalda data frå den aller fyrste kolonen i tabellen, som har index 0. Dermed skriv me `usecols=(0)`.

```python
x1  = np.genfromtxt('andel-jenter.csv', skip_header=1, usecols=(0), unpack=True, delimiter=',')
```
## {.tip}
I programmering startar ikkje data indexen på 1. Den aller fyrste tingen har index 0.
#

- [ ] No, lag ein variabel `y1` som blir din y-axis. Han skal innhalda data frå den andre kolonen i tabellen, som har index 1. Dermed skriv me `usecols=(1)`.

```python
y1 = np.genfromtxt('andel-jenter.csv', skip_header=1, usecols=(1), unpack=True, delimiter=',')
```

- [ ] Teikna diagrammet ved å bruke data som du har lagra i `x`og `y`.

```python
plt.plot(x,y, marker='p')
```

- [ ] Vis diagrammet:

```python
plt.show()
```

## Test prosjektet {.flag}

- [ ] Trykk på køyr knappen (over main.py tilttelen).

#

# Prøv sjølv {.try}

- Forandra nummer etter `skip_header` og køyr koden ein gong til. Kva skjer? Korfor bruker me `skip_header` ?

- Korfor trur du me burker `delimiter=','`?
#

## Utfordring #1 {.challenge}

Når du teikna diagrammet så skreiv du `plt.plot(x,y, marker='p')`. Kan du forandra det og velja sjølv kva type `marker` du vil bruke?

### Tips 

Prøv andre marker som finns i matplotlib [dokumentasjon](https://matplotlib.org/3.1.1/api/markers_api.html){target=_blank}      . Køyr koden ein gong til. Kva skjer?

#

# Tilsett kontekst {.activity}
#

No har du eit diagram men det står ikkje kva informasjon han viser. 

## Sjekkliste {.check}
#

- [ ] Tilsett ein label til x-axis:
```python
plt.xlabel('År')
```

- [ ] Tilsett ein label til y-axis:
```python
plt.ylabel('Andel jenter for 100 søkjarar')
```

- [ ] Tilsett ein tittel:
```python
plt.title('Andel jenter som vel teknologi utdanning som fyrste valg')
```

## Test prosjektet {.flag}

- [ ] Trykk på køyr knappen (over main.py tittelen).

#

# Tilsett ein andre linje med data {.activity}
#

Det kunne vera interessant å samanlikna data. No veit me kva andel av søkjarane innan teknologi er jenter. Kva med andre utdanningsområder? No skal du laga ein andre linje i diagrammet for å samanlikna data.

## Import data {.check}
#

- [ ] Me skal samanlikna data frå teknologi søkjarar med helsefag søkjarar. Den nye filen innheld data om andel jenter blant dei som søkjer for utdanning i helsefag. Filen med data som du skal lasta ned finn du [her](https://drive.google.com/file/d/1elt74YdjJwMwp4kQ-ZLIaLRvLfyqSybB/view?usp=sharing){target=_blank}

- [ ] Importer tabellen i Trinket ved å trykkja på `upload text file`.

## Utfordring #2 {.challenge}

- Kan du laga ein variabel `x2`, og lagra inni han data frå kolonen `0` i jenter-helsefag.csv? 
- Kan du lagra ein variabel `y2`, og lagra inni han data frå kolonen `1` i jenter-helsefag.csv?

### Tips

- Denne delen av koden må du skrive rett etter `x1`og `y1`variablane.
- Du treng å bruke `np.genfromtxt`. 
- Måten for å gjera det er det same enn når du har laga variablane `x1` og `y1`.
#

## Sjekkliste {.check}
#

- [ ] Skriv at du skal ha fleire dataset. Fyrst må du fjerna:
```python
plt.plot(x,y, marker='p')
```
og skrive i stad (over `plt.show()`):

```python
ax = plt.subplot()
```

- [ ] Teikna den fyrste linja:

```python
linje1 = ax.plot(x1,y1, label="teknologi")
```

- [ ] Teikna den andre linja:

```python
linje2 = ax.plot(x2,y2, label="helsefag")
```

- [ ] Vis label:

```python
ax.legend()
```

## Utfordring #3 {.challenge}

Kan du oppdatera tittelen til diagrammet?

#

## Test prosjektet {.flag}

- [ ] Trykk på køyr knappen.

# Prøv sjølv {.try}

- Kva skjer om du forandrar `label="teknologi"` og `label="helsefag"`  ?
# 

## Utfordring #4 {.challenge}

- Kan du bytta fargen til linjene? Du kan prøva å forandra fargen til tittelen og labelene òg.

### Tips

For å gjera det treng du å bruke parameter `color`:

```python
linje1 = ax.plot(x1,y1, color="")
```

Du kan velja fargen du vil bruka blant dei som står i [denne lista](https://www.w3schools.com/colors/colors_names.asp){target=_blank}
#


## Lagr og del {.save}

Du har laga eit programvare som viser fleire dataset i eit diagram. 

Programvaren har laga eit bilde som heiter `trinket_plot.png`. Du kan trykkja på det for å åpna bildet i ein ny fane og lagra det. 

Kva vis diagrammet når det gjeld datasetta som du har samanlikna?
