---
title: Labyrint
level: 1
author: 'Geir Arne Hjelle'
translator: 'Stein Olav Romslo'
language: nn
---

# Introduksjon {.intro}

I dette spelet skal me kontrollere ein liten utforskar medan han leitar etter
skatten gøymt inne i  labyrinten. Diverre er skatten beskytta av den skumle
froskekongen. Me vil lære korleis me kontrollerer figurar og korleis me kan
programmere figurar til å bevege seg sjølv.

![Bilete av labyrinten, froskekongen, utforskaren og skatten](labyrint.png)

# Steg 1: Korleis styre figurar med piltastane {.activity}

*Me startar med å sjå korleis me kan styre figurar med piltastane. For å få til
 dette vil me bruke `Hendingar`{.blockevents}-klossar som merkar når ein trykkar
 på tastaturet.*

## Sjekkliste {.check}

- [ ] Start eit nytt prosjekt.

- [ ] Slett kattefiguren ved å høgreklikke på den og velje `slett`.

- [ ] Legg til ein ny figur. Klikk på
  ![Vel figur frå biblioteket](../bilder/hent-fra-bibliotek.png)-knappen
  og vel ein figur du har lyst til å styre rundt. Me har brukt
  `Dyr/Beetle`-figuren.

- [ ] Gi den nye figuren namnet `Utforskar` ved å klikke på `i`{.blockmotion}.

Me startar med å la figuren bevege seg oppover skjermen når me trykkar på `pil
opp`-tasten.

- [ ] Legg til følgjande skript på `Utforskar`-figuren din.

  ```blocks
  når [pil opp v] vert trykt
  peik i retning (0 v)
  gå (5) steg
  ```

  Prøv å trykkje på `pil opp`-tasten. Beveger utforskaren din seg oppover
  skjermen? No må me lage liknande skript for dei andre tastane.

- [ ] Legg òg til desse skripta, slik at `Utforskar` har totalt fire skript,
  eitt for kvar tast.

  ```blocks
  når [pil ned v] vert trykt
  peik i retning (180 v)
  gå (5) steg

  når [pil høgre v] vert trykt
  peik i retning (90 v)
  gå (5) steg

  når [pil venstre v] vert trykt
  peik i retning (-90 v)
  gå (5) steg
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Beveger utforskaren din seg rundt slik du hadde forventa?

- [ ] Kan du forandre kor raskt utforskaren flyttar seg?

Talet `5` i `gå (5) steg`{.b}-klossane bestemmer kor raskt utforskaren flyttar
seg rundt. Me vil gjerne eksperimentere litt for å sjå kva fart som passar best
i spelet vårt, men for å endre farta må me bytte talet i fire ulike skript. Det
blir for mykje jobb!

## Sjekkliste {.check}

Me vil i staden bruke ein __variabel__ som kan styre farta til
`Utforskar`-figuren.

- [ ] Lag ein ny variabel ved å gå til `Data`{.blockdata}-kategorien og
  klikk `Lag en variabel`.

- [ ] Kall variabelen `hastigheit`, og vel at den berre skal gjelde `For
  denne figuren`.

- [ ] Til slutt må du fjerne avhukinga ved sidan av den nye
- `(hastigheit)`{.b}-klossen for at variabelen ikkje skal visast på scena.

No må me endre i skripta våre slik at dei brukar `(hastigheit)`{.b}-variabelen.

- [ ] Lag fyrst eit nytt skript som set verdien av `(hastigheit)`{.b} til `10`.

  ```blocks
  når @greenFlag vert trykt på
  set [hastigheit v] til [10]
  ```

- [ ] Deretter endrar me dei fire skripta me allereie har laga slik at dei
  brukar `(hastigheit)`{.b}.

  ```blocks
  når [pil opp v] vert trykt
  peik i retning (0 v)
  gå (hastigheit) steg

  når [pil ned v] vert trykt
  peik i retning (180 v)
  gå (hastigheit) steg

  når [pil høgre v] vert trykt
  peik i retning (90 v)
  gå (hastigheit) steg

  når [pil venstre v] vert trykt
  peik i retning (-90 v)
  gå (hastigheit) steg
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Beveger utforskaren din seg framleis rundt slik den gjorde tidlegare?

- [ ] Forandrar hastigheita til utforskaren seg viss du endrar verdien av
  `(hastigheit)`{.b} og klikkar på det grøne flagget att?

- [ ] Vel ei hastigheit du synest passar.


