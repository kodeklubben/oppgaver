---
title: Lyd
playlist: Scratchkort
level: Nivå 4
language: nb-NO
stylesheet: scratch
embeds: "*.png"
materials: "*.sb2"
---

## Sjekkliste { .check}

+ Lag en ny figur og se om du klarer å få den til å se ut som den lyden du vil lage.

+ I fanen `Lyder`{.blocklightgrey}, lag en et nytt opptak eller importer en lydfil.
  ![Lyder](sound-sample.png)

+ Trykk på figuren og lag et skript som sender en melding til figuren når man trykker på den:
```blocks
når denne figuren klikkes
send melding [katt v]
---
+ Nå må vi spille `lyd`{.blockpurple} når den får `meldingen`{.blockbrown}.
```blocks
når jeg mottar [katt v]
spill lyden [meow v]
---

+ Til slutt endrer vi utseende når `lyd`{.blockpurple} spilles.
```blocks
når jeg mottar [katt v]
spill lyden [moew v]
sett størrelse til (110) %
vent (0.1) sekunder
sett størrelse til (100) %
---

