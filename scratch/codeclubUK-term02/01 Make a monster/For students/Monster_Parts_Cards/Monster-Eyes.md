---
title: Øyne
playlist: Scratchkort
level: Nivå 4
language: nb-NO
stylesheet: scratch
embeds: "*.png"
materials: "*.sb2"
---

## Sjekkliste { .check}

+ Du kan gi monsteret øyne som følger musepekeren rundt på skjermen. Det kan ha så mange øyne som du vil,  kankje har det åtte øyne, som en edderkopp! Siden vi alltid vil at monsterøynene skal følge musepekeren må vi sette `for alltid`{.blockyellow} klossen. Når man trykker på det grønne flagget og skriptet har startet vil vi at øynene peker i retningen av musepekeren og flytter seg hvert brøkdelssekund.

```blocks
når denne figuren klikkes
for alltid
	pek mot [musepeker v]
	vent (0.2) sekunder

når jeg mottar [flyttet høyre v]
endre x med (hastighet)

når jeg mottar [flyttet venstre v]
endre x med ((hastighet) * (-1))
---

**Merk at vi ogå lytter til meldinger om at kroppen har flyttet seg, slik at øynene beveger seg sammen med kroppen og andre kroppsdeler. Er det noe annet du kan få øynene til å gjøre? Hvis du flytter muspekeren mellom monsterets øyne, så går øynene i kryss!**
