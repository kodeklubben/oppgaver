---
title: Snøballkrig
level: 4
author: 'Geir Arne Hjelle'
translator: 'Stein Olav Romslo'
language: nn
---


# Introduksjon {.intro}

I denne oppgåva skal me lage eit spel der det er om å gjere å jage bort dei
slemme gutane ved å kaste snøball på dei. Undervegs lærer me korleis me kan
gjere spelet meir utfordrande etter kvart ved at figurane me speler mot blir
raskare og vanskelegare å jage bort.

![Illustrasjon av eit ferdig snøballkrig-spel](snoballkrig.png)


# Steg 1: Ein snøballkastar {.activity}

*Me startar med å lage ein passande bakgrunn og snøballkastaren me skal styre.*

## Sjekkliste {.check}

- [ ] Start eit nytt prosjekt. Slett kattefiguren.

- [ ] Me skal lage ein bakgrunn. Til dette spelet treng me ein ganske enkel
  bakgrunn med litt vinterstemning. Den kan me teikne sjølv:

  Vel ![Teikn ny bakgrunn](../bilder/tegn-ny.png) for å teikne ein ny bakgrunn.
  Pass på at du brukar vektorgrafikk. Teikn ein stor firkant som dekker heilt
  bakgrunnen. Vel ei mørkeblå framgrunnsfarge og ei lysare bakgrunnsfarge. Klikk
  på målingsspannet for å fylle firkanten med farge, og vel ein overgang nedst
  til venstre. Klikk på bakgrunnen for å fylle den med farge.

  Så vel du kvit som framgrunnsfarge og lagar ein mindre boks som dekker nedre
  del av bakgrunnen. Fyll den ed passande fargar.

  ![Bilete av ein passande bakgrunn for spelet](bakgrunn.png)

  Kall bakgrunnen for `Spel`.

- [ ] Legg det følgjande skriptet på scena:

  ```blocks
  når @greenFlag vert trykt på
  send meldinga [start v]
  ```

  Dette trikset har du kanskje sett før. Det gjer det enklare for oss å kome
  attende og leggje til ein startmeny og liknande.

- [ ] Neste steg er å finne ein passande figur som me kan styre rundt og kaste
  snøballar med. Me har brukt snømannen `Fantasi/Snowman`, men du kan bruke ein
  annan figur du likar. Gi figuren namnet `Helten`.

- [ ] Lag ein ny variabel, `hastigheit`{.blockdata}, som berre gjeld for denne
  figuren, og lag dette skriptet:

  ```blocks
  når @greenFlag vert trykt på
  set storleik til (75) %
  avgrens rotering til [venstre-høgre v]
  set [hastigheit v] til [5]
  ```

  På det grøne flagget legg me innstillingar som skal gjelde for `Helten`
  gjennom heile spelet. Du må gjerne endre på storleiken og hastigheita etter
  kvart som du testar spelet, slik at du finn innstillingar du likar.

- [ ] No kan me lage hovudløkka til `Helten`. Lag ei løkke som startar på
- meldinga `start`:

  ```blocks
  når eg får meldinga [start v]
  gå til x: (0) y: (-75)
  gjenta for alltid
  slutt
  ```

- [ ] Inne i løkka treng me to `viss`{.blockcontrol}-klossar som flyttar
  `Helten` `hastigheit`{.blockdata} steg mot høgre eller venstre når piltastane
  høgre eller venstre blir trykka på. Desse lagar du sjølv.

- [ ] Til slutt lagar du ein `viss`{.blockcontrol}-kloss som sender meldinga
  `kast` når mellomrom-tasten blir trykka på.

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Beveger figuren din seg rundt på scena når du trykkar høgre og venstre
  piltast? Førebels skal det ikkje skje noko når du trykkar mellomrom, sidan det
  ikkje er nokon figurar som svarar på `kast`-meldinga.

- [ ] Sannsynlegvis må du endre litt på `y`-posisjonen figuren din startar på,
  slik at det passar med bakgrunnen.

