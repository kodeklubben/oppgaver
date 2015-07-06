---
title: Lister og indekser
level: 2
author: Ole Kristian Pedersen, Kodeklubben Trondheim
---

# Introduksjon {.intro}

I denne oppgaven skal vi lære å bruke lister - et kjempeviktig verktøy for
programmerere. Ettersom lister er tett knyttet med løkker i Python, bør
du være sikker på at du husker løkker før du begynner på denne oppgaven.
Hvis du ikke husker løkker, eller er usikker, kan du gå tilbake til
[repetisjonsoppgaven om løkker](../repetisjon/repetisjon.html#løkker).

# Lag ei liste! {.activity}

# {.protip}

Vi har tidligere i kurset brukt lister, og har lagd lister ved å skrive
elementene mellom `[` og `]` med et komma mellom hvert element. Slik:

```python
>>> lst = ['egg', 'ham', 'spam']
>>> lst
['egg', 'ham', 'spam']
```

Vi har nå en liste som inneholder ordene `'egg'`, `'ham'` og `'spam'`.
Vanskeligere er det ikke! Vi kan også lage tomme lister:

```python
>>> lst = []
>>> lst
[]
```

Ei liste kan inneholde alt mulig - tall, strenger og også andre lister:

```python
>>> lst = [ 3, 'komma', [1 , 4] ]
>>> lst
[3, 'komma', [1, 4]]
```


# Legge til og fjerne elementer {.activity}

# {.protip}

Hva om vi ønsker å legge til eller fjerne elementene fra lista vi vår? Vi skal
lære om to funksjoner for å gjøre dette - `lst.append(elm)` og `lst.remove(elm)`, der
`lst` er lista og `elm` er elementet vi ønsker å legge til eller fjerne.

I det følgende eksempelet ser vi hvordan 'lst.append(elm)' fungerer:

```python
>>> lst = []
>>> lst.append('Per')
>>> lst
['Per']
>>> lst.append('Ada')
>>> lst.append('Kim')
>>> lst
['Per', 'Ada', 'Kim']
```

Og her ser vi hvordan `lst.remove(elm)` fungerer:

```python
>>> lst = ['Per', 'Ada', 'Kim']
>>> lst.remove("Kim")
>>> lst
['Per', 'Ada']
```

# {.check}

Vi har lyst til å skrive et handleliste-program som lar brukeren skrive inn
matvarer helt til `'skriv ut'` skrives inn. Da skal programmet skrive ut
gjenstandene i lista. Programmet kan fungere slik:

<pre>
>>>
Skriv inn en gjenstand: <font color="green">ost</font>
Skriv inn en gjenstand: <font color="green">melk</font>
Skriv inn en gjenstand: <font color="green">brød</font>
Skriv inn en gjenstand: <font color="green">skriv ut</font>
ost
melk
brød
</pre>

Dette må du gjøre:

 * Lag ei tom liste
 * Så lenge brukeren ikke skriver inn `'skriv ut'`, legg til det nye elementet
   i lista

     **Hint:** Hva slags løkke kan vi bruke her?

 * Skriv ut hvert hvert element i lista

    **Hint:** Hva slags løkke kan vi bruke her?

# Indekser {.activity}

# {.protip}

Tenk deg at vi har ei liste, og ønsker å hente ut det andre elementet i lista.
Hvordan skal vi klare det?  Da bruker vi indekser. Da bruker vi `[` og `]` med
et tall mellom. Slik:

```python
>>> lst = [1, 2, 3, 4, 5]
>>> lst[1]
2
```

Du la kanskje merke til at vi skrev `1`, men fikk ut det andre elementet i
lista? Det er fordi vi begynner å telle fra `0`. Dermed har det første
elementet i lista indeks `0`, og det andre har indeks `1`. Datamaskiner
begynner å telle på null! Du husker kanskje at det samme skjer når vi bruker `range()`?

```python
>>> list(range(5))
[0, 1, 2, 3, 4]
```

Til nå har vi brukt `for element in lst` for å gå igjennom elementene i lista,
men noen ganger kan det være praktisk å bruke indekser til det samme. Da bruker
vi `range()` og `len()`. Husk at `len()` returnerer lengden til lista. De to
følgende kodesnuttene gjør akkurat det samme:

```python
lst = ['Per', 'Kim', 'Ada']
for element in lst:
    print(element)
```

```python
lst = ['Per', 'Kim', 'Ada']
for i in range(len(lst))
    print(lst[i])
```

# {.check}

Nå vil vi modifisere programmet fra forrige oppgave og skrive ut indekser ved
siden gjenstandene i handlelista. Slik kan det fungere:

<pre>
>>>
Skriv inn en gjenstand: <font color="green">ost</font>
Skriv inn en gjenstand: <font color="green">melk</font>
Skriv inn en gjenstand: <font color="green">brød</font>
Skriv inn en gjenstand: <font color="green">skriv ut</font>
0 ost
1 melk
2 brød
</pre>

Dette må du gjøre:

 * Skriv et program som likner på det du skrev i forrige oppgave
 * Endre på løkka slik at du skriver ut det samme som i eksempelet.

## Indekstrening {.challenge}

Vi vil nå la brukeren selv velge hvor mange gjenstander som skal skrives ut,
men vi må passe på at brukeren ikke skriver inn for høye eller lave tall.
Dersom brukeren skriver ut negative tall skal du skrive ut `"Feil!"` og
avslutte programmet. Hvis brukeren skriver ut et for høyt tall skal du skrive
ut alle gjenstandene i lista.

Her er noen eksempler:

<pre>
>>>
Skriv inn en gjenstand: <font color="green">ost</font>
Skriv inn en gjenstand: <font color="green">melk</font>
Skriv inn en gjenstand: <font color="green">brød</font>
Skriv inn en gjenstand: <font color="green">skriv ut</font>
Hvor mange gjenstander vil du skrive ut? <font color="green">2</font>
0 ost
1 melk
</pre>

<pre>
>>>
Skriv inn en gjenstand: <font color="green">ost</font>
Skriv inn en gjenstand: <font color="green">melk</font>
Skriv inn en gjenstand: <font color="green">brød</font>
Skriv inn en gjenstand: <font color="green">skriv ut</font>
Hvor mange gjenstander vil du skrive ut? <font color="green">6</font>
0 ost
1 melk
2 brød
</pre>

<pre>
>>>
Skriv inn en gjenstand: <font color="green">ost</font>
Skriv inn en gjenstand: <font color="green">melk</font>
Skriv inn en gjenstand: <font color="green">brød</font>
Skriv inn en gjenstand: <font color="green">skriv ut</font>
Hvor mange gjenstander vil du skrive ut? <font color="green">-1</font>
Feil!
</pre>

Dette må du gjøre:

 * Skriv et program som likner på det du gjorde i forrige oppgave.
 * Etter at du er ferdig med å legge til gjenstander i lista, spør brukeren om
   hvor mange gjenstander som skal skrives ut.
 * Dersom tallet er for lavt eller høyt, gjør som beskrevet i oppgaveteksten
 * Ellers, skriv ut antallet gjenstander brukeren ber om.
 * Test at programmet fungerer slik som i eksemplene.

# Strenger og indekser {.activity}

# {.protip}

Vi kan også bruke indekser på strenger. Koden for dette ser helt lik ut:

```python
>>> s = "Ada"
>>> s[0]
'A'
```

# {.check}

Vi vil skrive et program som henter input fra brukeren, og skriver ut annenhver
bokstav. Det kan fungere som dette:

<pre>
>>>
Skriv inn en setning: <font color="green">Hei på deg!</font>
H
i
p

e
!
</pre>

Dette må du gjøre:

 * Hent input fra brukeren
 * Bruk en løkke for å skrive ut annenhver bokstav
   **Hint:** Hvordan kan du gå igjennom alle partallsindeksene?

