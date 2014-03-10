---
title: Frantic Felix
level: Nivå 6
language: nb-NO
stylesheet: scratch
embeds: "*.png"
...

# Introduksjon: {.intro}
I dette prosjektet skal du lage et komplett spill. Det er et plattformspill, hvor katten Felix hopper rundt, unnslipper slemminger og samler nøkler for å slippe ut av hulen. Når han kommer seg ut, fortsetter spillet i neste hule.

I del av dette prosjektet, kommer du til å lære hvordan vi får Felix til å flytte seg og samhandle med forskjellige ting. I uke to, skal du designe egne brett og nivåer. Til slutt skal du sette brettene sammen til et ferdig spill.

# Del 1: Lag byggeklossene 

__Plattformspill__, som __Manic Miner__ og __Mario Bros__, handler om en figur som beveger seg rundt i en verden og hopper inn i ting. Noen ting, som vegger, stopper deg. Andre ting, som slemminger, ta livet av deg. Ting som nøkler må du samle på. Andre ting er bakgrunner og påvirker ikke spillet i det heletatt.

Det betyr at det å vite når du har kommet bort i noe er viktig. Scratch har noen klosser for å oppdage at noe berører noe annet:
`berører sprite`{.blocklightblue}, `berører farge []?`{.blocklightblue}, `farge [] berører []?`{.blocklightblue}, og
`avstand til []`{.blocklightblue}. Men for å lage spillet, må du vite mer enn at to figurer har kommet borti hverandre; du trenger å vite hvilken __side__ som berøres. Hvis du går mot en vegg til venstre, kan du ikke gå lengre til venstre. Men du kan fortsatt gå til høyre, eller hoppe, eller falle ned hvis det ikke er noe gulv å stå på.

Hvis du berører en slemming, kan dette skade deg; men hvis du berører slemmingen med beina, kan du skade den. Ingen av de innebygde Scratchklossene kan si noe om __retningen av berøringen__. Så vi må bygge våre egne berøringssensorer.

# Oppgave 1: Berøringssensor {.activity}

Vi skal ha fire figurer som følger etter Frantic Felix. __Hver figur oppdager berøring i én retning og setter en variabel hvis det oppstår en berøring__. Hovedfiguren Felix bruker disse variablene for å kontrollere hvordan Felix kan bevege seg. Hver berøringssensor har en farget linje og bruker `farge [] berører [] ?`{.blocklightblue}-klossen for å oppdage ting. Vi bruker  __svart__ for gulvet og  __grønn__ for hinder. Vi bruker __rød__ for berøringssensorene.

## Sjekkliste {.check}
1. __Åpne et nytt prosjekt__. Legg til __frantic-felix/testlevel__ bakgrunnen og slett den hvite __background1__.
2. __Endre navn på figur Sprite1 til Felix__. Kontroller at drakten bare kan flippe venstre-høyre.
3. Lag fire nye figurer fra bildene __frantic-felix/top__, __frantic-felix/bottom__, __frantic-felix/left__, and __frantic-felix/right__. Disse figurene skal bli berøringssensor. Gi de nye figurene navnene __topp__, __bunn__, __venstre__, og __høyre__. Kontroller at draktene deres ikke kan flippes eller roteres.
4. Lag fire `variabler` (for hver av figurene): __blokkert topp__, __blokkert bunn__, __blokkert høyre__, og __blokkert venstre__.
5. Lag dette skriptet for hver av sensorene:

``` scratch
når grønt flagg klikkes // eksempel for høyre sensor
for alltid
	gå til [Felix v]
	hvis <farge [rød v] berører [grønn v] ?>
		sett [blokkert høyre v] til (1)
	ellers	
		sett [blokkert høyre v] til (0)
	slutt
slutt
```
6. Endre variablene for hver av sensorene.
Den nederste sensoren trenger en __eller__ kloss slik at den setter __blokkert bunn__ hvis den berører grønn eller svart.

__Tips__: Det er enklere å velge fargene i én figur, for så å kopiere skriptet over til de andre figurene og oppdatere variablene som blir satt. Da slipper du å finne de riktige fargene fire ganger.
Inntil videre trenger Felix bare et skript for å følge muspekeren evig.

