---
title: Snake
level: 4
author: 'Geir Arne Hjelle og Martin Lie'
translator: 'Stein Olav Romslo'
language: nn
---


# Introduksjon {.intro}

Sidan slutten av 1970-talet har nesten alle personlege datamaskiner hatt ein
eller annan variant av Snake. Spelet vart ekstra populært då det dukka opp på
Nokia sine mobiltelefonar i 997. Dei siste åra har spelet til og med blitt tatt
med i New York Museum of Modern Art si samling.

Sjølve spelet går enkelt og greitt ut på å styre ein slange rundt på skjermen,
og passe på at slangen ikkje krasjar i kanten av skjermen eller seg sjølv.
Slangen veks når den et eple som dukkar opp tilfeldige stader på skjermen. Snake
kan vidareutviklast på mange måtar, til dømes ved å lage ekstra hindringar på
skjermen, ha ulike typer bonuseple, eller at to slanger konkurrerer om å ete
epla og om å stenge kvarandre inne.

![Illustrasjon av eit ferdig Snake-spel](snake.png)


# Oversikt over prosjektet {.activity}

*Du skal gjere mesteparten av kodinga av Snake sjølv. I Snake brukar me kloner
 på ein litt spesiell og ganske smart måte. Difor starar me med å jobbe med
 kloning.*

## Plan {.check}

- [ ] Slangen flyttar på seg... Eller?

- [ ] Styr slangen til den krasjar!

- [ ] Epler og anna snadder.

- [ ] Veggar, bonuseple, fleire slangar og andre utfordringar.


# Steg 1: Slangen flyttar på seg... eller? {.activity}

*I prinsippet er Snake eit enkelt spel å lage. Ei av dei største utfordringane
 er korleis slangen skal flyttast rundt. Fyrst virkar det kanskje som ein treng
 ei eller anna slags liste som hugsar kor kvar del av slangen er slik at ein kan
 flytte den.*

I staden for å bruke lister skal me bruke kloning på ein spesiell måte. Hugs at
når me kloner kopierer me både utsjånaden og oppførselen til ein figur. Me vil
starte med ein enkel boks som skal vere ein del av kroppen til slangen. Denne
boksen skal me flytte, klone, flytte, klone og så bortetter. Trikset for at det
skal sjå ut som om slangen flyttar på seg er at dei gamle klonene slettar seg
sjølv etter litt tid.

I figuren er den blå boksen hovudet til slangen, dei grøne boksane er kroppen
til slangen, og dei kvite viser kor slangen har vore (dei kvite er eigentleg
sletta kloner av boksane).

![Bilete av slangen og kor den har vore](teller.png)

For å vite når me skal slette kloner treng me tre variablar:
`lengde`{.blockdata} er lengda på slangen, `teljar`{.blockdata} er ein enkel
teljar som passar på kor mange steg slangen har gått sidan spelet stara, og til
slutt er `min id`{.blockdata} eit tal som fortel kor i rekkja ein gitt klone er.
I figuren over er `min id`{.blockdata} skrive i kvar bokse, `teljar`{.blockdata}
er 16 siden slangen har gått 16 steg, og `lengde`{.blockdata} er 6.

Trikset me skal bruke er ganske enkelt. Kvar klone slettar seg sjølv viss `min
id`{.blockdata} er mindre enn `teljar`{.blockdata} - `lengde`{.blockdata}. La
oss prøve det i praksis.

## Sjekkliste {.check}

- [ ] Start eit nytt prosjekt. Slett kattefiguren.

- [ ] Teikn ein boksfigur sjølv. Du bør lage den ganske liten slik at du får
  plass til ein lang slange på skjermen. Pass på at boksen blir like brei som
  den er høg. Ein stad mellom `10 x 10` og `20 x 20` passar bra.

  ![Bilete av ein boks i Scratch](boks.png)