# Steg 2: Me teiknar vår eigen labyrint {.activity}

*No som me kan bevege utforskaren vår rundt omkring på skjermen skal me gi han
 ei utfordring! Me vil teikne ein labyrint som han kan bevege seg rundt inni.*

## Sjekkliste {.check}

- [ ] Vel ![Teikn ny bakgrunn](../bilder/tegn-ny.png) nedst til venstre på
  skjermen for å teikne ein ny bakgrunn. Pass på at du faktisk teiknar ein ny
  __bakgrunn__, og ikkje en ny figur.

- [ ] Gi den nye bakgrunnen namnet `Labyrint`.

- [ ] Vel ei farge du likar og teikn ein liten labyrint. Det er viktig at alle
  veggane i labyrinten har same farge (me oppdagar kvifor snart). Du kan velje
  sjølv korleis labyrinten skal sjå ut, den treng ikkje eingong å ha rette
  veggar!

  ![Bilete av ein enkel liten labyrint](liten-labyrint.png)

  Dette er eit døme på ein liten og enkel labyrint. Du kan sjølv velje korleis
  labyrinten din skal sjå ut! Men ikkje bruk for lang tid på å teikne labyrinten
  no, for me vil jo fortsetje å programmere. I staden kan du kome attende og
  teikne ein meir avansert labyrint etter at du er ferdig med spelet!

## Tips {.protip}

Viss du vil teikne rette veggar er det enklast å bruke linjeverktøyet,
![Linjeverktøy](../bilder/tegn-linje.png). Du kan i tillegg halde inne
`shift`-knappen for at linjene skal bli heilt rette.

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Kan du bevege utforskarfiguren din rundt inne i labyrinten?

- [ ] Dersom figuren din er for stor kan du gjere den mindre ved å trykkje
  på ![krymp](../bilder/krymp.png)-knappen på toppen av skjermen.

- [ ] Kva skjer viss figuren din går på veggen i labyrinten?


# Steg 3: Utforskaren kan ikkje gå gjennom veggen {.activity}

*Sjølv om me har teikna ein flott labyrint bryr ikkje utforskaren seg noko om
 den. Han kan berre gå gjennom veggane. Det skal me gjere noko med no*

## Sjekkliste {.check}

For å oppdage når `Utforskar`-figuren vår går gjennom veggen på labyrinten vil
me bruke ein `<rører fargen [#ffffff]>`{.b}-kloss. Denne klossen merkar om ein
figur kjem borti ei særskilt farge. Her er det viktig at me har teikna alle
veggane i labyrinten i same farge.

- [ ] Me legg `<rører fargen [#ffffff]>`{.b}-klossen inn i skriptet me
  allereie har laga som set `(hastigheit)`{.b}-variabelen.

  ```blocks
  når @greenFlag vert trykt på
  set [hastigheit v] til [10]
  gjenta for alltid
      viss <rører fargen [#cc0000]?>
          snu @turnRight (180) gradar
          gå (hastigheit) steg
          snu @turnRight (180) gradar
      slutt
  slutt
  ```

- [ ] For å få rett farge i `rører fargen [#cc0000]`{.b}-klossen klikkar du
  fyrst på den vesle firkanten der farga visast. Så flyttar du  musepeikaren
  slik at den peikar på ein vegg i labyrinten din. Då blir farga i den vesle
  firkanten forandra. Klikk igjen for å velje denne farga.

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Blir utforskaren stoppa når han prøver å gå gjennom veggen?

- [ ] Forstår du korleis skriptet seier at utforskaren ikkje kan gå gjennom
  veggen?

## Tips {.protip}

Ein måte me kan bruke for å avgrense kor ein figur kan gå, er å tvinge
den til å ta eit skritt tilbake når den gjer noko feil. I koden

```blocks
  snu @turnRight (180) gradar
  gå (hastigheit) steg
  snu @turnRight (180) gradar
```

vil figuren fyrst snu seg heilt rundt (180 gradar), så ta eit skritt, og til
slutt snu seg rundt att slik at den peikar i same retning som då den starta.


# Steg 4: På leiting etter skatten {.activity}

*No kan me bevege oss rundt i labyrinten. Men det blir jo fort keisamt om me
 ikkje har noko å gjere inne i labyrinten. La oss sjå om me kanskje finn ein
 skatt!*

## Sjekkliste {.check}

