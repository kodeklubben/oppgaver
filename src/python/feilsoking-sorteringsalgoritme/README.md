---
title: "Feilsøking: Sorteringsalgoritme"
author: "Øyvind Stengrundet, Carl A. Myrland"
language: "nb"
---


# Om oppgaven {.activity}

I denne oppgaven skal elevene lese Python-kode som inneholder feil, identifisere feilene og fikse dem. Når det er gjort, kan de utvide og forbedre sorteringsalgoritmen

## Oppgaven passer til: {.check}

 **Fag**: Matematikk, Programmering

**Anbefalte trinn**: 8.-13. klasse

**Tema**: Fikse feil

**Tidsbruk**: 1 skoletime

## Kompetansemål {.challenge}

**Matematikk, 8. årstrinn**:
- [ ] utforske korleis algoritmar kan skapast, testast og forbetrast ved hjelp av programmering


## Forslag til læringsmål {.challenge}

- [ ] Elevene kan lese og vurdere enkel Python-kode og identifisere og rette opp enkle syntaksfeil.
- [ ] Elevene kan med utvikle og forbedre en eksisterende algoritme.

## Forslag til vurderingskriterier {.challenge}

Det er mange ulike måter man kan vurdere et programmeringsprosjekt, og her må en
selv vurdere hva som er den beste måten ut ifra hvilket fag man jobber i,
hvilken aldergruppe og hviklet nivå elevene er på, hva man ønsker å teste og
hvor mye tid man har til rådighet til å jobbe med prosjektet. I vårt
[lærerdokument](https://github.com/kodeklubben/oppgaver/wiki/Hvordan-undervise-i-og-vurdere-programmering){target=_blank} har vi blant
annet beskrevet ulike måter dette kan gjøres på, tillegg til en del andre
nyttige tips til hvordan man underviser i programmering.

## Forutsetninger og utstyr {.challenge}

**Forutsetninger**:
- [ ] Elevene bør ha kodet i Python før og ha en viss kjennskap til syntaksen.

**Utstyr**:
- [ ] PC/læringsbrett med enten IDLE, Thonny, Anaconda eller andre editorer installert, eller [repl.it](https://repl.it/){target=_blank}

# Fasit {.activity}

Slik skal koden i oppgave 1 se ut når den er ferdig feilrettet.

```python
# Et program for å sortere 4 navn etter lengde
navn = []      # Definerer 'navn' som en tom liste
x = 1      # Sier at det skal skje en forandring
for t in range(1,5):      # Gjentar løkken 4 ganger
    svar = input("Legg til et navn: ")       # Ber om et navn
    navn.append(svar)      # Legger navnet til i listen 'navn'.
while x == 1:      # Gjentar løkken så lenge det gjøres forandringer
    for s in range(4):       # Gjentas 4 ganger, en gang for hvert navn
        x = 0      # Sier at det ikke er gjort noen forandringer inne i løkken ennå
        for t in range(3):      # Gjenta 3 ganger, for å kunne flytte lange navn oppover i lista
           if len(navn[t]) < len(navn[t+1]):      # Flytt lange navn fremover i lista
              bytte = navn[t]      # Legger det første navnet i en tom variabel
              navn[t] = navn[t+1]      # Gjør det første navnet likt som det andre
              navn[t+1] = bytte      # Lar det andre navnet bli likt som det første var
              x = 1      # Sier at det er gjort en forandring
print("Navnene sortert etter lengde:" , navn)      # Skriver ut hele lista
```

## Variasjoner {.challenge}

- [ ]  *Vi har dessverre ikke noen variasjoner tilknyttet denne oppgaven enda.*

## Eksterne ressurser {.challenge}

- [ ] Foreløpig ingen eksterne ressurser ...
