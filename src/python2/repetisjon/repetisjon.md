---
title: Repetisjon
level: 1
author: Ole Kristian Pedersen, Kodeklubben Trondheim
---

# Introduksjon {.intro}

I denne oppgaven skal vi reptere litt Python-syntaks. Hele dette kurset
er for de som har programmert Python før. Dersom du aldri har programmert
Python før bør du starte med [introduksjonskurset i Python](../../python/index.html).

# Input og output {.activity}

## input() og print() {.protip}

Vi kan bruke `print()` når vi skal skrive ut tekst til brukeren.

```python3
>>> print("Hei, verden")
Hei, verden
```

`input()` brukes når du ønsker å la brukeren gi input til programmet ditt.

```python3
>>> number = input("Skriv inn et tall: ")
Skriv inn et tall: 15
>>> print("Du skrev inn: " + str(number))
Du skrev inn: 15
```
<!--A little workaround to avoid checklist being a part of protip-->
# {.check}

* Skriv et program som spør om brukerens navn, og så skriver ut en
  hilsen til brukeren. Det kan for eksempel fungere slik:

    <pre>
    >>>
    Hei! Hva er navnet ditt?
    <font color="blue">Per</font>
    Hyggelig å treffe deg, Per!
    </pre>

# if-elif-else {.activity}

## {.protip}

`if`- og `elif`-setninger trenger en test. Koden som skal kjøres i testen må
bli sann eller usann. Dersom testen er sann, kjøres koden i testblokken. `else`
trenger ikke en test, men kjøres bare når de tidligere testene har vært usanne.

Husk at du alltid må starte med en `if`-setning, og må ha alle `elif`-setningene
før en `else`-blokk. Du *trenger* ikke å bruke verken `elif`-setninger eller
`else`-blokk dersom du ikke ønsker det.

For eksempel slik:

```python3
name = "Ada"
if name == "Per":
    print("Per er et guttenavn")
elif name == "Ada":
    print("Ada er et jentenavn")
elif name == "Kim":
    print("Kim kan være både guttenavn og jentenavn.")
else:
    print("Jeg vet ikke om " + navn + " er en gutt eller ei jente.")
```

<!--A little workaround to avoid checklist being a part of protip-->
# {.check}

* Skriv et program som spør om brukerens alder, og skriver ut om de er barn,
  ungdom, voksen eller pensjonist. Du kan selv bestemme hvor aldersgrensene
  skal gå, men det må være realistisk. Det kan for eksempel fungere slik:

    <pre>
    >>>
    Hei! Hva er alderen din?
    <font color="blue">77</font>
    Du er visst en pensjonist.
    </pre>

# Løkker {.activity}

## for-løkker {.protip}

`for`-løkker brukes når vi ønsker å gjøre ting flere ganger.

```python3
# print "Hello" three times
for i in range(3):
    print("Hello")
```

Da får vi ut:

```
>>>
Hello
Hello
Hello
```

Vi kan også bruke `for`-løkker når vi ønsker å gå igjennom ei liste:

```python3
# print each element in the list `food_list`
food_list = ["eggs", "ham", "spiced ham", "jam"]
for food in food_list:
    print(food)
```

Dette programmet vil skrive ut:

```
>>>
eggs
ham
spiced ham
jam
```

<!--A little workaround to avoid checklist being a part of protip-->
# {.check}

* Lag ei liste med navn, og skriv ut alle navnene i lista. Dette kan se slik ut:

    <pre>
    >>>
    Per
    Ada
    Kim
    </pre>

# range() {.protip}

Vi kan bruke `range()` for å få ei slags liste med tall, som vi kan bruke
løkker for å gå igjennom. `range()` tar inn tre argumenter `start`, `stop`,
`step`.

 * `start` forteller hvor vi skal begynne å telle fra
 * `stop` forteller hvor vi skal slutte å telle fra, merk at vi **ikke** teller
    med slutt tallet.
 * `step` forteller hvor mye vi skal telle med om gangen. Vi kan for eksempel
    telle med `2` om gangen, eller med `100` om gangen, hvis vi vil.

Dersom vi ønsker å skrive ut lista, må vi bruke `list()` som konverterer
`range()` til ei liste. Her er noen eksempler:


```python3
>>> print(list(range(1, 10, 1)))
[0, 1, ..., 8, 9]
>>> print(list(range(10)))
[0, 1, ..., 8, 9]
>>> print(list(range(200, 500)))
[200, 201, ..., 498, 499]
>>> print(list(range(0, 50, 5)))
[0, 5, ..., 40, 45]
```

`range()` kan prukes på mange måter, vi kan for eksempel gå igjennom den og
summere alle tallene fra 1 til 100:

```python3
sum = 0
for number in range(1, 101):
    sum += number
print(number)
```

# while-løkker {.protip}

`while`-løkker har mange ulike bruksområder. De kan for eksempel brukes når
du vil kjøre kode så lenge du ikke får en bestemt verdi:

```python3
word = ""
while word != "exit":
    print(word)
    word = input("Please write a word: ")
```

Den samme løkken kan også skrive slik:

```python3
while True:
    word = input("Please write a word: ")
    if word == "exit":
        break
    print(word)
```

<!--A little workaround to avoid checklist being a part of protip-->
# {.check}

* Skriv et program som summerer alle tallene fra 1 til 100, ved hjelp av ei
  `while`-løkke. Pass på at du får `5050` som svar.

# Funksjoner {.activity}

# {.protip}

Funksjoner lar oss gjenbruke kode, og er svært nyttig når vi skal programmere
mer enn noen få linjer. En funksjon er på formen:

```python3
def greet(name):
    print("Hei, " + name + "!")

greet("Per")
```

Her har vi en funksjon med navn `greet`, som skriver ut en hilsen. `name` er
et **parameter**, det vil si at `name` er en variabel som funksjonen `greet`
tar imot. Når vi *kaller* funksjonen `greet`, med `greet("Per")` er `"Per"` et
**argument** til funksjonen. Et argument er den variabelen vi gir til funksjonen
når vi kaller den.

Vi kan også ha funksjoner som returnerer en verdi. Det vil se slik ut:

```python3
def multiply(x, y):
    product = x*y
    return product
```

<!--A little workaround to avoid checklist being a part of protip-->
# {.check}

* Skriv en funksjon, `add(x, y)` som tar inn to tall som parametre, skriver ut tallene den
  får inn, før den så _returnerer_ summen av tallene. Test at funksjonen din
  fungerer som dette:

    ```python3
    >>> sum = add(3, 4)
    Fikk inn 3 og 4
    >>> print(sum)
    7
    ```