- [ ] Legg til ein ny figur. Du kan velje ein figur frå biblioteket ved å
  trykkje
  ![Vel figur frå biblioteket](../bilder/hent-fra-bibliotek.png)
  eller teikne ein figur sjølv ved å trykkje
  ![Teikn ny figur](../bilder/tegn-ny.png). Me brukte figuren
  `Ting/Star1`.

- [ ] Gi den nye figuren namnet `Skatt`.

- [ ] Dra skatten rundt inne i labyrinten din, og gøym den ein stad den er
  vanskeleg å kome til.

No skal me lage litt kode som oppdagar når utforskaren finn skatten. Her har me
eit val: me kan lage eit skript på  `Utforskar` som sjekkar om han rører
`Skatt`, eller me kan gjere det omvendt og lage eit skript på `Skatt` som
sjekkar om den rører `Utforskar`.

I dette tilfellet speler det lita rolle kva me vel, men om me tenker oss at me
kanskje vil lage fleire skattar seinare kan det vere litt enklere om me lagar
skriptet på `Skatt`.

- [ ] Pass på at figuren `Skatt` er markert, og skriv følgjande kode:

  ```blocks
  når @greenFlag vert trykt på
  gjenta for alltid
      viss <rører [Utforskar v]?>
          gøym
      slutt
  slutt
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Forsvinn skatten når utforskaren finn fram til den?

- [ ] Kva skjer når du prøver å starte spelet på nytt etter å ha funne skatten?
  Kor har skatten blitt av?

## Sjekkliste {.check}

Det er eit problem i spelet vårt. Etter at utforskaren har funne skatten ein
gong, forblir skatten borte.

- [ ] Me må passe på at skatten visast på starten av spelet. Endre skriptet på
  `Skatt` ved å leggje til `vis`{.b} heilt i starten.

  ```blocks
  når @greenFlag vert trykt på
  vis
  gjenta for alltid
      viss <rører [Utforskar v]?>
          gøym
      slutt
  slutt
  ```

Me har endå eit problem: Når me startar spelet på nytt står utforskaren framleis
der den fann skatten sist. Det blir ikkje veldig spanande.

- [ ] Klikk på `Utforskar`-figuren.

- [ ] Legg til ein `gå til x: () y: ()`{.b}-kloss rett etter `sett
  [hastigheit v] til (10)`{.b}-klossen.

- [ ] For å finne ut kva tal me vil bruke for `x` og `y` kan me gjere følgjande.
  Dra utforskaren til ein stad det er fint å starte frå. Sjå øvst i høgre
  hjørne. Saman med `Utforskar`-figuren står det `x` og `y` og to tal. Dette er
  posisjonen til figuren akkurat no. Skriv desse to tallene inn i `gå til x: ()
  y: ()`{.b}-klossen.

- [ ] Heile skriptet vil no sjå slik ut (dine tall for `x` og `y` vil vere
  noko anna):

  ```blocks
  når @greenFlag vert trykt på
  set [hastigheit v] til [10]
  gå til x: (-200) y: (0)
  gjenta for alltid
      viss <rører fargen [#cc0000]?>
          snu @turnRight (180) gradar
          gå (hastigheit) steg
          snu @turnRight (180) gradar
      slutt
  slutt
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Forsvinn framleis skatten når utforskaren finn fram til den?

- [ ] Virkar spelet slik det skal når du startar det på nytt etter å ha funne
  skatten?


# Steg 5: Froskekongen voktar i gangene {.activity}

*No skal me gjere spelet vanskelegare. Froskekongen vandrar rundt i
 labyrinten og passar på skatten.*

## Sjekkliste {.check}

- [ ] Legg til ein ny figur. Me brukte `Dyr/Frog`. Gi den namnet
  `Froskekonge`.

- [ ] Plasser den nye figuren ein stad i labyrinten. Gjer den mindre eller
  større om nødvendig.

Me startar med å la `Froskekonge` merke at den fangar utforskaren. Dette blir
veldig likt korleis `Skatt` merka at den vart funne.

- [ ] Legg til følgjande kode:

  ```blocks
  når @greenFlag vert trykt på
  gjenta for alltid
      viss <rører [Utforskar v]?>
          sei [Tok deg!] i (1) sekund
          stopp [alle v] :: control
      slutt
  slutt
  ```

Linja `stopp [alle v] :: control`{.b} gjer at skriptet på `Skatt` sluttar å
køyre. Det tyder at me ikkje kan få tak i skatten etter at me har blitt tatt av
`Froskekonge`.

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Kva skjer viss utforskaren kjem borti froskekongen?

- [ ] Kva skjer når du finn skatten etter å ha blitt tatt av froskekongen?

## Sjekkliste {.check}

Til slutt skal me få froskekongen til å bevege seg rundt i labyrinten.

- [ ] Start eit nytt skript på `Froskekonge`-figuren. Igjen kan du bytte ut tala
  for `x` og `y` med noko som passar for labyrinten din.

  ```blocks
  når @greenFlag vert trykt på
  gå til x: (50) y: (100)
  peik i retning (-90 v)
  ```

- [ ] Før me lar `Froskekonge` begynne å bevege seg lagar me ein
  `(hastigheit)`{.b}-variabel for han òg. Klikk på `Data`{.blockdata}, og så
  `Lag en variabel`. Kall variabelen `hastigheit` og la den gjelde kun `For
  denne figuren`. Til slutt fjernar du avhukinga på variabelen.

- [ ] No kan me utvide skriptet slik at froskekongen går fram og tilbake. Me får
  han til å snu når han treffer veggen på nesten same måte som me hindrar
  utforskaren i å gå gjennom veggen.

  ```blocks
  når @greenFlag vert trykt på
  gå til x: (50) y: (100)
  peik i retning (-90 v)
  set [hastigheit v] til [5]
  gjenta for alltid
      gå (hastigheit) steg
      viss <rører fargen [#cc0000]?>
          snu @turnRight (180) gradar
          gå (hastigheit) steg
      slutt
  slutt
  ```

Heilt til slutt kan me gjere det endå vanskelegare ved å la froskekongen endre
retning av og til.

- [ ] Legg til kode som let `Froskekonge` snu seg tilfeldig rundt i labyrinten:

  ```blocks
  når @greenFlag vert trykt på
  gå til x: (50) y: (100)
  peik i retning (-90 v)
  set [hastigheit v] til [5]
  gjenta for alltid
      gå (hastigheit) steg
      viss <rører fargen [#cc0000]?>
          snu @turnRight (180) gradar
          gå (hastigheit) steg
      slutt
      viss <(tilfeldig tal frå (1) til (25)) = [1]>
          snu @turnRight ((tilfeldig tal frå (-1) til (1)) * (90)) gradar
      slutt
  slutt
  ```

Dei to siste klossane ser litt kompliserte ut. La oss sjå nærare på dei.

- [ ] Klossen `viss <(tilfeldig tal frå (1) til (25)) = [1]>`{.b} seier at me
  skal gjere *noko* om lag ein av 25 gonger.

- [ ] Dette *noko* er `snu @turnRight ((tilfeldig tal frå (-1) til (1)) * (90))
  gradar`{.b}. Teiknet `*` tyder gange, slik at om me vel tilfeldig mellom tala
  `-1`, `0` og `1`, tyder det at froskekongen vil vende `-90`, `0` eller `90`
  gradar. Det vil seie at han svingar mot venstre, fortset rett fram eller
  svingar mot høgre.

## Tips {.protip}

Du kan av og til oppleve at `Froskekonge` set seg fast i veggen. Det er fordi
`Froskekonge` framleis rører labyrintveggen etter at han har snudd seg. Eit par
ting du kan prøve for å forbetre dette er å gjere `Froskekonge`-figuren mindre,
leggje ein `bruk roteringstypen [ikkj roter v]`{.b}-kloss øvst i
`Froskekonge`-skriptet, eller velje ein figur som er _rundare_ (prøv òg å viske
bort tunga til `Froskekonge` viss du brukar `Dyr/Frog`-figuren).

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Klarar du å få tak i skatten?

- [ ] Om du synest spelet er for lett eller vanskeleg er det mange måtar du kan
  endre det på! Prøv å lage froskekongen større eller mindre. Prøv å endre
  hastigheita på både utforskaren og froskekongen. Om du endrar talet `25` i det
  siste skriptet me laga for `Froskekonge` vil han endre retning oftare eller
  sjeldnare.

- [ ] Du kan prøve å lage fleire skattar. Prøv å høgreklikke på
  `Skatt`-figuren og vel `Lag ein kopi`.

## Lagre prosjektet {.save}

*Då var me ferdige med labyrint-spelet!*

No kan du gå på skattejakt! Viss du vil kan du dele spelet med familie og venner
ved å trykkje `Legg ut`.
