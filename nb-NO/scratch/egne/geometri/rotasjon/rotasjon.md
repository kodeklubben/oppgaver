---
title: Rotasjon
level: 1.2
language: nb-NO
stylesheet: scratch
embeds: ["*.png", "../../bilder/*.png"]
note: "README.md"
---

# Læringsmål {.tips}
+ beskrive og gjennomføre spegling, rotasjon og parallellforskyving
+ beskrive plassering og flytting i rutenett, på kart og i koordinatsystem, med og utan digitale hjelpemiddel, og bruke koordinatar til å berekne avstandar parallelt med aksane i eit koordinatsystem

# Introduksjon {.intro}


I denne oppgaven skal vi importere en geometrisk figur og deretter __rotere__ den på ulike måter.


![](Geometri.png)

# Steg 1: Vi roterer en likebeint trekant {.activity}

*For å gjøre det enkelt å komme i gang, henter vi inn en ferdig figur fra biblioteket til Scratch. 
Denne figuren er tilnærmet lik en likebeint trekant*

## Sjekkliste {.check}

+ Start et nytt prosjekt.
+ Slett kattefiguren ved å høyreklikke på den og velge `slett`.
+ Legg til en ny figur. Klikk på ![Velg figur fra biblioteket](hent-fra-bibliotek.png)-knappen og velg trollmannshatten. Vi har brukt `Ting/Wizard Hat`-figuren.
+ Gi den nye figuren navnet `Hattulf` ved å klikke på `i`.

Vi skal nå gi Scratch beskjed om å rotere hatten 90 grader.

+ Legg til følgende skript på `Hattulf`-figuren din.

    ```blocks
        når @ klikkes
		vend @ (90) grader
	```
    
## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

+ Hva skjer når du trykker på det grønne flagget? 
+ Roterer hatten som forventet?
+ Hva tror du skjer om du trykker på det grønne flagget en gang til? I hvilken retning vil toppen av hatten peke?
+ Hvor mange ganger må du be hatten om å rotere før den er tilbake til utgangspunktet? 

## Sjekkliste {.check}

Rotasjon er jo gøy! Men at ting roterer med 90 grader av gangen er jo litt kjedelig, og litt unaturlig.

+ Halver antall grader hatten skal rotere per gang:

    ```blocks
        når grønt flagg klikkes
		vend @ (45) grader
	```

## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

+ Hvor mange ganger må du trykke på hatten for at den skal rotere hele veien rundt nå?
+ Fortsett å halvere antall grader hatten skal rotere. Prøv å finne en sammenheng mellom hvor mange grader den roteres, og hvor mange ganger du må trykke på det grønne flagget for at den skal roteres helt rundt.
 
Du oppdager kanskje at det begynner å bli veldig mange klikk etterhvert?

# Steg 2: A little more action, please! {.activity}

Heldigvis kan vi ved hjelp av litt programmeringsmagi få datamaskinen til å gjøre jobben for oss! 
 
## Sjekkliste {.check}

+ Vi legger til en styring{.blockyellow} -kloss som ber hatten om å rotere et bestemt antall ganger:

	```blocks
        når grønt flagg klikkes
		gjenta (8) ganger
		vend ↺ (45) grader
end
	```
+ Tips: For hver gang du halverer vinkelen, må du doble antall repetisjoner for at hatten skal snurre like langt.

## Avslutning

+ Lagre prosjektet ved å gi det et navn
+ Ved å sette antall grader du roterer pr gang til 1, hvor mange ganger må du rotere `Hattulf` for at han skal gjøre to fulle roteringer? Hva med tre og en halv rotasjon?

