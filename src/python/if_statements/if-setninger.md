---
title: If-setninger
level: 2
author: Ole Kristian Pedersen, Kodeklubben Trondheim
---

# Introduksjon {.intro}
Vi lærte i [Kuprat](../kuprat/kuprat.html) at vi kan bruke `input()` for å få tekst fra
brukeren og `print()` for å skrive ut tekst til brukeren. Det kan for
eksempel gjøres slik:

```python
navn = input("Hva er navnet ditt? ")
print("Hei, " + navn)
```

I denne oppgaven skal vi lære hvordan vi kan bruke `if`-setninger for å la
programmet bestemme hva det skal gjøre, helt avhengig av hva brukeren
skriver inn.

# Steg 1: En enkel if-setning {.activity}

En `if`-setning fungerer slik:

```python
age = 22
if age > 18:
    print("Du er voksen!")
```

`if age > 18:` kan deles opp i tre deler.

 * `if` forteller datamaskinen at nå kommer det en `if`-setning
 * `age > 18` tester om `age`-variabelen er større enn 18
 * `:` betyr at vi er ferdig med testen vår, og nå kommer koden som skal kjøres hvis testen er sann.

Legg merke til at det er et "innrykk" før `print`. Dette innrykket sørger for
at datamaskinen vet nøyaktig hvilken kode som skal kjøres hvis `if`-setningen er
sann. Dersom du glemmer dette kan det være at datamaskinen gjør noe annet enn
det du hadde tenkt, eller ikke vil kjøre programmet ditt i det hele tatt!

## Test prosjektet {.flag}
Skriv koden selv, kjør den og se hva som skjer. Prøv å endre `age`-variabelen,
du kan for eksempel endre til `age = 13` eller `age = 67`.

Hva skjer om du endrer retningen på ulikhetstegnet, til `age < 18`?

# Steg 2: Hvis.. {.activity}

Vi lærte i [Steg 1](#steg-1-en-enkel-if-setning) at `if`-setninger sjekker om en test
blir sann, og hvis testen er sann kjøres koden som har innrykk etter
`if`-setningen.

Hva skjer når vi kjører denne koden?

```python
if 3 == 2+1:
    print("3 er lik 2+1")
```

Du skjønte kanskje at `==` tester om `3` er lik `2+1`. Det er viktig at vi har
**to** likhetstegn, for det er bare da den **tester** om to variabler eller verdier
er like.

Vi kan også sjekke om to verdier er ulike, ved å bruke `!=`.

```python
if 4 != 2+1:
    print("4 er ikke lik 2+1")
```

## Utfordring {.challenge}

Her har en av CodeMasterne gjort en feil. Kan du hjelpe oss å finne feilen?

```python
if 7 == 2*4:
    print("7 er ikke lik 2*4")
```

**Hint**: Se på teksten som skal skrives ut!

# Steg 3: Litt mer avansert {.activity}

* Vi har lyst til å skrive et program som hilser på personer som heter "Per".
  Dette kan vi gjøre slik:

  ```python
  navn = input("Hva heter du? ")
  if navn == "Per":
      print("Hei!")
      print("Hyggelig å hilse på deg," + navn + "!")
  ```

  Her har vi to linjer med innrykk! Begge disse kjøres om testen er sann, og
  kjører ikke om testen er usann.

* Men hva skjer om den ene linjen ikke har et innrykk, slik som i koden under?

  ```python
  navn = input("Hva heter du? ")
  if navn == "Per":
      print("Hei!")
  print("Hyggelig å hilse på deg," + navn + "!")
  ```

  Hva blir skrevet ut nå?

* Prøv deg frem med ulike navn!
