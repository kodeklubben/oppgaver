---
title: Skoleklassen
level: 4
author: Vegard Bjerkli Bugge
---

# Introduksjon {.intro}

Frøken Fjerding er klasseforstander for en stor skoleklasse. Alle barna har unike fornavn. Frøken Fjerding vil vite hvor mange elever hun underviser av hvert kjønn. Skriv et program som teller opp hvor mange gutter og jenter som går i klassen Frøken Fjerding er kontaktlærer for.

I denne oppgaven får du oppgitt en ordliste som inneholder navnene til alle elevene i skoleklassen. Ordlista heter for -klassensElever-, og finnes i fila pyKodeKlubb_Dictionary_Variabler.  I denne ordlista slår man opp på navnet til en elev, som er lagret som en streng, for å finne hvilket kjønn barnet er, som også errepresentert ved en streng i programmet. Samtlige navn i ordlista er unike. Når du lager en ordliste vil Python til enhver tid sørge for at alle nøklene (variabler eller strenger du slår opp på i ordlista) har unike navn, for å unngå forvirring. I ordlista ser hvert enkelt element slik ut:

```python
#ENTEN
navn : "gutt"
#ELLER
navn : "jente"
```

*navn* viser til navnet til eleven i klassen. Skriv en eller flere linjer kode kun der det står #SKRIV KODE HER .

```python
klassensElever = { "Oskar" : "Gutt", "Thomas" : "Gutt", "Tora" : "Jente", "Eigil" : "Gutt", "Torild" : "Jente", "Isak" : "Gutt", "Erika" : "Jente", "Mari" : "Jente", "Bente" : "Jente", "Werner" : "Gutt", "Nils" : "Gutt", "Ada" : "Jente", "Igor" : "Gutt", "Pelle" : "Gutt", "Kaja" : "Jente", "Ella" : "Jente", "Petra" : "Jente", "Lina" : "Jente", "Silje" : "Jente", "Cecilie" : "Jente", "Kai" : "Gutt", "Trond" : "Gutt", "Anne" : "Jente", "Berit" : "Jente" }

def main():
    antall_gutter = 0 # Denne variabelen holder rede på hvor mange gutter i skoleklassen vi har telt opp
    antall_jenter = 0 # Denne variabelen holder rede på hvor mange jenter i skoleklassen vi har telt opp
    #SKRIV KODE HER
    print ( "Det er " + antall_jenter + " jenter og " + antall_gutter + " gutter i skoleklassen." )

main()
```

Nyttige kunnskaper for oppgaven: Iterasjon/telling, variabler, funksjoner, løkker, moduler, ordlister

## Ekstra spørsmål: Hvorfor er argumentet til print skrivet slik som det er skrivet?
