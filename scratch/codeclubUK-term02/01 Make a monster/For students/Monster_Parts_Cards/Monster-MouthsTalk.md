---
title: Munn som prater
playlist: Scratchkort
level: Nivå 4
language: nb-NO
stylesheet: scratch
embeds: "*.png"
materials: "*.sb2"
---

## Sjekkliste { .check}

+ For å få monsteret til å snakke, kan du bruke `si`{.blockpurple}-kloss.

```blocks
når [mellomrom v] trykkes
si [Hallo!] i (2) sekunder
```
+ For å gjøre det litt mere imponerende, kan du få monsteret til å **åpne** og **lukke munnen** mens det prater. For å
 gjøre dette, rediger figuren som inneholder munnen  - opprett en ny  `drakt`{.blockpurple} som har lukket munn. Ved å
  bytte mellom de to, kan du animere at munnen åpner og lukker seg.

```blocks
gjenta (8) ganger
	vent (0.1) sekunder 
	bytt drakt til [munnLukket v]
	vent (0.1) sekunder 
	bytt drakt til [munnÅpen v]
slutt
```
+ For å koble de to sammen, få `si`{.blockpurple}-klossen til å sende en melding, som den andre klossen kan reagere på.

```blocks
når [mellomrom v] trykkes
send melding [snakk v]
si [Hallo!] i (2) sekunder

når jeg mottar [snakk v]
gjenta (8) ganger
	vent (0.1) sekunder
	bytt drakt til [munnLukket v]
	vent (0.1) sekunder
	bytt drakt til [munnÅpen v]
slutt
```

+ For å gjøre det litt mer fleksibelt, bruk en variabel for å kontrollere `snakketid`{.blockorange} hvor lenge monsteret
 sier noe, og for å kontrollere hvor mange ganger animasjonsløkken er gjentatt.

```blocks
når [mellomrom v] trykkes
sett [snakketid v] til (2)
send melding [snakk v]
si [Hallo!] i (snakketid) sekunder

når [a v] trykkes
sett [snakketid v] til (4)
send melding [snakk v]
si [Noe litt lengre] i (snakketid) sekunder

når jeg mottar [snakk v]
gjenta ((snakketid) * (4)) ganger
	vent (0.1) sekunder 
	bytt til drakt [munnLukket v]
	vent (0.1) sekunder
	bytt til drakt [munnÅpen v]
slutt
```
**(Merk at vi multipliserer snakketid med 4 for å være sikkre på at løkken gjentas nok ganger)**

+ Du kan også få monsteret ditt til å si lyder ved å bruke en av lydklossene. Husk å importere lydene i `Lyd`{.blocklightgrey}.

```blocks
når jeg mottar [snakk v]
spill lyden [Screech v]
```
**Prøv å legge til lyder til andre hendelser, du kan bruke en skummel svevende lyd for et spøkelse som flyr rundt på
 skjermen! Har du mikrofon på datamaskinen kan du ta opp dine egne lyder, overrask de andre ved å ta opp et høyt
 monster BRØØØØØØØØØL!!!**
