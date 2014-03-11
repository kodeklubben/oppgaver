---
title: Hva er det?
level: 1.7
language: nb-NO
stylesheet: scratch
embeds: ["*.PNG", "../../bilder/*.png"]
...

# Introduksjon { .intro}

Et bilde av en tilfeldig ting vises på tavlen. Men bildet er forvrengt, slik at du må gjette hva det er ved å klikke på et av alternativene som vises under. Desto raskere du gjetter riktig, desto flere poeng får du.


![skjermbilde](hvaerdet.PNG)

#Steg 1: Få flere ting til å vise seg på tavlen { .activity}
__Vi vil at noen forskjellige bilder skal komme opp på tavlen.__

## Sjekkliste { .check}

+ Start et nytt Scratch-prosjekt og slett kattefiguren.
+ Klikk på Scene og deretter Bakgrunner-fanen. Åpne biblioteket med bakgrunner ved å trykke på ![Velg en ferdig bakgrunn](velg-bakgrunn.png) og velg så __Innendørs/chalkboard__.
+ Importer en valgfri figur. Velg gjerne en fra Ting-mappen.
+ Plasser figuren på midten av tavlen, og endre størrelsen hvis den ikke passer.
+ Legg til fire nye drakter fra Ting-mappen. Du kan velge hva du vil!
+ La oss nå få en tilfeldig ting til å dukke opp. Bruk dette skriptet. 

    ```blocks
        når grønt flagg klikkes
        gjenta (tilfeldig tall fra (1) til (5)) ganger
            neste drakt
		slutt
    ```

##Test prosjektet { .flag}
__Trykk på det grønne flagget.__
Endrer figuren seg? Klikk flere ganger. Får figuren stadig nye drakter? Flott. 

Det gjør ingenting om samme drakt kommer opp flere ganger på rad. Det er helt normalt når det trekkes en tilfeldig drakt hver gang. 
Du legger kanskje merke til at det flimrer litt når drakten skiftes? Det skal vi fikse i neste steg.


##Lagre prosjektet {.save}

#Steg 2: Forvreng bildet {.activity}

__La oss nå forvrenge figuren når den dukker opp på tavlen, så det blir vanskeligere å gjette hva det er. Deretter skal vi gradvis gjøre vi den tydeligere igjen.__

Vi skal bruke en poeng-variabel til å kontrollere graden av forvrenging. Dersom poengscoren er høy vil bildet bli veldig forvrengt. Når antallet poeng synker, vil også graden av forvrenging synke. Poengvariabelen fungerer dermed som en tidteller.

## Sjekkliste { .check}

+ Velg Data-paletten og opprett en variabel kalt __poeng__. 

+ Endre skriptet slik:

    ```blocks	
		når grønt flagg klikkes
		skjul
		gjenta (tilfeldig tall fra (1) til (5)) ganger
            neste drakt
        slutt
        sett [poeng v] til (110)
        gjenta til ((poeng) = (0))
            endre [poeng v] med [-10]
            sett [piksel v] effekt til (poeng)
            sett [farge v] effekt til (poeng)
            vis
            vent (1) sekunder
        slutt
    ```

##Test prosjektet { .flag}
__Trykk på det grønne flagget.__

Kommer det opp et tilfeldig og forvrengt bilde?

Blir bildet gradvis tydeligere?

Går poengsummen ned i takt med at bildet blir tydeligere?

Blir bildet fullstendig tydelig når poengsummen er 0?

Får du fremdeles nye ting på tavlen når du klikker på det grønne flagget?


##Lagre prosjektet{ .save}

##Ting å prøve { .try .activity}

+ __Prøv å endre poengsummen fra start, samt hvor mye den skal forandre seg for hver gang den går gjennom løkka.__ Hvordan endrer deg utseendet til bildet? Blir det vanskeligere eller enklere å se hva bildet forestiller?

+ __Forsøk noen ulike grafiske effekter fra nedtrekkslisten.__ Hvordan påvirker dette vanskelighetgsraden?

#Steg 3: La spilleren prøve å gjette bildet {.activity}

Så langt har vi fått vårt tilfeldige bilde til gradvis å bli tydeligere, samtidig som poengsummen synker. Men hvordan skal man vinne spillet? Vi vil legge til noen figurer nederst på skjermen som spilleren kan klikke på. Klikker man på den rette, vinner man spillet. Klikker man på feil, forsvinner figuren og spillet fortsetter med en ny figur.

Først må vi å vite hva det rette svaret er.