- [ ] Lag dei tre variablane: `lengde`{.blockdata} og `teljar`{.blockdata}
  skal gjelde for alle figurar, medan `min id`{.blockdata} må gjelde kun for
  denne figuren, sidan den skal være unik for kvar klone.

- [ ] No skal me lage hovudløkka i spelet. Fyrst set me dei nødvendige
  variablane, så brukar me ei løkke til å lage stadig nye slangeboksar.

  ```blocks
  når eg får meldinga [Nytt spel v]
  set [teljar v] til [0]
  set [lengde v] til [5]
  gjenta til <rører [kant v]>
      set [min id v] til (teljar)
      endra [teljar v] med (1)
      vent (0.1) sekund
      lag klon av [meg v]
      gå (10) steg
  slutt
  ```

  Pass på at du endrar `10`-talet i `gå 10 steg`{.blockmotion}-klossen til det
  same som storleiken på boksen du laga.

- [ ] Sjølve kloneboksane treng berre å vente til dei skal slette seg sjølv. Det
  er ganske enkelt.

  ```blocks
  når eg startar som klon
  vent til <((teljar) - (lengde)) > (min id)>
  slett denne klonen
  ```

  Samanlikn skripta med figuren og forklaringa over. Forstår du korleis dei
  fungerer?

- [ ] Prøv spelet ditt. Det kan vere greitt å lage eit skript på scena som
  sender ut meldinga `Nytt spel` når du klikkar det grøne flagget. Du skal sjå
  ein slange som beveger seg over skjermen, men du kan ikkje styre den endå!


# Steg 2: Styr slangen til den krasjar! {.activity}

*No skal me kontrollere slangen med piltastane.*

Det er lett å bruke piltastane til å kontrollere slangen. Sidan den går av seg
sjølv må me berre endre retninga når piltastane blir trykka på.

## Sjekkliste {.check}

- [ ] Lag eit nytt skript som òg startar på `Nytt spel`-meldinga. Lag ei `for
  alltid`{.blockcontrol}-løkke der du testar om kvar piltast er trykka, og
  endrar kva retning figuren peikar tilsvarande.

- [ ] Legg til ein `gå til x: y:`{.blockmotion}- og ein `peik i
  retning`{.blockmotion}-kloss fyrst i skriptet ditt slik at slangen startar ein
  fornuftig stad i starten av spelet.

- [ ] Du kan markere hovudet til slangen ved å lage ei ekstra drakt. Lag til
  dømes ein kopi av boksen du allereie har teikna, og endre fargen på den. Kall
  ei av draktene `hovud` og den andre `kropp`. Då kan du bruke `hovud`-drakta i
  hovudløkka når klonen blir generert. I skriptet for kvar klon endrar du drakta
  til `kropp` før `vente`{.blockcontrol}-klossen.

- [ ] Legg inn ein sjekk på om slangen krasjar i seg sjølv. Det kan du til dømes
  gjere ved å utvide testen i `gjenta til`{.blockcontrol}-klossen med
  `elles`{.blockoperators} og `rører fargen`{.blocksensing}.

- [ ] Prøv spelet ditt. No skal du kunne styre slangen din rundt på skjermen
  heilt til du krasjar i kanten eller i deg sjølv.


# Steg 3: Eple og anna snadder {.activity}

*No skal me gi slangen mål og meining. Ved å ete eple kan slangen vekse seg stor
 og sterk!*

Epla er ganske enkle å lage, sidan me berre treng ein figur som blir borte når
slangen et dei. For å enklare kunne utvide med fleire eple og slikt seinare
brukar me kloner av epla òg.

## Sjekkliste {.check}

- [ ] Lag ein ny eplefigur. Den bør vere omlag like stor som slangeklossane. Til
  dømes kan du bruke ein raud disk (fylt sirkel) som er `10 x 10` pikslar.

