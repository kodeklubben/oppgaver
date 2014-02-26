---
title: Fyrverkeri
level: 1.3
language: nb-NO
embeds: ["*.png"]
...

# Introduksjon { .intro}
I dette prosjektet skal vi skyte opp fyrverkeri over en by.

![skjermbilde](bilde01.png)

# Steg 1: Lag en rakett som flyr mot muspekeren { .activity}
__Importer forskjellige bilder for spillet__

## Sjekkliste { .check}

+ Lag et nytt Scratch-prosjekt. Fjern katten ved å høyreklikke på den og velge `slett`
+ Bytt bakgrunnsbilde til `outdoor/city-with-water`
+ Klikk på "Ny figur: velg figur fra biblioteket" for å legge en rakett-figur til prosjektet (bruk Resources/Rocket.png)
+ Vi vil at raketten skal skjules når du klikker på det grønne flagget.

    ```blocks
	når grønt flagg klikkes
	skjul
    ```

Nå vil vi gjerne at raketten skal bevege seg mot muspekeren når du klikker med musa.

+ Legg til en kloss `når mellomrom trykkes`. Deretter legger vi to klosser som gjør raketten synlig og lar den bevege seg mot muspekeren.

    ```blocks
	når (mellomrom) trykkes 
	vis
	gli (1) sekunder til x: (mus x) y: (mus y)
    ```
		
## Test prosjektet { .flag}
__Klikk på det grønne flagget, plaser muspekeren over scenen og trykk mellomromstasten.__

Får du opp raketten som beveger seg mot muspekeren?
Hva skjer hvis du flytter på muspekeren og trykker mellomromstasten igjen?

## Sjekkliste { .check}

+ Fyrverkeri pleier ikke å fly fra side til side, så du bør gjøre det slik at raketten alltid flyr mot muspekeren fra bunnen av skjermen. Før du fyrer opp raketten: bruk klossen "gå til" for å få raketten til å flytte seg til bunnen av skjermen, men bli værende samme sted horisontalt.

    ```blocks
	når grønt flagg klikkes
	skjul

	når (mellomrom) trykkes
	gå til x: (mus x) y: (-200)
	vis
	gli (1) sekunder til x: (mus x) y: (mus y)
    ```

## Test prosjektet { .flag}
__Klikk på det grønne flagget, plaser musa over scenen og trykk mellomromstasten.__
Flyr raketten mot muspekeren fra bunnen av skjermen? Hva skjer hvis du flytter på musa og trykker mellomromstasten igjen?

## Sjekkliste { .check}

+ Endelig, prøv å få til det samme ved å bruke musknappen istedenfor mellomromstasten. For å gjøre dette kan vi vikle skriptet vårt i "for alltid hvis museknappen er nede".
Bytt så klossen "når mellomrom trykkes" til "når grønt flagg klikkes" og sist men ikke minst sørg for at raketten er skjult når alt starter opp.

    ```blocks
        når grønt flagg klikkes
	skjul
	for alltid 
		hvis <(museknappen er nede?)>
			gå til x: (mus x) y: (-200)
			vis
			gli (1) sekunder til x: (mus x) y: (mus y)
    ```

## Test prosjektet { .flag}
__Klikk på det grønne flagget og så trykk musknappen over scenen. Klikk igjen et annet sted.__ 

## Utfordringer { .try}
+ Prøv å få noen raketter til å bevege seg litt saktere eller fortere enn andre.
+ Prøv å endre måten raketten snur seg mot muspekeren på: få den til å bue seg litt.

## Lagre prosjektet { .save}

# Steg 2: Få raketten til å eksplodere { .activity}

## Sjekkliste { .check}

+ Første steg for å få raketten til å eksplodere er å få den til å spille av en bang lyd (Resources\bang) før den begynner å bevege seg og så gjemme seg når den når muspekeren. For å importere en lyd gå til fanen "Lyder" og klikk på "Velg lyd" fra biblioteket.

    ```blocks
	når grønt flagg klikkes
	skjul
	for alltid
		hvis <(museknappen er nede?)>
			gå til x: (mus x) y: (-200)
			spill lyden [bang]
			vis
			gli (1) sekunder til x: (mus x) y: (mus y)
			skjul
    ```
+ Neste steg er å få raketten til å sende melding når den eksploderer. Vi skal høre på meldingen senere.

    ```blocks
	når grønt flagg klikkes
	skjul
	for alltid
		hvis <(museknappen er nede?)>
			gå til x: (mus x) y: (-200)
			spill lyden [bang]
			vis
			gli (1) sekunder til x: (mus x) y: (mus y)
			skjul
			send melding [explode]
    ```

