---
title: 'Kva er det?'
level: 3
author: 'Omsett frå [Code Club UK](//codeclub.org.uk)'
translator: 'Stein Olav Romslo'
language: nn
---


# Introduksjon {.intro}

Me viser eit forvrengt bilete av ein tilfeldig ting på tavla. Spelaren skal
gjette kvar det er ved å klikke på eitt av alternativa under. Jo raskare
spelaren gjettar riktig, jo fleire poeng får han.

![Illustrasjon av eit ferdig "Kva er det"-spel](hva_er_det.png)


# Steg 1: Få fleire ting til å vise seg på tavla {.activity}

*Me vil at fleire ulike bilete skal kome til syne på tavla.*

## Sjekkliste {.check}

- [ ] Start eit nytt Scratch-prosjekt og slett kattefiguren.

- [ ] Klikk på scena og så `Bakgrunner`-fana. Åpne biblioteket med bakgrunnar
  ved å trykke på ![Vel ein ferdig bakgrunn](../bilder/velg-bakgrunn.png) og vel
  `Innendørs/chalkboard`.

- [ ] Importer ein valfri figur. Du kan gjerne velje noko frå `Ting`-mappa.

- [ ] Plasser figuren på midten av tavla, og endre storleiken viss den ikkje
  passar.

- [ ] Legg til fire nye drakter frå `Ting`-mappa. Du kan velje dei figurane du
  vil!

- [ ] No skal me få ein tilfeldig ting til å dukke opp på tavla. Bruk dette
  skriptet:

  ```blocks
  når @greenFlag vert trykt på
  byt drakt til (tilfeldig tal frå (1) til (5))
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Endrar figuren seg?

- [ ] Klikk fleire gonger. Får figuren stadig nye drakter? Flott.

Det gjer ikkje noko viss den same drakta kjem opp fleire gonger på rad. Det er
heilt normalt når me vel ei tilfeldig drakt kvar gong.


# Steg 2: Forvreng biletet {.activity}

*No skal me forvrenge figuren når den dukkar opp på tavla, slik at det blir
vanskelegare å gjette kva det er . Så skal me gradvis gjere den tydelegare
att.*

Me skal bruke ein `poeng`{.blockdata}-variabel til å kontrollere graden av
forvrenging. Viss poengscoren er høg er biletet veldig forvrengt. Når poenga går
ned, så skal graden av forvrenging gå ned. Slik fungerer poengvariabelen som ein
slags tidteljar.

## Sjekkliste {.check}

- [ ] Vel `Data`{.blockdata}-kategorien og lag ein variabel du kallar
  `poeng`{.blockdata}. La den gjelde `for alle figurar`.

- [ ] Endre skriptet slik:

  ```blocks
  når @greenFlag vert trykt på
  byt drakt til (tilfeldig tal frå (1) til (5))
  set [poeng v] til [110]
  gjenta til <(poeng) = [0]>
      endra [poeng v] med (-10)
      set [piksel v]-effekt til (poeng)
      set [farge v]-effekt til (poeng)
      vent (1) sekund
  slutt
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Kjem det opp eit tilfeldig og forvrengt bilete?

- [ ] Blir biletet gradvis tydelegare?

- [ ] Går poengsummen ned i takt med at biletet blir tydelegare?

- [ ] Blir biletet fullstendig tydelig når poengsummen er 0?

- [ ] Får du framleis nye ting på tavla når du klikkar på det grøne flagget?

## Ting å prøve {.challenge}

- [ ] Prøv å __endre poengsummen__ frå start og kor mykje den skal __forandre
  seg__ for kvar gong den går gjennom løkka. Korleis endrar det utsjånaden til
  biletet? Blir det vanskelegare eller enklare å sjå kva biletet er?

- [ ] Prøv nokre __ulike grafiske effektar__ frå nedtrekkslista. Korleis
  påverkar dette vanskegraden?


# Steg 3: La speleren prøve å gjette biletet {.activity}

Til no har me fått det tilfeldige biletet til å bli gradvis tydelegare
samstundes som poengsummen går ned. Men korleis vinn ein spelet? Me skal leggje
til nokre figurar nedst på skjermen som spelaren kan klikke på. Klikkar ein på
den rette vinn ein spelet. Klikkar ein feil blir figuren borte og spelet
fortset.

Fyrst må me vite kva det rette svaret er.

## Sjekkliste {.check}

