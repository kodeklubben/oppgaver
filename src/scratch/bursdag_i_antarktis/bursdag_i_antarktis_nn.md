---
title: Bursdag i Antarktis
level: 2
author: Caroline Tandberg
translator: 'Stein Olav Romslo'
language: nn
---

# Introduksjon {.intro}

Bursdag i Antarktis er ein interaktiv animasjon som fortel historia om ein
liten katt som har gått seg bort på bursdagen sin. Heldigvis treff han
nokre hyggelege pingvinar han kan feire saman med.

![Bilete av Felix, eit peparkakehus og to pingvinar](bursdag_i_antarktis.png)

# Steg 1: Ein katt på villspor {.activity}

*Me lagar ein katt som kan gå rundt i Antarktis på eiga hand.*

Me skal etter kvart fortelje ei spanande historie om katten som møter
dansande pingvinar på bursdagen sin. Men som alltid kjem me til å starte med
noko ganske enkelt, og så byggje vidare på det.

## Sjekkliste {.check}

- [ ] Start eit nytt prosjekt. Gi kattefiguren namnet `Felix` og set
  rotasjonsmåten hans til ![sidevegs](../bilder/rotasjonsmate-hv.png).

- [ ] Lag ein ny bakgrunn ved å klikke på
  ![vel ein ferdig bakgrunn](../bilder/velg-bakgrunn.png) nede til
  venstre på skjermen. Vel `Holiday/winter`.

- [ ] Legg til bakgrunnen `Holiday/winter-lights`.

- [ ] Me startar med eit skript på scena som passar på at me viser
  `winter`-bakgrunnen når animasjonen startar. Gå til `Skript`{.blocklightgrey}-
  fana og legg til

  ```blocks
  når @greenFlag vert trykt på
  byt bakgrunn til [winter v]
  ```

- [ ] No kan me få katten til å flytte på seg. Klikk på Felix og gi han dette
  skriptet:

  ```blocks
  når @greenFlag vert trykt på
  gå til x: (-100) y: (-50)
  ```

  Her kan du eksperimentere med å variere `x`og `y` til du finn noko du
  synest ser bra ut.

- [ ] La oss få Felix til å bevege seg over skjermen. Me skiftar mellom dei to
  draktene han har for at det skal sjå ut som om han går. Utvid skriptet til
  Felix på denne måten:

  ```blocks
  når @greenFlag vert trykt på
  gå til x: (-100) y: (-50)
  peik i retning (100 v)
  gjenta til <(x-posisjon) > [240]>
      gå (10) steg
      neste drakt
      vent (0.1) sekund
  slutt
  ```

  Talet 100 i `peik i retning`{.blockmotion}-klossen gjer at Felix går litt
  nedover medan han går over skjermen. Prøv gjerne med andre tal for å sjå
  effekten dei har.

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Går Felix over skjermen?

- [ ] Stoppar han når han kjem til kanten av skjermen?

- [ ] Startar han på nytt på venstre side av skjermen om du klikkar på det
  grøne flagget att?

### Antarktis {.protip}

Antarktis er namnet på området der Sørpolen ligg. Sjølv om det ikkje bur
verken menneske eller kattar fast på Antarktis finst det veldig mange
pingvinar der.

## Sjekkliste {.check}

No vil me få bakgrunnen til å endre seg når katten kjem til enden av skjermen.
Me startar med noko enkelt, men som diverre ikkje fungerer så veldig bra.

- [ ] Lag eit nytt skript på scena.

  ```blocks
  når @greenFlag vert trykt på
  vent (3) sekund
  byt bakgrunn til [winter-lights v]
  ```

- [ ] Legg til ein kloss som flyttar Felix inn til vegen etter at bakgrunnen
  er bytta.

  ```blocks
  når @greenFlag vert trykt på
  gå til x: (-100) y: (-50)
  peik i retning (100 v)
  gjenta til <(x-posisjon) > [240]>
      gå (10) steg
      neste drakt
      vent (0.1) sekund
  slutt
  gå til x: (-20) y: (-100)
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Skiftar bakgrunnen når Felix kjem til enden av skjermen?

- [ ] Klarar du å endre talet i klossen `vent 3 sekund`{.blockcontrol}
  slik at det ser betre ut?

# Steg 2: Det blir enklare med meldingar {.activity}

*No skal me starte å bruke meldingar for å få ting til å skje samstundes.*

Me har set at me kan klare å få ting til å skje samstundes ved å bruke
`vent`{.blockcontrol}-klossar. Men det er vanskeleg å finne ut akkurat kor
lenge me bør vente, og det er keisamt å måtte endre på denne tida om me til
dømes endrar kor fort Felix går.

I staden skal me bruke __meldingar__. Det er noko figurane kan sende til
kvarandre eller til scena utan at dei er synlege for oss som ser på.

## Sjekkliste {.check}

- [ ] La katten sende ei melding når han når kanten av skjermen.

  ```blocks
  når @greenFlag vert trykt på
  gå til x: (-100) y: (-50)
  peik i retning (100 v)
  gjenta til <(x-posisjon) > [240]>
      gå (10) steg
      neste drakt
      vent (0.1) sekund
  slutt
  send meldinga [Scene 2 v]
  ```

- [ ] No kan me slette det gamle skriptet på scena som bytta bakgrunnen til
  `winter-lights`, og bruke dette i staden:

  ```blocks
  når eg får meldinga [Scene 2 v]
  byt bakgrunn til [winter-lights v]
  ```

- [ ] Felix kan sende meldingar til seg sjølv. Me kan bruke dette til å flytte
  han inn på vegen samstundes som me byttar bakgrunn. Legg til følgande som
  eit nytt skript på Felix:

  ```blocks
  når eg får meldinga [Scene 2 v]
  gå til x: (-20) y: (-100)
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Går Felix framleis over skjermen?

