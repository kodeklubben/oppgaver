---
title: Scratchkort - Hjul
level: Nivå 4
language: no-NB
stylesheet: scratch
embeds: "*.png"
materials: "*.sb2"
...

## Sjekkliste { .check}

+ For å få et hjul til å bevege seg, kan vi **rotere** det litt av gangen og flytte det når vi mottar en **flyttet melding**.
```blocks
når jeg mottar [flyttet venstre v]
endre x med ((hastighet) * (-1))
vend høyre (15) grader 

når jeg mottar [flyttet høyre  v]
endre x med (hastiget)
vend venstre (15) grader
```

+ Hvis du vil, kan du erstatte verdiene med variabler som `hastiget`{.blockorange}, slik at du kan kontrollere hastigheten
 i alle retninger fra ett sted.

**(Merk at vi har multiplisert `hastiget`{.blockorange} med -1 for å få negativ verdi?)**
