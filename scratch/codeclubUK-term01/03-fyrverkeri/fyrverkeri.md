---
title: Fyrverkeri
level: 1.3
language: nb-NO
stylesheet: scratch
embeds: ["*.png", "../../bilder/*.png"]
materials: "ressurser/*"
...

# Introduksjon { .intro}
I dette prosjektet skal vi skyte opp fyrverkeri over en by.

![](skjermbilde.png)

# Steg 1: Lag en rakett som flyr mot muspekeren { .activity}
*Vi starter med å importere forskjellige bilder vi skal bruke i spillet*

## Sjekkliste { .check}

+ Lag et nytt Scratch-prosjekt. Fjern katten ved å høyreklikke på den og velge `slett`
+ Bytt bakgrunnsbilde til `utendørs/city-with-water`
+ Klikk på *Ny figur: Last opp figur fra fil*, ![Last opp figur fra fil](hent-fra-fil.png), for å legge til en rakett-figur i prosjektet, for eksempel `ressurser/rocket.png`
+ Vi vil at raketten skal skjules når du klikker på det grønne flagget.

    ```blocks
	når grønt flagg klikkes
	skjul
    ```

*Nå vil vi gjerne at raketten skal bevege seg mot muspekeren når du klikker med musa.*

+ Legg til en kloss `når mellomrom trykkes`{.blockgrey}. Deretter legger vi to klosser som gjør raketten synlig og lar den bevege seg mot muspekeren.

    ```blocks
	når [mellomrom v] trykkes 
	vis
	gli (1) sekunder til x: (mus x) y: (mus y)
    ```
		
## Test prosjektet { .flag}
__Klikk på det grønne flagget, plasser muspekeren over scenen og trykk mellomromstasten.__

+ Får du opp raketten som beveger seg mot muspekeren?
+ Hva skjer hvis du flytter på muspekeren og trykker mellomromstasten igjen?

## Sjekkliste { .check}

*Fyrverkeri pleier ikke å fly fra side til side, så du bør gjøre det slik at raketten alltid flyr mot muspekeren fra bunnen av skjermen.*

+ Før du fyrer opp raketten: bruk klossen `gå til`{.blockblue} for å få raketten til å flytte seg til bunnen av skjermen, men bli værende samme sted horisontalt.

    ```blocks
	når grønt flagg klikkes
	skjul

	når [mellomrom v] trykkes
	gå til x: (mus x) y: (-200)
	vis
	gli (1) sekunder til x: (mus x) y: (mus y)
    ```

## Test prosjektet { .flag}
__Klikk på det grønne flagget, plaser musa over scenen og trykk mellomromstasten.__

+ Flyr raketten mot muspekeren fra bunnen av skjermen?
+ Hva skjer hvis du flytter på musa og trykker mellomromstasten igjen?

## Sjekkliste { .check}

+ Endelig, prøv å få til det samme ved å bruke musknappen istedenfor mellomromstasten. For å gjøre dette kan vi pakke skriptet vårt inn i en `for alltid - hvis museknappen er nede`{.blockyellow}-blokk.
+ Bytt så klossen `når mellomrom trykkes`{.blockgrey} til `når grønt flagg klikkes`{.blockgrey} og sist men ikke minst sørg for at raketten er skjult når alt starter opp.

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
__Klikk på det grønne flagget__

+ Trykk musknappen over scenen. Klikk igjen et annet sted.

## Utfordringer { .try}
+ Prøv å få noen raketter til å bevege seg litt saktere eller fortere enn andre.
+ Prøv å endre måten raketten snur seg mot muspekeren på: få den til å bue seg litt.

# Steg 2: Få raketten til å eksplodere { .activity}

## Sjekkliste { .check}

+ Første steg for å få raketten til å eksplodere er å spille av en bang-lyd (`ressurser/bang.wav`) før den begynner å bevege seg og så gjemme seg når den når muspekeren. For å importere en lyd gå til fanen `Lyder`{.blocklightgrey} og klikk på *Last opp lyd fra fil*, ![Last opp lyd fra fil](hent-fra-fil.png).

    ```blocks
	når grønt flagg klikkes
	skjul
	for alltid
		hvis <(museknappen er nede?)>
			gå til x: (mus x) y: (-200)
			spill lyden [bang v]
			vis
			gli (1) sekunder til x: (mus x) y: (mus y)
			skjul
    ```
+ Neste steg er å få raketten til å sende en melding til resten av spillet når den eksploderer. Vi skal lytte etter meldingen senere. Lag en ny melding som heter `eksploder`.

    ```blocks
	når grønt flagg klikkes
	skjul
	for alltid
		hvis <(museknappen er nede?)>
			gå til x: (mus x) y: (-200)
			spill lyden [bang v]
			vis
			gli (1) sekunder til x: (mus x) y: (mus y)
			skjul
			send melding [eksploder v]
    ```

## Test prosjektet {.flag}
__Klikk på det grønne flagget.__ 