- [ ] Kva skjer når han kjem til kanten av skjermen? Me har laga to skript som
  seier at bakgrunnen skal endre seg og katten skal flytte seg til midten
  av skjermen. Skjer det?

# Steg 3: Felix introduserer seg sjølv {.activity}

*Før Felix går synest me at han burde introdusere seg sjølv!*

Som alle høflige kattar introduserer Felix seg når han treff nye folk.

## Sjekkliste {.check}

- [ ] Start eit nytt skript på Felix:

  ```blocks
  når eg får meldinga [Si hei v]
  sei [Å nei! Kor er eg?] i (2) sekund
  tenk [Eg har gått meg bort... Og så på bursdagen min!] i (2) sekund
  spør [Kor gamal blir eg, eigentleg?] og vent
  ```

- [ ] For å teste korleis skriptet virkar kan du klikke på klossen
  `når eg får meldinga Si hei`{.blockevents}. Ser du at Felix snakkar og tenker?

- [ ] Når du svarar på Felix sitt spørsmål blir svaret ditt lagra i ein
  variabel som heiter `svar`{.blocksensing}. Me vil lage ein ny variabel med
  eit betre namn som kan ta vare på dette svaret. Lag ein ny variabel som
  heiter `alder`{.blockdata}. La denne variabelen gjelde for alle figurar, og
  fjern avhukinga slik at variabelen ikkje synast.

- [ ] Legg til ein kloss nedst i skriptet:

  ```blocks
  når eg får meldinga [Si hei v]
  sei [Å nei! Kor er eg?] i (2) sekund
  tenk [Eg har gått meg bort... Og så på bursdagen min!] i (2) sekund
  spør [Kor gamal blir eg, eigentleg?] og vent
  set [alder v] til (svar)
  ```

- [ ] No vil me at Felix skal seie og gjere alt dette før han går gjennom
  Antarktis. Legg til ein `send meldinga`{.blockevents}-kloss i det
  fyrste skriptet til Felix:

  ```blocks
  når @greenFlag vert trykt på
  gå til x: (-100) y: (-50)
  peik i retning (100 v)
  send meldinga [Si hei v]
  gjenta til <(x-posisjon) > [240]>
      gå (10) steg
      neste drakt
      vent (0.1) sekund
  slutt
  send meldinga [Scene 2 v]
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Pratar Felix som han skal?

- [ ] Det er kanskje litt uhøflig at Felix berre spring av garde medan han
  pratar med oss?

## Sjekkliste {.check}

- [ ] Me vil at Felix pratar ferdig før han startar å gå. Dette er
  heldigvis ganske enkelt. Viss me byttar ut `send
  meldinga`{.blockevents}-klossen med ein `send meldinga og
  vent`{.blockevents}-kloss, så vil ikkje Felix starte å gå før han er
  ferdig med å prate (og me har svara på spørsmålet han stiller):

  ```blocks
  når @greenFlag vert trykt på
  gå til x: (-100) y: (-50)
  peik i retning (100 v)
  send meldinga [Si hei v] og vent
  gjenta til <(x-posisjon) > [240]>
      gå (10) steg
      neste drakt
      vent (0.1) sekund
  slutt
  send meldinga [Scene 2 v]
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Ventar Felix med å gå til du har svara på spørsmålet han stiller?

# Steg 4: Gå opp mot husa {.activity}

*No er me klare til å hjelpe Felix med å finne vegen opp til dei to husa.*

Me skal la Felix gå langs vegen opp til husa. For at det skal sjå ut som han
går oppover mot husa vil me la han bli mindre og mindre medan han går.

## Sjekkliste {.check}

