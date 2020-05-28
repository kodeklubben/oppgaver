---
title: Rekne med løkker
author: Tjerand Silde
translator: Stein Olav Romslo
language: nn
---


# Introduksjon

Ein ting menneske ikkje er så flinke til, men som datamaskiner er ekspertar på,
er å gjenta noko mange gonger etter kvarandre. I Python kan me gjere det med
løkker, og snart skal du sjå at det kan spare oss for mykje tid og skriving.


# Hello World! {.activity}

La oss ta eit døme der me vil ha Python til å seie **Hei!** 100 gonger.
Sjølvsagt kan du setje i gang med å skrive:

```python
print("Hello World!")
print("Hello World!")
print("Hello World!")
...
```

Som du forstår vil det ta lang tid. Programmerarar vil gjerne løyse oppgåva så
enkelt som mogleg, og difor har ein funne opp løkker som kan gjere det for oss!
Koden under løyser problemet me skulle løyse på berre to linjer:

```python
for i in range(100):
    print(i, "Hello World!")
```

Lurt, ikkje sant?


# Range() {.protip}

Når me skal jobbe med løkker i Python er `range`-funksjonen svært nyttig. Når du
skriv `range(10)` får du ei liste med tala 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. Range
kan òg ta fleire parametrar. Skriv du `range(4, 6)`, får du ei liste med tala
frå 4 til (men ikkje med) 6, og viss du skriv `range(6, 4, -1)` får du dei same
tala i motsett rekkefølgje.


# Telje til 10 {.activity}

Bruk ei for-løkke til å skrive ut alle tala mellom 0 og 10.


# Liftoff {.activity}

- [ ] Bruk ei for-løkke og range-funksjonen til å telje ned frå 10. Når du kjem
  til 0 skal programmet skrive **liftoff!**

![Bilete av program som teljer ned til liftoff](liftoff.png)


# Summere 100 tal {.activity}

Eit vanleg problem i matematikk er å summere ei følgje med tal. Dette er veldig
lett når ein kan å programmere! Lag ei for-løkke som går frå 0 til 100, som legg
saman alle tala før den skriv ut resultatet. Svaret skal bli 5050.


# Summere n tal {.activity}

- [ ] Lag ein funksjon `summer(n)`, som tek inn ein parameter og returnerer
  summen av alle tala frå 0 til og med `n`. Definer funksjonen slik:

```python
def summer(n):
    summert = 0
    # Din kode
    return summert
```

Når koden din er rett skal den fungere slik som dette:

![Bilete av summering av talfølgjer med Python](summer.png)
