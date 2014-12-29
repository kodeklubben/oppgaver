---
title: Tromme
playlist: Scratchkort
level: Nivå 4
language: nb-NO
stylesheet: scratch
embeds: "*.png"
materials: "*.sb2"
---

## Sjekkliste { .check}

+ Importer en ny figur og velg Ting -> Tromme. Gi den navnet “Tromme”.

+ Vi vil at trommen skal lage lyd når vi klikker på den eller trykker på `mellomromstasten`{.blockbrown}.

```blocks
når denne figuren klikkes
send melding [tromme v]

når [mellomrom v] trykkes
send melding [tromme v]
---

+ Nå må vi lage lyd når den mottar `tromme`{.blockbrown}. Ved å endre tallet, kan du endre lyden trommen lager.

```blocks
når jeg mottar [tromme v]
trommeslag (48 v) som varer (0.2) takter
---

+ Prøv å endre utseende slik at man ser hvilket instrument som spiller.

```blocks
når jeg mottar [tromme v]
trommeslag (48 v) som varer (0.2) takter
sett størrelse til (110) %
vent (0.1) sekunder
sett størrelse til (100) %
---

