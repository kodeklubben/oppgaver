---
title: 3D-Flakser
level: 1.5
language: nb-NO
stylesheet: scratch
embeds: ["*.png", "../../bilder/*.png"]
note: "README.md"
...

# Introduksjon {.intro}

I dette prosjektet skal vi lage en utgave av Flaksefugl (som er en kopi av Flappy Bird) i *tre dimensjoner*! Spillet går ut på at man styrer en flyvende figur gjennom ringer som kommer mot deg. Spilleren må styre figuren opp og ned og side til side. Hovedutfordringen i dette spillet er å få det til å virke som om ringene faktisk kommer mot flakseren, og så forsvinner forbi. Prosjektet er delt inn i to deler siden det er ganske mye vi skal igjennom. I denne første delen skal vi få ringene til å fungere som de skal. La oss sette i gang!

![](flakser.png)

# Steg 1: Lag ringer, og få dem til å komme mot deg. { .activity}

Spillet skal bestå av tre figurer: __Ring__, __Flakser__ og __Bakken__. 

Vi begynner med å lage ringefiguren. Du kan enkelt tegne den selv som to sirkler inni hverandre, fyllt med en farge imellom.  

## Sjekkliste { .check}
+ Tegn figuren __Ring__. Jo enklere jo bedre.
+ Gi ringfiguren disse skriptene:

```blocks
	når jeg mottar [nytt spill v]
		skjul
		for alltid
			lag en klon av [meg v]
			vent (1) sekunder
```
```blocks
	når jeg starter som klon
		gå til x: (0) y: (0)
		vis
		gjenta (10) ganger
			endre størrelse med 5
			vent (0.1) sekunder
		slett denne klonen
```

Du må også lage et skript som sørger for at meldingen ‘nytt spill’ sendes når det grønne flagget klikkes. 

## Test prosjektet {.flag}

+ Hva gjør de to skriptene over? Ser det ut som om ringene kommer mot deg?

De to skriptene vi har foreløpig er en OK start, men de er ikke gode nok til å virkelig kalles 3D! Tenk litt på hvordan det virker som om noe vokser i størrelse når det kommer mot deg. Når det er langt unna så vokser det ganske sakte, mens når det er nærme så vokser det mye fortere. Dette skal vi få til ved hjelp av en *variabel* som vi kaller __avstand__. Når __avstand__ er stor, så er ringen langt borte, og skal vokse sakte. Når __avstand__ er liten så betyr det at ringen er nærme, og den skal vokse fort.

## Sjekkliste { .check}

+ Lag en variabel som heter __avstand__. Pass på at den kun gjelder ‘for denne figuren’. 
+ Endre skriptet over til dette:

 ```blocks
	når jeg starter som klon
		gå til x: (0) y: (0)
		vis
		sett [avstand v] til (10)
		gjenta til ((avstand) < (1))
			sett størrelse til ((150) / (avstand)) %
			endre [avstand v] med (-0.5)
			vent (0.1) sekunder
		slett denne klonen
```
+ Det kan hende du må endre litt på tallene i skriptet over for at det skal se bra ut. Prøv deg frem! 		

## Utfordring: Gjennomsiktig effekt {.challenge}

Dette er ikke viktig for å kunne fortsette med spillet, men prøv hvis du vil. For at det skal se enda mer ut som at ringene først er langt borte og så nærme, så kan du bruke klossen `endre [gjennomsiktig v] effekt med (25)`{.blockpurple}-klossen for å gjøre ringene mer gjennomsiktig når de er langt borte. Hvor må du putte denne klossen for at det skal se bra ut, og hvilket tall passer bra?

# Steg 2: Få ringene til å dukke opp tilfeldige steder { .activity}

For at spillet skal bli mest mulig utfordrende så burde ringene dukke opp på forskjellige steder hver gang. Å først få dem til å dukke opp på forskjellige steder er ikke så vanskelig, men det å få dem til å vokse på riktig måte er litt vrient. 


===========================================================================
- Ting å prøve: `## Ting å prøve {.try}`,
- Utfordringer: `## Utfordring: Flere ting {.challenge}`,
- Test prosjektet: `## Test prosjektet {.flag}`,
- Lagre prosjektet: `## Lagre prosjektet {.save}`.
    ```blocks
        når grønt flagg trykkes
        for alltid
            pek mot [musepekeren v]
        slutt
    ```
    - `` `Bevegelse`{.blockblue}``
    - `` `Utseende`{.blockpurple}``
    - `` `Lyd`{.blockpink}``
    - `` `Penn`{.blockgreen}``
    - `` `Data`{.blockorange}``
    - `` `Hendelser`{.blockgrey}``
    - `` `Styring`{.blockyellow}``
    - `` `Sansning`{.blocklightblue}``
    - `` `Operatorer`{.blocklightgreen}``
    - `` `Flere klosser`{.blockpurple}``