- [ ] Viss du har ein figur med fleire drakter kan du bruke `neste
  drakt`{.blocklooks}-klossar for å animere figuren din slik at den beveger seg
  meir naturleg.


# Steg 2: Mange snøballar {.activity}

*Det blir ingen snøballkrig utan snøballar. No skal me lage kjempemange av dei!*

## Sjekkliste {.check}

- [ ] Teikn ein ny figur. Bruk sirkelverktøyet til å teikne ein liten kvit
  sirkel, og fargelegg den slik at den blir heilt kvit. Trykk på ![Vel
  senterpunkt](../bilder/velg_senterpunkt.png) og pass på at senterpunktet er
  mitt på snøballen. Kall figuren `Snøball`.

- [ ] På same måte som for `Helten` set me opp nokre standardinnstillingar for
  snøballen. Lag en variabel `hastigheit`{.blockdata} som berre gjeld for denne
  figuren.

  ```blocks
  når @greenFlag vert trykt på
  gøym
  set storleik til (40) %
  set [hastigheit v] til [10]
  ```

- [ ] Me brukar `gøym`{.blocklooks} fordi me vil lage kloner (kopiar) av
  snøballen som me kastar av garde. Dette er eit veldig nyttig triks i Scratch.
  Sjølve koden som reagerer på `kast`-meldinga er veldig enkel.

  ```blocks
  når eg får meldinga [kast v]
  lag klon av [meg v]
  ```

