---
title: Enarmet Banditt
level: 1.4
language: nb-NO
stylesheet: scratch
embeds: ["*.PNG", "*.png", "../../bilder/*.png"]
...

# Introduksjon {.intro}
Dette er et spill med tre figurer som endrer utseende. Spillerens oppgave er å stoppe figurene én etter én, slik at alle blir like. 

![](skjermbilde.png)

# Steg 1: Lag en figur som bytter drakt {.activity}

*La oss importere de bildene vi trenger for spillet*

## Sjekkliste { .check}

+ __Start et nytt Scratch-prosjekt__. __Slett katten__ ved å høyreklikke og velge `slett`.
+ Importer __en ny figur__, ![Velg figur fra biblioteket](figur-fra-bibliotek.png). Velg den figuren du vil.
+ Gå til `Drakter`{.blocklightgrey}, og importer to ekstra drakter fra biblioteket, så figuren til sammen har tre drakter.

# Steg 2: Få figuren til å rullere {.activity}

*Nå som figuren har noen drakter, ønsker vi at den skal veksle mellom dem.*

## Sjekkliste { .check}

+ Klikk på `Skript`{.blocklightgrey}-fanen,
+ Velg `Hendelser`{.blockgrey} og hent en `Når grønt flagg klikkes`{.blockgrey}-blokk. Denne vil kjøre hver gang du klikker på det grønne flagget over scenen.
+ Hent en `for alltid`{.blockyellow}-blokk fra `Styring`{.blockyellow}-kategorien og legg den under den andre blokken slik at den fester seg til den.
+ __Klikk på det grønne flagget__. Du ser at du får en hvit linje rundt skriptet. Det betyr at skriptet kjører.
+ Velg nå `Utseende`{.blockpurple} og dra en `neste drakt`{.blockpurple}-blokk inn i `for alltid`{.blockyellow}-blokken.
+ __Hvordan kan vi få draktbyttet til å gå saktere?__ Velg `Styring`{.blockyellow} og dra inn en `vent (1) sekunder`{.blockyellow}-blokk. 
+ Tilpass tiden til figuren endrer drakt i et hurtigere tempo (0.5 sekunder ser bra ut). Hva tror du ville skjedd om vi ikke hadde med `vent`{.blockyellow}-blokken?

    ```blocks
        Når grønt flagg klikkes
        for alltid
            neste drakt
            vent (0.5) sekunder
    ```

## Test Prosjektet { .test}
__Klikk det grønne flagget.__

+ Endrer figuren drakt i et fornuftig tempo? 

## Ting å prøve { .try}
Tilpass tiden i `vent`{.blockyellow}-blokken. Hvilke tall gjør spillet for vanskelig eller for lett?

# Steg 3: Frys ruletten! {.activity}

## Sjekkliste { .check}

**Bra! Vi kan få draktene til å bytte i det uendelige, 
men hvordan får vi de til å stoppe når vi klikker på det?**
En måte å gjøre dette på er ved å bruke en variabel som setter statusen til figuren. Dette vil også være praktisk senere...

1. Klikk på `Data` {.blockgrey} og `lag en ny variabel`{.blocklightgrey}. Kall den `stoppet`{.blockorange} og huk av for `For denne figuren`{.blocklightgrey}. Fjern avhukingen foran variabelen slik at den ikke vises på scenen.
2. På starten av spillet vil ikke figuren ha blitt klikket så da setter vi variabelen til **0**.

    ```blocks
    Når grønt flagg klikkes
    sett [stoppet v] til (0)
    for alltid 
        neste drakt
        vent (0.1) sekunder
    ```
3. Nå vil vi sette variabelen `stoppet`{.blockorange} til  **1** når noen trykker på figuren.  

    ```blocks
    når denne figuren klikkes
    sett [stoppet v] til (1)
    ```
4. Til slutt må vi få figuren til å slutte å forandre drakt når variabelen 
 `stoppet`{.blockorange} blir "1". Legg til en `hvis` { .blockyellow}-løkke 
 og bruk en **er lik** `[] = []` {.blockgreen} operator blokk
(se under *Operatorer*) for å sjekke om `stoppet`{.blockorange} fremdeles er "0".

    ```blocks
    Når grønt flagg klikkes
    sett [stoppet v] til (0)
    for alltid
        hvis <(stoppet) = [0]>	
            neste drakt
			vent (0.1) sekunder
    ```

## Test prosjektet{ .flag}
__Klikk på det grønne flagget, vent et øyeblikk og klikk så på figuren.__ 

Endres drakten før du klikker på den?

Stopper den når du klikker på den?


__Start skriptet igjen.__ 

Stopper den når du setter pekeren over den uten å klikke? 

Stopper den når du klikker andre steder på scenen eller andre steder i Scratch?

