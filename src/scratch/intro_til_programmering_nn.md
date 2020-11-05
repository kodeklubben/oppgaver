---
title: Introduksjon til programmering
author: Gubrand Tandberg
translator: 'Stein Olav Romslo'
indexed: false
language: nn
---


# Programmering

Scratch er eit programmeringsspråk som gjer det enkelt å lage dine eigne
interaktive eventyr, spel og animasjonar - og så dele det med andre på
Internett. Dette dokumentet er ein liten introduksjon til kva dataprogrammering
eigentleg er, og litt om dei grunnleggjande konsepta i dataprogrammering. Desse
grunnleggjande konsepta er ikkje berre grunnleggjande i Scratch, men faktisk i
alle andre programmeringsspråk òg.

Du brukar dataprogram kvar einaste dag, anten du veit det eller ikkje. Nokre
finn du på datamaskina di, til dømes Word eller Minecraft, andre ser du ikkje i
det heile. Døme på skjulte dataprogram er program som styrer trafikklys,
autopilot til fly, sanntidsystemet på bussen, betalingsautomatar for kort,
navigasjonsystem i bilen og mykje, mykje meir. Kort sagt kan eit dataprogram
gjere akkurat det du vil gjere, for bak kvart einaste dataprogram som finst er
det eit menneske som har skrive det.

Når eit menneske skriv eit program til ein datamaskin, så kan ho ikkje skrive på
norsk. Datamaskinar pratar jo ikkje norsk! Engelsk fungerer heller ikkje. Dei
språka datamaskina kan heiter __programmeringsspråk__, og det er desse soråka me
skriv dataprogram i. Scratch er eit døme på eit programmeringsspråk. Andre
kjente programmeringsspråk er Java, Python og C.

Men kva er eigentleg eit dataprogram. Et dataprogram er ei __mengde med
instruksar__ som programmeraren ynskjer at datamaskina skal følgje til punkt og
prikke. Ein kan sjå på det som ei slags oppskrift som datamaskina skal følgje.
Men sidan datamaskina ikkje kan tenke må oppskrifta vere så nøyaktig at det
ikkje *kan* gå gale. Jobben til ein programmerar er å skrive oppskrifter som
datamaskiner må følgje til punkt og prikke. For sjølv om datamaskiner ikkje kan
tenke sjølv, så er dei utruleg flinke til å gjere akkurat det me menneske har
bedt dei om å gjere.

La oss sjå på dei grunnleggjande byggjeklossane i eit dataprogram.

## Variablar

I dei aller fleste program har me bruk for å lagre informasjon, og på ein slik
måte at den er legg tilgjengeleg for å bruke seinare. Då brukar me ein
__variabel__ for å halde på informasjonen. Viss eg vil skrive eit
biblioteksprogram kan det vere ein god idé å lage ein variabel for kvar bok i
biblioteket. Ein kan gi variablar eit __namn__ og eit __innhald__. I
biblioteksdømet kunne me gitt ein variabel namnet "Ringenes Herre" og innhaldet
vil vere all teksten i Ringenes Herre-bøkene. Sånn sett kan ein sjå på variablar
som skuffar for å oppbevare data du brukar i programmet ditt. I Scratch finn du
alt som har med variablar å gjere under `Data`{.blockorange}. For å lage ein ny
variabel klikkar du på `Lag en variabel`{.blocklightgrey}. Du kan endre verdien
til variabelen med blokka `sett [variabel v] til [0]`{.blockorange}. I spel kan
variablar vere nyttige for å halde styr på poeng, tid, tur, hastigheit, vinnar
og mykje meir.

## Løkker