- [ ] Sjølve oppførselen til kvar enkelt snøball programmerer me på ein `når
  eg startar som klon`{.blockcontrol}-kloss.

  ```blocks
  når eg startar som klon
  gå til [Helten v]
  peik i retning ([retning v] av [Helten v])
  vis
  gjenta til <rører [kant v]>
      gå (hastigheit) steg
  slutt
  slett denne klonen
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Kva skjer når du trykkar mellomrom-tasten? Blir det kasta snøballar i rett
  retning?

- [ ] Det ser kanskje ikkje ut som om `Helten` kastar snøballane med hendene? Du
  kan leggje på nokre `Bevegelse`{.blockmotion}-klossar rett før du
  `vis`{.blocklooks}er snøballen for at det skal sjå betre ut.

- [ ] Som ei lita utfordring kan du prøve å leggje på litt effekt av
  tyngdekrafta på snøballen ved å endre litt på `y` medan snøballen flyr.

- [ ] Eit problem me kan leggje merke til er at `Helten` er *for* flink til å
  kaste snøball! Kvar gong me trykkar mellomrom blir det kasta mange snøballar.
  Dette kan me løyse enkelt ved å vente til mellomromtasten blir sluppe før me
  kastar snøballen. Legg til

  ```blocks
  vent til <ikkje <tasten [mellomrom v] er trykt?>>
  ```

  på `Helten`-figuren før `kast`-meldinga blir sendt.


# Steg 3: Slemme gutar {.activity}

*No skal me lage slemme gutar som prøver å ta oss. Me skal jage dei bort med
 snøballar.*

## Sjekkliste {.check}

- [ ] Lag ein ny figur. Me har brukt `Mennesker/Boy3 walking`, men du kan bruke
  den figuren du likar. Kanskje er det meir morosamt å ha snøballkrig mot eit
  monster? Kall figuren `Skumling`.

- [ ] På same måte som for snøballane vil me lage kloner av `Skumling`. Men
  fyrst bestemmer me korleis han skal sjå ut. Lag ein ny variabel
  `hastigheit`{.blockdata} som berre gjeld for denne figuren. Så lagar du
  skriptet

  ```blocks
  når @greenFlag vert trykt på
  gøym
  gå til x: (0) y: (-70)
  avgrens rotering til [venstre-høgre v]
  set storleik til (30) %
  set [hastigheit v] til [3]
  ```

- [ ] Me vil at klonene skal dukke opp med litt tilfeldig mellomrom, og frå
  begge sider av skjermen.

  ```blocks
  når eg får meldinga [start v]
  gjenta for alltid
      viss <(tilfeldig tal frå (0) til (1)) = [0]>
          peik i retning (90 v)
          set x til (-250)
      ellers
          peik i retning (-90 v)
          set x til (250)
      slutt
      lag klon av [meg v]
      vent (tilfeldig tal frå (2) til (4)) sekund
  slutt
  ```

- [ ] På same måte som for snøballane må me bestemme oppførselen for kvar enkelt
  `Skumling`.

  Lag ein `når eg startar som klon`{.blockcontrol}-kloss der du fyrst viser
  figuren, og så lagar ei `for alltid`{.blockcontrol}-løkke der figuren beveger
  seg `hastigheit`{.blockdata} steg og så ventar ein augneblink, til dømes 0,1
  sekund.

- [ ] Så lagar me ein *ny* `når eg startar som klon`{.blockcontrol}-kloss
  der me undersøker om me treffer anten ein `Snøball` eller `Helten`.

  ```blocks
  når eg startar som klon
  gjenta for alltid
      viss <rører [Helten v]?>
          send meldinga [slutt v]
          slett denne klonen
      slutt
      viss <rører [Snøball v]?>
          slett denne klonen
      slutt
  slutt
  ```

  Grunnen til at desse må liggje i eit eige skript er at det fyrste skriptet
  ventar litt mellom kvar gong figuren tek eit steg. Hadde me lagt desse
  `viss`{.blockcontrol}-klossane i det same skriptet ville me berre sjekka om
  `Skumling` vart treft av ein snøball mellom ventinga. Ved å lage eit eige
  skript sjekkar me det heile tida.

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Dukkar det opp skumlingar? Kjem dei frå begge sider? Går dei mot midten?

- [ ] Kva skjer når ein `Skumling` blir treft av ein `Snøball`? Du kan kanskje
  leggje på ein passande lydeffekt og animasjon før klonen blir sletta? Me ser
  og at snøballen flyr vidare etter at den har truffe ein `Skumling`. Prøv å
  endre i skriptet for `Snøball` slik at snøballen forsvinn når den treff.

- [ ] Kva skjer når ein `Skumling` tek `Helten`?


# Steg 4: Telje poeng og avslutte spelet {.activity}

*No som me nesten har eit ferdig spel, så vil me telje poeng!*

## Sjekkliste {.check}

- [ ] Å telje poeng er ganske lett. Lag ein variabel som heiter
  `Poeng`{.blockdata} og la den gjelde for alle figurar. La variabelen vere
  synleg på scena, slik at me ser kor mange poeng me har fått.

- [ ] Pass på at `Poeng`{.blockdata} blir sett til 0 når meldinga `start`
  blir sendt, til dømes med eit skript på scena.

- [ ] Endre `Poeng`{.blockdata} med 1 når ein `Skumling` blir treft av ein
  snøball.

Tidlegare laga me meldinga `slutt` som blir sendt ut når `Helten` blir teken av
ein `Skumling`. No skal me bruke denne til å avslutte spelet. Fyrst lagar me ein
meny og ein bakgrunn som fortel att me tapte.

- [ ] Klikk på `Scene` til venstre for `Figurer`, og vel `Bakgrunnar`-fana.
  Lag to kopiar av bakgrunnen din og kall dei henhaldsvis `Meny` og `Slutt`.

  På `Meny`-bakgrunnen kan du lage ein fin tittel. Skriv `Trykk 'S' for å
  starte`.

  På `Slutt`-bakgrunnen kan du skrive ei passande melding for når spelet er
  slutt. Skriv `Trykk 'S' for å spele igjen`.

- [ ] Endre litt på skripta på scena. Fyrst vil me berre vise menyen når det
- grøne flagget blir klikka på:

  ```blocks
  når @greenFlag vert trykt på
  byt bakgrunn til [Meny v]
  ```

  Så vil me starte spelet når `S` blir trykka på:

  ```blocks
  når [s v] vert trykt
  send meldinga [start v]
  ```

  Pass på at du byttar til bakgrunnen `Spel` når meldingen `start` blir motteke,
  og til bakgrunnen `Slutt` når meldinga `slutt` blir motteke.

- [ ] Til slutt må me passe på at spelet faktisk blir avslutta når
  `slutt`-meldingen blir sendt. Legg på skript for å `slette denne
  klonen`{.blockcontrol} på `Snøball` og `Skumling`, og skript for å gøyme
  `Helten` når `slutt` blir motteke.

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Fungerer programflyten? Startar spelet når du trykkar `S`? Blir spelet
  avslutta når `Helten` blir fanga? Visast dei riktige bakgrunnane når dei skal?

- [ ] Du må gjerne leggje på lydeffektar og enkle animasjonar der det passar.


# Steg 5: Store, slemme gutar {.activity}

*Til slutt skal me gjere spelet vanskelegare di lengre me speler.*

- [ ] Fyrst lagar me ein ny variabel `Nivå`{.blockdata} som skal gjelde for alle
  figurar. Denne styrer kor vanskeleg spelet skal vere. Du må gjerne la den vere
  synleg.

- [ ] Me reknar ut nivå basert på `Poeng`{.blockdata}. Utvid skriptet ditt som
  tek imot `start`-meldinga på scena med den følgjande løkka:

  ```blocks
  gjenta for alltid
      set [Nivå v] til ((1) + ([golv v] av ((Poeng) / (5))))
  slutt
  ```

  Funksjonen `gulv`{.blockoperators} rundar nedover. Så med denne løkka aukar
  `Nivå`{.blockdata} for kvar femte `Skumling` me jagar vekk.

- [ ] No kan me bruke `Nivå`{.blockdata} til å endre `Skumling`. Til dømes kan
  dei bli større, gå raskare og kanskje trenge fleire snøballar før dei blir
  borte.

  Lag eit par nye variablar som gjeld for denne figuren: `Slem`{.blockdata} og
  `Liv`{.blockdata}. `Slem`{.blockdata} seier kor stor og slem den enkelte
  `Skumling` er. Ved å la det vere eit tal mellom 1 og `Nivå`{.blockdata} blir
  spelet vanskelegare etter kvart som `Nivå`{.blockdata} aukar. Til dømes kan du
  leggje til desse klossane i hovudskriptet til `Skumling`:

  ```blocks
  når eg startar som klon
  set [Slem v] til (tilfeldig tal frå (1) til (Nivå))
  set [Liv v] til (Slem)
  endra [hastigheit v] med (Slem)
  endra [farge v]-effekt med ((10) * (Slem))
  endra storleik med ((5) * (Slem))
  vis
  gjenta for alltid
      gå (hastigheit) steg
      vent (0.1) sekund
  slutt
  ```

- [ ] For at ein `Skumling` skal tåle fleire snøballar må me endre litt på kva
  som skjer når den blir treft. I staden for å berre slette klonen vil me endre
  `Liv`{.blockdata} med -1, og så gi poeng og slette klonen berre viss
  `Liv`{.blockdata} er 0.

- [ ] Kanskje bør me gi fleire poeng for å jage bort ein større `Skumling`. Det
  gjer du ved å endre `Poeng`{.blockdata} med `Slem`{.blockdata} når ein
  `Skumling` blir jaga bort.

- [ ] Viss me får meir enn eitt poeng for kvar `Skumling` bør me endre på
  korleis me reknar ut `Nivå`{.blockdata}. Viss ikkje blir spelet veldig fort
  mykje vanskelegare. Til dømes kan du bruke denne utrekninga:

  ```blocks
  gjenta for alltid
      set [Nivå v] til ((1) + ([gulv v] av ([kvadratrot v] av ((Poeng) / (3)))))
  slutt
  ```

  Då aukar framleis nivået for omlag kvar femte `Skumling` som blir jaga bort.

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Blir spelet vanskelegare etter kvart? Prøv å endre på dei ulike variablane
  og innstillingane me har laga slik at spelet blir passe vanskeleg.

- [ ] Har du fleire idear til korleis spelet kan bli endå meir morosamt? Prøv
  dei ut!
