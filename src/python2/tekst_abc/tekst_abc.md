---
title: Tekststrenger 1
level: 1
author: Ole Kristian Pedersen, Kodeklubben Trondheim
---

# Introduksjon {.intro}

I denne oppgaven skal vi begynne med litt enkel manipulering av tekststrenger.
**Manipulering** betyr i denne sammenhengen å forandre på tekstrengene på ulike
måter. En **tekststreng** er flere bokstaver etter hverandre. Tekststrenger er
veldig mye brukt innen programmering, og det er dermed viktig å kunne manipulere
teksten på ulike måter.

# Store og små bokstaver {.activity}

## {.protip}

Den enkleste måten å manipulere tekst på er ved hjelp av funksjoner som endrer
mellom store og små bokstaver. Disse finnes det mange av. Gitt at vi har en
tekststreng `s`, så kan vi for eksempel bruke disse funksjonene:
`s.lower()`, `s.upper()`, `s.title()`, `s.swapcase()` og `s.capitalize()`.

Legg merke til at vi funksjonene kalles **på tekstrengen** istedenfor å gi
tekststrengen til funksjonene.


Her er noen eksempler på hvordan funksjonene brukes. Legg merke til hvilke
bokstaver som er store og små det skrives ut:

```python
>>> s = "Per og Ada"
>>> print(s.upper())        # Bare store bokstaver
PER OG ADA
>>> print(s.lower())        # Bare små bokstaver
per og ada
>>> print(s.capitalize())   # Første bokstav i tekststrengen er stor
Per og ada
>>> print(s.title())        # Første bokstav i hvert ord er stor
Per Og Ada
>>> print(s.swapcase())     # Gjør store bokstaver små, og motsatt
pER oG aDA
```

Når bruker vi de ulike funksjonene? Her er noen flere eksempler:

* `s.capitalize()` kan brukes når vi ønsker stor forbokstav i en tekststreng:

    ```python
    >>> sentence = "dENne sETNinGeN har IKKE riKTige bokSTAVstØrReLSER."
    >>> print(sentence.capitalize())
    Denne setningen har ikke riktige bokstavstørrelser.
    ```
* `s.title()` kan eksempelvis brukes når vi skal skrive filmtitler:

    ```python
    >>> movie_title = "star wars: a new hope"
    >>> print(movie_title.title())
    Star Wars: A New Hope
    ```

* `s.upper()` og `s.lower()` har mange ulike bruksområder. De er kanskje mest
  nyttige når du skal sammenlikne setninger uten å ta hensyn til store og
  små bokstaver. Her er et galt eksempel, og et riktig eksempel:

    ```python
    >>> answer = "JA"
    >>> answer == "ja"  # Galt - bare små bokstaver tillatt
    False
    ```

    ```python
    >>> answer = "JA"
    >>> answer.lower() == "ja"  # Rikig
    True
    ```

Det er en ting som man må huske på når man bruker disse funksjonene. De
endrer **ikke** på variabelen. Derfor må du lagre resultatet i en ny variabel
om du vil beholde endringen din:

```python
>>> s = "tekst"
>>> print(s.upper())  # Vi endrer ikke på variabelen!!
TEKST
>>> print(s)  # Fremdeles små bokstaver
tekst
>>> s = s.upper()  # Nå endrer vi på variabelen
>>> print(s)  # Denne gangen er det store bokstaver
TEKST
```

<!--Workaround-->
# {.check}

Nå skal du lage et lite program som skriver ut filmtitler med store bokstaver
først i hvert ord:

<pre>
>>>
Skriv inn en filmtittel: <font color="green">alice in wonderland</font>
Alice In Wonderland
</pre>

Dette må du gjøre:

 * Be om at brukeren skriver inn en filmtittel.
 * Lagre filmtittelen i en variabel.
 * Manipuler tekststrengen slik at resultatet blir som beskrevet over.
 * Skriv ut den nye tekststrengen.


# Telling av substrenger {.activity}

# s.count() {.protip}

En tekststreng i en annen tekststreng ofte en **substreng**. For eksempel er
`"verden"` en substreng av `"Hei verden!"`. Noen ganger ønsker man å finne ut
om en tekststreng har en bestemt substreng, og hvor mange ganger substrengen
finnes i tekststrengen.

Tenk deg at du ønsker å finne ut hvor mange kommaer (`,`) som er i denne
tekststrengen: `"A, B, C, D, E, F, G, H, I, J, K, L"`. Du tenker sikkert at
det er enkelt å telle for hånd, men dette er ikke like gøy som å få
datamaskinen til å gjøre det for oss. Til dette kan vi bruke `s.count()`.

```python
>>> s = "A, B, C, D, E, F, G, H, I, J, K, L"
>>> s.count(",")
11
```

Vi kan også telle lengre substrenger, for eksempel `"Per"`:

```python
>>> s = "Per, Ada, Kim, Per, Kim, Per"
>>> s.count("Per")
3
```


<!--Workaround-->
# {.check}

Du skal nå skrive et lite program som teller hvor mange ord det er i
tekststrengen brukeren skriver inn. Dette kan vi løse ved å telle hvor mange
mellomrom (`" "`) det er, også legge til `1`. Forstår du hvorfor det er slik?

Slik skal programmet fungere:

<pre>
>>>
Skriv inn en tekststreng: <font color="green">Hei på deg</font>
Du skrev inn 3 ord.
</pre>

Dette må du gjøre:

 * Be brukeren om en tekststreng.
 * Lagre tekstrengen i en variabel.
 * Lagre antall mellomrom i en variabel.
 * Legg til `1` til mellomroms-variabelen.
 * Skriv ut en tekst til brukeren som forteller hvor mange ord det er.

    **Hint:** husk å konvertere fra tall til tekst med `str()`-funksjonen.