## Test prosjektet {.flag}
__Klikk på det grønne flagget.__ 
Sørg for at raketten spiller av lyden og gjemmer seg når den når muspekeren.

## Sjekkliste { .check}

+ Opprett en ny figur fra Fil(Resources/firework1.png)
+ Når den får meldingen "explode" bør den gjemme seg og så bevege mot raketten ved bruk av klossen "gå til", vise seg og forsvinne igjen 1 sekund senere.

    ```blocks
	når jeg mottar [explode]
	skjul
	gå til x: ([x-posisjon] av [rocket]) y: ([y-posisjon] av [rocket])
	vis
	vent (1) sekunder
	skjul
    ```

## Test prosjektet { .flag}
__Fyr av en rakett til.__ 
Blir den erstattet med et eksplosjonsbilde når den eksploderer?
Hva skjer hvis du holder musknappen nede mens du beveger på musa? (Ikke bekymre deg, vi skal fikse det senere).

##Lagre prosjektet { .save}

# Steg 3: Gjør hver eksplosjon unik { .activity}

+ Nå kan vi gjøre hver eksplosjon enda mer unik ved å bruke klossen "sett farge effekt" og velge en tilfeldig farge mellom 1 og 200 før eksplosjonen vises. 

    ```blocks
	når jeg mottar [explode]
	skjul
	sett [farge] effekt til (tilfeldig tall fra (1) til (200))
	gå til x: ([x-posisjon] av [rocket]) y: ([y-posisjon] av [rocket])
	vis
	vent (1) sekunder
	skjul	
    ```

## Test prosjektet { .flag}
__Klikk på det grønne flagget.__ 

Har hver eksplosjon en annen farge?

## Sjekkliste { .check}

+ Legg til forskjellige bilder av eksplosjon som drakter ved bruk av Resources/firework2.png og Resources/firework3.png og bytt mellom dem for hver rakett før eksplosjonen vises.

## Test prosjektet { .flag}
__Klikk på det grønne flagget.__ 

Har hver rakett et forskjellig bilde av eksplosjonen?

## Sjekkliste { .check}

+ Endelig, gjør eksplosjonen større etter at raketten eksploderte! Istedenfor å vente i 1 sekund sett størrelsen til figuren til 5% før den vises, og så når den blir synlig øk størrelsen med 2 femti ganger ved bruk av klossen "gjenta".  

    ```blocks
	når jeg mottar [explode]
	skjul
	sett [farge] effekt til (tilfeldig tall fra (1) til (200))
	gå til x: ([x-posisjon] av [rocket]) y: ([y-posisjon] av [rocket])
	vis
	sett størrelse til (5) %
	gjenta (50) ganger
	    endre størrelse med (2)
	slutt
	vent (1) sekunder
	skjul
    ```

## Test prosjektet { .flag}
__Klikk på det grønne flagget.__ 

Har bildet av eksplosjonen spredt ut fra midten av raketten? Vokser det gradvis?

## Utfordringer { .try}
Prøv å gjøre hver eksplosjon unik: endre størrelsen og veksthastigheten for eksplosjonen.

## Lagre prosjektet { .save}

#Steg 4: Fikse "send melding"-feilen { .activity}

Husker du at vi tidligere hadde et problem med å holde museknappen nede?
Dette problemet oppstår fordi når raketten sender sin melding om eksplosjonen, den gjentar hvis-løkka med en gang og sender en eksplosjonsmelding til, før den siste er ferig med animasjonen. I informatikkverden kaller vi slike problemer for "bugs"(insekter).

## Sjekkliste { .check}

+ For å fikse dette må du erstatte klossen "send melding" med "send melding og vent". Da kommer ikke løkken til å gjentas før eksplosjonen er ferdig.

    ```blocks
	når grønt flagg klikkes
	skjul
	for alltid
		hvis <(museknappen er nede?)> 
			gå til x: (mus x) y: (-200)
			spill lyden [bang]
			vis
			gli (1) sekunder til x: (mus x) y: (mus y)
			skjul
			send melding [explode] og vent
    ```

## Test prosjektet { .flag}
__Klikk på det grønne flagget, hold museknappen nede og beveg litt på musa.__ 

Får du eksplosjonen til å dukke opp riktig sted og til riktig tid?

## Lagre prosjektet { .save}

__Gratulerer, du er ferdig! Nå kan du kose deg med spillet!__

Ikke glem å dele spillet ditt med alle dine venner og familien! Klikk på "del" i menylinjen.
