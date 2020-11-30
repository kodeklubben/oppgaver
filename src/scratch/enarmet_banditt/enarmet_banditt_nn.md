---
title: 'Einarma banditt'
level: 2
author: 'Omsett frå [Code Club UK](//codeclub.org.uk)'
translator: 'Stein Olav Romslo'
language: nn
---


# Introduksjon {.intro}

Dette spelet brukar tre figurar som endrar utsjånad. Du skal gjere slik at
figurane stoppar ein etter ein, og målet er at alle skal vere like.

![Bilete av to dinosaurar og ein banan](enarmet_banditt.png)

# Steg 1: Lag ein figur som byttar drakt {.activity}

*Fyrst må me importere dei bileta me treng i spelet.*

## Sjekkliste {.check}

- [ ] Start eit nytt Scratch-prosjekt. __Slett katten__ ved å høgreklikke og
  velje `slett`.

- [ ] Importer __ein ny figur__,
  ![Vel figur frå biblioteket](../bilder/hent-fra-bibliotek.png). Vel den
  figuren du vil.

- [ ] Gå til `Drakter`{.blocklightgrey}, og importer to ekstra drakter frå
  biblioteket, slik at figuren har tre drakter til saman. Det er bra om draktene
  er så ulike at du raskt ser skilnaden på dei.


# Steg 2: Få figuren til å bytte drakter {.activity}

*No som me har gitt figuren drakter, så vil me at den skal rullere mellom dei.*

## Sjekkliste {.check}

- [ ] Klikk på `Skript`-fana,

- [ ] Legg til dette skriptet:

  ```blocks
  når @greenFlag vert trykt på
  gjenta for alltid
      neste drakt
      vent (0.5) sekund
  slutt
  ```

- [ ] Tilpass tida i `vent`{.blockcontrol}-klossen til figuren endrar drakt i
  eit passande tempo. Kva trur du ville skjedd dersom me ikkje hadde hatt med
  `vent`{.blockcontrol}-klossen?

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Endrar figuren drakt i eit fornuftig tempo?

## Ting å prøve {.challenge}

Tilpass tida i `vent`{.blockcontrol}-klossen. Kva tal gjer spelet for vanskeleg
eller for lett?

# Steg 3: Frys rulletten! {.activity}

*Me vil at draktene skal stoppe å rullere når me klikkar på figuren.*

Bra jobba så langt. Me kan få draktene til å bytte i det uendelege, men korleis
får me dei til å stoppe når me klikkar på dei? Ein måte å gjere det på er å
bruke ein variabel som set statusen til figuren. Seinare vil me sjå at det kan
vere ei praktisk løysing.

## Sjekkliste {.check}

- [ ] Klikk på `Data`{.blockdata} og `Lag ein variabel`. Kall variabelen
  `stoppa`{.blockdata} og vel at den skal gjelde for `For denne figuren`. Fjern
  avhukinga framfor variabelen slik at den ikkje er synleg på scena.

- [ ] På starten av spelet er ikkje figuren klikka på, så då set me variabelen
  til `0`.

  ```blocks
  når @greenFlag vert trykt på
  set [stoppa v] til [0]
  gjenta for alltid
      neste drakt
      vent (0.5) sekund
  slutt
  ```

- [ ] No vil me at verdien til variabelen `stoppa`{.blockdata} blir endra til
  `1` når nokon klikkar på figuren.

  ```blocks
  når denne figuren vert trykt på
  set [stoppa v] til [1]
  ```