- [ ] Lag eit skript som startar på ei ny melding `Lag eple`. Dette skriptet
  skal flytte eplet til ein tilfeldig stad på skjermen, og så lage ein klon. Men
  me vil vere nøye med at eplet havnar i same "rutenett" som slangen. Til dømes,
  viss slangeboksane dine er `10 x 10` kan du bruke noko som dette:

  ```blocks
  gå til x: ((10) * (tilfeldig tal frå (-23) til (23))) y: ((10) * (tilfeldig tal frå (-16) til (16)))
  ```

  Hugs at skjermen har koordinatar frå `-240` til `240` i `x`-retning, og `-180`
  til `180` i `y`-retning. Pass på at epla dine landar godt innanfor skjermen
  slik at slangen kan ete dei.

- [ ] No treng me eit skript som sender ut `Lag eple`-meldingar. Lag eit skript
  som startar når det mottek `Nytt spel`. Dette skriptet skal
  `skjule`{.blocklooks} eplet og så sende ei `Lag eple`-melding.

- [ ] Til slutt lagar me oppførselen for eit kloneeple. Lag eit nytt skript som
  startar med `når eg startar som klon`{.blockcontrol}. Dette skriptet må
  `vise`{.blocklooks} eplet, `vente til`{.blockcontrol} det `rører
  slangen`{.blocksensing}, auke `lengde`{.blockdata} på slangen, så
  `sende`{.blockevents} ei `Lag eple`-melding og til slutt `slette denne
  klonen`{.blockcontrol}.

- [ ] Legg på nokre enkle lydeffektar! Til dømes passar lyden `chomp` ganske bra
  når eit eple blir ete. Kva lyd passar når slangen krasjar?


# Steg 4: Vidareutvikling av spelet {.activity}

*Du står heilt fritt til korleis du vil jobbe vidare med spelet ditt. Her er
 nokre idear som kan gjere spelet endå meir morosamt.*

## Idear til vidareutvikling {.check}

- [ ] Legg til ein poeng-teljar. Det enklaste er å berre bruke
  `lengde`{.blockdata} som poeng. Vis denne variabelen på skjermen. Høgreklikk
  på den og vel `stor`.

- [ ] La hastigheita auke etter kvart i spelet. Vanlegvis gjer me det ved å
  endre kor mange steg ein figur går. Det kan me ikkje gjere her sidan kvar boks
  i slangekroppen må henge saman. I staden kan du endre kor lang ventetid som er
  før det lagast ein ny boks på kroppen.

- [ ] Kanskje kan du vidareutvikle heile konseptet og bruke bonuseple? Til dømes
  kan det vere eple som aukar lengda på slangen med meir enn 1, eple som lagar
  fleire eple, ekstra store eple, eller noko heilt anna.

- [ ] Det må ikkje vere berre eitt eple om gongen. Til dømes kan du starte med
  tre eple i starten av spelet. Då blir det mindre leiting etter kvart eple, som
  kan gjere spelet meir morosamt. Du kan gjere det ved hjelp av kloning. Berre
  pass på at du ikkje får kvar klone til å lage tre nye eple, då blir skjermen
  heilt full veldig snart!

- [ ] La epla flytte seg viss det går ei viss tid utan at dei blir etne. For å
  halde styr på tida kan du bruke `tid`{.blocksensing}-klossen i
  `Sansing`{.blocksensing}-kategorien.

- [ ] I staden for at slangen berre kan krasje i seg sjølve eller i kanten, så
  kan du lage hindringar på sjølve brettet. Desse kan du til dømes teikne på
  bakgrunnen i ei spesiell farge, og så undersøke om slangen `rører
  fargen`{.blocksensing}. Du kan til og med ha fleire brett med dører mellom.

- [ ] Kva med å lage ein versjon for to spelarar? Spelarane styrer kvar sin
  slange, og konkurrerer både om å ete epla og om å sperre kvarandre inne.

- [ ] Spelet ditt fortener ei framside og ein meny som kan starte spelet. Her
  kan du la spelaren velje vanskegrad ved å justere på lengde, hastigheit,
  hinder på banen og så bortetter.