- [ ] No skal me fortsetje på skriptet til Felix som startar med at han
  mottek meldinga `Scene 2`. Legg til ein liten `si`{.blocklooks}-kloss først:

  ```blocks
  når eg får meldinga [Scene 2 v]
  gå til x: (-20) y: (-100)
  sei [Å! Der er det nokre hus!] i (2) sekund
  ```

- [ ] No skal me la Felix følgje vegen oppover. Prøv fyrst med følgjande skript:

  ```blocks
  når eg får meldinga [Scene 2 v]
  gå til x: (-20) y: (-100)
  sei [Å! Der er det nokre hus!] i (2) sekund
  peik i retning (20 v)
  gjenta (6) gongar
      gå (9) steg
      neste drakt
      endra storleik med (-2)
      vent (0.1) sekund
  slutt
  ```

- [ ] Følgjer Felix vegen oppover? Blir han mindre når han går? Hugs at du
  kan teste skriptet ved å klikke på `når eg får meldinga Scene 2`{.blockevents}-
  klossen. Du bør klikke på `set storleik til 100%`{.blocklooks}-klossen i
  `Utsjånad`{.blocklooks}-kategorien innimellom, slik at Felix får tilbake
  den vanlege storleiken sin.

- [ ] No vil me at Felix skal endre retning slik at han følgjer vegen. Eit
  triks er at me kan gange retninga hans med -1. Då blir det som om han snur
  seg rundt. Sidan me vil gjere dette fire gonger lagar me ein ny
  `gjenta`{.blockcontrol}-kloss:

  ```blocks
  når eg får meldinga [Scene 2 v]
  gå til x: (-20) y: (-100)
  sei [Å! Der er det nokre hus!] i (2) sekund
  peik i retning (20 v)
  gjenta (4) gongar
      gjenta (6) gongar
          gå (9) steg
          neste drakt
          endra storleik med (-2)
          vent (0.1) sekund
      slutt
      peik i retning ((retning) * (-1))
  slutt
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Følgjer Felix vegen oppover mot dei to husa?

Viss du ser litt nærare på vegen ser du at den flatar ut. Dette kan me
etterlikne for Felix ved å gange med eit tal som er litt ulikt -1, slik at
retninga blir justert.

## Sjekkliste {.check}

- [ ] Endre `-1` i `peik i retning`{.blockmotion}-klossen til `-1.5`.

- [ ] For å forstå betre kva som skjer kan du klikke på `i`{.blockmotion}
  på Felix og følgje med på `retning` når skriptet køyrer.

- [ ] Når Felix kjem fram til huset skal me skjule han, og skifte
  til ei ny scene.

  ```blocks
  når eg får meldinga [Scene 2 v]
  gå til x: (-20) y: (-100)
  sei [Å! Der er det nokre hus!] i (2) sekund
  peik i retning (20 v)
  gjenta (4) gongar
      gjenta (6) gongar
          gå (9) steg
          neste drakt
          endra storleik med (-2)
          vent (0.1) sekund
      slutt
      peik i retning ((retning) * (-1.5))
  slutt
  gøym
  vent (1) sekund
  send meldinga [Scene 3 v]
  ```

- [ ] For den scena treng me ein ny bakgrunn. Klikk
  ![vel ein ferdig bakgrunn](../bilder/velg-bakgrunn.png) og legg
  til bakgrunnen `Holiday/gingerbread`. Gi scena dette skriptet:

  ```blocks
  når eg får meldinga [Scene 3 v]
  byt bakgrunn til [gingerbread v]
  ```

- [ ] Når me skiftar til den nye scena vil me òg at Felix skal få tilbake
  den vanlege storleiken sin. Klikk på Felix og start eit nytt skript:

  ```blocks
  når eg får meldinga [Scene 3 v]
  set storleik til (100)%
  gå til x: (-160) y: (-65)
  vis
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Har Felix blitt flinkare til å følgje vegen oppover mot dei to husa?

- [ ] Skiftar bakgrunnen over til huset som den skal?

- [ ] Får Felix riktig storleik att på slutten av animasjonen? Og når
  du startar animasjonen på nytt?

- [ ] Korleis kan dy syte for t Felix alltid dukkar opp i full storleik
  når du klikkar på det grøne flagget?

# Steg 5: Si hei til pingvinane {.activity}

*Felix skal møte to pingvinar som bur inne i peparkakehuset. Dei skal kome ut
av huset og prate litt med Felix.*

## Sjekkliste {.check}

- [ ] Lag to nye figurar ved å trykke på
  ![vel figur frå biblioteket](../bilder/hent-fra-bibliotek.png). Vel
  `Dyr/Penguin1` og `Dyr/Penguin2`. Gi pingvinane namn du likar, me har
  valt å kalle dei `Pingu` og `Pappa Pingu`.

