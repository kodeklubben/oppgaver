---
title: Bondegården
level: 4
author: Vegard Bjerkli Bugge
---

# Introduksjon {.intro}

Hensikten med denne oppgaven er å kombinere det vi har lært om ordbøker, løkker og if-setninger slik at vi kan løse vanskeligere og mer komplekse problemstillinger. For å løse oppgaven kan vi kalle på en metode i **dictionary** som kalles for *values()*. En metode er en funksjon skrevet inni en klasse som vi kaller på ved først å skrive variabelnavnet til for eksempel ordboka, etterfulgt av punktum og deretter navnet på funksjonen samt tilhørende argumenter omringet av paranteser.

# Oppgave {.activity}

Budeie-Barbi og Bottolf Bonde driver en bondegård på Hofstad i Roan kommune. Til tross for at de har drevet gård helt siden de flyttet hit fra Trondheim i 1997 har de ENNÅ ikke bestemt seg for om de vil drive sauedrift eller melkeproduksjon, så de holder både kyr, sauer, og til og med et par griser i en og samme store innhegning.

Det lokale bondelaget har sett seg lei av denne ineffektive måten å holde husdyr på, og har derfor forlanget av Bottolf og Budeie-Barbi at de skiller dyra sine inn i forskjellige innhegninger, og for å gjøre vondt verre krever de at alle kyr og sauer skal skilles inn i totalt seks forskjellige innhegninger, to for hanndyra (vær og okser), to for hodyra (kyr og søyer) og to for barna (kalver og lam). De har ikke sagt noe om å skille mellom kjønna på grisene, men så er det jo heller ingen i bondelaget som vet at Bonde - paret holder griser også, så grisene kan være igjen i den store innhegningen. Kan du hjelpe Bottolf og Budeie-Barbi med å sortere ut sauene, oksene og kyrne?

I denne oppgaven får du oppgitt en ordbok (på engelsk "dictionary") med alle dyra til bøndene. Ordboka heter for -innhegning-, og finnes i ei fil som du kan laste ned [her](./bondegaard.py). Lagre den der du pleier å lagre Python-koden din. I denne ordboka kan man gjøre oppslag på dyrets navn, som er en streng. Som verdi angis hva slags dyr det er, som også er en streng. Samtlige navn i ordboka er unike. Når du lager en ordbok i Python 3 vil Python til enhver tid sørge for at alle nøklene (variabler eller strenger du slår opp på i ordboka) har unike navn, for å unngå forvirring. I den importerte ordboka ser hvert enkelt element slik ut:

```python
{ "navn" : "dyretype" }
```

Du skal skrive en funksjon som tar inn en streng som sier hvilket dyr vi skal telle opp. Funksjonen skal ta inn enten "Ku", "Okse", "Kalv", "Søye", "Vær", eller "Lam". Skriv der vi har kommentert #SKRIV KODE HER. Ikke endre på kode som omkranses av kommentaren # IKKE ENDRE PÅ DENNE KODEN.

## Tips {.protip}

Gitt ei ordbok `min_ordbok`, så vil metoden values() returnere ei liste av alle verdiene i ordboka. Kodeblokka nedenfor viser funksjoner og teknikker som kan være relevante for koden du skriver.

```python
>>> min_ordbok = {'nøkkel': 'verdi', 'nynøkkel':4, 'tredjenøkkel': False}
>>> l = min_ordbok.values()
>>> l
dict_values(['verdi', False, 4])
>>> t = 0
>>> for v in l:
...     if v == 'verdi': a+=1
>>> t
1
```

## Ekstra spørsmål: Finnes det en liknende metode for å få alle nøklene i ei ordbok returnert i en liste? Prøv selv i kommandolinjen til IDLE.