## Lagre prosjektet { .save}

# Steg 4: Lag de andre figurene {.activity}
__Nå trenger vi to figurer til for å gjøre spillet komplett!__

## Sjekkliste { .check}

1. **Dupliser figuren din** (Figuren) ved å høyreklikke og velg `lag en kopi`{.blocklightgrey}.
2. Lag en kopi til slik at du har tre figurer på skjermen. Vi har kalt våre figurer Figur1, Figur2 og Figur3.
3. Flytt figurene slik at de er en linje. Gjør dem mindre med krympeknappen hvis det
trengs med ![krymp](krymp.png).

## Test prosjektet{ .flag}
__Klikk på det grønne flagget.__ alle figurene skal nå forandre seg. 
Prøv å stoppe dem, én for én!

## Lagre prosjektet { .save}

# Steg 5: Start hver figur med en tilfeldig drakt { .activity}
__La oss få figurene til å skifte til en tilfeldig drakt når det grønne flagget klikkes.__

Når du starter spillet rett vil du se at alle figurene skifter drakt samtidig.
Spillet vil bli mer gøy (og vanskeligere) dersom de endres litt mer uforutsigbart.


## Sjekkliste { .check}

1. Hvis du ser under `drakter`{.blocklightgrey}-fanen
til en figur vil du se at hver drakt har et nummer.
Du kan spesifisere hvilken drakt figuren skal ha ved å bruke navnet eller nummeret.
2. For å få figuren til å starte med en tilfeldig drakt, 
la oss legge til en `bytt drakt til` { .blockpurple} blokk med 
 `tilfeldig tall fra (1) til (3)` { .blockgreen} for å velge draktnummer.
3. Vi kan også bruke samme blokken i `for alltid`{.blockyellow} løkka
slik at figuren skifter til en ulik drakt hver gang den forandres. 


    ```blocks
    Når grønt flagg klikkes
    sett [stoppet v] til (0)
	bytt drakt til <tilfeldig tall fra (1) til (3)>
    for alltid
        hvis <(stoppet) = [0]>	
            bytt drakt til <tilfeldig tall fra (1) til (3)>
			vent (0.1) sekunder
    ```

4. Gjør det samme for hver av figurene. 

## Test prosjektet{ .flag}
__Klikk på det grønne flagget.__ 
Alle figurene burde skifte drakter uforutsigbart.

Hvordan må vi forandre skriptet dersom vi legger til en annen drakt?

 
## Lagre prosjektet { .save}

## Ting å prøve{ .try}
 
 __Gjør spillet vanskeligere!__ 


Se om du klarer å endre vanskelighetsgraden på et eller annet vis. Å få draktene til å rullere
raskere er enkelt. Prøv å gjøre noe litt mer oppfinnsomt. Noen muligheter du kan tenke på er:

+ Endre antall drakter hver figur har.
+ Gi noen av figurene helt forskjellige drakter.
+ Endre tid mellom draktbytte.

__Lek og kom opp meg egne idéer!__

Hver gang du endrer noe, tenk på om det vil gjøre spillet lettere eller vanskeligere. Er spillet for lett
eller for vanskelig? Hvordan kan du justere det slik at det blir akkurat passe?


## Steg 6: Vis en melding når spillet er over { .activity}
__La oss vise en "Game Over" melding når spillet er over__

## Sjekkliste { .check}

La oss først hente en ny bakgrunn som vi viser når spillet er over.

1. Klikk på scenen og så `Bakgrunnen`{.blocklightgrey} fanen. Forandre navnet til den eksisterende bakgrunen til **"GameOn"**. 
2. Dupliser bakgrunne og legg til en tekst som sier **"Game over"**. Du kan forandre størrelsen på teksten ved å klikke på den og dra i hjørnene. Kall bakgrunnen **"GameOver"**.
3. Klikk på `Skript`{.blocklightgrey} fanen for bakgrunnen og sett "GameOn" bakgrunne til å vises når spillet starter.
4. Hvordan kan vi se at alle figurene har stoppet? Husk at vi brukte `stoppet`{.blockorange} variabelen til å sjekke om figurene hadde blitt klikket på. La oss sjekke `stoppet`{.blockorange} variabelen for **Fruit3** figuren (din figur nr.3 kan ha et annet navn) for å se om spillet er over. Velg den tredje frukten og bruk en `x-posisjon av Figur3`{ .blockblue} blokk fra `Sansing`{.blocklightgrey}, men bytt ut **x-posisjon** med `stoppet`{.blockorange}.
	
    ```blocks
	Når grønt flagg klikkes
	bytt bakgrunn til [GameOn v]
    for alltid
        hvis <([stoppet v] av [Figur3 v])  = [1]>	
            bytt bakgrunn til [GameOver v]
    ```