- [ ] Lag ein ny variabel og kall den `riktig`{.blockdata}. Pass på at den er
  tilgjengeleg `for alle figurar`. Fjern avhukinga slik at variabelen ikkje er
  synleg i spelet.

- [ ] Endre skriptet slik at det klarar å halde styr på kva som er rett svar.
  Etter at me har bestemt drakta må du difor leggje til klossen `set riktig
  til`{.blockdata}`drakt nr.`{.blocklooks}:

  ```blocks
  når @greenFlag vert trykt på
  byt drakt til (tilfeldig tal frå (1) til (5))
  set [riktig v] til (drakt nr.)
  set [poeng v] til [110]
  gjenta til <(poeng) = [0]>
      endra [poeng v] med (-10)
      set [piksel v]-effekt til (poeng)
      set [farge v]-effekt til (poeng)
      vent (1) sekund
  slutt
  ```

No skal me leggje til fleire figurar som spelaren kan klikke på.

- [ ] Gi figuren din namnet `Spørsmål`.

- [ ] Lag ein kopi av figuren ved å høgreklikke på den. På scena dreg du den nye
  figuren ned i venstre hjørne.

- [ ] Endre namnet til den nye figuren til `Svar1`.

- [ ] Slett skriptet til `Svar1` og alle draktene bortsett frå den første.

- [ ] Gjenta dei tre siste stega (kall neste kopi `Svar2`), plasser `Svar2` ved
  sidan av `Svar1` og slett alle bortsett frå den andre drakta.

- [ ] Gjenta dette tre gonger til, slik at du har figurane `Svar3`, `Svar4` og
  `Svar5` òg.

  No skal du ha ei rad med fem svar-figurar nedst på scena, der kvar har ei
  drakt som hovudfiguren kan ha. Ingen av svar-figurane skal ha skript knytta
  til seg.

- [ ] Det neste me må gjere er å få figurane til å reagere når me klikkar på
  dei. Kva som skal skje er avhengig av om spelaren svarar riktig eller feil.
  Legg til dette skriptet til `Svar1`:

  ```blocks
  når denne figuren vert trykt på
  viss <(riktig) = [1]>
      send meldinga [Vann v]
  ellers
      gøym
  slutt
  ```

- [ ] Dra skriptet over til dei andre figurane, slik at alle får kvar sin kopi.
  For kvar figur må du bytte 1 til 2, 3, 4 og 5.

