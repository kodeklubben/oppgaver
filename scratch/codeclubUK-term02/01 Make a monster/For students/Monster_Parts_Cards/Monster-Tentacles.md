---
title: Scratchkort - Tentakler
level: Nivå 4
language: nb-NO
stylesheet: scratch
embeds: "*.png"
materials: "*.sb2"
...

## Sjekkliste { .check}

+ For å få en tentakel til å bevege seg, kan vi **rotere** den og **endre størrelse** ved å bruke `tilfeldig tall`{.blockgreen} med en lav verdi i en variabel, for så å vente et øyeblikk før vi gjenoppretter den originale størrelsen.

```blocks
sett [tentakelRotasjon v] til (tilfeldig tall fra (1) til (10))
sett [tentakelStørrelse v] til (tilfeldig tall fra (1) til (10))
endre størrelse med (tentakelStørrelse)
vend venstre (tentakelRotasjon) grader
vent (0.5) sekunder
endre størrelse med ((tentakelStørrelse) * (-1))
vend høyre (tentakelRotasjon) grader
```

**(Merk at vi multipliserer tentakelStørrelse med -1 for å få en negativ verdi?)**
