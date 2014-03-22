---
title: Ørkenløp
level: 1.6
language: nb-NO
stylesheet: scratch
embeds: ["*.png", "../../bilder/*.png"]
note: "README.md"
...

#Ørkenløp

# Introduksjon { .intro}
Dette er et spill for to, der en papegøye og en løve kjemper om å komme først gjennom ørkenen. Hver spiller må trykke en tast så fort og ofte som mulig for å flytte figuren sin, og den som kommer først til kanten av skjermen vinner.


![skjermbilde](orkenlop.png)

# Steg 1: Lage en scene og legg til figurer { .activity}

## Sjekkliste { .check}

+ Klikk på Scene og hent en ny bakgrunn fra biblioteket. Velg __Natur/desert__.
+ Fjern Sprite1 ved å høyreklikke på figuren og velg Slett.
+ Legg til en ny figur ved å trykke på ![Velg figur fra biblioteket](hent-fra-bibliotek.png). Velg __Dyr/Lionness__.
+ Legg så til enda en ny figur: velg Dyr/Parrot. Krymp figuren slik at den er omtrendt like stor som løvinnen ved å bruke ![Krymp](krymp.png).


# Steg 2: La løven og papegøyen bevege seg { .activity}

Vi vil at figurene skal bevege seg når du trykker på en knapp.

## Sjekkliste { .check}

+ Velg først løvefiguren og få den til å `gå (4) steg`{.blockblue} når du trykker __‘L’__ tasten.

    ```blocks
    når [l v] trykkes
    gå (4) steg
    ```

+ Velg så papegøyefiguren og la den `gå (4) steg`{.blockblue} når du trykker __‘A’__ tasten.

    ```blocks
    når [a v] trykkes
    gå (4) steg
    ```

## Test prosjektet { .flag}

__Trykk på det grønne flagget.__ 
Beveger løven og papegøyen seg over skjermen når du trykker på ‘A’ og ‘L’ tastene?

## Lagre prosjektet { .save}

# Steg 3: Start kappløpet { .activity}

__Nå må vi kjøre i gang kappløpet og kåre en vinner. Vi begynner med å lage startknapp.__

## Sjekkliste { .check}

+ Legg til en ny figur. Velg __Ting/Button3__. Flytt den til midten av scenen. 
+ Klikk på Drakter-fanen og symbolet T for å legge til tekst. Trykk på venstre kant av knappen for å legge til et tekstfelt og skriv inn teksten ‘start’. Du kan flytte på teksten ved å trykke en gang på den, og endre innhold ved å dobbeltklikke.
+ Legg nå til et skript som viser figuren når spillet starter:

    ```blocks
        når grønt flagg klikkes
        vis
    ```
+ I tillegg vil vi ha en knapp som teller ned fra 3, sier ‘LØP’ og deretter blir skjult når den klikkes. Dette ordner du med følgende skript:

    ```blocks
    når denne figuren klikkes
        si [3] i (1) sekunder
        si [2] i (1) sekunder
        si [2] i (1) sekunder
        si [LØP!] i (1) sekunder
        skjul
    ```

## Test prosjektet { .flag}

__Klikk på det grønne flagget__ og __trykk på startknappen__.
Teller knappen ned? Sier den ‘LØP’? Blir den borte?

## Lagre prosjektet { .save}

Vi ønsker at figurene bare beveger seg etter at kappløpet er startet og vi ønsker å vite når kappløpet er over.

+ For å vite når kappløpet har startet og sluttet lager vi en variabel med navnet `kappløp`{.blockorange}. Variabelen skal være tilgjengelig for alle figurer. Fjern avhukingen foran variabelen, slik at den ikke vises på scenen.
+ Sett __kappløp__ til __[0]__ når spillet startes. Forandre `når flagget klikkes`{.blockyellow} skriptet slik:

    ```blocks
    når grønt flagg klikkes
        vis
        sett [kappløp v] til (0)
    ```

+ Når nedtellingen er ferdig og løpet begynner, forandrer vi __kappløp__verdien til 1. Dette gjør du ved å legge til blokken `Sett [kappløp] til (1)`{.blockorange} under `si [1] i (1) sekunder`{.blockpurple} i skriptet som starter med `når denne figuren klikkes`{.blockyellow}.
+ Så må vi lage en regel som sier at figurene bare får lov til å bevege seg når løpet har startet – det vil si når kappløp har verdien 1. Klikk først på papegøyen. Så legger du til:

    ```blocks
	når [a v] trykkes
	hvis <(kappløp) = [1]>
		gå (4) steg
    ```
+ Gjenta det samme for løvinnen.

## Test prosjektet { .flag}
__Klikk på det grønne flagget.__

Kan løven og papegøyen bare flytte seg når nedtellingen er ferdig?

## Lagre prosjektet { .save}

# Steg 4: Avslutte kappløpet { .activity}

__Nå vil vi vite hvem som vinner kappløpet, og i tillegg gjøre klart for en ny runde.__

## Sjekkliste { .check}

+ Legg til en blokk i papegøyens skript som `setter [kappløp] til (0)`{.blockorange} hvis figuren berører kanten av skjermen.


    ```blocks
    når [a v] trykkes
    hvis <(kappløp) = [1]>
        gå (4) steg
        hvis (berører [kant v]?)
			sett [kappløp v] til (0)
    ```