- [ ] No skal me lage skriptet som gir melding til spelaren om at han har vunne.
  Klikk `Spørsmål` att og legg til dette skriptet:

  ```blocks
  når eg får meldinga [Vann v]
  sei (set saman [Gratulerer! Poengsummen din vart ] (poeng))
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

Når du testar spelet kan du sjå på spørsmålsfiguren under scena for å sjå kva
som er rett svar. Det fungerer bra når du skal teste det.

- [ ] Kva skjer når du klikkar på riktig svar?

- [ ] Kva skjer når du klikkar på feil svar?

- [ ] Kva skjer med det galne svaret når du startar eit nytt spel?

## Sjekkliste {.check}

Denne testen viser oss __to problem__: Fyrst og fremst, ting som vart klikka på
og var feil kjem ikkje tilbake når du startar eit nytt spel. For det andre
fortset poengsummen å gå ned, også etter at du har klikka på riktig svar.

- [ ] For å fikse det fyrste problemet kan me leggje til det følgande skriptet
  for kvar av dei fem svarfigurane.

  ```blocks
  når @greenFlag vert trykt på
  vis
  ```

For å fikse det andre problemet må me stoppe `gjenta til`{.blockcontrol}-løkka
til spørsmålfiguren når spelaren klikkar på rett svar. Me kan bruke ein ny
variabel for å gjere det. Denne vil me kalle `vant`{.blockdata}. Me legg inn ein
`sett`{.blockdata}-kloss som gir den verdien `0` når spelet startar, og ein
tilsvarande kloss som set verdien til `1` når spelaren vinn. Sjå skripta under.

- [ ] Vidare må me stoppe `gjenta til`{.blockcontrol}-løkka når poengsummen har
  blitt `0` eller `vant`{.blockdata} er `1`.

- [ ] Til slutt legg me inn ein `ta bort grafiske effekter`{.blocklooks}-kloss
  som viser kva spørsmålsfiguren er når brukaren har gjetta riktig. No skal
  skripta på `Spørsmål` sjå slik ut:

  ```blocks
  når @greenFlag vert trykt på
  byt drakt til (tilfeldig tal frå (1) til (5))
  set [riktig v] til (drakt nr.)
  set [poeng v] til [110]
  set [vant v] til [0]
  gjenta til <<(poeng) = [0]> eller <(vant) = [1]>>
      endra [poeng v] med (-10)
      set [piksel v]-effekt til (poeng)
      set [farge v]-effekt til (poeng)
      vent (1) sekund
  slutt

  når eg får meldinga [Vann v]
  set [vant v] til [1]
  ta vekk grafiske effektar
  sei (set saman [Gratulerer! Poengsummen din vart ] (poeng))
  ```

## Lagre prosjektet {.save}

__Gratulerer! Du er ferdig med spelet.__

Men det er mange fleire ting du kan gjere med spelet. Du må gjerne prøve på
utfordringane under!

## Utfordring 1: Gjer spelet enklare eller vanskelegare {.challenge}

Endre vanskegraden for spelet.

- Prøv å endre kor lenge biletet blir vist fram og kor raskt poengsummen minkar.

- Prøv å endre forvrenginga av biletet.

- Prøv å gjere figurane likare kvarandre eller meir ulike. Hugs å endre draktene
  på svarfigurane!

## Utfordring 2: Forvreng biletet ulikt frå gong til gong {.challenge}

No brukar spelet same forvrengingsalgoritme heile tida. Men i steg 2 prøvde du
kanskje nokre andre alternativ. Prøv om du kan finne nokre andre forvrengingar
som du synest fungerer like bra som `farge` og `piksler`.

Endre spelet slik at kvart spel brukar ulike forvrengingar i `gjenta
til`{.blockcontrol}-løkka.

__Hint:__ Lag ein ny variabel som du kallar `forvrenging`. Set denne til ein
tilfeldig verdi i starten av spelet. Så brukar du `viss`{.blockcontrol}-klossar
i `gjenta til`{.blockcontrol}-løkka for å velje ei forvrengingsalgoritme til
kvart spel.

## Utfordring 3: La kvart spel ha fleire runder {.challenge}

No er kvart spel uavhengig av andre. Prøv å leggje til fleire runder slik at du
kan gjette til dømes tre ting, og få inntil 300 poeng.

__Hint:__ Du treng ein ekstra variabel for å lagre den totale poengsummen.
Dessutan må du ha ei løkke som går rundt for kvar runde.

## Utfordring 4: Auk vanskegraden gradvis {.challenge}

Gjer spelet vanskelegare og vanskelegare for kvar runde.

Skal kvar runde gi ulikt antal poeng? Bør spelaren få ekstra mange poeng for å
gjette raskt i dei vanskelegaste rundene?

__Hint:__ Korleis kan du vite kva runde du er i? Korleis kan du bruke det til å
endre vanskegraden og poengsummen?

## Utfordring 5: Fortset til spelaren gjer feil {.challenge}

I staden for eit bestemt antal runder kan du la spelet gå til det blir klikka på
feil svar. Det fungerer nok best dersom du også aukar vanskegraden utover i
spelet.

## Utfordring 6: Tilpass spelet til kor flink spelaren er {.challenge}

I staden for at spelet stadig blir vanskelegare kan vanskegraden bli tilpassa
spelaren. Viss dei gjettar riktig ting raskt, så kan du gjere den neste runden
vanskelegare. Viss dei klikkar feil eller gjettar sakte kan neste runde vere
enklare.

Dette fungerer berre viss du ikkje samlar opp poengsummen frå runde til runde.
Ellers må du lage endå fleire variablar.

## Utfordring 7: Hald styr på rekorden {.challenge}

Finn ein måte å lagre den høgaste poengsummen på. Klarar du å lagre namnet til
spelaren og å få spelet til å seie kven som har rekorden?

## Utfordring 8: Gi ein straff for feil svar {.challenge}

No kan ein klikke på alle svaralternativa og slik finne det rette svaret raskt.
Kanskje det er lurt å trekke frå poeng kvar gong spelaren klikkar på feil figur?

Blir spelet betre?

## Lagre prosjektet {.save}

__Veldig bra! No er du ferdig og kan spele det nye spelet du har laga!__

Ikkje gløym å dele spelet ditt med vener og familie ved å trykke på `Legg ut` i
menyen!
