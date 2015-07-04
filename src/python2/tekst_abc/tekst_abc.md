---
title: Tekst ABC
level: 1
author: Ole Kristian Pedersen, Kodeklubben Trondheim
---

# Introduksjon {.intro}

I denne oppgaven skal vi gjøre enkle operasjoner på tekst, som å endre
størrelsen på bokstavene og telle ord.

I Python lagrer vi tekst til en **variabel** slik som dette:

```python
streng = "teksten er her"
```

Variabelen kalles da **tekststreng** eller bare **streng**, som er typen til
variabelen.

# Store og små bokstaver {.activity}

## {.protip}

En måte å endre tekst på er ved hjelp av funksjoner. Innebygget i Python finnes
flere slike funksjoner. Gitt at vi har tekst i en variabel kalt `s`, så kan vi
bruke disse funksjonene: `s.lower()`, `s.upper()`, `s.title()`, `s.swapcase()`
og `s.capitalize()`.

Legg merke til at funksjonen kalles **på** strengen - `s.lower()` - istedenfor
å **gi** strengen til funksjonen - `lower(s)`.


Her er noen eksempler på hvordan funksjonene brukes (legg merke til hvilke
bokstaver som er store og små i utskriften):

```python
>>> s = "Per og Ada"
>>> s.upper()        # store bokstaver
'PER OG ADA'
>>> s.lower()        # små bokstaver
'per og ada'
>>> s.capitalize()   # første bokstav er stor
'Per og ada'
>>> s.title()        # første bokstav i hvert ord er stor
'Per Og Ada'
>>> s.swapcase()     # bytter stor og små
'pER oG aDA'
```

Her er noen eksempler på hva funksjonene kan brukes til:

* `s.capitalize()` brukes når vi ønsker stor forbokstav kun i begynnelsen av teksten:

    ```python
    >>> sentence = "dENne sETNinGeN har IKKE riKTige bokSTAVstØrReLSER."
    >>> sentence.capitalize()
    'Denne setningen har ikke riktige bokstavstørrelser.'
    ```
* `s.title()` kan brukes når vi skal skrive filmtitler:

    ```python
    >>> movie_title = "star wars: a new hope"
    >>> movie_title.title()
    'Star Wars: A New Hope'
    ```

* `s.upper()` og `s.lower()` kan brukes når vi ønsker å sammenlikne tekst uten
  å ta hensyn størrelsen på bokstavene:

    ```python
    >>> answer = "JA"
    >>> answer == "ja"  # JA og ja er ikke lik
    False
    ```

    ```python
    >>> answer = "JA"
    >>> answer.lower() == "ja"  # konverter JA til ja for testen
    True
    ```

Du må huske på at disse funksjonene **ikke** endrer på variabelen. Derfor må du
lagre resultatet i en ny variabel om du vil beholde endringen din:

```python
>>> s = "tekst"
>>> s.upper()  # Vi endrer ikke på variabelen!!
'TEKST'
>>> s  # Fremdeles små bokstaver
'tekst'
>>> s = s.upper()  # Nå endrer vi på variabelen
>>> s  # Denne gangen er det store bokstaver
'TEKST'
```

<!--Workaround-->
# {.check}

Lag et program som skriver ut filmtitler med store bokstaver først i hvert ord.

Programmet skal se slik ut:

<pre>
>>>
Skriv inn en filmtittel: <font color="green">alice in wonderland</font>
Alice In Wonderland
</pre>

Dette må du gjøre:

 * Be om at brukeren skriver inn en filmtittel.
 * Lagre filmtittelen i en variabel.
 * Manipuler strengen slik at resultatet blir som beskrevet over.
 * Skriv ut den nye strengen.


# Telling av tekst {.activity}

# {.protip}

Ved hjelp av `s.count()` kan vi finne ut om en streng inneholder en bestemt
tekst og hvor mange ganger den finnes i strengen. For eksempel så inneholder
strengen `"Hei verden!"` teksten `"verden"` en gang.

Tenk deg at du ønsker å finne ut hvor mange kommaer som er i `"A, B, C, D, E,
F, G, H, I, J, K, L"`. Det er enkelt å telle for hånd, men ikke like gøy som å
la datamaskinen gjøre det:

```python
>>> s = "A, B, C, D, E, F, G, H, I, J, K, L"
>>> s.count(",")
11
```

Vi kan også telle tekst som er lengre, for eksempel `"Per"`:

```python
>>> s = "Per, Ada, Kim, Per, Kim, Per"
>>> s.count("Per")
3
```


<!--Workaround-->
# {.check}

Lag et program som teller hvor mange ord det er i det brukeren skriver inn.
Antall ord kan regnes ut ved å telle antall mellomrom, og deretter legge til 1.
Forstår du hvorfor man må legge til 1?

Slik skal programmet se ut:

<pre>
>>>
Skriv inn en streng: <font color="green">Hei på deg</font>
Du skrev inn 3 ord.
</pre>

Dette må du gjøre:

 * Be brukeren om tekst.
 * Lagre teksten til en variabel.
 * Regn ut hvor mange ord som er i teksten.
 * Skriv ut hvor mange ord teksten inneholder.

    **Hint:** husk å konvertere fra tall til tekst med `str()`-funksjonen.
