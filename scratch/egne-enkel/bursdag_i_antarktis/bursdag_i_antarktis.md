---
title: Bursdag i Antarktis
level: 1.3
language: nb-NO
stylesheet: scratch
embeds: ["*.png", "../../bilder/*.png"]
note: "README.md"
...

# Introduksjon {.intro}

Bursdag i Antarktis er en interaktiv animasjon som forteller
historien om en liten katt som har gått seg bort på bursdagen
sin. Heldigvis treffer han noen hyggelige pingviner han kan feire
sammen med.

![](bursdag_i_antarktis.png)

# Steg 1: En katt på villspor {.activity}

*Vi lager en katt som kan gå rundt i Antarktis på egen hånd.*

Vi skal etterhvert fortelle en ganske spennende historie om katten som
møter dansende pingviner på bursdagen sin. Men som alltid er det greit
å begynne med noe ganske enkelt, for deretter å bygge videre på det.

## Sjekkliste {.check}

+ Start et nytt prosjekt. Gi kattefiguren navnet `Felix`, og sett
rotasjonsmåten hans til ![sideveis](rotasjonsmate-hv.png).
+ Lag en ny bakgrunn ved å klikke
![velg en ferdig bakgrunn](velg-bakgrunn.png) nede til venstre på
skjermen. Velg `Utendørs/winter`.
+ Legg også til bakgrunnen `Alt/winter-lights`.
+ Vi begynner med et skript på scenen, som passer på at vi viser
`winter`-bakgrunnen når animasjonen starter. Gå til
`Skript`{.blocklightgrey}-fanen og legg til

    ```blocks
        når grønt flagg klikkes
        bytt bakgrunn til [winter v]
    ```

+ Da kan vi få katten til å flytte på seg. Klikk på `Felix` og gi ham
dette skriptet:

    ```blocks
        når grønt flagg klikkes
        gå til x: (-100) y: (-50)
    ```
    
    Her kan du eksperimentere litt med tallene for `x` og `y` til du
    finner noe som du synes ser bra ut.
    
+ La oss nå få Felix til å bevege seg over skjermen. Vi skifter mellom
de to draktene hans for at det skal se ut som om han går. Utvid
skriptet til Felix på denne måten:

    ```blocks
        når grønt flagg klikkes
        gå til x: (-100) y: (-50)
        pek i retning (100 v)
        gjenta til ((x-posisjon) > (240))
            gå (10) steg
            neste drakt
            vent (0.1) sekunder
    ```
	
	Tallet 100 i `pek i retning`{.blockblue}-klossen gjør at Felix går
	litt nedover mens han går over skjermen. Prøv gjerne med noen
	andre tall for å se effekten av dem.

## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

+ Vandrer Felix over skjermen?
+ Stopper han når kommer til kanten på skjermen?
+ Starter han på nytt på venstre side av skjermen om du klikker på det
grønne flagget igjen?

### Antarktis {.protip}

Antarktis er navnet på området der Sydpolen ligger. Selv om det ikke
bor verken mennesker eller katter fast på Antarktis finnes det veldig
mange pingviner der.

## Sjekkliste {.check}

Vi vil nå få bakgrunnen til å endre seg når katten kommer til enden av
skjermen. Vi begynner med noe enkelt, men som ikke fungerer så veldig
bra.

+ Lag et nytt skript på Scenen.

    ```blocks
        når grønt flagg klikkes
        vent (3) sekunder
        bytt bakgrunn til [winter-lights v]
    ```

+ Legg også til en kloss som flytter Felix inn på veien etter at
bakgrunnen er byttet.

    ```blocks
        når grønt flagg klikkes
        gå til x: (-100) y: (-50)
        pek i retning (100 v)
        gjenta til ((x-posisjon) > (240))
            gå (10) steg
            neste drakt
            vent (0.1) sekunder
        slutt
		gå til x: (-20) y: (-100)
    ```

## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

+ Skifter bakgrunnen når Felix kommer til enden av skjermen?
+ Klarer du å endre tallet i klossen `vent 3 sekunder`{.blockyellow}
slik at det ser bedre ut?

# Steg 2: Det blir enklere med meldinger {.activity}

*Vi skal nå begynne å bruke meldinger for å få ting til å skje på
 samme tid.*

Vi har sett at vi kan klare å få ting til å skje samtidig ved å bruke
`vent`{.blockyellow}-klosser. Men det er vanskelig å finne ut akkurat
hvor lenge vi bør vente, og det er kjedelig å måtte endre på denne
tiden om vi forandrer for eksempel hvor fort Felix går.

Vi skal derfor i stedet bruke __meldinger__. Slike meldinger er noe
figurene kan sende til hverandre eller til scenen uten at de er
synlige for oss som ser på.

## Sjekkliste {.check}

+ La katten sende en melding når han når kanten av skjermen.

    ```blocks
        når grønt flagg klikkes
        gå til x: (-100) y: (-50)
        pek i retning (100 v)
        gjenta til ((x-posisjon) > (240))
            gå (10) steg
            neste drakt
            vent (0.1) sekunder
        slutt
		send melding [scene 2 v]
    ```

