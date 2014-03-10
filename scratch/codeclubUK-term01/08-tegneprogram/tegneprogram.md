---
title: Tegneprogram
level: 1.8
language: nb-NO
embeds: ["*.png", "../../bilder/*.png"]
stylesheet: scratch
...

# Introduksjon { .intro}
Dette prosjektet lager tegneprogram slik at du kan lage din egen kunst. Du kan tegne med forskjellige farger, bruke viskelær, lage stempler og mye mer!

![skjermbilde](skjermbilde.png)

## FORBEREDELSER: Last ned nødvendige ressurser.

Denne første delen kan du godt få hjelp fra en voksen til å gjøre!

## Sjekkliste { .check}

+ Lag en ny tab i nettleseren din
+ Skriv inn denne nettadressen: http://bit.ly/Tegneutstyr
+ Last ned zip-fila "Ressurser_Tegneprogram.zip" og legg det på skrivebordet på datamaskinen din eller en annen plass du husker.
+ Pakk ut zip-filen ved å høyreklikke på den og velge "Extract All"/"Pakk ut filer".

## Steg 1: Dra og tegn!

Vi starter med en penn som tegner når du drar den rundt på scenen.

+ Start et nytt Scratch-prosjekt. Slett katten ved å høyreklikke og velge slett.
+ Klikk på __Scene__ og så på __Bakgrunner__-fliken. Last opp bakgrunnen som heter frame.bmp fra folderen du hentet i forberedelsene.
+ Lag en figur som heter __penn__ av bildet __green-pencil__ som ligger i den nedlastede mappen.
+ Bytt til __drakter__-fliken og velge senterpunkt for figurer ved hjelp av ![Velg senterpunkt](velg_senterpunkt.png). Flytt blyanten slik at spissen peker på det lille grå korset i midten. Da vil spissen tegne og ikke midten av blyanten.
![Velg senterpunkt](steg1.png)
+ Få pennen til å følge musa rundt på scenen ved å bruke __for alltid__-blokka og __gå til musepeker__-blokka.

```blocks
	når grønt flagg klikkes
	for alltid
		gå til musepeker
	slutt
```

__Nå vil vi bruke denne pennefiguren som en ordentlig penn.__ Om du ser under penn-kategorien kan du se alle slags tegefunksjoner. De vi er interessert i nå er __penn på__ og __penn av__

+ Vi vil bruke museknappen til å kontrollere pennen - når museknappen er nede går pennen ned og når museknappen er oppe er pennen oppe. Vi kan gjøre dette ved å bruke enn hvis ... ellers ... og en mus nede-blokk

```scratch
	når grønt flagg klikkes
	for alltid
		gå til [musepeker v]
		hvis <museknappen er nede?>
			penn på
		ellers
			penn av
		(slutt hvis)
	(slutt for alltid)
```
## Test prosjektet ditt
__Klikk på det grønne flagget.__
Følger pennen musa rundt? Hva skjer om du holder museknappen nede og flytter på musa? Ikke bry deg om pennefargen enda.

## Sjekkliste { .check}

+ Etterhvert vil skjermen bli ganske full av rabbel. Vi kan bruke slett-blokka til å fjerne dette.

```blocks
	når grønt flagg klikkes
	slett
	for alltid
		gå til [musepeker v]
		hvis <museknappen er nede?>
			penn på
		ellers
			penn av
		(slutt hvis)
	(slutt for alltid)
```

## Test prosjektet ditt
__Klikk på det grønne flagget.__

Forsvinner tegningene dine når du klikker på det grønne flagget?

## Lagre prosjektet { .save}

## Steg 2: Rydde opp

I stedet for å måtte starte og stoppe prosjektet for å slette tavla kan vi lage en knapp som sletter alt i stedet. Vi kan bruke slett-blokka.

## Sjekkliste { .check}

+ Lag en ny figur fra ressursmappa du lasta ned i begynnelsen av prosjektet. Velg __cancel-button__.
+ Bytt navn på figuren til __slett__.
+ Flytt figuren til nederste høyre hjørne av scenen.
+ Gi slette-figuren dette skriptet:

```blocks
	når denne figuren klikkes
	slett
```

## Test prosjektet ditt
__Klikk på det grønne flagget.__

Sletter sletteknappen alle tegningene dine?

## Lagre prosjektet { .save}

## Steg 3: Bytte farge

Til nå har vi bare kunnet tegne blå streker. Vi kan bruke andre farger også! Vi legger til noen figurer i bunn av rammen. Figurene vil se ut som fargede knapper. Når vi klikker på en knapp endres pennefagen til den fargen knappen har. For å vite at vi har byttet farge skal vi gjøre det slik at blyanten skifter farge til den fargen vi bruker.