## Test prosjektet {.flag}
__Trykk på det grønne flagget.__

Du burde se at Felix følger etter musepekeren, omringet av et rødt rektangel. Rektanglet er en berøringssensor. Hvis du følger med på variablene, ser du at de endrer seg når du drar Felix rundt og når han berører ulike deler av skjermen. For øyeblikket beveger Felix seg gjennom plattformene og grønne hindre. Det skal vi fikse nå.

## Lagre endringer {.save}
Husk å lagre endringer.

# Oppgave 2: Bevegelse, gulv og falling {.activity}

## Sjekkliste {.check}
1. Neste steg er å få Felix til å gå. Vi bruker __venstre__ og __høre piltast__ for å flytte ham venstre og høyre. Hvis han ikke står på et gulv, faller han ned (vi fikser hopping etterpå). Vi vil at når man trykker på venstre piltast, så skal Felix peke til venstre og flytter seg litt. Men vi vil ikke at han skal flytte seg hvis det er en hindring i veien.
2. Vi kunne brukt `når [tast] trykkes`{.blockgrey} for å få flytte Felix, men det gir en hakkete bevegelse. Det blir en mykere bevegelse hvis du bruker
`hvis tast [pil venstre] trykket?`-klosser i en `for alltid` løkke. Berøringsensorer betyr at vi må teste  __blokkert venstre__ variablen i `hvis`, og bruke en __og kloss__ slik at Felix bare beveger seg til venstre når man trykker på en tast og
__blokkert venstre__ er null. Vi må gjøre tilsvarende for bevegelse til høyre.
3. Vi kunne animet Felixs bein i samme block, men da beveger de seg for raskt. Gjør animasjonen i en egen `for alltid`-kloss under en annen `når grønt flagg klikkes` hatt.
4. Det siste vi må gjøre er å ordne __falling__. Hvis Felix ikke står på fast grunn vil vi at han skal falle ned. Det ordner vi med en `for alltid`-løkke under en `når grønt flagg klikkes` hatt.

```scratch
når grønt flagg klikkes // håndter flytting
for alltid
	hvis < <tast [pil venstre v] trykket?> og (blokkert venstre)=(0)>
		pek i retning (-90)
		gå (2) steg
        slutt	
	hvis < <tast [pil høyre v] trykket?> og (blokkert høyre)=(0)>
		pek i retning (90)
		gå (2) steg
	slutt
slutt

når grønt flagg klikkes // beveg Felix
for alltid
	hvis < <tast [pil venstre v] trykket?> eller <tast [pil høyre v] trykket?> >
	neste drakt	
	vent (0.1) sekunder 
	slutt
slutt

når grønt flagg klikkes // håndter falling
for alltid
	hvis <(blokkert bunn)=(0)>
		endre y med (-2)
	slutt
slutt
```

## Test prosjektet ditt {.flag}

__Bruk musen for å dra Felix et sted på scenen og trykk så på det grønne flagget__. Hvis Felix hopper til muspekeren, må du fjerne det skriptet!
Du bør kunne bruke venstre og høyre knaper for å få Felix til å gå fra side til side. Hvis han ikke står på gulvet, bør han falle sakte nedover.

5. Vi vil også at berøringssensorene ikke skal vises. Det er ikke mulig å bruke en skjult blokk, for da vil ingen berøringer bli detektert. Isteden, legg til en `set [ghost] effect to 100` rett under den grønn flag hatt'en i hver kollisjonssensor. Dette gjør figuren gjennomsiktig, uten å å skjule den.

## Test prosjektet ditt {.flag}
__Nå du klikker på det grønne flagget__, skal kollisjonssensorene forsvinne. De dukker opp igjen når du trykker på det røde stopskiltet.

## Lagre endringer {.save}
Husk å lagre endringer.

# Oppgave 3: Hopping {.activity}

__Det er et par utfordringer med hopping.__

