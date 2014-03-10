---
title: Scratchkort - Bein
level: Nivå 4
language: nb-NO
stylesheet: scratch
embeds: "*.png"
materials: "*.sb2"
...

## Sjekkliste { .check}

+ Ved å bruke to figurer til bein kan vi få monsteret vårt
 til å gå. For å gjøre dette lager vi en
 **variabel** som bytter mellom de to tilstandene, én for
 når beinet peker forover og en annen når beinet går
 bakover (vi bytter om på tilstandene for det andre
 beinet). For å gjøre dette må vi først lage en `steg`{.blockorange}
 variabel, så hver gang melding om bevegelse
 mottas, **øker vi variabelen med 1**. Hvis
 variablen går høyere enn 1 (vi kan teste dette
 med større enn operatøren `>`{.blockgreen}) nullstiller vi den.
```blocks
når grønt flagg klikkes
sett [hastighet v] til [5]
sett [steg v] til [0]

når jeg mottar [flyttet venstre v]
endre [steg v] med [1]
hvis < (steg) > [1] >
	sett [steg v] til [0]
slutt

når jeg mottar [flyttet høyre v]
endre [steg v] med [1]
hvis < (steg) > [1] >
	sett [steg v] til [0]
slutt
```

+	 Nå kan vi sette beina i bevegelse ved å sjekke
	 vår `steg`{.blockorange} variabel. **Når variabelen
	 blir satt til null** kan vi bytte retning på
	 beinet (her har vi brukt en fast `retning`{.blockblue} for
	 å hindre at beinet går amok hvis variabelen og
	 graden på vinkelen ikke stemmer, men kanskje vil
	 du at monstret skal gjøre det!). Ikke glem å flytte
	 beina langs kroppen ved å bruke
	 `hastighet`{.blockorange} variabel.
```blocks
når jeg mottar [flyttet høyre v]
endre x med (hastighet)
hvis < (steg) = [0] >
	pek i retning (180 v)
ellers
	pek i retning (165 v)
slutt

når jeg mottar [flyttet venstre v]
endre x med ((hastighet) * [-1])
hvis < (steg) = [1] >
	pek i retning (165 v)
else
	pek i retning (180 v)
slutt
```

**Du kan bruke samme type handling for å lage
armer som vinker, eller fuglevinger som flakser.**