## Sjekkliste { .check}

+ Hent en ny figur fra  __ressurser/red-selector__.
+ Gi den navnet __Rød__ og flytt den ned i venstre hjørne
+ Gi den et skript som sender meldingen __rød__.

```scratch
	når denne figuren klikkes
	send melding [rød v]
```
__Dette er alt den gjør. Det vanskelige arbeidet gjøres av blyanten.__

+ Klikk på blyanten og importer drakten __Ressurser/red-pencil__ . Sett midtpunktet til blyantspissen for denne drakten også.

+ Legg til et nytt skript. Når blyanten får meldingen __rød__, skal den også forandre drakt til rød (red-pencil). Og så skal den selvsagt også begynne å tegne rødt. Slik bygger du skriptet:

__Hint:__ Når du skal velge farge kan du flytte dråpeplukkeren bort til fargeblyanten og velge rødfargen derifra også.


```scratch
	når jeg mottar [rød v]
	bytt drakt til [red-pencil v]
	velg pennefarge (#FF0000)
```

## Test prosjektet ditt
__Klikk på det grønne flagget.__

Begynn å tegne en strek. Bytt til rødt, og se om fargen forandres.
Kommer streken fra blyantspissen nå også?

## Lagre prosjektet { .save}

+ Gjenta punktene for å lage blå, gule og grønne knapper.

## Test prosjektet ditt
__Klikk på det grønne flagget.__

Funker alle knappene?
Skifter de til en annen farge på blyanten?
Tegner de med riktig farge?
Tegner alle figurene fra tuppen av blyanten?

## Lagre prosjektet { .save}

## Steg 4: Bare tegne på tavla

Du har sikkert lagt merke til at man kan tegne over hele scenen, og det blir jo litt rotete. Skal vi begrense skriblingen til bare den lysegrå tavla må vi sette grenser for hvor blyanten kan gå.

Du husker kanskje at Scratch definerer punkter på scenen ved hjelp av en x- og en y-akse. Når du flytter musepekeren rundt omkring vil du se disse verdiene nede i det venstre hjørnet.
For å finne ut hvor grensene for tavla går kan vi begynne nede i det venstre hjørnet. Da står det x: - 230 og y: 120. Flytter vi pekeren rett bort til det høyre hjørnet ser vi at y er uforandret, mens x har blitt til 230. Da vet vi at x-aksen er -230 til 230. y-aksen finner vi ved å flytte pekeren opp i toppen av tavla. Da finner vi ut at y-aksen er 170 til -120.

Disse verdiene kan vi bruke in en `hvis`{.blockyellow}-blokk, og si at når musepekeren er utenfor tavlas x- og y-akse, så virker ikke blyanten

## Sjekkliste { .check}

+ Fyll inn sjekkene som sier at __blyanten får følge musepekeren bare hvis__:
y er større enn -120 og mindre enn 170
x er større enn -230 og mindre enn 230

__NB__ For å få plass til alle sjekkene må du først leggge inn en `<> og <>`{.blockgreen}-blokk, og deretter legge til to nye `<> og <>`{.blockgreen}-blokker inni denne.

```scratch
	når grønt flagg klikkes
	slett
	for alltid 
		hvis <<<(mus x) > (-230)> og <(mus x) < (230)>> og <<(mus y) > (-120)> pg <(mus y) < (170)>>>
			gå til [musepeker v]
			hvis <museknappen er nede?>
				penn på
			ellers
				penn av
			(slutt hvis)
		(slutt hvis)
	(slutt for alltid)
```
+ Siden vi ikke kan tegne utenfor tavla er det like greit at blyanten bare blir borte når
musepekeren går utenfor tavlen. For å gjøre dette må vi erstatte `hvis`{.blockyellow}-blokka ovenfor med en
`hvis.. ellers..`{.blockyellow}-blokk. Reglene blir nå:
hvis musepekeren er innenfor tavlas x- og y-akse følger blyanten pekeren. 
ellers skjules blyanten.

__NB!__ Fordi blyanten vil skjules når pekeren går utenfor tavla, må vi få den til å vise
igjen når den går innenfor igjen. Pass derfor på at du får lagt inn en `vis`{.blockblue}-kommando i
`hvis`{.blockyellow}-blokka.


```scratch
	når grønt flagg klikkes
	slett
	for alltid 
		hvis <<(mus x) > (-230)> og <(mus x) < (230)> og <(mus y) > (-120)> og <(mus y) < (170)>>
			gå til [musepeker v]
			vis
			hvis <museknappen er nede?>
				penn på
			ellers
				penn av
			(slutt hvis)
		ellers
			skjul
		(slutt hvis)
	(slutt for alltid)
```