* Vi vil ikke at Felix __faller__ hvis han er _på vei opp__.
* Vi vil ikke at Felix skal hindres av gulv når han er på vei opp, men vi vil fortsatt at han skal stoppes av gulvet når han __er på vei ned__.
* Vi vil ikke at Felix skal  __hoppe opp_ i undersiden av et __grønt hinder__.
* Vi vil at hoppet skal være en myk bevegelse, så vi vil ikke at Felix flytter seg mye for raskt.
* Felix skal bare kunne hoppe hvis han __står på gulvet__. Spiller blir litt for enkelt hvis Felix kan hoppe fra løse luften.

## Sjekkliste {.check}
1. Det som gjenstår nå, er å få Felix til å hoppe. La oss bruke __mellomromstasten__ for å få Felix til å hoppe.
2. For å kontroller hoppet, bruker vi en ny 'variabel', __hopphøyde__. Hvis denne er høyere enn null, er Felix på vei opp. Hvis den er null, faller han (eller har falt), som beskrevet over.
3. Vi vil at Felix skal hoppe opp til __100 pixeler__. Legg til en ny hvis-kloss inni `for alltid`-klossen som håndterer tastetrykk. Hvis vi trykker __mellomromstasten__ og Felix står på gulvet (variablen __blokkert under__ er satt til 1, så setter vi __hopphøyde til 100__.
4. Vi må endre falle-skriptet. I `for alltid`, trenger vi en `hvis-ellers`-kloss som oppdater hvis Felix hopper opp eller ikke. Kravet for denne `hvis-ellers`-klossen er hvis __hopphøyde__ er __større enn null_. Den eksisterende faller ned `hvis`-klossen går inn ellers delen av den nye `hvis-ellers`-klossen.
5. Når vi vet at Felix hopper opp, må vi sjekke om hodet han treffer noe. Hvis __blokkert topp__ er __1__, sett __hopphøyde__ til  __null__. (Dette gjør at Felix ikke kan hoppe inn i hindringer). __Ellers, flytt Felix opp 10 og reduser hopphøyde med ti.__
6. Du ender opp med noe tilsvarende dette:

```scratch
når grønt flagg klikkes // håndtere falling
for alltid
	hvis <(hopphøyde)=(0)>
		hvis <(blokkert topp)=(1)>
			sett (hopphøyde) til (0)
		ellers	
			endre y med (10)
			endre [hopphøyde v] med (-10)
		slutt
	ellers	
		hvis <(blokkert bunn)=(0)>
			endre y med (-2)
		slutt
	slutt
slutt
```

## Test prosjektet ditt {.flag}
__Trykk på det grønne flagget__. Kan Felix hoppe? Hopper han fra en plattform til en annen? Faller han hvis han går over kanten? Hva om han oppover over kanten av en plattform? Hva om han prøver å hoppe under den grønne blokken til høyre? Hva skjer når du trykker på mellomromstasten mens Felix faller?

## Lagre endringer {.save}
Husk å lagre endringer.

# Oppgave 4: Nøkler og mål {.activity}

__Vi har klart å få Felix til å bevege seg rundt i verdenen. Nå må vi få han til å klare ett nivå__.
Vi plasserer tre nøkler rundt i hulen. Felix kan plukke dem opp ved å gå til dem. Når han har samlet alle tre, kan han klatre til en rediningskapsel og redde seg selv ut av hulen.

1. Vi lager en ny `variabel`, __nøkler igjen__, som holder orden på hvor mange nøkler som gjenstår. Et nytt skript på __scenen__ skal sette denne til __3__ når det __grønne flagget__ klikkes.
2. Både nøklene og redningskapselen må være figurer. (Bruk __frantic-felix/key__ for nøklene og __frantic-felix/escape-pod__ for the kapselen.)
3. Hver nøkkel trenger __to skript__: det første plasserer nøklen på riktig sted, med størrelse og vinkel, og en `for alltid` løkke for å endre fargen (som gjør det enklere å se den på skjermen). Det andre skriptet er en `forever if` løkke som venter til Felix kommer bort til nøkkelen. Når dette skjer, skjuler skiptet nøkkelen og reduserer antall nøkler.
4. Redninigskapselen er et litt vanskeligere skirpt. Den bruker en `forever if` blokk for å vente på at __keys to get__ blir __null__. Med en gang dette skjer, begynner kapselen å blinke (for å vise spilleren at
de kan komme seg ut). Så kan vi bruke
en annen `if` for å oppdage når Felix berører den blinkende redningskapselen. Så snart han gjør det, sender kapselen en du vinner melding og sier “Du vant!”. Felix svarer på meldingen ved å gjemme seg.

```scratch
når grønt flagg klikkes
gå til x:(220) y:(-125)
for alltid
	hvis <(key to get) = (0)>
		endre [farge v] effekt med (25)
		hvis <berører [Felix v]?>
			send melding [seier v]
			si [Du vant!]
		slutt	
	slutt
slutt
```

## Test prosjektet ditt {.flag}
__Trykk på det grønne flagget__.

## Lagre endringer {.save}
Husk å lagre endringer.

# Oppgave 5: Slemmnger og dødlige omgivelser {.activity}

__Nå er det på tide med slemminger!__

Det skal være to typer farlige ting. En type vil være slemminger som går rundt og skader Felix hvis kan krasjer inn i dem. Den andre typen er farlige ting i bakgrunnen.

__La oss først lage en slemming. Den vil bare bevege seg langs en fast sti.__

## Sjekkliste {.check}
1. __Lag en ny figur__, bruk hvilken som helst drakt. Den bør være samme størrelse som Felix (Vi brukte __things/flower-vase__ drakt, og gjorde den fire steg mindre). Slemmingen trenger bare et enkelt skript som beveger den og oppdager om den berører Felix.
2. Lag tre `if` uttrykk inni en evig løkke. Den første sjekker om en slemming berører Felix; hvis den gjør det, sender den en `broadcasts` __lose__ melding. De to andre `if`'ene sjekker om slemmingen har nådd slutten av stien; hvis den har, snur slemmingen. Tilslutt, tar slemmingen to steg. (Ved å bruke __move__ isteden for __glide__ blokker gjør det enklere å kontrollere hvor raskt slemmingen går.)
__Vi trenger ikke å bruke kollisjonssensor her, da vi ikke bryr oss om hvilken side Felix berører slemmingen.__

```scratch
når grønt flagg klikkes
gå til x:(-50) y:(47)
pek i retning (-90)
for alltid
	hvis <berører [Felix v]?>
		send melding [tap v]
	slutt
	hvis < (x-posisjon) > (-200) >
		pek i retning (90)
	slutt
	hvis < (x-posisjon) > (-50) >
		pek i retning (-90)
	slutt
	gå (2) steg
slutt
```

3. Legg skript til både Felix og redningskapselen slik at den svarer på tap meldingen. Felix skal bare skjule seg selv.  Kapselen skal si [Du tapte!].

## Test prosjektet ditt {.flag}
__Trykk på det grønne flagget__. Beveger vasen seg? Stopper den og snur ved kanten? Hva skjer når Felix går inn i den? Hva skjer hvis Felix hopper på den, fra oversiden eller undersiden? Forsvinner Felix? Sier kapselen ifra når du har tapt? Kan du forsatt vinne spillet?

## Lagre endringer {.save}
Husk å lagre endringer.

4. __Neste, farlige ting!__ La oss si at alt som er lyseblå er dødlig for Felix. Last inn bakgrunnen __frantic-felix/level2__, som har en blå rose på det øverste nivået. Legg til enda et skipt på Felix, under et grønnt flagg hatt:
`<forever if touching [blue] broadcast [tap]>`

## Test prosjektet ditt {.flag}
__Trykk på det grønne flagget__. Dør Felix hvis han kommer borti den blå rosen? Hva skjer når han berører andre ting?

## Lagre endringer {.save}
Husk å lagre endringer.

## Oppsummering

__Det du har laget nå er et veldig enkelt plattformspill. Akkurat nå, er det et ganske kjedelig spill. Men det er ikke poenget. Dette spillet er en verktøykasse som du kan bruke til å lage egne spill og brett. I neste del skal du lage egne brett.__

## Del 2: Brettdesign

__Forrige gang bygde du alle delene et plattformspill består av. Nå skal du bruke disse
delene for å lage egne brett..__

Kort oppsummert gjorde du:

* Felix kan gå til venstre og høyre og han kan hoppe.
* Felix faller ned hvis han ikke står på gulvet.
* Felix kan ikke gå igjennom grønne hinder.
* Blå ting i bakgrunnen og slemminger tar livet av Felix.
* Slemminger beveger seg i faste ruter.
* Slemminger kan ta livet av Felix hvis han kommer borti dem.
* Felix kan samle nøkler ved å gå bor til dem.
* Når Felix har samlet alle nøkklene, kommer en redningskapsel tilsyne og han kan rømme i sikkerhet (eller til neste nivå).

Dette kan være byggeklossene dine. __Bruk dem til å lage egne brett.__

Du kan lage en hel trekke med brett som Felix må klare. Neste gang skal vi se på hvordan vi kan knytte brettene sammen.
Brett kan ha store eller små plattformer, mange eller få plattformer. Det kan være mange slemminger eller ingen. Det kan være mange hindringer eller dødlige ting i bakgrunnen. Prøv å lage flere måter man kan klare brettet på, selv om en kanskje er enklere enn andre. Tenk over hvor vanskelig eller enkelt brettet er.

Du kan endre de spesielle fargene (svart, grønn og blå), men da må du __oppdatere fargeberøringsblokkene__ i alle skriptene, men det må være samme farge i alle brett. (Du kunne ha forskjellige farger i forksjellige brett, men det betyr at du må legge inn mange `or` blokker rundt fargeberøringsblokkene.)

__Test brettene dine__. Hvis du har tid, opprett brett i Scratch og spill dem. Sjekk at de ikke er __for vanskelig__ og __ikke for enkle__. Hvis du programerer brettene, må du __lagre bakgrunnen du lager__ og noter __start posisjon__ for Felix, nøkler, og eventuelle slemminger. I tillegg må du huske retningen slemmingen beveger seg i og hvor langt de går.

Hvis du har laget et par brett og lagt dem inn i Scratch, prøv disse ekstraoppgavene:

## Utvidelse: Tramping {.try}

__Hva om slemmingene døde hvis de blir trampet på?__ Kanskje du kan legge til et skript på slemmingene som gjør noe hvis slemmingen berører den nederste kollisjonssensoren.

## Utvidelse: Kraftpiller {.try}

__Du kan lage en “kraftpille” som gjør at Felix kan ødelegge slemmingene__. Når Felix tar kraftpillen, ødelegger Felix slemmingene han berører. Effekten går over etterhvert

Det er opp til deg hvordan du får dette til å fungere. Kanskje vil du at slemmingene skal endre utseende når Felix kan ta dem.

## Test prosjektet ditt {.flag}
__Trykk på det grønne flagget__.

## Lagre endringer {.save}
Husk å lagre endringer.

## Del 3: Sett sammen spillet

__Nå har du noen brett. Du har nok verktøy til å få dem til å fungere. Det siste vi må gjøre er å sette delene sammen til et ferdig spill!__ Hvis du klarer å sette sammen brettene kjapt, kan du ta en titt på aktivitet 2 and 3 før du begynner å spille spillet ditt.

# Oppgave 1: Vise et nytt brett{.activity}

__Når Felix klarer ett brett, må vi flytte til neste__. Det betyr at vi må få redningskapselen til å sende en __start level message__ (isteden for seier meldigen) når Felix har funnet alle nøklene og klatret inn i kapselen. Vi kan bruke start brett melding for å klargjøre neste brett. Vi trenger også en `variable`, __current level__, som settes av redningskapselen før den sender __start level__ melding.

Alt må stort sett svare på __start level__ meldinger for å klargjøre neste brett.

__Scenen__ trenger å vise riktig bakgrunn. Hver av slemmingene, alle nøkler, og redningskapselen trenger å flytte til __correct positions__. Slemmingene rute trenger __updating__. Felix må flyttes til sin __new starting position__. Først da er brettet klart til start.

De fleste figurene må svare på __start level melding__ isteden for det grønne flagget. Det betyr at du må __endre hatt klossenes__ i de fleste skript.

## Lagre endringer {.save}
__Før du gjør noe må du lage__. Du kommer til å gjøre mange endriger i spillet, så husk å lagre regelmessig.

## Test prosjektet ditt {.flag}

__Fortsett å teste spillet etter hver endring. Husk å test de delene som har allerede har endret, slik at de fortsatt virker som planlagt.__ Vi kommer ikke beskrive alle endringene, men vi skal vise hvordan Felixs oppdaterte skript for å vise hva som må gjøres.

```scratch
når jeg mottar [start brett v]
gå til x:(element [nåværende nivå v] av [xs v]) y: (element [nåværende nivå v] av [ys v])
pek i retning (element [nåværende nivå v] av [retning v])
vis
for alltid
	hvis <<tast[pil venstre v] trykket?> og <(blokkert venstre)=(0)>
		pek i retning (-90)
		gå (2) steg
	slutt
	hvis <<tast [pil høyre v] trykket?> og <(blokkert høyre)=(0)>
		pek i retning (90)
		gå (2) steg
	slutt
	hvis <<tast [mellomrom v] trykket?> og <(blokkert bunn)=(1)>
		sett [hopphøyde v] til (100)
	slutt
slutt
```

Du legger kanskje merke til at start verdiene __x__, __y__, og __retning__ for Felix settes med lister. Vi laget noen lister for hver figur (hver liste privat til den figuren) for å lagre verdiene vi trenger for den figuren. Du trenger en liste for hver ting du lagrer. Du trenger ikke bruke lister, du kan bruke `if` blokker som sjekker hvilket brett du er på og gjør riktig ting basert på dette.

Og her er redningskapselen, som håndterer all nivå-endringen:

```scratch
når grønt flagg klikkes
sett [nåværende nivå v] til (1)
send melding [start brett v]

når jeg mottar [start brett v]
gå til x: (element [nåværende nivå v] av [xs v]) y: (element [nåværende nivå v] av [ys v])
for alltid
	hvis <[keys to get v] = (0)>
	endre [farge v] effekt med (25)
		hvis <berører [Felix v]?>
			hvis <[nåværende nivå v] = <lengden av [nøkler per brett v]>
				si [Du vant!!]
				send melding [seier v]
				stopp [alle v]
			ellers
				endre [nåværende nivå v] med (1)
				send melding [start brett v]
			slutt
		slutt
	slutt
slutt
```

# Oppgave 2: Spill! {.activity}

__Du har laget spill__. De andre i kodeklubben har laget spill. Spill de forskjellige spillene! Klarer du å runde deres spill? Kan de andre runde spillet ditt?

## Utvidelse 1: Flere liv {.challenge}

Felix trenger kanskje et par sjanser, eller et par liv for å klare seg igjennom brettene. __Legg til en ny figur__ med tre drakter, som viser __ett__, __to__, og __tre hjerter__.
Bruk frantic-felix/1-heart, frantic-felix/2-heart, and frantic-felix/3-heart draktene. Plasser figuren i hjørnet av scenen. Når det __grønne flagget__ blir trykket, skal det vises tre hjerter. Hver gang det mottar en tap melding, skal det vises et hjerte mindre. Isteden for å vise ingen hjerter, skal figuren skjules og sende en __slutt over__ melding.

__spill slutt__ og __seier__ meldinger bør håndteres av en __ny figur__, som __skjules__ når det grønne flagget trykkes og viser riktig plakat når __spill slutt__ og __seier__ meldinger sendes. Denne figurer skal også stoppe alle skript når den vises seg selv.

Du må endre hvordan redningskapselen håndterer vinning og tap, da dette er ansvaret for liv og ferdigplakat figurene.

Kanskje er slemmingen litt for kjappe på foten, de tar Felix før brettet er kommet igang. Hvis Felix taper mer enn et liv når han kommer borti en slemming, __skjul__ slemmingen så snart den sender __lose__ meldingen. Det gir resten av spillet (inkludert Felix) å nullstille før slemmingene oppdager en ny kollisjon med Felix.

## Utvidelse 2: Tidsbegrensninger {.challenge}

__Ta tiden på Felix!__ Bruk et __Timer Scratchkort__ for å legge til en tidsbegrensning. Hvis timeren løper ut, sender den __lose__ melding. Husk å __nullstille timeren__ når et nytt brett starter.