Veldig ofte har me behov for å gjere nokre instruksar fleire
gonger. La oss seie at me vil at datamaskina vår skal lage
(data)pannekaker. Då vil me at datamaskina skal hente eit egg, knuse
det i bollen og røre rundt. Og me vil at den skal gjere det mange
gonger. Då kan me bruke det som heiter ei __løkke__ for å be den gjere
den same oppgåva (blande inn eit egg) så mange gonger me vil. I
Scratch finn me alle løkkene under
`Styring`{.blockyellow}-kategorien. Viss me vil at noko skal bli
repetert eit bestemt tal gonger brukar me ein `gjenta (10)
ganger`{.blockyellow}-blokk. Du legg kanskje merke til at denne blokka
ikkje er som alle andre blokker? Den har nemleg eit lite holrom der du
kan setje inn dei instruksane du vil skal repeterast. Ein annan viktig
type løkke heiter `gjenta for alltid`{.blockyellow}. I staden for å
repetere noko eit bestemt tal gonger, så repeterer den noko *for
alltid*. Då gjeld det å vere forsiktig så ein ikkje ender opp med ei
uendeleg stor eggerøre!

## Testar

Nokre gonger vil me at datamaskina berre skal utføre ein instruks *viss* eitt
eller anna vilkår er sant. Me vil til dømes berre at datamaskina skal blande eit
egg i røra *viss det ikkje er råttent*. Difor brukar me __testar__ i eit
dataprogram. Vilkåret me testar etter må vere noko som kan vere sant eller
usant. Anten er eit egg råttent, eller så er det ikkje det! Døme på andre testar
me kunne tenke oss å gjere er å sjekke om to tal er like, eller om ein figur i
eit spel har blitt eten eller om tida har gått ut. I Scratch finn me alt som har
med testar å gjere under `Styring`{.blockyellow}-kategorien. Den mest vanlege
testen me brukar heiter `hvis <>`{.blockyellow}. Legg merke til at det er eit
tomrom i blokka. Her skal du dra inn vilkåret du ynskjer å sjekke om er oppfylt
(hugs: noko som kan vere sant eller usant!). Du får ofte bruk for blokkane med
spisse kantar i `Operatorer`-kategorien i desse tomromma. Dette er blokker som
`( )=( )`{.blocklightgreen} og `( ) < ( >`{.blocklightgreen} som brukast for å
sjekke om noko er likt som eller mindre enn noko anna.

## Lister

Når ein jobbar med større mengder data, så kan det vere lurt å bruke lister. Det
er like sant for menneske på handletur som for datamaskiner. Viss me ser på ein
variabel som ein slags skuff ein kan putte informasjon i, så kan me sjå på
__lister__ som kommoder! Lister er slik sett ein lur måte å handsame mange ting
som ein einaste ting. I staden for å halde styr på ein variabel per bok i
bibliotekprogrammet vårt, så kan me putte alle bøkene (variablane) inn i ei
liste som heiter "AlleBøkene". Kommandoane i Scratch for å jobbe med lister er
ganske like som dei for variablar. Du finn dei under `Data`{.blockorange} og
lagar ei ny liste ved å trykkje på `Lag en liste`{.blocklightgrey}. Då kan du
bruke blokkar som `legg [MinVariabel] inn i [MiListe v]`{.blockorange}, for å
leggje variabelen `MinVariabel` inn i lista `MiListe` og `slett (1) fra [MiListe
v]`{.blockorange} for å slette det fyrste elementet i lista `MiListe`.

## Kodedøme

Til slutt viser me eit døme på eit tenkt program ei datamaskin kunne brukt for å
lage (data)pannekakter. Legg merke til at programmet verken er skrive heilt på
god norsk eller i eit programmeringsspråk. Det er for å gjere det meir
forståeleg.

  hent 3 egg
  hent 2 dl mjølk
  hent 2 dl mjøl
  hent 1 bakebolle

  bland mjøl i bakebolle
  bland mjølk i bakebolle

  gjenta 3 gonger:
    viss egg ikkje er råttent
      bland 1 egg i bakebollen

  gjenta til bakebollen er tom:
    steik 1 pannekake
