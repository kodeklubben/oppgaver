---
title: Breakout
level: 4
author: 'Geir Arne Hjelle og Martin Lie'
language: nn
translator: 'Stein Olav Romslo'
---

# Introduksjon {.intro}

Breakout er eit klassisk spel som vart laga av Steve Jobs og Steve Wozniak
(grunnleggjarane av Apple) på 1970-talet. På same måte som i Pong skal ein
kontrollere ein sprettande ball ved hjelp av ein racket. Breakout kan spelast
av ein spelar, og ein får poeng for å skyte boksar ved hjelp av ballen. Nyare
versjonar har vidareutvikla det originale Breakout på fleire måtar. Til dømes
ved at nokre boksar git spesielle bonusar, ved at det er ulike brett med ulike
vanskegradar og så bortetter.

![Illustrasjon av eit ferdig Breakout-spel](breakout.png)

# Oversikt over prosjektet {.activity}

*Du skal gjere mesteparten av kodinga av Breakout sjølv. Koden for racketen og
ballen liknar ein del på den tilsvarande koden i Pong. Derfor kjem me til å
fokusere på boksane i dette prosjektet, og spesielt korleis kloner kan bli
brukt på ein effektiv måte.*

## Plan {.check}

- [ ] Boksar... Mange boksar!

- [ ] Ein sprettande ball og ein enkel racket

- [ ] Boksane forsvinn...

- [ ] Dettande boksar, bonusar, fleire brett og andre utfordringar

# Steg 1: Boksar... Mange boksar! {.activity}

*Ein sentral del av Breakout er alle boksane ein skal prøve å skyte
ned. Sidan alle desse boksane oppfører seg (nesten) likt vil me bruke den
same koden for alle boksane. Til dette brukar me kloning.*

I Scratch kan me klone figurar. Det tyder at me lagar ein kopi av ein figur,
både av utsjånaden og oppførselen. Her kjem me til å lage ein boks, og så
lage mange kopiar av den fyrste.

## Sjekkliste {.check}

- [ ] Start eit nytt prosjekt. Slett kattefiguren.

- [ ] Lag ein boksfigur. Denne kan du teikne sjølv eller bruke `Button3` i
  biblioteket.

- [ ] No vil me klone denne eine boksen mange gonger. For å lage fleire
  rekker med boksar brukar me to løkker. Me treng òg å vite kor mange boksar
  me har, slik at me seinare kan sjekke om me har skote ned alle. Derfor må
  du lage ein variabel `Antal boksar`{.blockdata} som gjeld for alle figurar.
  I denne koden må du kanskje endre dei ulike tala litt, slik at dei passar
  til akkurat din boks.

  ```blocks
  når eg får meldinga [Nytt spel v]
  gøym
  set [Antal boksar v] til [0]
  set y til (160)
  gjenta (5) gongar
      set x til (-200)
      gjenta (11) gongar
          endra [Antal boksar v] med (1)
          lag klon av [meg v]
          endra x med (40)
      slutt
      endra y med (-25)
  slutt
  ```

- [ ] Sjølve oppførselen til kvar enkelt boks kan me kode i eit eige skript
  som startar når klonen blir laga. Sidan me ikkje har ein ball endå, lagar me
  eit enkelt skript der kvar boks (altså alle) blir borte når du trykkar
  mellomrom.

  ```blocks
  når eg startar som klon
  vis
  vent til <tasten [mellomrom v] er trykt?>
  endra [Antal boksar v] med (-1)
  slett denne klonen
  ```

  Etter at me har laga ein ball og ein racket skal me oppdatere denne koden
  slik at boksane forsvinn når dei blir truffe av ballen i staden.

# Steg 2: Ein sprettande ball og ein enkel racket {.activity}

*Når ein lagar nye program og spel er det alltid lurt å lage ein enkel
  versjon av spelet tidleg. Denne tidlege versjonen treng ikkje kunne gjere
  veldig mykje, men du kan starte å teste at programmet blir som du hadde
  tenkt nesten med ein gong.*

Me startar med grunnmekanismen i spelet: ein ball som sprett og ein racket
som kan ta imot ballen.

## Sjekkliste {.check}

- [ ] Lag ein racket-figur. Du kan gjerne teikne ein sjølv, eller bruke
  `Paddle` frå biblioteket.

- [ ] Lag eit skript som startar når det mottek `Nytt spel`. Dette skriptet
  må plassere racketen ein passande stad nederst på skjermen. Så kan det gå
  inn i ei løkke der racketen blir flytta sidelengs når `Pil venstre`- eller
  `Pil høgre`-tastane blir trykka inn.

- [ ] Lag ein ball-figur. Du kan finne ein i biblioteket, eller
  teikne ein sjølv.

- [ ] Me vil ha moglegheita til å endre hastigheita til ballen enkelt seinare.
  Lag ein ny variabel `hastigheit`{.blockdata} som gjeld for ball-figuren.