+ Vi kan nå slette det gamle skriptet på scenen som byttet bakgrunn
til `winter-lights`, og heller bruke dette:

    ```blocks
        når jeg mottar [scene 2 v]
        bytt bakgrunn til [winter-lights v]
    ```
	
+ Felix kan også motta meldinger han sender selv. Vi kan bruke dette
til å flytte han inn på veien samtidig som vi bytter bakgrunn. Legg
til følgende som et nytt skript på Felix:

    ```blocks
	    når jeg mottar [scene 2 v]
		gå til x: (-20) y: (-100)
    ```

## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

+ Går Felix fortsatt over skjermen?
+ Hva skjer når han kommer til kanten av skjermen? Vi har laget to
skript som sier at bakgrunnen skal endre seg og katten skal flytte til
midten av skjermen. Skjer dette?

# Steg 3: Felix introduserer seg selv {.activity}

# Steg 4: Gå opp mot husene {.activity}

# Steg 5: Si hei til pingvinene {.activity}

*Felix skal nå møte to pingviner som bor inne i pepperkakehuset. De skal komme ut av huset og snakke litt med Felix*

## Sjekkliste {.check}
+ Lag to nye figurer ved å trykke på ![velg figur fra biblioteket](hent-fra-bibliotek.png). Velg `Penguin1` og `Penguin2`

+ For å få pingvinene til dukke opp i scene 3, må vi først skjule de. Legg til følgende script på begge figurene:

    ```blocks
        når grønt flagg klikkes
        skjul
    ```
+ Først skal Felix spørre om det er noen hjemme og så sende en melding. Legg til følgende skript på Felix:

    ```blocks
        når jeg mottar [scene 3 v]
        gå til x: (-160) y: (-50)
        si [Oj, så flott hus! Er det noen hjemme?] i (2) sekunder
        send melding [kom ut v]
    ```
+ Pingvin 1 skal nå komme ut av døra og gå litt til siden. Sjekk med musepeker hva x og y -posisjonen til døren er. Legg til følgende skript på Pingvin 1:

    ```blocks
        når jeg mottar [kom ut v]
        gå til x: (41) y: (-73)
        vis
        gli (1) sekunder til x: (128) y: (-100)
    ```
+ Pingvin 2 kommer ut litt etterpå, og spør Felix et spørsmål. Legg til følgende script på Pingvin 2:

    ```blocks
        når jeg mottar [kom ut v]
        vent (2) sekunder
        gå til x: (41) y: (-73)
        vis
        vent (1) sekunder
        spør [Hva heter du?] og vent
    ```

## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

+ Kommer pingvinene ut av huset som forventet?
+ Hva tror du skjer med navnet som du skrev inn?

# Steg 6: Pingvinene danser {.activity}
*Pingvinene blir glad for å treffe Felix, og etter en liten samtale begynner den ene pingvinen å danse siden det er Felix sin bursdag.*

## Sjekkliste {.check}
+ Få Pingvin 2 til å sende en melding etter at han har spurt hva Felix heter. Kall for eksempel meldingen [navn1] 

+ Legg til følgende skript på Pingvin 1

    ```blocks
        når jeg mottar [navn1 v]
        si (svar) i (2) sekunder
        si [Det er et rart navn!] i (2) sekunder
        send melding [navn2 v]
    ```
	
+ Legg til følgende skript på Felix for å få han til å svare tilbake og si at han har bursdag:

    ```blocks
        når jeg mottar [navn2 v]
        si [Jeg har bursdag i dag!] i (2) sekunder
        si (sett sammen [Jeg blir](alder)) i (2) sekunder
        send melding [party v]
    ```
	
+ Nå skal vi få Pingvin 1 til å danse! Lag to nye drakter for pingvin 1 ved å velge `Penguin1` to ganger. Vri de litt i vinkel.
+ Legg til en lyd du liker under [Lyder], og lag følgende skript på Pingvin 1:

    ```blocks
        når jeg mottar [party v]
        spill lyden [human beatbox1 v]
        gjenta (20) ganger
            neste drakt
            vent (0.2) sekunder
        slutt
    ```
	
## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

+ Danser pingvinen sånn som du forventet?
+ Hva er forskjellen mellom å lagre svaret i en variabel og å ikke gjøre det?

## Lagre prosjektet {.save}

*Nå har vi begynt på historien om katten som feirer bursdagsen sin i
 Antarktis. Men kanskje du kan fortelle mer om hva som skjer videre?*

Eller om du heller vil vise fram historien din til familie og venner
kan du velge `Legg ut` på toppen av skjermen.

## Utfordring: Historien fortsetter {.challenge}

Kan du fortsette på historien? Hva skjer videre?

Kanskje du kan introdusere flere figurer, eller flere bakgrunner? For
eksempel kan det hende at pingvinene inviterer katten med seg inn i
huset? Eller kanskje de sammen går videre på leting etter en båt som
katten kan bruke for å komme seg hjem til Norge?

Husk at du kan også blande animasjonen med et lite spill, og så gå
tilbake til mer animasjon! Det er helt opp til deg!