- [ ] Til slutt må me få figuren til å slutte å forandre drakt når variabelen
  `stoppa`{.blockdata} blir `1`. Legg til ei `viss`{.blockcontrol}-løkke og
  bruk ein `_ = _`{.blockoperators}-operator-kloss for å sjekke om
  `stoppa`{.blockdata} framleis er `0`.

  ```blocks
  når @greenFlag vert trykt på
  set [stoppa v] til [0]
  gjenta for alltid
      viss <(stoppa) = [0]>
          neste drakt
          vent (0.5) sekund
      slutt
  slutt
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Endrer draktene seg før du klikkar på figuren?

- [ ] Stoppar rulleringa av drakter når du klikkar på figuren?

__Start skriptet ein gong til ved å klikke på det grøne flagget att.__

- [ ] Stoppar rulleringa når du heldt musepeikaren over den utan å klikke?

- [ ] Stopper rulleringa når du klikkar andre stader på scena eller andre stader
  i Scratch?


# Steg 4: Lag dei andre figurane {.activity}

*Me treng to figurar til for å fullføre spelet.*

## Sjekkliste {.check}

- [ ] __Kopier figuren din__ ved å høgreklikke på den og velje `lag en kopi`.

- [ ] Lag ein kopi til slik at du har tre figurar på skjermen. Du kan til dømes
  gi figurane namna `Figur1`, `Figur2` og `Figur3`.

- [ ] Flytt figurane slik at dei er på lijnje. Du kan gjere dei mindre med
  krympeknappen ![Krympeknappen](../bilder/krymp.png) viss du treng det.

## Test prosjektet{.flag}

__Klikk på det grøne flagget.__

- [ ] No skal alle figurane endre på seg. Prøv å stoppe dei ein etter ein!


# Steg 5: Start kvar figur med ei tilfeldig drakt {.activity}

*Få figurane til å skifte til ei tilfeldig drakt når du klikkar på det grøne
flagget.*

Når du startar spelet ser du at alle figurane skiftar drakt samstundes. Spelet
blir meir morosamt (og vanskelegare) viss dei endrar drakt meir tilfeldig.

## Sjekkliste {.check}

- [ ] Under `Drakter`{.blocklightgrey}-fana til ein figur ser du at kvar drakt
  har eit nummer. Du kan spesifisere kva drakt figuren skal ha ved å bruke
  namnet eller nummeret til drakta.

- [ ] For å få figuren til å starte med ei tilfeldig drakt legg me til ein
  `byt drakt til`{.blocklooks}-kloss med `tilfeldig tal frå 1 til
  3`{.blockoperators}. Den vel eit tilfeldig draktnummer.

- [ ] Me kan bruke den same klossen i `gjenta for alltid`{.blockcontrol}-løkka
  slik at figuren byttar til ei tilfeldig drakt kvar gong.

  ```blocks
  når @greenFlag vert trykt på
  set [stoppa v] til [0]
  byt drakt til (tilfeldig tal frå (1) til (3))
  gjenta for alltid
      viss <(stoppa) = [0]>
          byt drakt til (tilfeldig tal frå (1) til (3))
          vent (0.5) sekund
      slutt
  slutt
  ```

- [ ] Gjer det same for kvar av dei andre figurane.

## Test prosjektet{.flag}

__Klikk på det grøne flagget.__

- [ ] Alle figurane skal skifte drakter i tilfeldig rekkefølgje.

- [ ] Korleis må me forandre skriptet viss me legg til ei ny drakt?

## Ting å prøve {.challenge}

 __Gjer spelet vanskelegare!__

Prøv å endre vanskegraden på eitt eller anna vis. Det er enkelt å få draktene
til å rullere raskare, så prøv om du kan vere meir kreativ. Nokre moglegheiter
er:

- [ ] Endre kor mange drakter kvar figur har.

- [ ] Gi nokre av figurane heilt ulike drakter.

- [ ] Bruk ulik tid mellom kvart draktbytte.

__Leik og kom opp med eigne idear!__

Kvar gong du endrar noko bør du tenke over om det vil gjere spelet vanskelegare
eller lettare. Er det for lett eller for vanskeleg? Korleis kan du justere det
slik at det blir akkurat passe?


# Steg 6: Vis ei melding når spelet er over {.activity}

*Me skal lage ei `Spelet er slutt`-melding når spelet er over.*

## Sjekkliste {.check}

Fyrst hentar me inn ein ny bakgrunn som skal visast når spelet er over.

- [ ] Klikk på scena og så `Bakgrunner`{.blocklightgrey}-fana. Endre namnet på
  den gjeldande bakgrunnen til `Spel`.

- [ ] Lag ein kopi av bakgrunnen og legg til ein tekst som seier `Spelet er
  slutt!`. Du kan endre storleiken på teksten ved å klikke på den og dra i
  hjørna. Kall bakgrunnnen `Slutt`.

- [ ] Klikk på `Skript`-fana for scena og pass på at du byttar til
  `Spel`-bakgrunnen når spelet startar.

- [ ] Korleis sjekkar me om alle figurane har stoppa? Hugs at me brukte
  `stoppa`{.blockdata}-variablane for å sjekke om figurane var blitt klikka på.
  La oss sjekke `stoppa`{.blockdata}-variabelen for `Figur3` for å sjå om den
  har blitt klikka på. For å gjere det brukar me ein `x-posisjon av
  Figur3`{.blocksensing}-kloss frå `Sansing`{.blocksensing}, men me byttar ut
  `x-posisjon` med `stoppa`.

  ```blocks
  når @greenFlag vert trykt på
  byt bakgrunn til [Spel v]
  vent til <([stoppa v] av [Figur3 v])  = [1]>
  byt bakgrunn til [Slutt v]
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Blir `Spelet er slutt`-meldinga vist når du klikkar på `Figur3`?

