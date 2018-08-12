---
title: Lærerveiledning - Huskespill
author: Øistein Søvik
language: nb
---


# Om oppgaven {.activity}

I denne oppgaven skal du lage et huskespill hvor spilleren skal huske flest
mulig ord i riktig rekkefølge.

## Oppgaven passer til: {.check}

__Fag__: Programmering, Engelsk

__Anbefalte trinn__: 7.-10. trinn

__Tema__: Lister, brukerinteraksjon, if-setninger, spill, while-løkker

__Tidsbruk__: Dobbelttime

## Kompetansemål {.challenge}

- [ ] __Engelsk, 4. trinn__: forstå og bruke engelske ord, uttrykk og
  setningsmønstre knyttet til egne behov og følelser, dagligliv, fritid og
  interesser

- [ ] __Programmering, 10. trinn__: bruke flere programmeringsspråk der minst
  ett er tekstbasert

- [ ] __Programmering, 10. trinn__: bruke grunnleggende prinsipper i
  programmering, slik som løkker, tester, variabler, funksjoner og enkel
  brukerinteraksjon

- [ ] __Programmering, 10. trinn__: omgjøre problemer til konkrete delproblemer,
  vurdere hvilke delproblemer som lar seg løse digitalt, og utforme løsninger
  for disse

## Forslag til læringsmål {.challenge}

- [ ] Klarer å gjøre om innputt fra brukeren til en liste

- [ ] Klarer å gjøre grunnleggene operasjoner på lister: legge til elementer,
  hente ut elementer, lese innholdet i listen.

## Forslag til vurderingskriterier {.challenge}

- [ ] Eleven viser middels måloppnåelse ved å fullføre oppgaven.

- [ ] Eleven viser høy måloppnåelse ved å videreutvikle egen kode basert på
  oppgaven, for eksempel ved å gjøre en eller flere av variasjonene nedenfor.

## Forutsetninger og utstyr {.challenge}

- [ ] __Forutsetninger__: Grunnleggende kjennskap til while-løkker,
  if-setninger, variabler og å ha skrevet en del Python-kode tidligere.

- [ ] __Utstyr__: Datamaskin med Python installert.


# Fremgangsmåte

Her kommer tips, erfaring og utfordringer til de ulike stegene i den faktiske
oppgaven. [Klikk her for å se
oppgaveteksten.](../huskespill/huskespill.html){target=_blank}

- [ ] Når en skal huske ord fra listen, er det en fordel at en har tømt skjermen
  for innhold, ellers blir jo oppgaven triviell! En løsning er å legge på mange
  linjer f.eks

```python
print(liste_med_ord)
for _ in range(1,100):
    print()
text = input('Skriv inn ordene du husker fra listen: ')
```

Alternativt kan dette og gjøres uten en for-løkke, ved å heller skrive
`print(100*'\n')`. Denne koden vil og skrive ut hundre tomme linjer til
skjermen, hvor `\n` betyr linjeskift. Problemet med metoden ovenfor er at det er
vanskelig å vite hvor mange linjer som er nødvendig, er hundre for mye eller for
lite? Hvis en har en stor skjerm trengs det nødvendigvis flere tomme linjer. Som
du kanskje vet går det ann å tømme skjermen manuelt ved å bruke `CTRL+L`, går
det ann å bruke i koden vår? Det gjør det faktisk om en bruker `system os`
biblioteket som koden under illustrerer

```python
import os

print(liste_med_ord)
os.system('cls')
text = input('Skriv inn ordene du husker fra listen: ')
```

Dette er nok den "beste" metoden å tømme skjermen på, men bør nok bare nevnes
for de mest ivrige elevene.Det er verdt å merke seg at dersom noen av elevene
bruker Linux, så må `cls` erstattes med `clear`.

## Variasjoner {.challenge}

- [ ] Denne oppgaven kan tilpasses de fleste fag. Det enkleste er å enten be
  elevene bruke ord fra en spesiell liste. For eksempel fargenavn på fransk,
  gloser på engelsk, navn på planeter, eller navn på ulike deler av
  menneskekroppen.

## Eksterne ressurser {.challenge}

- [ ] Foreløpig ingen eksterne ressurser
