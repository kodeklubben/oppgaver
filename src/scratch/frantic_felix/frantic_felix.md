---
title: Frantic Felix
level: 4
indexed: false
logo: ../../assets/img/ccuk_logo.png
author: Oversatt fra [Code Club UK](//codeclub.org.uk)
translator: Lars-Erik Wollan
license: "[Code Club World Limited Terms of Service](https://github.com/CodeClub/scratch-curriculum/blob/master/LICENSE.md)"
---

# Introduksjon: {.intro}

I dette prosjektet skal du lage et komplett spill. Det er et
plattformspill, hvor katten Felix hopper rundt, unnslipper slemminger
og samler nøkler for å slippe ut av hulen. Når han kommer seg ut,
fortsetter spillet i neste hule.

I del 1 av dette prosjektet kommer du til å lære hvordan vi får Felix
til å flytte seg og samhandle med forskjellige ting. I del 2 skal du
designe egne brett og nivåer. Til slutt skal du sette brettene sammen
til et ferdig spill.

# Del 1: Lag byggeklossene

Plattformspill, som for eksempel __Manic Miner__ og __Mario Bros__,
handler om en figur som beveger seg rundt i en verden og hopper inn i
ting. Noen ting, som vegger, stopper deg. Andre ting, som slemminger,
tar livet av deg. Ting som nøkler må du samle på. Andre ting er
bakgrunner og påvirker ikke spillet i det heletatt.

Det betyr at det å vite når du har kommet bort i noe er
viktig. Scratch har noen klosser for å oppdage at noe berører noe
annet: `berører sprite`{.blocksensing}, `berører
farge?`{.blocksensing}-kloss, `farge berører?`{.blocksensing}-kloss,
og `avstand til`{.blocksensing}-kloss. Men for å lage spillet, må du
vite mer enn at to figurer har kommet borti hverandre; du trenger å
vite hvilken __side__ som berøres. Hvis du går mot en vegg til
venstre, kan du ikke gå lengre til venstre. Men du kan fortsatt gå til
høyre, eller hoppe, eller falle ned hvis det ikke er noe gulv å stå
på.

Hvis du berører en slemming, kan dette skade deg; men hvis du berører
slemmingen med beina, kan du skade den. Ingen av de innebygde
Scratchklossene kan si noe om __retningen av berøringen__. Vi må
derfor bygge våre egne berøringssensorer.

# Steg 1: Berøringssensor {.activity}

Vi skal ha fire figurer som følger etter Frantic Felix. __Hver figur
oppdager berøring i én retning og setter en variabel hvis det oppstår
en berøring__. Hovedfiguren Felix bruker disse variablene for å
kontrollere hvordan Felix kan bevege seg. Hver berøringssensor har en
farget linje og bruker `farge berører?`{.blocksensing}-klossen for å
oppdage ting. Vi bruker __svart__ for gulvet og __grønn__ for
hinder. Vi bruker __rød__ for berøringssensorene.

## Sjekkliste {.check}

+ __Åpne et nytt prosjekt__. Legg til __frantic-felix/testlevel__
  bakgrunnen og slett den hvite __background1__.

+ __Endre navn på figur Sprite1 til Felix__. Kontroller at drakten bare kan flippe venstre-høyre.

+ Lag fire nye figurer fra bildene (be om hjelp hvis du ikke har
  disse) __frantic-felix/top__, __frantic-felix/bottom__,
  __frantic-felix/left__, og __frantic-felix/right__. Disse figurene
  skal bli berøringssensor. Gi de nye figurene navnene __topp__,
  __bunn__, __venstre__, og __høyre__. Kontroller at draktene deres
  ikke kan flippes eller roteres.

+ Lag fire variabler (for hver av figurene): `blokkert
  topp`{.blockdata}, `blokkert bunn`{.blockdata}, `blokkert
  høyre`{.blockdata} og `blokkert venstre`{.blockdata}.

+ Lag dette skriptet for hver av sensorene:

  ```blocks
  når grønt flagg klikkes // eksempel for høyre sensor
  for alltid
    gå til [Felix v]
      hvis <farge [rød v] berører [grønn v] ?>
      sett [blokkert høyre v] til [1]
      ellers
      sett [blokkert høyre v] til [0]
      slutt
  slutt
  ```

+ Endre variablene for hver av sensorene. Den nederste sensoren
  trenger en __eller__ kloss slik at den setter __blokkert bunn__ hvis
  den berører grønn eller svart.

__Tips__: Det er enklere å velge fargene i én figur, for så å kopiere
skriptet over til de andre figurene og oppdatere variablene som blir
satt. Da slipper du å finne de riktige fargene fire ganger.  Inntil
videre trenger Felix bare et skript for å følge musepekeren evig.

## Test prosjektet {.flag}

__Trykk på det grønne flagget.__

Du bør se at Felix følger etter musepekeren, omringet av et rødt
rektangel. Rektangelet er en berøringssensor. Hvis du følger med på
variablene, ser du at de endrer seg når du drar Felix rundt og når han
berører ulike deler av skjermen. For øyeblikket beveger Felix seg
gjennom plattformene og grønne hindre. Det skal vi fikse nå.

# Steg 2: Bevegelse, gulv og falling {.activity}

## Sjekkliste {.check}

+ Neste steg er å få Felix til å gå. Vi bruker __venstre__ og __høre
  piltast__ for å flytte ham til venstre og høyre. Hvis han ikke står
  på et gulv, faller han ned (vi fikser hopping etterpå). Vi vil at
  når man trykker på venstre piltast, så skal Felix peke til venstre
  og flytter seg litt. Men vi vil ikke at han skal flytte seg hvis det
  er en hindring i veien.

+ Vi kunne brukt `når tast trykkes`{.blockevents} for å flytte Felix,
  men det gir en hakkete bevegelse. Det blir en mykere bevegelse hvis
  du bruker `hvis `{.blockcontrol}`tast pil venstre
  trykket?`{.blocksensing}-klosser i en `for
  alltid`{.blockcontrol}-løkke.  Berøringssensorer betyr at vi må
  teste __blokkert venstre__ variabelen i `hvis`{.blockcontrol}, og
  bruke en __og kloss__ slik at Felix bare beveger seg til venstre når
  man trykker på en tast og __blokkert venstre__ er 0. Vi må gjøre
  tilsvarende for bevegelse til høyre.

+ Vi kunne animere Felix sine bein i samme kloss, men da beveger de
  seg for raskt. Gjør animasjonen i en egen `for
  alltid`{.blockcontrol}-løkke under en annen `når grønt flagg
  klikkes`{.blockevents}-hatt.

+ Det siste vi må gjøre er å ordne __falling__. Hvis Felix ikke står
  på fast grunn vil vi at han skal falle ned. Det ordner vi med en
  `for alltid`{.blockcontrol}-løkke under en `når grønt flagg
  klikkes`{.blockevents}-hatt.

  ```blocks
  når grønt flagg klikkes // håndter flytting
  for alltid
      hvis < <tast [pil venstre v] trykket?> og ((blokkert venstre)=(0))>
      pek i retning (-90)
          gå (2) steg
      slutt
      hvis < <tast [pil høyre v] trykket?> og ((blokkert høyre)=(0))>
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

__Bruk musen for å dra Felix et sted på scenen og trykk så på det
grønne flagget__. Hvis Felix hopper til muspekeren, må du fjerne det
skriptet!  Du bør kunne bruke venstre og høyre knapper for å få Felix
til å gå fra side til side. Hvis han ikke står på gulvet, bør han
falle sakte nedover.

+ Vi vil også at berøringssensorene ikke skal vises. Det er ikke mulig
  å bruke en skjult blokk, for da vil ingen berøringer bli
  oppdaget. Istedet, legg til en `sett gjennomsiktig effekt til
  100`{.blocklooks}-kloss rett under den grønn flag hatt'en i hver
  kollisjonssensor. Dette gjør figuren gjennomsiktig, uten å å skjule
  den.

## Test prosjektet ditt {.flag}

__Nå du klikker på det grønne flagget__, skal kollisjonssensorene
forsvinne. De dukker opp igjen når du trykker på det røde
stoppskiltet.

# Steg 3: Hopping {.activity}

__Det er et par utfordringer med hopping.__

* Vi vil ikke at Felix __faller__ hvis han er __på vei opp__.

* Vi vil ikke at Felix skal hindres av gulv når han er på vei opp, men
  vi vil fortsatt at han skal stoppes av gulvet når han __er på vei
  ned__.

* Vi vil ikke at Felix skal __hoppe opp_ i undersiden av et __grønt
  hinder__.

* Vi vil at hoppet skal være en myk bevegelse, så vi vil ikke at Felix
  flytter seg for raskt.

* Felix skal bare kunne hoppe hvis han __står på gulvet__. Spillet
  blir litt for enkelt hvis Felix kan hoppe fra løse luften.

## Sjekkliste {.check}

+ Det som gjenstår nå, er å få Felix til å hoppe. La oss bruke
  __mellomromstasten__ for å få Felix til å hoppe.

+ For å kontrollere hoppet, bruker vi en ny variabel,
  `hopphøyde`{.blockdata}. Hvis denne er høyere enn 0, er Felix på vei
  opp. Hvis den er 0, faller han (eller har falt), som beskrevet over.

+ Vi vil at Felix skal hoppe opp til __100 pixler__. Legg til en ny
  `hvis`{.blockcontrol}-kloss inni `for alltid`{.blockcontrol}-klossen
  som håndterer tastetrykk. Hvis vi trykker __mellomromstasten__ og
  Felix står på gulvet (variablen `blokkert under`{.blockdata} er satt
  til 1, så setter vi `hopphøyde`{.blockdata} til 100.

+ Vi må endre falle-skriptet. I `for alltid`{.blockcontrol}, trenger
  vi en `hvis-ellers`{.blockcontrol}-kloss som oppdater hvis Felix
  hopper opp eller ikke. Kravet for denne
  `hvis-ellers`{.blockcontrol}-klossen er at hvis
  `hopphøyde`{.blockdata} er __større enn 0__. Den eksisterende faller
  ned `hvis`{.blockcontrol}-klossen går inn i ellers-delen av den nye
  `hvis-ellers`{.blockcontrol}-klossen.

+ Når vi vet at Felix hopper opp, må vi sjekke om hodet hans treffer
  noe. Hvis `blokkert topp`{.blockdata} er __1__, sett
  `hopphøyde`{.blockdata} til __0__. (Dette gjør at Felix ikke kan
  hoppe inn i hindringer). __Ellers, flytt Felix opp 10 og reduser
  hopphøyde med 10.__

+ Du ender opp med noe tilsvarende dette:

  ```blocks
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

__Trykk på det grønne flagget__. Kan Felix hoppe? Hopper han fra en
plattform til en annen? Faller han hvis han går over kanten? Hva om
han hopper oppover over kanten av en plattform? Hva om han prøver å
hoppe under den grønne blokken til høyre? Hva skjer når du trykker på
mellomromstasten mens Felix faller?

# Steg 4: Nøkler og mål {.activity}

__Vi har klart å få Felix til å bevege seg rundt i verdenen. Nå må vi
få han til å klare ett nivå__.

Vi plasserer tre nøkler rundt i hulen. Felix kan plukke dem opp ved å
gå til dem. Når han har samlet alle tre, kan han klatre til en
redningskapsel og redde seg selv ut av hulen.

+ Vi lager en ny variabel, `nøkler igjen`{.blockdata}, som holder
  orden på hvor mange nøkler som gjenstår. Et nytt skript på
  __scenen__ skal sette denne til __3__ når det __grønne flagget__
  klikkes.

+ Både nøklene og redningskapselen må være figurer. (Bruk
  __frantic-felix/key__ for nøklene og __frantic-felix/escape-pod__
  for kapselen.)

+ Hver nøkkel trenger __to skript__: det første plasserer nøklen på
  riktig sted, med størrelse og vinkel, og en `for
  alltid`{.blockcontrol}-løkke for å endre fargen (som gjør det
  enklere å se den på skjermen). Det andre skriptet er en `for
  alltid`{.blockcontrol}-løkke som venter til Felix kommer bort til
  nøkkelen. Når dette skjer, skjuler skiptet nøkkelen og reduserer
  antall nøkler.

+ Redningskapselen er et litt vanskeligere skript. Den bruker en `for
  alltid`{.blockcontrol}-løkke for å vente på at `nøkler
  igjen`{.blockdata} blir __0__. Med en gang dette skjer, begynner
  kapselen å blinke (for å vise spilleren at de kan komme seg ut). Så
  kan vi bruke en annen `hvis`{.blockcontrol} for å oppdage når Felix
  berører den blinkende redningskapselen. Så snart han gjør det,
  sender kapselen en `seier`-melding og sier “Du vant!”. Felix svarer
  på meldingen ved å gjemme seg.

  ```blocks
  når grønt flagg klikkes
  gå til x:(220) y:(-125)
  for alltid
    hvis <(nøkler igjen) = [0]>
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

# Steg 5: Slemminger og dødelige omgivelser {.activity}

__Nå er det på tide med slemminger!__

Det skal være to typer farlige ting. En type vil være slemminger som
går rundt og skader Felix hvis kan krasjer inn i dem. Den andre typen
er farlige ting i bakgrunnen.

__La oss først lage en slemming. Den vil bare bevege seg langs en fast
sti.__

## Sjekkliste {.check}

+ __Lag en ny figur__, bruk hvilken som helst drakt. Den bør være
  samme størrelse som Felix (Vi brukte __things/flower-vase__ drakt,
  og gjorde den fire steg mindre). Slemmingen trenger bare et enkelt
  skript som beveger den og oppdager om den berører Felix.

+ Lag tre `hvis`{.blockcontrol}-klosser inni en `for
  alltid`{.blockcontrol}-løkke. Den første sjekker om en slemming
  berører Felix; hvis den gjør det, sender den en `tap`-melding. De to
  andre `hvis`{.blockcontrol}-klossene sjekker om slemmingen har nådd
  slutten av stien; hvis den har det, snur slemmingen. Tilslutt, tar
  slemmingen to steg. (Ved å bruke `gå`{.blockmotion} isteden for
  `gli`{.blockmotion} -klosser blir det enklere å kontrollere hvor
  raskt slemmingen går.)

  __Vi trenger ikke å bruke kollisjonssensor her, da vi ikke bryr
  oss om på hvilken side Felix berører slemmingen.__

  ```blocks
  når grønt flagg klikkes
  gå til x:(-50) y:(47)
  pek i retning (-90)
  for alltid
    hvis <berører [Felix v]?>
      send melding [tap v]
      slutt
      hvis < (x-posisjon) > [-200] >
      pek i retning (90)
      slutt
      hvis < (x-posisjon) > [-50] >
      pek i retning (-90)
      slutt
      gå (2) steg
  slutt
  ```

+ Legg skript til både Felix og redningskapselen slik at den svarer på
  `tap`-meldingen. Felix skal bare skjule seg selv.  Kapselen skal si
  "Du tapte!".

## Test prosjektet ditt {.flag}

__Trykk på det grønne flagget__. Beveger vasen seg? Stopper den og
snur ved kanten? Hva skjer når Felix går inn i den? Hva skjer hvis
Felix hopper på den, fra oversiden eller undersiden? Forsvinner Felix?
Sier kapselen ifra når du har tapt? Kan du forstatt vinne spillet?


+ __Neste, farlige ting!__ La oss si at alt som er lyseblå er dødlig
   for Felix. Last inn bakgrunnen __frantic-felix/level2__, som har en
   blå rose på det øverste nivået. Legg til enda et skript på Felix,
   under et grønt flagg hatt:

  ```blocks
  for alltid
      hvis <berører fargen [blå v]?>
          send melding [spill slutt v]
      slutt
  slutt
  ```

## Test prosjektet ditt {.flag}

__Trykk på det grønne flagget__. Dør Felix hvis han kommer borti den
blå rosen? Hva skjer når han berører andre ting?

## Oppsummering

__Det du har laget nå er et veldig enkelt plattformspill. Akkurat nå,
er det et ganske kjedelig spill. Men det er ikke poenget. Dette
spillet er en verktøykasse som du kan bruke til å lage egne spill og
brett. I neste del skal du lage egne brett.__

# Del 2: Brettdesign

__Forrige gang bygde du alle delene et plattformspill består av. Nå
skal du bruke disse delene for å lage egne brett..__

Kort oppsummert gjorde du:

* Felix kan gå til venstre og høyre og han kan hoppe.

* Felix faller ned hvis han ikke står på gulvet.

* Felix kan ikke gå gjennom grønne hindere.

* Blå ting i bakgrunnen og slemminger tar livet av Felix.

* Slemminger beveger seg i faste ruter.

* Slemminger kan ta livet av Felix hvis han kommer borti dem.

* Felix kan samle nøkler ved å gå bort til dem.

* Når Felix har samlet alle nøklene, kommer en redningskapsel til syne
  og han kan rømme i sikkerhet (eller til neste nivå).

Dette kan være byggeklossene dine. __Bruk dem til å lage egne brett.__

Du kan lage en hel rekke med brett som Felix må klare. Neste gang skal
vi se på hvordan vi kan knytte brettene sammen.

Brett kan ha store eller små plattformer, mange eller få
plattformer. Det kan være mange slemminger eller ingen. Det kan være
mange hindringer eller dødelige ting i bakgrunnen. Prøv å lage flere
måter man kan klare brettet på, selv om et kanskje er enklere enn et
annet. Tenk over hvor vanskelig eller enkelt brettet er.

Du kan endre de spesielle fargene (svart, grønn og blå), men da må du
__oppdatere fargeberøringsblokkene__ i alle skriptene. Det må være
samme farge i alle brett. (Du kunne hatt forskjellige farger i
forskjellige brett, men det betyr at du måtte legge inn mange
`eller`{.blockoperators}-klosser rundt fargeberøringsblokkene.)

__Test brettene dine__. Hvis du har tid, opprett brett i Scratch og
spill dem. Sjekk at de ikke er __for vanskelige__ og __ikke for
enkle__. Hvis du programmerer brettene, må du __lagre bakgrunnen du
lager__ og notere __start posisjon__ for Felix, nøkler, og eventuelle
slemminger. I tillegg må du huske retningen slemmingene beveger seg i
og hvor langt de går.

Hvis du har laget et par brett og lagt dem inn i Scratch, prøv disse
ekstraoppgavene:

## Utvidelse: Tramping {.challenge}

__Hva om slemmingene døde hvis de ble trampet på?__ Kanskje du kan
legge til et skript på slemmingene som gjør noe hvis slemmingen
berører den nederste kollisjonssensoren.

## Utvidelse: Kraftpiller {.challenge}

__Du kan lage en “kraftpille” som gjør at Felix kan ødelegge slemmingene__. Når Felix tar kraftpillen, ødelegger Felix slemmingene han berører. Effekten går over etterhvert

Det er opp til deg hvordan du får dette til å fungere. Kanskje vil du at slemmingene skal endre utseende når Felix kan ta dem?

## Test prosjektet ditt {.flag}

__Trykk på det grønne flagget__.

## Del 3: Sett sammen spillet

__Nå har du noen brett. Du har nok verktøy til å få dem til å
fungere. Det siste vi må gjøre er å sette delene sammen til et ferdig
spill!__ Hvis du klarer å sette sammen brettene kjapt, kan du ta en
titt på aktivitet 2 and 3 før du begynner å spille spillet ditt.

# Steg 1: Vise et nytt brett{.activity}

__Når Felix klarer ett brett, må vi flytte til neste__. Det betyr at
vi må få redningskapselen til å sende en `start brett`-melding
(istedet for `seier`-meldingen) når Felix har funnet alle nøklene og
klatret inn i kapselen. Vi kan bruke start brett melding for å
klargjøre neste brett. Vi trenger også en variabel, `nåværende
nivå`{.blockdata}, som settes av redningskapselen før den sender
`start brett`-melding.

Alt må stort sett svare på `start brett`-meldinger for å klargjøre
neste brett.

__Scenen__ må vise riktig bakgrunn. Hver av slemmingene, alle nøkler,
og redningskapselen trenger å flytte til __riktig start
posisjon__. Slemmingenes rute trenger __oppdatering__. Felix må
flyttes til sin __nye startposisjon__. Først da er brettet klart til
start.

De fleste figurene må svare på `start brett`-meldingen istedet for det
grønne flagget. Det betyr at du må __endre hatt-klossene__ i de fleste
skript.

## Test prosjektet ditt {.flag}

__Fortsett å teste spillet etter hver endring. Husk å teste de delene
som du allerede har endret, slik at de fortsatt virker som planlagt.__

Vi kommer ikke beskrive alle endringene, men vi skal vise hvordan
Felix sitt oppdaterte skript for å vise hva som må gjøres.

```blocks
når jeg mottar [start brett v]
    gå til x: (element [nåværende nivå v] av [xs v]) y: (element [nåværende nivå v] av [ys v])
pek i retning (element [nåværende nivå v] av [retning v])
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
    sett [hopphøyde v] til [100]
    slutt
slutt
```

Du legger kanskje merke til at start verdiene __x__, __y__, og
__retning__ for Felix settes med lister. Vi laget noen lister for hver
figur (hver liste privat til den figuren) for å lagre verdiene vi
trenger for den figuren. Du trenger en liste for hver ting du
lagrer. Du trenger ikke bruke lister, du kan bruke
`hvis`{.blockcontrol}-klosser som sjekker hvilket brett du er på og
gjør riktig ting basert på dette.

Og her er redningskapselen, som håndterer all nivå-endringen:

```blocks
når grønt flagg klikkes
sett [nåværende nivå v] til [1]
send melding [start brett v]

når jeg mottar [start brett v]
gå til x: (element [nåværende nivå v] av [xs v]) y: (element [nåværende nivå v] av [ys v])
for alltid
  hvis <[nøkler å ta v] = [0]>
      endre [farge v] effekt med (25)
        hvis <berører [Felix v]?>
      hvis <[nåværende nivå v] = <lengden av [nøkler per brett v]>
        si [Du vant!!]
                send melding [seier v]
                stopp [alle v] :: control
            ellers
        endre [nåværende nivå v] med (1)
                send melding [start brett v]
            slutt
        slutt
    slutt
slutt
```

# Steg 2: Spill! {.activity}

__Du har laget spill__. De andre i kodeklubben har laget spill. Spill
de forskjellige spillene! Klarer du å runde deres spill? Kan de andre
runde spillet ditt?

## Utvidelse 1: Flere liv {.challenge}

Felix trenger kanskje et par sjanser, eller et par liv for å klare seg
igjennom brettene. __Legg til en ny figur__ med tre drakter, som viser
__ett__, __to__, og __tre hjerter__.

Bruk frantic-felix/1-heart, frantic-felix/2-heart, and
frantic-felix/3-heart draktene. Plasser figuren i hjørnet av
scenen. Når det __grønne flagget__ blir trykket, skal det vises tre
hjerter. Hver gang det mottar en tap melding, skal det vises et hjerte
mindre. Isteden for å vise ingen hjerter, skal figuren skjules og
sende en `slutt over`-melding.

`spill slutt`- og `seier`-meldinger bør håndteres av en __ny figur__,
som __skjules__ når det grønne flagget trykkes og viser riktig plakat
når `spill slutt`- og `seier`-meldinger sendes. Denne figurer skal
også stoppe alle skript når den viser seg selv.

Du må endre hvordan redningskapselen håndterer vinning og tap, da
dette er ansvaret for liv og ferdigplakat figurene.

Kanskje er slemmingen litt for kjappe på foten, de tar Felix før
brettet er kommet igang. Hvis Felix taper mer enn et liv når han
kommer borti en slemming, `skjul`{.blocklooks} slemmingen så snart den
sender `tap`-meldingen. Det gir resten av spillet (inkludert Felix)
tid å nullstille før slemmingene oppdager en ny kollisjon med Felix.

## Utvidelse 2: Tidsbegrensninger {.challenge}

__Ta tiden på Felix!__ Bruk et __Timer Scratchkort__ for å legge til
en tidsbegrensning. Hvis timeren løper ut, sender den `spill
over`-melding. Husk å __nullstille timeren__ når et nytt brett
starter.
