---
title: "Bugfiksing: Smelt snømennene!"
author: "Carl A. Myrland" 
translator: "https://scratch.mit.edu/projects/30592006"
language: "nb"
---


# Om oppgaven {.activity}

I denne oppgaven skal elevene lese, feilsøke og forbedre eksisterende kode. Formålet er å lage et lite program der snømennene sier "Klar, ferdig, smelt!" i tur og orden, for så å smelte bort samtidig. Dette forutsetter noe kjennskap til koding fra før, og anbefales først og fremst til elever med kodeerfaring fra ca 6.-/7.-trinn og oppover. Eldre elever på 9.-/10. trinn kan sannsynligvis løse oppgaven uten tidligere kodeerfaring, ved å følge hintene som gis i oppskriften.

Det gis ingen fasit i oppgaveteksten, kun hint og skriftlige instruksjoner. Til slutt i oppgaven viser vi et forslag til ferdig kode for Snømann 1. Du finner løsningsforslag til hvert enkelt steg her i lærerveiledningen.

## Oppgaven passer til: {.check}

 **Fag**: Programmering, Matematikk

**Anbefalte trinn**: 5.-7. klasse, 8.-10. klasse

**Tema**: Animasjon, Blokkbasert

**Tidsbruk**: 1 skoletime

## Kompetansemål {.challenge}

**Matematikk, 8. årstrinn**:
- [ ] utforske korleis algoritmar kan skapast, testast og forbetrast ved hjelp av programmering

## Forslag til læringsmål {.challenge}

- [ ] Elevene kan lese, feilsøke og fikse enkle algoritmer ved å bruke enkle problemløsningsstrategier, alene og sammen med andre.

## Forslag til vurderingskriterier {.challenge}

Det er mange ulike måter man kan vurdere et programmeringsprosjekt, og her må en
selv vurdere hva som er den beste måten ut ifra hvilket fag man jobber i,
hvilken aldergruppe og hviklet nivå elevene er på, hva man ønsker å teste og
hvor mye tid man har til rådighet til å jobbe med prosjektet. I vårt
[lærerdokument](https://github.com/kodeklubben/oppgaver/wiki/Hvordan-undervise-i-og-vurdere-programmering){target=_blank} har vi blant
annet beskrevet ulike måter dette kan gjøres på, tillegg til en del andre
nyttige tips til hvordan man underviser i programmering.

## Forutsetninger og utstyr {.challenge}

- [ ] **Forutsetninger**: Å ha noe programmeringserfaring er en fordel, spesielt for elever på mellomtrinnet.

- [ ] **Utstyr**: Læringsbrett/PC 

## Løsningsforslag

Her følger forslag til hvordan koden bør se ut etter hvert steg i oppgaven. Vær obs på at det finnes flere måter å løse oppgaven på, og spesielt erfarne elever kan finne andre, bedre og mer effektive måter å løse oppgaven på. Spør hva de tenker og hva de ønsker å få til! 

# Steg 1: Remiks oppgaven {.activity}

I Steg 1 skal elevene bare remikse og testkjøre koden sånn den er, og forsøke å finne ut hva som er feil i koden på egenhånd. De bør notere ned eller diskutere det de observerer med en læringspartner.

# Steg 2: Klar, ferdig, smelt! {.activity}

Her må elevene bruke `vent`{.blockcontrol}-funksjonen for å få snømennene til å snakke i tur og orden. Snømann 1 trenger ikke vente, siden han snakker først. Snømann 2 venter i 2 sekunder, siden det er tiden Snømann 1 bruker på å si "Klar". Snømann 3 må vente i fire sekunder, siden Snømann 2 også bruker 2 sekunder på å si "Ferdig".

Koden til Snømann 1 bør ligne på dette:
```blocks
Når grønt flagg klikkes
si [Klar] i (2) sekunder
```
Koden til Snømann 2 bør ligne på dette:
```blocks
Når grønt flagg klikkes
vent (2) sekunder
si [Ferdig] i (2) sekunder
```
Koden til Snømann 3 bør ligne på dette:
```blocks
Når grønt flagg klikkes
vent (4) sekunder
si [Smelt!] i (2) sekunder
```
Øvrige klosser i koden kommer vi tilbake til senere!

# Steg 3: Smelt! {.activity}

Koden til Snømann 1 bør ligne på dette når de er ferdig med dette steget.

```blocks
Når grønt flagg klikkes
sett størrelse til [100]%
si [Klar] i (2) sekunder
gjenta (4) ganger
endre [ghost v] effekt med (25)
vent (1) sekunder
endre størrelse med (-10)
```

# Steg 4: Siste justeringer {.activity}

Koden til Snømann 1 bør se omtrent slik ut:
 
```blocks
Når grønt flagg klikkes
sett størrelse til [100]%
si [Klar] i (2) sekunder
vent (4) sekunder
gjenta (4) ganger
endre [ghost v] effekt med (25)
vent (1) sekunder
endre størrelse med (-10)
```
Koden til Snømann 2 bør se omtrent slik ut:
 
```blocks
Når grønt flagg klikkes
sett størrelse til [100]%
vent (2) sekunder
si [Ferdig] i (2) sekunder
vent (2) sekunder
gjenta (4) ganger
endre [ghost v] effekt med (25)
vent (1) sekunder
endre størrelse med (-10)
```
Koden til Snømann 3 bør se omtrent slik ut:
 
```blocks
Når grønt flagg klikkes
sett størrelse til [100]%
vent (4) sekunder
si [Smelt!] i (2) sekunder
gjenta (4) ganger
endre [ghost v] effekt med (25)
vent (1) sekunder
endre størrelse med (-10)
```

## Variasjoner {.challenge}

- [ ] Elevene kan lage en liten historie eller et spillbart spill ut i fra dette utgangspunktet. De har fått noen tips helt til slutt i oppgaven. 

## Eksterne ressurser {.challenge}

- [ ] Foreløpig ingen eksterne ressurser ...