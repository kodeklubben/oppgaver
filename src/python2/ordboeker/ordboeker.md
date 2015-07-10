---
level: 2
title: Ordbøker
author: Ole Kristian Pedersen, Kodeklubben Trondheim
---

# Introduksjon {.intro}

Dette er en kort oppgave der vi skal lære litt om ordbøker, og hva disse kan
brukes til.

# Nøkler og verdier {.activity}

## {.protip}

En ordbok, på engelsk *dictionary*, brukes for å lagre nøkkel/verdi-par.
Tenk deg at du skal ha en norsk-engelsk ordbok. Da vi nøkkelen være ordet du
slår opp på, altså det norske ordet. Verdien vil være det engelske ordet.
F.eks. kan `"ost"` være en nøkkel, mens `"cheese"` vil være den tilhørende
verdien.

```python
>>> d = {'ost':'cheese', 'brød':'bread'}
>>> d
{'ost': 'cheese', 'brød': 'bread'}
```

I eksempelet over lagde vi en norsk-engelsk ordbok. Nøklene og verdiene har
et kolon (`:`) mellom seg, mens nøkkel/verdi-parene skilles med komma. For å
slå opp på en nøkkel, bruker vi `[` og `]`, slik som dette:

```python
>>> d = {'ost':'cheese', 'brød':'bread'}
>>> d['ost']
'cheese'
```

Vi kan bruke den samme skrivemåten for å lage nye nøkkel/verdi-par eller endre
verdien knyttet til en nøkkel:

```python
>>> d = {'ost':'cheese', 'brød':'bread'}
>>> d['farge'] = 'colour'    # Her legger vi til en ny verdi
>>> d
{'ost': 'cheese', 'brød': 'bread', 'farge': 'colour'}
>>> d['farge'] = 'color'     # Her endrer vi verdien
>>> d
{'ost': 'cheese', 'brød': 'bread', 'farge': 'color'}

En tom ordbok opprettes slik:
```

```python
>>> d = {}
>>> d
{}
```

Det trenger ikke bare strenger som nøkler og verdier - du kan bruke både tall
og strenger som nøkler og hva som helst (strenger, tall, funksjoner, lister,
ordbøker, ...) som verdier. Dette kan du for eksempel bruke til å lage en handleliste.

# {.check}

Vi ønsker å skrive et program som lar en bruker skrive inn 3 nøkkel/verdi-par,
før brukeren så skriver inn en nøkkel og får ut den tilhørende verdien. Det kan fungere slik:

<pre>
Skriv inn en nøkkel: <font color="green">ost</font>
Skriv inn en verdi: <font color="green">cheese</font>
Skriv inn en nøkkel: <font color="green">brød</font>
Skriv inn en verdi: <font color="green">bread</font>
Skriv inn en nøkkel: <font color="green">farge</font>
Skriv inn en verdi: <font color="green">color</font>
Hvilken nøkkel vil du slå opp på? <font color="green">brød</font>
Tilhørende verdi er bread
</pre>

Dette må du gjøre:

 * Lag ei tom ordbok
 * Bruk ei løkke for å hente inn 3 nøkkel/verdi-par

    * Lagre nøkkel/verdi-parene i ordboka

 * Spør om en nøkkel, og skriv ut den tilhørende verdien


# Gå igjennom ordbøker {.activity}

## {.protip}

Du kan hente ut nøklene i en ordbøker ved å bruke `d.keys()`, og verdiene ved å
bruke `d.values()`. Disse kan gås igjennom med en `for`-løkke:

```python
>>> d = {'brød': 3, 'ost': 1}
>>> for key in d.keys():
        print("Nøkkel: " + key + ", verdi: " + d[key])
Nøkkel: brød, verdi: 3
Nøkkel: ost, verdi: 1
```

Vi kan iterere gjennom `d.values()` på samme måte.

# {.check}

Vi ønsker å skrive et nytt handleliste-program som lar brukeren velge hvor
mange av hver gjenstand som skal stå på lista. Dette kan se slik ut:

<pre>
Skriv en gjenstand: <font color="green">brød</font>
Hvor mange? <font color="green">2</font>
Skriv en gjenstand: <font color="green">tomat</font>
Hvor mange? <font color="green">5</font>
Skriv en gjenstand:
Her er handlelista:
2 brød
5 tomat
</pre>

Dette må du gjøre:

* Så lenge brukeren ikke skriver inn en tom streng (`""`)
* Ta inn en gjenstand, og et antall som lagres i handlelista
* Skriv ut handlelista som i eksempelet

    **Hint:** Gå  igjennom nøklene.
