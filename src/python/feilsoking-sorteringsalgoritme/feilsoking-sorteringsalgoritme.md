---
title: "Feilsøking: Sorteringsalgoritme"
author: "Øyvind Stengrundet, Carl A. Myrland" 
language: 
---


# Introduksjon {.intro}


Å kunne lete opp feil og rette på dem er helt grunnleggende når det gjelder programmering. Selv om man er aldri så nøyaktig og flittig, vil det nesten alltid dukke opp små feil i programkoden på et eller annet tidspunkt. Det kan være et punktum i stedet for et komma, det kan være en parentes for lite eller for mye, eller det kan være en stor bokstav eller et innrykk som er feil plassert.


# Steg 1: Les og analyser koden {.activity}

I koden nedenfor er det 5 feil. Prøv å lese deg frem til feilene her først. Så kan skrive inn koden i editoren din, og rette opp feilene der. Virker programmet nå?

```python
# Et program for å sortere 4 navn etter lengde
navn = []      # Definerer 'navn' som en tom liste
x = 1      # Sier at det skal skje en forandring
for t in range(1,5):      # Gjentar løkken 4 ganger
    svar = input("Legg til et navn: "       # Ber om et navn
    navn.append(svar)       Legger navnet til i listen 'navn'.
while x == 1:      # Gjentar løkken så lenge det gjøres forandringer
    for s in range(4):       # Gjentas 4 ganger, en gang for hvert navn
        x = 0      # Sier at det ikke er gjort noen forandringer inne i løkken ennå
        for t in range(3)      # Gjenta 3 ganger, for å kunne flytte lange navn oppover i lista
           if len(navn[t]) < len(navn[t+1]):      # Flytt lange navn fremover i lista
              bytte = navn[t]      # Legger det første navnet i en tom variabel
              navn[t) = navn[t+1]      # Gjør det første navnet likt som det andre
              navn[t+1] = bytte      # Lar det andre navnet bli likt som det første var
              x = 1      # Sier at det er gjort en forandring
print(Navnene sortert etter lengde:" , navn)      # Skriver ut hele lista
```

## Sjekkliste {.check}

- [ ] Les gjennom koden. Finner du noen umiddelbare feil?

- [ ] Kopier koden over i editoren du bruker.

- [ ] Det kan være lurt å rydde litt før du begynner. Bruk tab eller linjeskift for å få litt mer system på kommentarene.

## Test prosjektet {.flag}

**Klikk på det grønne flagget.** / **Start prosjektet for å teste koden så
langt.**

- [ ] Fungerer koden?

- [ ] Forteller editoren din deg hva som eventuelt er feil?

- [ ] Forstår du hvorfor dette skjer?

# Steg 2: Fiks alle feilene! {.activity}
#

## Sjekkliste {.check}

- [ ] Les koden nøye på nytt og rett opp de feilene du finner.
- [ ] Kjør programmet på nytt. Funker det nå?

- [ ] Gjenta disse punktene til alle feilene er rettet!


## Utfordring {.challenge}

- [ ] Gjør om programmet slik at det skriver ut de korteste navnene først. 
- [ ] Prøv også om du kan programmet til å skrive ut ett og ett navn, under hverandre.