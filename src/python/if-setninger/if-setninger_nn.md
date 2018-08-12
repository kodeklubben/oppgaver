---
title: If-setningar
author: Ole Kristian Pedersen, Kodeklubben Trondheim
translator: Stein Olav Romslo
language: nn
---


# Introduksjon {.intro}

I [Kuprat](../kuprat/kuprat_nn.html) lærte me at me kan bruke `input()` for å få
tekst frå brukaren og `print()` for å skrive ut tekst til brukaren. Det kan til
dømes gjerast slik:

```python
namn = input("Kva heiter du? ")
print("Hei, " + namn)
```

I denne oppgåva skal me lære korleis me kan bruke `if`-setningar for å la
programmet bestemme kva det skal gjere, heilt avhengig av kva brukaren skriv
inn.


# Steg 1: Ei enkel if-setning {.activity}

Ei `if`-setning fungerer slik:

```python
age = 22
if age > 18:
    print("Du er vaksen!")
```

`if age > 18:` kan delast opp i tre delar:

- `if` forteller datamaskinen at nå kommer det en `if`-setning.

- `age > 18` testar om `age`-variabelen er større enn 18.

- `:` tyder at me er ferdig med testen vår, og no kjem koden som skal køyrast
  viss testen er sann.

Legg merke til at det er eit innrykk før `print`. Innrykket syt for at
datamaskina veit akkurat kva som skal køyrast viss `if`-setninga er sann. Viss
du gløymer det kan det vere at datamaskina gjer noko anna enn det du hadde
tenkt, elles vil ikkje programmet ditt køyre i det heile!

## Test prosjektet {.flag}

Skriv koden sjølv, køyr den og sjå kva som skjer. Prøv å endre `age`-variabelen,
du kan til dømes endre til `age = 13` eller `age = 67`.

Kva skjer viss du endrar retninga på ulikskapsteiknet, så du får `age < 18`?


# Steg 2: Viss.. {.activity}

Me lærte i [Steg 1](#steg-1-ei-enkel-if-setning) at `if`-setningar sjekkar om
ein test blir sann, og viss testen er sann køyrast koden som har innrykk etter
`if`-setningen.

Kva skjer når me køyrer denne koden?

```python
if 3 == 2+1:
    print("3 er lik 2+1")
```

Du forsto kanskje at `==` testar om `3` er lik `2+1`. Det er viktig at me har
**to** likskapsteikn, for det er berre då den **testar** om to variablar eller
verdiar er like.

Me kan òg sjekke om to verdiar er ulike, ved å bruke `!=`.

```python
if 4 != 2+1:
    print("4 er ikkje lik 2+1")
```

## Utfordring {.challenge}

- [ ] Her har ein av CodeMasterane gjort ein feil. Kan du hjelpe oss å finne
  feilen?

```python
if 7 == 2*4:
    print("7 er ikkje lik 2*4")
```

**Hint**: Sjå på teksten som skal skrivast ut!


# Steg 3: Litt meir avansert {.activity}

- Me har lyst til å skrive eit program som helsar på personar som heiter "Per".
  Det kan me gjere slik:

  ```python
  namn = input("Kva heiter du? ")
  if namn == "Per":
      print("Hei!")
      print("Hyggjeleg å helse på deg, " + namn + "!")
  ```

  Her har me to linjer med innrykk! Begge desse blir køyrt viss testen er sann,
  og ingen av dei blir køyrt om testen er usann.

- [ ] Men kva skjer om den eine linja ikkje har eit innrykk, slik som i koden
  under?

  ```python
  namn = input("Kva heiter du? ")
  if namn == "Per":
      print("Hei!")
  print("Hyggjeleg å helse på deg, " + namn + "!")
  ```

- [ ] Kva blir skrive ut no?

- [ ] Prøv deg fram med ulike namn!
