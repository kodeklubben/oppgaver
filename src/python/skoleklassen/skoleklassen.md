---
title: Skoleklassen
level: 2
author: Vegard Bjerkli Bugge
---

# Introduksjon {.intro}

I denne oppgave skal vi bruke en funksjon kalt `list.count(element)`, det vil si at hvis du i et program definerer en liste til å være variabelen `liste`, så kan vi skrive `liste.count(1)` for å finne ut hvor mange ganger heltallet 1 forekommer i listen `liste`.

# Eksempel {.activity}

```python
>>> liste = ['a','b','b','a','c','a','b','c','c','c','b','a','a','a','a','b','b','c','a','b','b','a','a','c','a','a','b','a','c','a']
>>> liste.count('a')
14
>>> liste.count('b')
9
>>> liste.count('c')
7
>>> liste.count('d')
0
```

I de to oppgavene som følger skal du arbeide i med en Python-fil laget på forhånd. Den inneholder nødvendige variable for å fullføre oppgavene. Fila kan lastes ned [her](./skoleklassen.py).

# Oppgave 1 {.activity}
Frøken Fjerding er klasseforstander for en stor skoleklasse. Enkelte av barna har like fornavn. Frøken Fjerding vil vite hvor mange elever det er som har samme navn. Skriv ferdig funksjonen `antallEleverMedSammeNavn(navn)`. Under `main()`-funksjonen er det skrevet kode som tar inn en tekst fra kommandolinjen. Funksjonen sender denne strengen inn i funksjonen du skriver, og printer deretter ut det tallet funksjonen returnerer.

Kjør programmet. Hvor mange elever i klassen til Frøken Fjerding heter Petra?

# Oppgave 2 {.activity}
Hvordan kan vi finne ut hvilket navn som flest elever i klassen har? Skriv en funksjon `mestPopulareNavn(liste)` som går igjennom listen `liste` og returnerer elementet i listen som forekommer flest ganger i en egen liste. Hvis det er flere elementer som forekommer like mange ganger, skal alle returneres i samme liste. Skriv funksjonen inn i samme fil som du har har gjort oppgave 1 i. For å unngå å bruke en egen liste til å telle med, kan du bruke `liste.count(element)`. Sørg for at `main()`-funksjonen står sist i programmet.

Kjør programmet. Hvilket navn er mest typisk i Frøken Fjerdings klasse?