## Test prosjektet ditt
__Klikk på det grønne flagget.__
Kan du fremdeles tegne på tavla? Kan du tegne utenfor tavla?
Hva skjer med blyanten når musepekeren går ut og inn av tavla?

## Lagre prosjektet { .save}

## Steg 5: Viskelær

__Nå kan vi tegne hva vi vil. Men hva om vi trenger et viskelær? Hmm… da kan vi jo bare få
blyanten til å tegne med samme farge som tavla! Og så gir vi blyanten en viskelærdrakt!__

## Sjekkliste { .check}

+ Last opp en figur fra fil. Velg figuren __eraser__ fra mappen du lastet ned i starten. Kall figuren __viskelær__.
+ Gjør figuren litt mindre med krympeknappen ![Krymp](krymp.png), og så drar du den ned i høyre hjørne, ved siden av slett-knappen.
+ Gi viskelær-figuren et skript som sender meldingen __visk__.

```scratch
	når denne figuren klikkes
	send melding [visk v]
```

+ For å få blyanten til å viske må du legge til en viskelæret som en drakt til figuren. 
+ Blyanten svarer på __visk__ meldingen med å bytte pennefarge til grå (bruk fargevelgeren for å velge bakgrunnen til tavlen).
Husk å sette midtpunktet på viskelæret foran.

```scratch
	når jeg mottar [visk v]
	bytt drakt til [eraser v]
	velg pennefarge (grå)
```


## Test prosjektet ditt
__Klikk på det grønne flagget.__

Klarer viskelæret å viske? Fungerer det helt ut til kantene av tavla? 
Går det greit å veksle mellom blyant og viskelær?

## Lagre prosjektet { .save}

## Steg 6: Stempel

__Nå skal vi lage et stempel som kan lage små avtrykk på tavla.__

## Sjekkliste { .check}

+ Legg til en ny figur med valgfri drakt og kall den stempel. Vi valgte Scratch-logoen fra __ting__-mappen.
Krymp figuren og plasser den nederst på skjermen ved siden av de andre verktøyene.
Når figuren klikkes skal den sende meldingen __stempel__.
+ Legg til en ny drakt for blyantfiguren. Det skal være samme drakt som du nettopp ga stempelet.
+ Velg blyanten og legg til en ny variabel som bare gjelder for denne figuren.
Kall variabelen __stempelmodus__. 
Fjern avhukingen foran variabelen slik at den ikke vises på scenen. 
Oppgaven til denne variabelen er å holde styr på om vi skal tegne eller stemple.
+ Legg til et skript for blyanten som responderer på meldingen. 
Skriptet skal skifte drakt til den samme drakten du valgte for stempelet. 
Og så skal det sette verdien til __stempelmodus__ til på.

```scratch
	når jeg mottar [stempel v]
	bytt drakt til [scratch logo v]
	sett [stempelmodus v] til (på)
```

+ Forandre de andre skriptene som er knyttet til fargevelgerne og viskelæret
slik at de setter __stempelmodus__ til av. Eksempel (for viskelæret):

```scratch
	når jeg mottar [visk v]
	bytt drakt til [eraser v]
	velg pennefarge (grå)
	sett [stempelmodus v] til (av)
```

+ Til slutt må vi sjekke variabelen __hvis museknappen er nede?__ 
for å se om vi skal tegne eller stemple. Hvis stempelmodus er satt til på
skal vi stemple, hvis ikke skal vi bruke den eksiterende __penn på__.
 

```scratch
	når grønt flagg klikkes
	slett
	for alltid 
		hvis <<(mus x) > (-230)> og <(mus x) < (230)> og <(mus y) > (-120)> og <(mus y) < (170)>>
			gå til [musepeker v]
			vis
			hvis <museknappen er nede?>
				hvis <(stempelmodus) = (av)>
					penn på
				ellers
					stemple avtrykk
				(slutt hvis)
			ellers
				penn av
			(slutt hvis)
		ellers
			skjul
		(slutt hvis)
	(slutt for alltid)
```


## Test prosjektet ditt
__Klikk på det grønne flagget.__

Klarer du å lage avtrykk?
Hva skjer når du skifter tilbake til en av blyantene?


## Lagre prosjektet { .save}

__Veldig bra jobba! Du er nå ferdig med programmet.
Prøv disse utfordringene!__

## Utfordring 1: Regnbueblyant { .challenge}

I denne utfordringen skal du legge til en blyant som kan forandrer farge mens du tegner.
Kult, ikke sant?

## Sjekkliste { .check}

Først må du legge til regnbue-valget og regnbue-kostymen:

