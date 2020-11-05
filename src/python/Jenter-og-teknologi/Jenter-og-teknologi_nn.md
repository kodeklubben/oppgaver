---
title: "Jenter og teknologi"
author: "Béatrice Bieuville" 
language: "nn"
---


# Introduksjon {.intro}

Speler det noko rolle å vera ei jenta eller ein gut når det gjeld å velja utdanning? Finst det eit kjønnsgap? I denne oppgåva skal du undersøkja spørsmålet, ved å laga ei programvare som viser data i eit diagram. Data som du skal bruke vart henta på samordnaopptak.no. Du skal programmera i Python, som er eit veldig godt programmeringsspråk for å handtere datasett.


# Førebu koding {.activity}

Her skal du henta filene som trengs, og førebu programmering i Python.

## Sjekkliste {.check}

- [ ] Opne og last ned .csv-fila på [lenka her](https://drive.google.com/file/d/1af07oztwUAdDiuckpxpGhjmPQYAOSoSA/view?usp=sharing){target=_blank}.

## {.tip}
.csv (for comma-separated values) er eit format for å lagra tabelldata i tekstform. Data frå ein vanleg tabell er lagra som tekst og ser slik ut:

```
Olympe de Gouges, 1791
Simone de Beauvoir, 1949
Simone Veil, 1975
```

I .csv-fila er det  `,` eller `;` mellom kvar kolonne.
#

- [ ] Opne python 3 i [Trinket](https://trinket.io/python3){target=_blank}

## {.tip}
Trinket gjer det mogleg å skrive og køyre Python i nettlesaren. Vanlegvis køyrer Python på PCen, ikkje i nettlesaren.
#

- [ ] Last opp .csv-filaved å trykkja på "upload text file"-ikonet. Vel dokumentet som du har lasta ned i "nedlastingar"-mappa på PC-en din.

![ikon upload](ikonUpload.png)

- [ ] No har du eit prosjekt med to filer (main.py og jenter-teknologi.csv) og eit slikt arbeidsområde:

![pyhton3 trinket prosjekt](arbeidsO.png)

#
# Bygg diagrammet i main.py {.activity}
#

No skal du laga eit diagram for å presentera data frå tabellen du har importert. Skriv koden under i main.py.

## Sjekkliste {.check}
#

- [ ] Import bibliotek: 
**Bibliotek** innheld mellom anna ferdig laga funksjonar, som gjer at når me bruker dei så slepper me å skrive all koden sjølv. Meir informasjon om [programvarebibliotek på wiki](https://nn.wikipedia.org/wiki/Programvarebibliotek)

```python
import matplotlib.pyplot as plt
import numpy as np
```

## {.tip}
Det er OK å vera litt lat av og til. Dermed tilsetter me `as np`, slik at me kan skrive `np` i staden for `numpy` i koden.
#

- [ ] Lagre data frå jenter-teknologi.csv i main.py med `np.genfromtext`. Fyrst, lag ein variabel `x1` som blir x-aksen. Den skal innehalda data frå den aller fyrste kolonna i tabellen, som har index 0. Dermed skriv me `usecols=(0)`.

```python
x1  = np.genfromtxt('jenter-teknologi.csv', skip_header=1, usecols=(0), unpack=True, delimiter=',')
```
## {.tip}
I programmering startar ikkje data indexen på 1. Den aller fyrste tingen i ei liste har index 0.
#

- [ ] No, lag ein variabel `y1` som blir y-aksem. Den skal innhalda data frå den andre kolonna i tabellen, som har index 1. Dermed skriv me `usecols=(1)`.

```python
y1 = np.genfromtxt('jenter-teknologi.csv', skip_header=1, usecols=(1), unpack=True, delimiter=',')
```

- [ ] Teikn diagrammet ved å bruke data som du har lagra i `x`og `y`.

```python
plt.plot(x1,y1, marker='p')
```

- [ ] Vis diagrammet:

```python
plt.show()
```

## Test prosjektet {.flag}

- [ ] Trykk på køyr-knappen (over main.py tilttelen).

![køyr](koeyr.png)

#

# Prøv sjølv {.try}

- Endre nummer etter `skip_header` og køyr koden ein gong til. Kva skjer? Kvifor bruker me `skip_header` ?
#

## Utfordring #1 {.challenge}

Når du teikna diagrammet, skreiv du `plt.plot(x,y, marker='p')`. Kan du endre på det og velja sjølv kva type `marker` du vil bruke?

### Tips 

Prøv andre marker som finns i matplotlib [dokumentasjon](https://matplotlib.org/3.1.1/api/markers_api.html){target=_blank}. Køyr koden ein gong til. Kva skjer?

#

## Utfordring #2 {.challenge}

I .csv-filene: endre alle `,` med `;` og køyr koden. Kva skjer? Kan du fiksa koden i `main.py` slik at den kan lese .csv-filene som no innheld `;` ?

### Tips 
Sjekk  `delimiter` parameter i `main.py`.
#

# Tilsett kontekst {.activity}
#

No har du eit diagram, men det står ikkje kva informasjon det viser. Desse linjene treng du å skrive over `plt.show()`.

## Sjekkliste {.check}
#

- [ ] Tilsett ein label til x-aksen:
```python
plt.xlabel('År')
```

- [ ] Tilsett ein label til y-aksen:
```python
plt.ylabel('Andel jenter per 100 søkjarar')
```

- [ ] Tilsett ein tittel:
```python
plt.title('Andel jenter som vel teknologi utdanning som fyrsteval')
```

## Test prosjektet {.flag}

- [ ] Trykk på køyr-knappen (over main.py tittelen).

#

# Tilsett ei andre linje med data {.activity}
#

Det kunne vera interessant å samanlikna data. No veit me kor mangeav søkjarane innan teknologi som er jenter. Kva med andre utdanningsområder? No skal du laga ein andre linje i diagrammet for å samanlikna data.

## Import data {.check}
#

- [ ] Me skal samanlikna data frå teknologi-søkjarar med søkjarar til helsefag. Den nye fila inneheld data om kor mange jenter det er som har søkt, av alle dei som søkjer for utdanning i helsefag. Fila med data som du skal lasta ned finn du [her](https://drive.google.com/file/d/1elt74YdjJwMwp4kQ-ZLIaLRvLfyqSybB/view?usp=sharing){target=_blank}

- [ ] Importer tabellen i Trinket ved å trykkja på `upload text file`. No har du ein ny tekstfil som heiter jenter-helsefag.csv.

## Utfordring #3 {.challenge}

- Kan du laga ein variabel `x2`, og lagra data frå kolonna `0` i jenter-helsefag.csv inni den? 
- Kan du laga ein variabel `y2`, og lagra data frå kolonna `1` i jenter-helsefag.csv inni den?

### Tips

- Denne delen av koden må du skrive rett etter `x1- og `y1`-variablane.
- Du treng å bruke `np.genfromtxt`. 
- Måten å gjera det er det same når du har laga variablane `x1` og `y1`.
#

## Sjekkliste {.check}
#

- [ ] Skriv at du skal ha fleire datasett. Fyrst må du fjerna:
```python
plt.plot(x1,y1, marker='p')
```
og i staden skrive (over `plt.show()`):

```python
ax = plt.subplot()
```

- [ ] Teikn den fyrste linja:

```python
linje1 = ax.plot(x1,y1, label="teknologi")
```

- [ ] Teikn den andre linja:

```python
linje2 = ax.plot(x2,y2, label="helsefag")
```

- [ ] Vis label:

```python
ax.legend()
```

## Utfordring #4 {.challenge}

Kan du oppdatera tittelen til diagrammet?

#

## Test prosjektet {.flag}

- [ ] Trykk på køyr-knappen.

# Prøv sjølv {.try}

- Kva skjer om du endrer `label="teknologi"` og `label="helsefag"`  ?
# 

## Utfordring #5 {.challenge}

- Kan du bytta fargen til linjene? Du kan prøva å endre fargen til tittelen og labelene òg.

### Tips

For å gjera det treng du å bruke parameter `color`:

```python
linje1 = ax.plot(x1,y1, color="")
```

Du kan velja fargen du vil bruka blant dei som står i [denne lista](https://www.w3schools.com/colors/colors_names.asp){target=_blank}
#


## Lagre og del {.save}

Du har laga ei programvare som viser fleire dataset i eit diagram. 

Programvara har laga eit bilete som heiter `trinket_plot.png`. Du kan trykkja på det for å åpna biletet i ei ny fane og lagra det. 

Kva viser diagrammet når det gjeld datasetta som du har samanlikna?