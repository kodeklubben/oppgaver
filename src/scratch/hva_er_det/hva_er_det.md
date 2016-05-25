---
title: Hva er det?
level: 3
logo: ../../assets/img/ccuk_logo.png
author: Oversatt fra [Code Club UK](//codeclub.org.uk)
translator: Anne-Marit Gravem
license: "[Code Club World Limited Terms of Service](https://github.com/CodeClub/scratch-curriculum/blob/master/LICENSE.md)"
---

# Introduksjon {.intro}

Et bilde av en tilfeldig ting vises på tavlen. Men bildet er
forvrengt, slik at du må gjette hva det er ved å klikke på et av
alternativene som vises under. Desto raskere du gjetter riktig, desto
flere poeng får du.

![](hva_er_det.png)

# Steg 1: Få flere ting til å vise seg på tavlen {.activity}

*Vi vil at noen forskjellige bilder skal komme opp på tavlen.*

## Sjekkliste {.check}

+ Start et nytt Scratch-prosjekt og slett kattefiguren.

+ Klikk på scenen og deretter `Bakgrunner`-fanen.  Åpne biblioteket
  med bakgrunner ved å trykke på
  ![Velg en ferdig bakgrunn](../bilder/velg-bakgrunn.png) og velg
  så `Innendørs/chalkboard`.

+ Importer en valgfri figur. Velg gjerne en figur fra `Ting`-mappen.

+ Plasser figuren på midten av tavlen, og endre størrelsen hvis den
  ikke passer.

+ Legg til fire nye drakter fra `Ting`-mappen. Du kan velge de
  figurene du vil!

+ La oss nå få en tilfeldig ting til å dukke opp på tavlen. Bruk dette
  skriptet.

  ```blocks
  når grønt flagg klikkes
  bytt drakt til (tilfeldig tall fra (1) til (5))
  ```

## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

+ Endrer figuren seg?

+ Klikk flere ganger. Får figuren stadig nye drakter? Flott.

Det gjør ingenting om samme drakt kommer opp flere ganger på rad. Det
er helt normalt når det velges en tilfeldig drakt hver gang.

# Steg 2: Forvreng bildet {.activity}

*La oss nå forvrenge figuren når den dukker opp på tavlen, så det blir
 vanskeligere å gjette hva det er. Deretter skal vi gradvis gjøre vi
 den tydeligere igjen.*

Vi skal bruke en `poeng`{.blockdata}-variabel til å kontrollere
graden av forvrenging. Dersom poengscoren er høy vil bildet bli veldig
forvrengt. Når antallet poeng synker, vil også graden av forvrenging
synke. Poengvariabelen fungerer dermed som en slags tidteller.

## Sjekkliste {.check}

+ Velg `Data`{.blockdata}-kategorien og lag en variabel kalt
  `poeng`{.blockdata}. La den gjelde `for alle figurer`.

+ Endre skriptet slik:

  ```blocks
  når grønt flagg klikkes
  bytt drakt til (tilfeldig tall fra (1) til (5))
  sett [poeng v] til [110]
  gjenta til <(poeng) = [0]>
      endre [poeng v] med (-10)
      sett [piksel v] effekt til (poeng)
      sett [farge v] effekt til (poeng)
      vent (1) sekunder
  slutt
  ```

## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

+ Kommer det opp et tilfeldig og forvrengt bilde?

+ Blir bildet gradvis tydeligere?

+ Går poengsummen ned i takt med at bildet blir tydeligere?

+ Blir bildet fullstendig tydelig når poengsummen er 0?

+ Får du fremdeles nye ting på tavlen når du klikker på det grønne
  flagget?

## Ting å prøve {.try}

+ Prøv å __endre poengsummen__ fra start, samt hvor mye den skal
  __forandre seg__ for hver gang den går gjennom løkken. Hvordan
  endrer det utseendet til bildet? Blir det vanskeligere eller enklere
  å se hva bildet forestiller?

+ Forsøk noen __ulike grafiske effekter__ fra nedtrekkslisten. Hvordan
  påvirker dette vanskelighetgsraden?

# Steg 3: La spilleren prøve å gjette bildet {.activity}

Så langt har vi fått vårt tilfeldige bilde til å gradvis bli
tydeligere samtidig som poengsummen synker. Men hvordan skal man
vinne spillet? Vi vil legge til noen figurer nederst på skjermen som
spilleren kan klikke på. Klikker man på den rette, vinner man
spillet. Klikker man feil forsvinner figuren og spillet fortsetter.

Først må vi å vite hva det rette svaret er.

## Sjekkliste {.check}

+ Lag en ny variabel og kall den `riktig`{.blockdata}. Pass på at den
  er tilgjengelig `for alle figurer`. Fjern avhukingen slik at
  variabelen ikke vises i spillet.

+ Endre skriptet slik at det klarer å holde styr på hva som er rett
  svar.  Etter at vi har bestemt drakten legger du derfor til klossen
  `sett riktig til`{.blockdata}`drakt nr.`{.blocklooks}:

  ```blocks
  når grønt flagg klikkes
  bytt drakt til (tilfeldig tall fra (1) til (5))
  sett [riktig v] til (drakt nr.)
  sett [poeng v] til [110]
  gjenta til <(poeng) = [0]>
      endre [poeng v] med (-10)
      sett [piksel v] effekt til (poeng)
      sett [farge v] effekt til (poeng)
      vent (1) sekunder
  slutt
  ```

Nå skal vi legge til flere figurer som spilleren kan klikke på.

+ Gi først figuren din navnet `Spørsmål`.

+ Lag så en kopi av figuren ved å høyreklikke på den. På scenen drar
  du deretter den nye figuren ned i venstre hjørne.

+ Endre denne nye figurens navn til `Svar1`.

+ Slett skriptet til `Svar1` og alle draktene bortsett fra den første.

+ Gjenta de tre siste stegene igjen (kall neste kopi `Svar2`), plasser
  `Svar2` ved siden av `Svar1` og slett alle bortsett fra den andre
  drakten.

+ Gjenta disse punktene tre ganger til, slik at du har også figurene
  `Svar3`, `Svar4` og `Svar5`.

  Du skal nå ha en rad med fem svar-figurer nederst på scenen, hver
  viser en drakt som hovedfiguren kan ha. Ingen av `Svar`-figurene
  skal ha skript knyttet til seg.

+ Nå må vi få alle figurene til å reagere når de blir klikket på. Hva
  som skal skje avhenger av om spilleren har klikket riktig eller
  galt. Legg til dette skriptet til `Svar1`:

  ```blocks
  når denne figuren klikkes
  hvis <(riktig) = [1]>
      send melding [Vant v]
  ellers
      skjul
  slutt
  ```

+ Dra skriptet over til de andre figurene, slik at alle får hver sin
  kopi. For hver figur, bytt 1 til 2, 3, og så videre.

+ Nå skal vi lage skriptet som gir melding til spilleren når han har
  vunnet. Klikk på `Spørsmål` igjen og legg til dette skriptet:

  ```blocks
  når jeg mottar [Vant v]
  si (sett sammen [Gratulerer! Din poengsum ble ] (poeng))
  ```

## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

Når du tester spillet kan du se på spørsmålsfiguren under scenen for å
se hva riktig svar er. Det fungerer bra for testing.

+ Hva skjer når du klikker på riktig svar?

+ Hva skjer når du klikker på galt svar?

+ Hva skjer med det gale svaret når du starter et nytt spill?

## Sjekkliste {.check}

Denne testen viser oss __to problemer__: Først og fremst, ting som ble
klikket på ved galt svar kommer ikke tilbake når et nytt spill
starter.  For det andre, poengsummen fortsetter å gå ned, også etter
at man har klikket på riktig svar.

+ For å fikse det første problemet kan vi bare legge til følgende
  skript for hver av de fem svarfigurene:

  ```blocks
  når grønt flagg klikkes
  vis
  ```

For å fikse det andre problemet må vi få stoppet spørsmålfigurens
`gjenta til`{.blockcontrol}-løkke når spilleren klikker på riktig
svar. Vi kan bruke en ny variabel for å gjøre det.  Vi vil kalle denne
variabelen `vant`{.blockdata} og legger inn en
`sett`{.blockdata}-kloss som gir den verdien `0` når spillet starter,
og en tilsvarende kloss som setter verdien til `1` når spillet
vinnes. Se skriptene nedenfor.

+ Vi må videre stoppe `gjenta til`{.blockcontrol}-løkken når
  poengsummen har blitt `0` eller `vant`{.blockdata} er `1`.

+ Til slutt legger vi også inn en `ta bort grafiske
  effekter`{.blocklooks}-kloss som avslører spørsmålsfiguren når
  spilleren har gjettet riktig. Skriptene på `Spørsmål` skal nå se
  slik ut:

  ```blocks
  når grønt flagg klikkes
  bytt drakt til (tilfeldig tall fra (1) til (5))
  sett [riktig v] til (drakt nr.)
  sett [poeng v] til [110]
  sett [vant v] til [0]
  gjenta til <<(poeng) = [0]> eller <(vant) = [1]>>
      endre [poeng v] med (-10)
      sett [piksel v] effekt til (poeng)
      sett [farge v] effekt til (poeng)
      vent (1) sekunder
  slutt

  når jeg mottar [Vant v]
  sett [vant v] til [1]
  ta bort grafiske effekter
  si (sett sammen [Gratulerer! Din poengsum ble] (poeng))
  ```

## Lagre prosjektet {.save}

__Gratulerer! Du er nå ferdig med spillet.__

Men det finnes mange flere ting du kan gjøre med spillet. Prøv deg
gjerne på utfordringene nedenfor!

## Utfordring 1: Gjør spillet enklere eller vanskeligere {.challenge}

Endre vanskelighetsgrad for spillet.

* Forsøk å endre hvor lenge bildet vises frem og hvor raskt
  poengsummen minker.
* Forsøk å endre forvrengingen av bildet.
* Forsøk å gjøre figurene likere hverandre eller mer forskjellig. Husk
  også å forandre svarfigurenes drakter.

## Utfordring 2: Forvreng bildet ulikt fra gang til gang {.challenge}

For øyeblikket bruker spillet samme forvrengingsalgoritme hele
tiden. Men i steg 2 prøvde du kanskje ut noen forskjellige
alternativer. Prøv nå om du kan finne noen flere forvrenginger som du
synes fungerer like bra som `farge` og `piksler`.

Endre spillet slik at hvert spill bruker forskjellige forvrengninger i
`gjenta til`{.blockcontrol}-løkken.

__Hint:__ Forsøk å opprette en ny variabel som du kaller
`forvrenging`. Sett denne til en tilfeldig verdi i starten av
spillet. Bruk så `hvis`{.blockcontrol}-klosser i `gjenta
til`{.blockcontrol}-løkken for å velge ut en forvrenging til hvert
spill.

## Utfordring 3: La hvert spill ha flere runder {.challenge}

For øyeblikket er hvert spill uavhengig av andre. Prøv om du kan legge
til flere runder slik at man får gjette på for eksempel tre ting og
kan vinne inntil 300 poeng.

__Hint:__ Du vil trenge en ekstra variabel for å lagre den totale
poengsummen. Du må også ha en løkke som går rundt for hver runde.

## Utfordring 4: Øk vanskelighetsgraden gradvis {.challenge}

Gjør nå spillet vanskeligere og vanskeligere for hver runde.

Kanskje hver runde også skal gi ulikt antall poeng? Bør spilleren også
få ekstra mange poeng for å gjette kjapt i de vanskeligste rundene?

__Hint:__ Hvordan kan du vite hvilken runde du er i? Hvordan kan du
bruke det til å endre vanskelighetsgraden og poengsummen?

## Utfordring 5: Fortsett til spilleren gjør feil {.challenge}

I stedet for et bestemt antall runder kan du la spillet gå til det
blir klikket på feil svar. Dette fungerer nok best dersom man også
øker vanskelighetsgraden utover i spillet.

## Utfordring 6: Tilpass spillet til hvor flink spilleren er {.challenge}

I stedet for å gjøre det stadig vanskeligere kan vi tilpasse
vanskelighetsgraden til spillernes dyktighet. Hvis de raskt gjetter
riktig ting, kan den neste runden gjøres vanskeligere. Hvis de klikker
feil eller gjetter sakte, kan neste runde gjøres enklere.

Dette fungerer bare hvis du ikke samler opp poengsummen fra runde til
runde.

## Utfordring 7: Hold styr på rekorden {.challenge}

Finn en måte å lagre den høyeste poengsummen på. Klarer du også å
lagre navnet til spilleren, og få spillet til å si hvem som har
rekorden?

## Utfordring 8: Gi en straff for galt svar {.challenge}

Slik spillet er nå kan man bare klikke som en gal på alle svarene, og
dermed raskt finne riktig svar. Det kan derfor være en god idé å
trekke fra poeng hver gang spilleren klikker på feil figur.

Gjør dette spillet bedre?

## Lagre prosjektet{.save}

__Veldig bra! Nå er du ferdig og kan spille det nye spillet du har
laget!__

Ikke glem å dele spillet ditt med venner og familie ved å trykke på
`Legg ut` i menyen!