+ Sørg for at raketten spiller av lyden og gjemmer seg når den når muspekeren.

## Sjekkliste { .check}

+ Last opp en ny figur fra fil (`ressurser/firework1.png`).
+ Når denne figuren får meldingen `eksploder` passer vi på at den er gjemt, flytter den til raketten ved bruk av klossen `gå til`{.blockblue}, viser den og skjuler den igjen 1 sekund senere.

    ```blocks
	når jeg mottar [eksploder v]
	skjul
	gå til x: ([x-posisjon v] av [rocket v]) y: ([y-posisjon v] av [rocket v])
	vis
	vent (1) sekunder
	skjul
    ```

## Test prosjektet { .flag}
__Fyr av en rakett til.__ 

+ Blir den erstattet med et eksplosjonsbilde når den eksploderer?
+ Hva skjer hvis du holder musknappen nede mens du beveger på musa? (Ikke bekymre deg, vi skal fikse det senere).

# Steg 3: Gjør hver eksplosjon unik { .activity}

## Sjekkliste { .check}

+ Nå kan vi gjøre hver eksplosjon enda mer unik ved å bruke klossen `sett fargeeffekt`{.blockpurple} og velge en tilfeldig farge før eksplosjonen vises. 

    ```blocks
	når jeg mottar [eksploder v]
	skjul
	sett [farge v] effekt til (tilfeldig tall fra (1) til (200))
	gå til x: ([x-posisjon v] av [rocket v]) y: ([y-posisjon v] av [rocket v])
	vis
	vent (1) sekunder
	skjul	
    ```

+ Legg til forskjellige bilder av eksplosjoner som drakter ved å velge `Drakter`{.blocklightgrey}-fanen til `firework1`. Ved å klikke *Last opp drakt fra fil*, ![Last opp drakt fra fil](hent-fra-fil.png), kan du legge til `firework2.png`, `firework3.png` og `firework4.png` fra `ressurser`. 
+ Klarer du å få eksplosjonene til å bruke forskjellige drakter? (Hint: Du kan for eksempel bruke `neste drakt`{.blockpurple} et passende sted i skriptet til Firework1.)

## Test prosjektet { .flag}
__Klikk på det grønne flagget.__ 

+ Har hver eksplosjon en forskjellig farge?
+ Har hver rakett et forskjellig bilde av eksplosjonen?

## Sjekkliste { .check}

+ Endelig, gjør eksplosjonen større etter at raketten eksploderte! Istedenfor å vente i 1 sekund sett størrelsen til figuren til 5% før den vises, og så når den blir synlig øk størrelsen med 2 femti ganger ved bruk av klossen `gjenta`{.blockyellow}.  

    ```blocks
	når jeg mottar [explode]
	skjul
    neste drakt	
    sett [farge] effekt til (tilfeldig tall fra (1) til (200))
	gå til x: ([x-posisjon] av [rocket]) y: ([y-posisjon] av [rocket])
	sett størrelse til (5) %
	vis
	gjenta (20) ganger
	    endre størrelse med (5)
	slutt
	vent (1) sekunder
	skjul
    ```

## Test prosjektet { .flag}
__Klikk på det grønne flagget.__ 

+ Har bildet av eksplosjonen spredt ut fra midten av raketten?
+ Vokser eksplosjonen gradvis?

## Utfordringer { .try}
Prøv å gjøre hver eksplosjon unik: endre størrelsen og veksthastigheten for eksplosjonen.

#Steg 4: Fikse "send melding"-feilen { .activity}

Husker du at vi tidligere hadde et problem med å holde museknappen nede?

Dette problemet oppstår fordi når raketten sender sin melding om eksplosjonen, gjentar den hvis-løkka med en gang. Dermed blir det sendt en eksplosjonsmelding før den forrige er ferdig med animasjonen.

I programmeringsverden kaller vi denne type problemer for *bugs*, fordi man i gamle dager (da datamaskiner var mye større) kunne ha problemer med at innsekter ble fanget inne i datamaskinene og ødela programmer.

## Sjekkliste { .check}

+ For å fikse dette kan du erstatte klossen `send melding`{.blockgrey} med `send melding og vent`{.blockgrey}. Da vil ikke løkken gjentas før den forrige eksplosjonen er ferdig.

    ```blocks
	når grønt flagg klikkes
	skjul
	for alltid
		hvis <(museknappen er nede?)> 
			gå til x: (mus x) y: (-200)
			spill lyden [bang v]
			vis
			gli (1) sekunder til x: (mus x) y: (mus y)
			skjul
			send melding [eksploder v] og vent
    ```

## Test prosjektet { .flag}
__Klikk på det grønne flagget, hold museknappen nede og beveg litt på musa.__ 

+ Får du eksplosjonen til å dukke opp på riktig sted og til riktig tid?

## Lagre prosjektet { .save}

__Gratulerer, du er ferdig! Nå kan du kose deg med spillet!__

Ikke glem å dele spillet ditt med alle dine venner og familien! Klikk på `Legg ut` i menylinjen.