+ Legg til regnbue-selektoren som figur. Du finner den i mappen du lastet ned i starten (velg __rainbow-selector.gif__).
Sett den ved siden av de andre selektorene nederst til venstre.
Figuren skal sende meldingen __regnbue__ når den klikkes.
+ Legg til en regnbue-blyanten (__rainbow-pencil.png) som en ny drakt til blyanten.
Husk å justere midtpunktet.

+ Nå må du lage et skript som får blyantfargen til å skifte mange ganger i sekundet. 
(Vi fant ut at å endre den med 5 hvert 0.05 sekunder fungerer fint, men du bør prøve ut egne verdier).

__Hint:__ Scratch-kortet Timer/Tid viser hvordan du kan få noe til å forandre seg med
jevne mellomrom. Men i vårt tilfelle er det pennfarge, og ikke tid, som skal forandres.

Denne blokken må legges inn i en løkke. Men du trenger også noe å kontrollere
løkken med, så den bare endrer farge når regnbueblyanten er valgt.

__Hint:__ Du kan gjøre dette på en måte som ligner på hvordan stempelmodus styrte når
stempelet skulle skrus av og på. Prøv å lage en variabel som du kaller
regnbuemodus. La denne skrus på når regnbueblyanten klikkes, og av når de andre
velges.


## Test prosjektet ditt
__Klikk på det grønne flagget.__

Virker regnbueblyanten?
Hva skjer når du skifter tilbake til en av de andre blyantene?

## Lagre prosjektet { .save}

## Utfordring 1: Snarveier { .challenge}

Nå skal du få prøve å deg på å lage snarveier på tastaturet. Det betyr at man istedenfor å
klikke på knappene kan bruke tastene for å bytte farge, stemple eller viske ut.
Du kan bruke `hvis`{.blockyellow}` tast [] trykkes`{.blocklightblue} for å benytte tastaturet.
For hver tast du legger til trenger du en ny `hvis`{.blockyellow}` tast [] trykkes`{.blocklightblue}-blokk 
som sender samme meldingene som verktøy-valgene gjør når de klikkes. Legg til skriptene til scenen.

Vi brukte disse snarveiene:
* Slett alt - a
* Visk - v
* Rød blyant - r 
* Blå blyant - b
* Gul blyant - y
* Grønn blyant - g
* Regnbue blyant - w
* Stempel - s

## Test prosjektet ditt
__Klikk på det grønne flagget.__

Virker alle snarveiene? 
Virker knappene fremdeles også?

## Lagre prosjektet { .save}

## Utfordring 1: Større og mindre { .challenge}

En annen funksjon som tegneprogrammer gjerne har er å forandre størrelsen på
blyantstreken. Prøv å se om du får til dette.
Det er en ting som gjør dette vanskelig. Noen ganger trenger vi å endre
størrelsen på pennen og noen ganger trenger vi å forandre størrelsen på drakten.
Det er avhengig av om du bruker blyanten eller stemplet. 

+ Lag to nye figurer ved å importere bigger-selector og smaller-selctor fra mappen med ressurser.
Kall figurene __større__ og __mindre__.
+ La figurene sende ut meldingene __større__ og __mindre__.
+ Blyanten kan svare på meldingen ved å enten forandre pennestørrelsen med 1
eller kostymestørrelsen med 10, avhengig av verdien på __stempelmodus__.

__Hint:__ Du kan bruke en av endre-blokkene under Penn eller Utseende. For å forminske
setter du bare et minustegn foran tallet.

__Hint 2:__ For å holde styr på om det er blyantstørrelse eller stempel som skal endres må
du bruke en `hvis-ellers`{.blockyellow}-blokk

+ Glem ikke å lage snarveier for disse funksjonene også. For eksempel pil opp for
større og pil ned for mindre.


+ Har du lagt merke til at også blyantfiguren blir større når du forstørrer stempelet?
For å unngå dette kan vi sette størrelsen til 100% hver gang blyant klikkes.

+ For å gjøre det enda mer avansert kan du få stempelet til å huske størrelsen sin fra
gang til gang. Den enkleste måten å gjøre dette på er å opprette en variabel som du
kaller __stempelstørrelse__. Denne må oppdateres for hver gang størrelsen på stempelet
endres. Når man skifter fra blyant til stempel, bestemmes så størrelsen fra denne
variabelen.


## Test prosjektet ditt
__Klikk på det grønne flagget.__

Fungerer forstørrelsesknappen? Fungerer forminskingsknappen? 
Hva skjer om du bytter til stempelet, endrer størrelsen og så forandrer tilbake til
blyanten?


## Lagre prosjektet { .save}


__Veldig, veldig bra! Nå kan du tegne akkurat det du vil!__


Don’t forget you can share your game with all your friends and family by clicking on __Share__ on the menu bar!