## Sjekkliste { .check} 

+ __Opprett en ny variabel__ og kall den __svar__. Pass på at den er tilgjengelig for alle figurer.
+ Endre skriptet slik at det klarer å holde styr på hva som er rett svar.  Etter den første `gjenta`{.blockorange}-løkken legger du derfor til blokken `sett [svar] til`{.blockorange} `drakt #`{.blockpurple}:

    ```blocks
		når grønt flagg klikkes
		skjul
		gjenta (tilfeldig tall fra (1) til (5)) ganger
            neste drakt
        slutt
		sett [svar v] til (drakt #)
        sett [poeng v] til (110)
        gjenta til ((poeng) = (0))
            endre [poeng v] med [-10]
            sett [piksel v] effekt til (poeng)
            sett [farge v] effekt til (poeng)
            vis
            vent (1) sekunder
        slutt
    ```
__Nå må vi legge til flere figurer som spilleren kan klikke på.__

+ Gi først figuren din navnet __spørsmål__.
+ Lag så en kopi av figuren ved å høyreklikke på den. På scenen drar du deretter figuren ned til det venstre hjørnet.
+ Endre figurens navn til __svar1__.
+ Slett skriptet til __svar1__ og alle kostymer bortsett fra det første.
+ Gjenta de tre siste stegene igjen (kall neste kopi __svar2__), men plasser __svar2__ ved siden av __svar1__ og slett alle bortsett fra den andre drakten.
+ Gjenta disse punktene tre ganger til, slik at du har fått laget __svar3__, __svar4__ og __svar5__.
Du skal nå ha en rad med fem svar-figurer nederst på scenen, hver viser en drakt som hovedfiguren kan ha. __Ingen av svar-figurene skal ha skript knyttet til seg.__

+ Nå må vi få alle figurene til å reagere når de blir klikket på. Hva som skal skje avhenger av om spilleren har klikket riktig eller galt. Legg til dette skriptet til __svar1__:

    ```blocks
        når denne figuren klikkes
        hvis <(svar) = (1)>
            send melding [vant v]
        ellers
            skjul
        
    ```

+ Dra skriptet over til de andre figurene, slik at alle får hver sin kopi. __For hver figur, bytt 1 til 2, 3, osv.__
+ Nå skal vi lage skriptet som gir melding til spilleren når han har vunnet. Klikk på __spørsmål__ igjen og legg til dette skriptet:

    ```blocks
        når jeg mottar [vant v]
        si (sett sammen [Gratulerer! Din poengsum ble] (poeng))
    ```

##Test prosjektet {.flag}
__Trykk på det grønne flagget.__

Når du tester spillet kan du bruke svarskjermen på scenen for å si hva rett svar er. Det
fungerer bra for testing.

Hva skjer når du klikker på __riktig svar__?

Hva skjer når du klikker på __galt svar__?

Hva skjer med det gale svaret når du __starter på et nytt spill__?

__Testen viser oss to problemer:__
Først og fremst, ting som ble klikket på ved galt svar kommer ikke tilbake når et nytt spill starter. 
For det andre, poengsummen fortsetter å gå ned, selv når man har klikket på riktig svar.

+ For å fikse det første problemet må vi legge til følgende skript for hver av de fem svarfigurene:

    ```blocks
        når grønt flagg klikkes
        vis
    ```

For å fikse det andre problemet må vi få stoppet __spørsmålfigurens__s `gjenta til`{.blockyellow}-løkke, når spilleren klikker på riktig svar. Vi kan bruke en ny variabel for å gjøre det. 
Vi kaller denne __vant__ og legger inn en `sett`{.blockorange}-blokk som gir den verdien 0 når spillet starter, og en annen som setter verdien til 1 når spillet vinnes. Se skript under.
+ I tillegg må vi stoppe `gjenta til`{.blockyellow}-løkken når poengsummen har blitt 0 eller vant er 1. 
+ Til slutt legger vi også inn en `ta bort grafiske effekter`{.blockpurple}-blokk som avslører spørsmålsfiguren, når spilleren har gjettet riktig. Skriptet skal nå se slik ut:

    ```blocks
		når grønt flagg klikkes
		skjul
		gjenta (tilfeldig tall fra (1) til (5)) ganger
            neste drakt
        slutt
		sett [svar v] til (drakt #)
        sett [poeng v] til (110)
		sett [vant v] tuk (0)
        gjenta til (<(poeng) = (0)> eller <(vant) = (1)>)
            endre [poeng v] med [-10]
            sett [piksel v] effekt til (poeng)
            sett [farge v] effekt til (poeng)
            vis
            vent (1) sekunder
        slutt
	
	    
		når jeg mottar [vant v]
		sett [vant v] til (1)
		ta bort grafiske effekter
        si (sett sammen [Gratulerer! Din poengsum ble] (poeng))
        
    ```