- [ ] Lag eit skript som startar på `Nytt spel`-meldinga. Fyrst i skriptet
  vil du plassere ballen slik at den kvilar på racketen, og gi den ein
  tilfeldig retning oppover (til dømes mellom -45 og 45 gradar). Så kan ballen
  gå inn i ei løkke som blir gjenteke heilt til `y`-posisjonen til ballen blir
  mindre enn eit passande tal (`-160` er eit bra utgangspunkt, men det vil
  variere avhengig av kor du plasserer racketen og kor stor ballen er). Inne i
  denne løkka vil du flytte ballen `hastigheit`{.blockdata} steg, og la den
  `viss ved kant, sprett`{.blockmotion}.

- [ ] No vil me få til at ballen sprett på racketen. I løkka til racketen kan
  du legge til ein `viss`{.blockcontrol}-test der du sender ei `Sprett
  horisontalt`-melding når ballen kjem borti racketen.

- [ ] Ballen må svare på denne meldinga ved å endre retning. Til dømes med
  kode som ser omtrent slik ut:

  ```blocks
  når eg får meldinga [Sprett horisontalt v]
  peik i retning ((180) - (retning))
  ```

# Steg 3: Boksane forsvinn {.activity}

*No skal me kople saman boksane og ballen. Boksane skal jo forsvinne når dei
  blir truffe av ballen. Samstundes skal ballen sprette når den treff ein boks.*

## Sjekkliste {.check}

- [ ] Me har allereie laga kode som får boksane til å forsvinne. Til no har
  dei blitt borte når me trykkar mellomromtasten. Endre denne koden slik at
  boksane forsvinn når dei er borti ballen.

- [ ] La boksane sende ut ein `Sprett horisontalt`--melding etter at ballen
  har vore borti dei, men før dei (klonane) blir sletta.

Prøv spelet ditt. Grunnmekanismane skal fungere no.

- [ ] For at spelet skal sjå litt finare ut, så kan du legge til ein startmeny.
  Kanskje du kan lage ei stilig framside eller ein intro-animasjon?

- [ ] Legg på passande lydeffekter. Du bør spele av lydar når ballen sprett
  på boksane, men tenk og over om det er andre hendingar det passar å spele
  enkle lydar for.

- [ ] La noko skje når du tapar spelet. Det vil seie når
  `gjenta til`{.blockcontrol}-løkka på ballen er ferdig.

- [ ] Ved hjelp av `Antal boksar`{.blockdata}-variabelen kan du sjekke om
  spelaren har klart å fjerne alle boksane og vinne spelet. Gi spelaren beskjed
  om at ho har vunne!

- [ ] Tenk litt på korleis du har lyst til å utvikle spelet vidare. Korleis
  kan du gjere det endå meir morosamt for deg og venene dine? I neste del
  finn du nokre idear.

# Steg 4: Vidareutvikling av spelet {.activity}

*Du står heilt fritt til å jobbe vidare med spelet ditt slik du vil. Her er
  nokre idear som kan gjere det endå meir morosamt å spele.*

## Idear til vidareutvikling {.check}

- [ ] Legg til ein poengteljar. Du må fyrst bestemme kva spelaren skal få
  poeng for, til dømes når ballen treff ein boks. Så lagar du ein
  `Poeng`{.blockdata}-variabel som du endrar etter kvart.

- [ ] La hastigheita auke etter kvart i spelet.

- [ ] Ein meir morosam og naturleg sprett på racketen kan du få dersom du tek
  omsyn til kor på racketen ballen treff. Det kan du gjere ved å samanlikne
  `x`-posisjonen til ballen og racketen.

- [ ] Viss ballen treff på sida av ein boks burde den sprette på ein vertikal
  (ståande) vegg i staden for ein horisontal (liggjande). For å kode dette
  kan du lage ei ny melding tilsvarande `Sprett horisontalt`. Talet `180` i
  koden må byttast ut. Med kva tal?

- [ ] Kanskje du kan vidareutvikle heile konseptet, slik at det er mogleg å
  plukke opp power-ups etter kvart som ein spelar. Til dømes noko som endrar
  hastigheita på ballen, endrar storleiken på racketen, gir ekstra poeng,
  eller kanskje noko som lagar litt skru på ballen.

- [ ] I staden for at boksane berre forsvinne når ballen treff dei, så kan du
  la dei losne og dette ned. Vidare kan spelaren få ekstra poeng eller bonusar
  for å fange dei dettande boksane med racketen.

- [ ] Bruk ulike fargar på boksane. På denne måten kan du lage brett som ser
  ulike ut. Du kan la dei ulike boksane gi ulik poengsom eller bonusar.

  Ein måte å designe slike brett på kan vere å fyrst lage dei ulike boksane
  som ulike drakter. Så kan du lage ein `brett`{.blockdata}-variabel som listar
  opp kva drakt kvar boks skal bruke. Til dømes kan denne sjå slik ut:

  ```blocks
  set [brett v] til [1111111111111222222211112233322111122222221111111111111]
  ```

  Du kan bruke dette på denne måten når du set ut boksane:

  ```blocks
  byt drakt til (bokstav (antal boksar) i (brett))
  ```

  Vidare i spelet kan du teste på `drakt nr.`{.blocklooks} for å vite kva type
  boks du har med å gjere.
