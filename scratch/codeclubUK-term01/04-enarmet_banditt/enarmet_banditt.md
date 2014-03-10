---
title: Enarmet Banditt
level: 1.4
language: nb-NO
stylesheet: scratch
embeds: ["*.png", "../../bilder/*.png"]
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

Bra! Vi kan få draktene til å bytte i det uendelige, men hvordan får vi dem til å stoppe når vi klikker på dem?

+ Klikk på `data`{.blockorange} og __lag en ny variabel__. Gi den navnet __stoppet__ og la det stå huket av 'for denne figuren'. 
+ Når variabelen er opprettet __fjerner du avhukingen ved siden av__, slik at den ikke vises på scenen.
+ Nå skal vi gi __stoppet__ verdien 1 når spilleren klikker på figuren. Det gjør vi med en `når denne figuren klikkes`{.blockyellow} og en `sett stoppet til 1`. Husk å endre verdien fra 0 til 1 i den siste blokken.

    ```blocks
        Når denne figuren klikkes
        sett (stoppet v) til (1)
    ```

+ Neste steg er å __få ruletten til å stoppe__ når __stoppet__ får verdien 1. Velg `styring`{.block} og sett inn en `hvis`{.block}-blokk inni `for alltid`{.block}-blokken. Bruk så en `([] = [])`{.block}-blokk fra `operatorer`-kategorien i `hvis`{.block}-testen for å sjekke om `([stoppet v] = (0))`{.block}. 

    ```blocks
        Når grønt flagg klikkes
        for alltid
        hvis ((stoppet v) = (0))
        neste drakt
        vent (0.5) sekunder
    ```
                                                                    
+ Til slutt må du huske å nullstille __stoppet__ når spillet startes på nytt. For da vil vi jo at ruletten skal begynne å gå rundt igjen. Legg til en `sett (stoppet) til (0)`{.block} rett under `når grønt flagg klikkes`{.block}-blokken.


## Test prosjektet { .test}

+ __Klikk det grønne flagget__ og vent et øyeblikk. __Så klikker du på figuren__.
Endres drakten __før__ du klikker på den?
Stopper den __når__ du klikker på den?
+ __Start skriptet igjen__. 
Stopper den når du setter pekeren over den uten å klikke? 
Stopper den når du klikker andre steder på scenen eller andre steder i Scratch?



# Steg 4: Lag de andre figurene

## Sjekkliste { .check}

Nå trenger vi to figurer til for å gjøre spillet komplett!

+ __Dupliser figuren din__ ved å høyreklikke på den og velge `lag kopi`{.block}.
+ Gjør det en gang til - slik at vi får tre figurer på skjermen.
+ Flytt figurene slik at de er på en linje. Gjør dem mindre med krympeknappen ![](mindre.png) hvis det trengs.


## Test prosjektet { .test}

+ __Klikk det grønne flagget__ og kryss fingrene for at alle figurene nå endrer seg.
+ Prøv å stoppe dem én etter én.


## Ting å prøve { .try}

+ Når spillet startes første gang har alle figurene samme drakt og forandrer seg helt likt. Hva med å få dem til å __endre drakten i tilfeldig rekkefølge?__
*Tips:* Prøv å gi en tilfeldig drakt til hver figur hver gang spillet startes.


Bra jobba! Du er ferdig med første del av spillet! Men prøv gjerne disse utfordringene:


## Utfordring 1: Gjør spillet vanskeligere { .challenge}

Se om du klarer å __endre vanskelighetsgraden__ på et eller annet vis. Å få draktene til å rullere raskere er enkelt. Prøv å gjøre noe litt mer oppfinnsomt. Noen muligheter du kan tenke på er:

+ Endre antall drakter hver figur har.
+ Gir figurene en drakt hver som er helt forskjellig.
+ Endre tid mellom draktbytte.
+ Få figurene til å forandre drakter i ulik rekkefølge, ved at neste drakt er tilfeldig.
+ Andre ting?

Hver gang du endrer noe, tenk på om det vil gjøre spillet lettere eller vanskeligere. Er spillet for lett eller for vanskelig? Hvordan kan du justere det slik at det blir akkurat passe?

## Utfordring 2: Endre vanskelighetsgrad over tid { .challenge}

Noen spillere vil være gode og andre ikke fullt så gode. Hvordan kan du få spillet til å __justere vanskelighetsgrad ut ifra hvor god spilleren er?__

+ En måte er å __justere rulleringshastigheten for draktene__. Du kan bruke en variabel, som du kaller __forsinkelse__, som bestemmer varigheten til `vent`{.block}-blokken for hver figur. Hvis spilleren vinner en runde, kan verdien på __forsinkelse__-variabelen settes litt ned - for å gjøre spillet vanskeligere. Hvis spilleren taper en runde, så kan den justeres litt opp - for å gjøre det lettere.

## Utfordring 3:  Oppdag når spillet er vunnet - eller tapt { .challenge}

Spillets mål er å klikke på figurene slik at de stopper når alle har samme drakt. Da hadde det vært fint om spillet oppdaget når du var ferdig og fortalte deg om du hadde vunnet eller tapt. 
For å sjekke om spillet er slutt lager vi et eget skript. Denne sjekken kan kjøres hver gang en figur er klikket. 


+ Først må vi __gi scenen beskjed når en figur har blitt klikket på__. Finn tilbake til `når denne figuren klikkes`{.block} og legg til blokken `send melding (SjekkOmSlutt)`{.block}. Du må lage meldingen 'SjekkOmSlutt' selv. Gjør det samme for de andre figurene. 
+ Når scenen mottar beskjeden __SjekkOmSlutt__, setter den i gang skriptet som kjører sjekken. Hvis alle figurenes __stoppet__-variabel har verdien 1, så vet vi at spillet er ferdig. 
Bruk  blokken %(sansning)'x-posisjon' av Figur1'% og endre 'x-posisjon' til 'stoppet'. 
+ Neste punkt blir å sjekke om spilleren har vunnet. Det har hun eller han hvis alle tre figurene er frosset med samme drakt.
For å sjekke dette bruker vi nok en gang %(sansning)'x-posisjon' av Figur1'%. Men denne gangen er det draktnummeret vi sammenligner. 
I tillegg trenger vi en %(styring)hvis%-blokk som sjekker hver _stoppet_-variabel og inn i den en %(styring)hvis..ellers%-blokk. Kanskje det er lettest å skjønne når du ser litt på skriptet?

    ```blocks
        Når jeg mottar (SjekkOmSlutt)
    ```

+ Til slutt kan du annonsere resultatet ved å bruke en ny melding og en ny figur. Kanskje Felix kan komme tilbake for å gratulere spilleren?

Bra jobba! Nå kan du kose deg med å spille! Og glem ikke at du kan dele spillet med vennene dine ved å velge `Legg ut` fra toppmenyen.