##Lagre prosjektet{.save}

__Gratulerer! Du er nå ferdig med spillet. Men det fins mange flere ting du kan gjøre med det. Prøv deg gjerne på utfordringene vi har laget!__


##Utfordring 1:Gjør spillet enklere eller vanskeligere {.challenge}

Endre vanskelighetsgrad for spillet.

* Forsøk å endre hvor lenge bildet vises frem og hvor raskt poengsummen minker.
* Forsøk å endre forvrengingen av bildet.
* Forsøk å gjøre tingene likere hverandre eller mer forskjellig. Husk også å forandre svarfigurenes drakter.

##Lagre prosjektet{.save}

##Utfordring 2: Forvreng bildet ulikt fra gang til gang {.challenge}

For øyeblikket bruker spillet samme forvrengingsalgoritme hele tiden. Men i steg 2 prøvde du kanskje ut noen forskjellige alternativer. Prøv nå om du kan finne noen flere forvrenginger som du synes virker like bra som farge og piksler.
 
Endre spillet slik at hvert spill bruker forskjellige forvrengninger i gjenta til-løkken.

__Hint:__ 
Forsøk å opprette en ny variabel som du kaller forvrenging. Sett denne til en tilfeldig verdi i starten av spillet. Bruk så hvis-blokker i gjenta til-løkken for å velge ut en forvrenging til det hvert spill.


##Lagre prosjektet{.save}

##Utfordring 3: La hvert spill ha flere runder {.challenge}

For øyeblikket er hvert spill uavhengig av andre. Prøv om du kan legge til flere
runder slik at man får gjette på tre ting og kan vinne inntil 300 poeng.

__Hint:__ Du vil trenge en ekstra variabel for å lagre den totale poengsummen. Du må også ha en løkke som går rundt for hver runde.

__Hint:__ Du vil trenge en ekstra variabel for å lagre den totale poengsummen. Du må også ha en løkke som går rundt for hver runde.


##Lagre prosjektet{.save}

##Utfordring 4: Øk vanskelighetsgraden gradvis {.challenge}

Gjør nå spillet vanskeligere og vanskeligere for hver runde.

Kanskje hver runde
også skal gi ulikt antall poeng? Bør spilleren også få ekstra mange poeng for å gjette kjapt i de vanskeligste rundene? 


__Hint:__ : Hvordan kan du vite hvilken runde du er i? Hvordan kan du bruke det til å endre vanskelighetsgraden og poengsummen?


##Lagre prosjektet{.save}

##Utfordring 5: Fortsett til spilleren gjør feil {.challenge}

steden for et bestemt antall runder, kan du la spillet gå til det blir klikket på feil svar. Dette funker nok best dersom man også øker vanskelighetsgraden utover i spillet.

##Lagre prosjektet{.save}

##Utfordring 6: Gjør spillet enklere eller vanskeligere basert på hvor flink spilleren er {.challenge}

Istedenfor å gjøre det stadig vanskeligere kan vi tilpasse vanskelighetsgraden til spillernes dyktighet. Hvis de raskt gjetter riktig ting, kan den neste runden gjøres vanskeligere. Hvis de klikker feil eller gjetter sakte, kan neste runde gjøres enklere.

Dette fungerer bare hvis du ikke samler opp poengsummen fra runde til runde.

##Lagre prosjektet{.save}

##Utfordring 7: Hold styr på rekorden {.challenge}

Finn en måte å lagre den høyeste poengsummen på. Klarer du også å lagre navnet til spilleren, og få spillet til å si hvem som har rekorden?


##Lagre prosjektet{.save}

##Utfordring 8: Gi en straff for galt svar {.challenge}

Slik spillet er nå kan man bare klikke som en gal på alle svarene, så vil man raskt finne riktig svar. Det kan derfor være en god idé å trekke fra poeng hver gang spilleren klikker galt.

Gjør dette spillet bedre?

##Lagre prosjektet{.save}

__Veldig bra! Nå er du ferdig og kan nye spillet du har laget!__
Ikke glem å del spillet ditt med venner og familie ved å trykke på __Legg ut__ i menyen!