+ Spill så inn en lyd som skal avspilles hvis papegøyen vinner.
Trykk på Lyder-fanen og deretter mikrofon-ikonet og spill inn en morsom trudelutt! Opptaket starter når du har klikket på rundingen slik at den blir rød. Klikk Stopp (firkanten) når du er ferdig, og gi den et navn – for eksempel Polly. Noen nettlesere kan spørre om tillatelse til å spille inn lyd. Hvis du ikke ønsker dette, bruk lydene som følger med figurene.
+ Deretter legger du til blokkene som vil spille lyden og la papegøyen fortelle at den vant:

    ```blocks
	    når [a v] trykkes
		hvis <(kappløp) = [1]>
			gå (4) steg
			hvis (berører [kant v]?)
				sett [kappløp v] til (0)
                spill lyden [Polly v]
                si [Polly vinner! v] i (3) sekunder  
    ```
	
+ Gjør det samme for løvinnen.

## Test prosjektet { .flag}
__Klikk på det grønne flagget.__

Kan du trykke på startknappen og deretter bevege dyrene med tastene __A__ og __L__?
Kommer riktig vinnerlyd og melding opp på skjermen?

## Lagre prosjektet { .save}

# Steg 5: Nullstill spillet { .activity}

__Når kappløpet er over må vi fortelle de andre figurene at spillet er over og nullstille spillet, slik at er klart for en ny runde.__

## Sjekkliste { .check}

+ Klikk på papegøyefiguren og legg til en blokk som sender melding ‘avslutt’ etter at figuren sier den har vunnet.


    ```blocks
	når [a v] trykkes
	hvis <(kappløp) = [1]>
		gå (4) steg
		hvis (berører [kant v]?)
			sett [kappløp v] til (0)
			spill lyden [Polly v]
			si [Polly vinner! v] i (3) sekunder
			send melding [avslutt v]
    ```

+ Vi trenger nå et nytt skript som lytter etter denne avslutningsmeldingen og flytter papegøyen tilbake til start.

    ```blocks
    når jeg mottar [avslutt v]
    sett x til (-170)
    ```
	
+ Legg til det samme skriptet for løven. Test forskjellige __x__-verdier for å være sikker på at løven og papegøyen starter fra samme sted.
+ For at figurene skal stå på startstreken når kappløpet starter den aller første gangen må vi også legge til følgende blokk til begge figurene: 

    ```blocks
    når grønt flagg klikkes
        sett x til (-170)
    ```
	
+ For at spillerne skal kunne klikke i gang nye runder må passe på at start-knappen kommer etter hver avsluttet runde. Klikk på figuren og legg til et skript som viser knappen når avslutningsmeldingen er mottatt.

    ```blocks
    når jeg mottar [avslutt v]
    vis
    ```

	
## Test prosjektet { .flag}

__Klikk på det grønne flagget.__

Kan du spille mot en venn? En av dere styrer papegøyen ved å trykke A, og den andre løven
ved å trykke L.

## Lagre prosjektet { .save}


##Utfordring 1: Legg til en rakett! { .challenge}

* __Legg til en rakett__ som kan brukes én gang per kappløp og som flytter papegøyen eller løven __30 steg på en gang.__
* __Legg til en ny drakt__  med ild som kommer ut bak hver figur. La denne aktiveres når raketten avfyres.
* __Lag en lyd__ som figuren kan gi fra seg når raketten avfyres.

    ```blocks
	når [a v] trykkes
		hvis <((kappløp) = (1)) og ((rakett) = (0))> 
			bytt drakt til [parrot-b v]
			sett [rakett v] til (1)
			gå (4) steg
			spill lyden [Rooster v]
			hvis (berører [kant v]?)
				sett [kappløp v] til (0)
                spill lyden [Polly v]
                si [Polly vinner! v] i (3) sekunder
				send melding [avslutt v]
	
    
## Test prosjektet { .flag}

## Lagre prosjektet { .save}

## Utfordring 2: Bruk egendefinerte blokker for å forenkle skriptet ditt { .challenge}

Koden som brukes til å sjekke om kappløpet er over brukes nå to steder for hver figur; når figuren beveger seg normalt og når den beveger seg med rakett.
Vi kan forenkle skriptet vårt ved å bruke en egendefinert blokk. Dette er en samling kode som brukes flere steder. Det er nesten som at vi lager vår egen Scratch kodeblokk!

+  Velg papegøyens skript.
+ Velg `Flere klosser`{.blocklightgrey}-paletten og klikk så på `Lag en kloss`{.blocklightgrey} knappen.
+ Kall klossen din __ferdig__ og trykk OK.
+ Du vil nå få en `definer ferdig`{.blockpurple} blokk i skriptvinduet ditt. Flytt den litt for seg selv. 
+ Løsriv `hvis`{.blockyellow} `berører [kant v]?`{.blocklightblue}` blokken og dra den til `definer ferdig`{.blockpurple} blokken.

    ```blocks
    definer ferdig
	hvis (berører [kant v]?)
				sett [kappløp v] til (0)
                spill lyden [Polly v]
                si [Polly vinner! v] i (3) sekunder
				send melding [avslutt v]
    
    når [a v] trykkes 
    hvis <<(kappløp) = (1)> og <(rakett) = (0)>>
		bytt drakt til [parrot-b v]
		sett [rakett v] til (1)
		gå (4) steg
		spill lyden [Rooster v]
    ```
	
Kan du dra `ferdig`{.blockpurple} blokken fra paletten og bruke den slik som andre kodebiter?

Slett den andre `hvis`{.blockyellow}` berører [kant v]?`{.blocklightblue} blokken fra skriptet ditt og erstatt den med en `ferdig`{.blockpurple} blokk.

Gjør dette koden din enklere å lese? Kan du lage en tilsvarende egendefinert blokk for løvinnen?

## Test prosjektet { .flag}

## Lagre prosjektet { .save}

__Veldig bra! Nå er du ferdig og kan nye spillet du har laget!__