## Test prosjektet{ .flag}
__Klikk på det grønne flagget.__ 
Vises "Game Over" meldingen når du trykker på Figur3?

Hva skjer dersom du stoppet Figur3 før du har klikket begge den andre fruktene?
La oss forandre skriptet slik at det vil funke uansett hvilken rekkefølge figurene stoppes i.

5. For å sjekke om __alle tre__ fruktene har satt sine `stoppet`{.blockorange} variabler til **1**, kan vi bruke `og` {. blockgreen} operatoren. 
Dette er en komplisert blokk som kan være litt trøblette å lage, så forsøk å gjøre ett steg av gangen. 

    ```blocks
	Når grønt flagg klikkes
	bytt bakgrunn til [GameOn v]
    for alltid
		hvis <<<([stoppet v] av [Figur3 v])  = [1]> og <([stoppet v] av [Figur2 v])  = [1]>> og <([stoppet v] av [Figur1 v])  = [1]>>
            bytt bakgrunn til [GameOver v]
    ```

## Test prosjektet{ .flag}
__Klikk på det grønne flagget.__ 
Vises "Game Over" meldingen når alle tre fruktene er stoppet uansett hvilken rekkefølge du klikket på de?

## Lagre prosjektet { .save}

# Steg 7. Fortell spilleren om de vant eller tapte. { .activity}

__Målet med spillet er å klikke på figurene slik at de stopper når de viser samme drakten. Det ville være praktisk å vise en melding som forteller deg om du vant eller tapte.__

## Sjekkliste { .check}

1. Vi har tidligere skrevet kode som sjekker om spillet var over, så alt vi trenger å gjøre er å sjekke om spilleren har vunnet.
Gå tilbake til bakgrunnene og legg til mer tekst til GameOver bakgrunne slik at den også viser **"Du vant!"**. Skift navn til **"vinner"**.
2. Kopier bakgrunne og legg til en tekst hvor det står **"Du tapte"**. Gi bakgrunnen navnet **"taper"**.
3. Nå trenger vi kode for å velge hvilken bakgrunn vi skal vise når spillet er over.
Vi kan bruke en `hvis...ellers` { .blockyellow} blokk for å se om brukeren har vunnet eller tapt ved å sammenligne `drakt nr.`{.blockpurple}  
(drakt nummer). Vi bruker en blokk som ligner på `x-posisjon av Figur` { .blockblue} blokken vi brukte tidligere. 
Denne gangen, istedet for å se på `stoppet`{.blockorange} variabelen, skal vi sjekke `drakt nr.`{.blockpurple}  
og se om Figur1 har samme drakt som Figur2 og om Figur2 har samme drakt som Figur3.
 

    ```blocks
	Når grønt flagg klikkes
	bytt bakgrunn til [GameOn v]
    for alltid
        hvis <<<([stoppet v] av [Figur3 v])  = [1]> og <([stoppet v] av [Figur2 v])  = [1]>> og <([stoppet v] av [Figur1 v])  = [1]>>	
			hvis <<([drakt nr. v]  av [Figur1 v]) = ([drakt nr. v]  av [Figur2 v])> og <([drakt nr. v]  av [Figur2 v]) = ([drakt nr. v] av [Figur3 v])>>
				bytt bakgrunn til [vinner v]
			ellers
				bytt bakgrunn til [taper v]
    ```
 
## Test prosjektet{ .flag}
__Klikk på det grønne flagget.__ Vises den riktige meldingen når spillet er over? Hva skjer hvis draktnummerene ikke er like?

## Lagre prosjektet { .save}
   
__Veldig bra! Du har nå fullført spillet, men det er fremdeles ting du kan gjøre med spillet ditt. Prøv deg på disse utfordringene!__

## Utfordring: Gjør spillet enklere og vanskeligere med tiden { .challenge}

Alle er ikke like flinke til spillet. __Hvordan kan du la vanskelighetsgraden avhenge av spilleren?__

En måte å gjøre dtete på er å __endre hastigheten draktene forandres på__. Du kan bruke en variabel kallt `forsinkelse`{.blockorange}, for å gi varigheten til hver figurs venteblokk. 
Hvis spilleren vinner runden kan forsinkelsen reduseres litt (for å gjøre spillet vanskeligere).
Hvis spilleren taper runden kan man øke forsinkelsen litt for å gjøre spillet lettere.

Du må sikkert vurdere å bruke en annen måte å starte spillet på istedet for å bruke `når grønt flagg klikkes`{.blockyellow}.
Deretter kan du lagre verdiene i variabler som huskes mellom rundene.

## Lagre prosjektet { .save}

__Godt gjort, du er ferdig! Nå kan du nyte spillet ditt!__
Ikke glem at du kan dele spillet med alle vennene og familien din ved å klikke på __Legg ut__ i topp-menyen!