- [ ] Kva skjer viss du stoppar `Figur3` før du har klikka på begge dei andre
  figurane?

Me må forandre skriptet litt slik at det fungerer uansett kva rekkefølgje me
stoppar figurane i.

## Sjekkliste {.check}

- [ ] For å sjekke om __alle tre__ figurane sine `stoppa`{.blockdata}-variablar
  er `1` kan me bruke `og`{.blockoperators}-operatoren. Dette er ein kloss som
  kan vere litt trøblete å lage, så gjer eitt og eitt steg. Legg merke til at me
  set saman to `og`{.blockoperators}-klossar, tre
  `_ =_`{.blockoperators}-operatorar og tre
  `stoppa av Figur`{.blocksensing}-klossar.

  ```blocks
  når @greenFlag vert trykt på
  byt bakgrunn til [Spel v]
  vent til < < <([stoppa v] av [Figur1 v]) = [1]> og <([stoppa v] av [Figur2 v]) = [1]> > og <([stoppa v] av [Figur3 v]) = [1]> >
  byt bakgrunn til [Slutt v]
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Blir `Spelet er slutt`-meldinga vist når alle tre figurane er stoppa,
  uavhengign av kva rekkefølgje du klikka på dei i?


# Steg 7. Fortel spelaren om ho vann eller tapte. {.activity}

*Målet med spelet er å klikke på figurane slik at dei stoppar når dei viser same
drakt. Det er fint om du kan vise ei melding som viser spelaren om ho vann
eller tapte.*

## Sjekkliste {.check}

Tidlegare skreiv me kode som sjekkar om spelet er over, så me må berre sjekke om
spelaren vann.

- [ ] Gå tilbake til bakgrunnane og lag ein kopi av `Slutt`-bakgrunnen. Skift
  namn på `Slutt` til `Vinnar`. Gi kopien namnet `Tapar`.

- [ ] Legg til teksten `Du vann!` på `Vinnar`-bakgrunnen.

- [ ] Legg til teksten `Du tapte!` på `Tapar`-bakgrunnen.

No treng me kode for å velje kva bakgrunn me skal vise når spelet er slutt.

- [ ] Me kan bruke ein `viss ellers`{.blockcontrol}-kloss for å sjekke om
  brukaren har vunne eller tapt ved å samanlikne `drakt nr.` (drakt nummer). Me
  brukar ein kloss som liknar på `x-posisjon av Figur`{.blocksensing}-klossen me
  brukte tidlegare. Denne gongen skal me sjekke `drakt nr.` og sjå om `Figur1`
  har same drakt som `Figur2` og om `Figur2` har same drakt som `Figur3`.

  ```blocks
  når @greenFlag vert trykt på
  byt bakgrunn til [Spel v]
  vent til < < <([stoppa v] av [Figur1 v]) = [1]> og <([stoppa v] av [Figur2 v]) = [1]> > og <([stoppa v] av [Figur3 v]) = [1]> >
  viss <<([drakt nr. v]  av [Figur1 v]) = ([drakt nr. v]  av [Figur2 v])> og <([drakt nr. v]  av [Figur2 v]) = ([drakt nr. v] av [Figur3 v])>>
      byt bakgrunn til [Vinnar v]
  elles
      byt bakgrunn til [Tapar v]
  slutt
  ```

## Test prosjektet{.flag}

__Klikk på det grøne flagget.__

- [ ] Blir den riktige meldinga vist når spelet er over?

- [ ] Kva skjer viss draktnumra ikkje er like?

__Veldig bra!__ No har du fullført spelet, men det er framleis ting du kan
gjere. Prøv deg på desse utfordringane.

## Utfordring: Gjer spelet enklare og vanskelegare med tida {.challenge}

Det er ikkje alle som er like flinke til å spele. Korleis kan du la vanskegraden
__avhenge av spelaren__?

Ein måte å gjere det på er å __endre hastigheita draktane blir endra med__. Du
kan bruke ein variabel du kallar `forseinking`{.blockdata} for å gi ei ventetid
til kvar figur. Viss spelaren vinn kan forseinkinga bli redusert litt (slik at
spelet går raskare og blir vanskelegare), og viss spelaren tapar runden kan
forseinkinga auke for å gjere spelet lettare.

Du må vurdere om du kan lage ein annan måte å starte spelet på enn med `når
@greenFlag blir trykt på`{.blockgrey}. Så kan du lagre verdiane i variablar som blir
hugsa mellom rundene.

## Lagre prosjektet {.save}

__Godt gjort, du er ferdig! No kan du nyte spelet ditt!__

Ikkje gløym du du kan dele spelet med venene og familien din ved å klikke på
`Legg ut` i toppmenyen!