- [ ] For at pingvinane ikkje skal dukke opp før i `Scene 3`, så må me skjule
  dei når animasjonen startar. Legg til følgjande skript på begge figurane:

  ```blocks
  når @greenFlag vert trykt på
  gøym
  ```

- [ ] Fyrst skal Felix spørje om det er nokon heime, og så skal han sende
  ei melding der han ber pingvinane om å kome ut. Endre skriptet til Felix
  ved å leggje til to klossar på slutten:

  ```blocks
  når eg får meldinga [Scene 3 v]
  set storleik til (100)%
  gå til x: (-160) y: (-65)
  vis
  sei [Oi, så flott hus! Er det nokon heime?] i (2) sekund
  send meldinga [Kom ut v]
  ```

- [ ] No skal Pingu kome ut døra og gå litt til sida. Sjekk med
  musepeikaren kva `x`- og `y`-posisjonen til døra er. Legg til
  følgjande skript på Pingu:

  ```blocks
  når eg får meldinga [Kom ut v]
  gå til x: (45) y: (-70)
  vis
  gli (1) sekund til x: (150) y: (-100)
  ```

- [ ] Pappa Pingu kjem ut litt seinare, og stiller Felix eit spørsmål.
  Legg til følgjande skript på Pappa Pingu:

  ```blocks
  når eg får meldinga [Kom ut v]
  vent (2) sekund
  gå til x: (45) y: (-70)
  vis
  vent (1) sekund
  spør [Kva heiter du?] og vent
  send meldinga [Namn1]
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Kjem pingvinane ut av huset som forventa?

- [ ] Kva trur du skjer med namnet du skreiv inn?

# Steg 6: Pingvinane dansar {.activity}

*Pingvinane blir glade for å treffe Felix, og etter ei lita samtale
 startar den eine pingvinen å danse sidan det er Felix sin bursdag.*

## Sjekkliste {.check}

- [ ] Få Pappa Pingu til å sende ei melding etter at han har spurt kva
  Felix heiter. Du kan til dømes kalde meldinga `Namn1`

- [ ] Legg til følgjande skript på Pingu

  ```blocks
  når eg får meldinga [Namn1 v]
  sei (svar) i (2) sekund
  sei [Det er eit rart namn!] i (2) sekund
  send meldinga [Namn2 v]
  ```

- [ ] Legg til følgjande skript på Felix for å få han til å svare og seie at
  han har bursdag:

  ```blocks
  når eg får meldinga [Namn2 v]
  sei [Eg har bursdag i dag!] i (2) sekund
  sei (set saman [Eg blir ] (alder)) i (2) sekund
  send meldinga [Party v]
  ```

Legg merke til `set saman`{.blockoperators}-klossen. Denne kan me
bruke for å setje saman tekst. Pass på at du skriv eit mellomrom
etter ordet `blir`!

- [ ] No skal me få Pingu til å danse! Lag to nye drakter for Pingu ved å
  importere `Dyr/Penguin1` to gonger. Roter dei to nye draktene litt i
  forhold til kvarandre ved å klikke på draktene i teiknevindauget og
  rotere rundt med musa (du må kanskje bytte til vektorgrafikk).

  ![Viser korleis ein roterer pingvinen i Scratch](roter_pingu.png)

- [ ] Legg til en lyd du likar under `Lydar`{.blocklightgrey}, og lag
  følgjande skript på Pingu (me har brukt lyden `human beatbox1`):

  ```blocks
  når eg får meldinga [Party v]
  spel lyden [human beatbox1 v]
  gjenta (20) gongar
      neste drakt
      vent (0.2) sekund
  slutt
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Dansar pingvinen slik du forventa?

- [ ] Kvifor trur du det kan vere lurt å spare på svaret Pappa Pingu får
  i en variabel?

- [ ] Dukkar Pingu opp i riktig drakt når du startar animasjonen på nytt?
  Viss ikkje må du finne ut korleis du kan fikse det!

## Lagre prosjektet {.save}

*No har me starta på historia om katten som feirar bursdagen sin i Antarktis.
Kan du fortelje meir om kva som skjer vidare?*

Om du heller vil vise fram historia di til familie og vener kan du velje
`Legg ut` på toppen av skjermen.

## Utfordring: Historia heldt fram {.challenge}

Kan du fortsetje historia? Kva skjer vidare?

Kanskje du kan introdusere fleire figurar eller fleire bakgrunnar? Til dømes
kan det hende at pingvinane inviterer Felix inn i huset? Eller kanskje dei går
vidare saman for å leite etter ein båt katten kan bruke for å kome seg heim?

Hugs at du kan blande animasjonen saman med eit lite spel, og så gå tilbake
til meir animasjon. Det er heilt opp til deg!
