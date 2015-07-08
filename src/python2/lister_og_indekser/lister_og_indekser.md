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

`lst.append(elm)` legger til `elm` på slutten av `lst`, slik som illustrert i
eksempelet:

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

`lst.remove(elm)` sletter det første elementet `elm` fra `lst`. Det vil si at
dersom `elm` ligger flere ganger i `lst` slettes bare det første elementet lik
`elm`:

```python
>>> lst = ['Per', 'Ada', 'Ada', 'Kim']
>>> lst.remove("Ada")
>>> lst
['Per', 'Ada', 'Kim']
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
men noen ganger kan det være praktisk også å kunne bruke indeksen til
elementet. Til dette kan vi bruke `enumerate()`, som gir oss både verdien og
indeksen:

```python
>>> lst = ['Per', 'Kim', 'Ada']
>>> for i, value in enumerate(lst):
        print(str(i) + " " + value)

0 Per
1 Kim
2 Ada
```

I eksempelet over får `i` verdien av indeksen, og `value` får verdien av
elementet. Det er nesten som ei vanlig `for`-løkke, men vi får indeksen i
tillegg.

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
 * Endre på løkka slik at du skriver ut indeksen og gjenstanden som i
   eksempelet.

## Indekstrening {.challenge}

Vi vil nå la brukeren selv velge hvor mange gjenstander som skal skrives ut.
Slik som i eksempelet:

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

Dette må du gjøre:

 * Skriv et program som likner på det du gjorde i forrige oppgave.
 * Etter at du er ferdig med å legge til gjenstander i lista, spør brukeren om
   hvor mange gjenstander som skal skrives ut.
 * Skriv ut antallet gjenstander brukeren ber om.

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

    **Hint:** Hvordan kan du sjekke om et tall er partall eller oddetall?

