---
title: "PXT: Hermegåsa"
author: Felix Bjerke, Tjerand Silde og Susanne Rynning Seip
translator: Stein Olav Romslo
language: nn
---


# Introduksjon {.intro}

Hermegåsa er eit spel der ein person er *spelleiar*. Spelet går ut på at
spelleiaren skal utføre instruksjonar på micro:biten sin som dei andre spelarane
skal gjenta (herme etter) på micro:biten sin. Det er eit spel for fleire
spelarar, og det er om å gjere å vere den raskaste spelaren til å herme etter
spelleiaren. Spelleiaren har oversikt over poenga til dei ulike spelarane på
skjermen sin, og spelet blir avslutta når ein spelar har vunne 5 gonger.

![Bilete av tre micro:bitar som speler Hermegåsa](hermegaasa.png)

På biletet ser du at spelleiaren er i midten og har poengsummen til spelar 1 og
spelar 2 på skjermen sin. På sidene har spelarane fått beskjed om kva dei skal
gjere, i form av ei pil på skjermen. Fyrstemann som vippar micro:biten sin same
veg som pila vinn.


# Steg 1: Sjekk at du har riktig utstyr {.activity}

*Det er viktig at du har alt utstyret og tilbehøret for å kunne gjere denne
oppgåva.*

## Sjekkliste {.check}

  - [ ] 1 micro:bit med ein micro-usb-kabel som spelleiar.

  - [ ] 2-5 micro:bitar med strømforsyning (micro-usb-kablar eller batteri).

  - [ ] Ei datamaskin med Internett.

### Spelereglar {.protip}

*Her er eit oversyn over reglane i spelet:*

| Skjerm viser | Spelar utfører   |
| ------------ | ---------------- |
| A            | Trykk på A       |
| B            | Trykk på B       |
| C            | Trykk på A + B   |
| <            | Vipp til venstre |
| \>           | Vipp til høgre   |


# Steg 2: Programmere spelleiaren {.activity}

*Når spelet skal starte må me syte for at alle micro:bitane kan kommunisere med
kvarandre. For å få til det må me bestemme eit gruppe-nummer som alle
deltakarane brukar for å sende informasjon over bluetooth. I tillegg må me lagre
at me har sendt ut ei melding til deltakarane, slik at me ikkje sender ut fleire
meldingar før me har fått svar på den førre.*

## Sjekkliste {.check}

- [ ] Start eit nytt PXT-prosjekt, til dømes ved å gå til
  [makecode.microbit.org](https://makecode.microbit.org/?lang=no){target=_blank}.

- [ ] Finn klossen `ved start`{.microbitbasic} under `Basis`{.microbitbasic} og dra den inn i kodefeltet.

- [ ] Gå til `Radio`{.microbitradio} og finn klossen `radio sett gruppe`{.microbitradio}. I utgangspunktet står
  talet `1` i denne klossen, men du bestemmer sjølv kva tal du vil bruke.

- [ ] Til slutt går me til `Variabler`{.microbitvariables} og veljer klossen `sett variabel til`{.microbitvariables}.
  Denne kan du bytte namn på ved å klikke på _variabel_ og så på _Rename
  variable_. Den bør heite `MessageSent`{.microbitvariables}.

- [ ] Til `MessageSent`{.microbitvariables} koplar me klossen `usann`{.microbitlogic}, som du finn under `Logikk`{.microbitlogic}.

- [ ] Når spelet startar skal alle spelarane ha `0` poeng. Lag ein variabel for
  kvar spelar med namn `Player1`{.microbitvariables}, `Player2`{.microbitvariables} osb. som du set til `0` poeng.

- [ ] Viss du har gjort alt rett vil koden din sjå slik ut:

```microbit
  radio.setGroup(37)
  let Player5 = 0
  let Player4 = 0
  let Player3 = 0
  let Player2 = 0
  let Player1 = 0
  let MessageSent = false
```

### OBS! {.protip}

Hugs at gruppenummeret du har valt må brukast alle stader i spelet der du skal
bestemme gruppenumer. I denne oppgåva har me valt talet `37`.

I oppgåva antek me at me har fem spelarar. Viss de kjem til å vere færre
spelarar enn det, så treng du ikkje leggje til så mange.


# Steg 2: Vise poeng på skjermen {.activity}

*For å halde oversyn over kor mange poeng dei ulike spelarane har, så viser me
det på skjermen til spelleiaren. Viss nokon av spelarane får 5 poeng, så gir me
beskjed om at den spelaren vann.*

## Sjekkliste {.check}

- [ ] Fyrst legg me til `gjenta for alltid`{.microbitbasic}-klossen frå `Basis`{.microbitbasic}.

- [ ] Me vil vise poengsummen til kvar spelar i radene på skjermen til
  spelleiaren. Me viser `Player1`{.microbitvariables} i rad `1`, `Player2`{.microbitvariables} i rad `2` osb. Legg til
  klossen `tenn x y`{.microbitled} frå `Skjerm`{.microbitled}. La `y` vere lik `0`.

- [ ] Me må setje `x` til å vere lik poengsummmen til spelarane. Fordi
  koordinatane til skjermen startar på `(0,0)`, _ikkje_ `(1,1)`, så må me
  trekkje frå eitt poeng heile tida, slik at lysa seier kor mange poeng spelaren
  har. Det kan me gjere slik:

```microbit
  basic.forever(function () {
      led.plot(Player1 - 1, 0)
  })
```

- [ ] Gjer det same for `Player2`{.microbitvariables}, `Player3`{.microbitvariables}, `Player4`{.microbitvariables} og `Player5`{.microbitvariables}.

- [ ] Legg til ein `hvis`{.microbitlogic}-kloss og sjekk om `Player1`{.microbitvariables} er lik `5` poeng. Då har
  spelaren vunne.

- [ ] Viss `Player1`{.microbitvariables} har `5` poeng skal me sende ut beskjed om det til alle.
  Fyrst legg me til `radio send tekst`{.microbitradio}, og så legg me til `vis tekst`{.microbitbasic}. Sett
  begge tekstane til _P1 Won!_. Då ser koden slik ut:

```microbit
  basic.forever(function () {
      led.plot(Player1 - 1, 0)
      led.plot(Player2 - 1, 1)
      led.plot(Player3 - 1, 2)
      led.plot(Player4 - 1, 3)
      led.plot(Player5 - 1, 4)
      if (Player1 == 5) {
          radio.sendString("P1 won!")
          basic.showString("P1 won")
      }
```

- [ ] Utvid `hvis`{.microbitlogic}-klossen til `hvis - ellers hvis - ellers hvis - ellers hvis -
  ellers hvis`{.microbitlogic}, slik at du kan sjekke poenga til alle spelarane, og gjer det
  same for `Player2`{.microbitvariables}, `Player3`{.microbitvariables}, `Player4`{.microbitvariables} og `Player5`{.microbitvariables}.

- [ ] Viss du har gjort alt rett så vil koden din sjå slik ut:

```microbit
  basic.forever(function () {
      led.plot(Player1 - 1, 0)
      led.plot(Player2 - 1, 1)
      led.plot(Player3 - 1, 2)
      led.plot(Player4 - 1, 3)
      led.plot(Player5 - 1, 4)
      if (Player1 == 5) {
          radio.sendString("P1 won!")
          basic.showString("P1 won")
      } else if (Player2 == 5) {
          radio.sendString("P2 won!")
          basic.showString("P2 won")
      } else if (Player3 == 5) {
          radio.sendString("P1 won!")
          basic.showString("P1 won")
      } else if (Player4 == 5) {
          radio.sendString("P1 won!")
          basic.showString("P1 won")
      } else if (Player5 == 5) {
          radio.sendString("P1 won!")
          basic.showString("P1 won")
      }
  })
```

# Steg 3: Sende ut meldingar til deltakarane {.activity}

*Så må me sende ut meldingar til deltakarane om kva dei skal herme etter. Me
lagar ein kloss for kvar av dei ulike meldingane, ut frå reglane som er beskrive
lengre opp.*

## Sjekkliste {.check}

- [ ] Fyrst må me finne klossen som heiter `når knapp A trykkes`{.microbitinput}. Den ligg under
  `Inndata`{.microbitinput}.

- [ ] Så hentar me `hvis`{.microbitlogic}-klossen frå `Logikk`{.microbitlogic} og set den saman med
  `erlik-klossen`{.microbitlogic} (`=`) frå same kategori. Her skal du sjekke om `MessageSent`{.microbitvariables}
  er lik `usann`{.microbitlogic}. Klarar du å setje det saman?

- [ ] Inni `hvis`{.microbitlogic}-klossen set me `radio send tekst`{.microbitradio} med teksten `A`.

- [ ] Til slutt legg me til klossen `sett MessageSent til`{.microbitvariables} frå `Variabler`{.microbitvariables} og
  set verdien til `sann`{.microbitlogic}.

- [ ] Viss du har gjort alt rett så vil koden din sjå slik ut:

```microbit
  input.onButtonPressed(Button.A, function () {
    if (MessageSent == false) {
        radio.sendString("A")
        MessageSent = true
    }
  })
```

- [ ] Gjer det same for `B`, `C`, `<` og `>`. Sjekk tabellen over for å sjå kva
  som skal gjerast.

- [ ] Viss du har gjort alt rett så vil koden din sjå slik ut:

```microbit
  input.onButtonPressed(Button.A, function () {
      if (MessageSent == false) {
          radio.sendString("A")
          MessageSent = true
      }
  })
  input.onButtonPressed(Button.B, function () {
      if (MessageSent == false) {
          radio.sendString("B")
          MessageSent = true
      }
  })
  input.onButtonPressed(Button.AB, function () {
      if (MessageSent == false) {
          radio.sendString("C")
          MessageSent = true
      }
  })
  input.onGesture(Gesture.TiltLeft, function () {
      if (MessageSent == false) {
          radio.sendString("<")
          MessageSent = true
      }
  })
  input.onGesture(Gesture.TiltRight, function () {
      if (MessageSent == false) {
          radio.sendString(">")
          MessageSent = true
      }
  })
```

# Steg 4: Sjekke svaret til deltakarane {.activity}

*Etter kvar runde må spelleiaren sjekke kva deltakar som var raskast til å
herme.*

## Sjekkliste {.check}

- [ ] Finn `når radio mottar receivedNumber`{.microbitradio} frå `Radio`{.microbitradio}.

- [ ] Sjekk om `MessageSent`{.microbitvariables} er lik `sann`{.microbitlogic}.

- [ ] Viss `MessageSent`{.microbitvariables} er lik `sann`{.microbitlogic} skal du sjekke om `receivedNumber`{.microbitvariables} er lik
  `1`, for då vann `Player1`{.microbitvariables} denne runden. Me får altså ein `hvis`{.microbitlogic}-kloss inni
  ein annan `hvis`{.microbitlogic}-kloss.

- [ ] Viss `receivedNumber`{.microbitvariables} er lik `1` så set me klossen `endre Player1 med 1`{.microbitvariables}
  frå `Variabler`{.microbitvariables} inni den innerste `hvis`{.microbitlogic}-klossen.

- [ ] Under `endre Player1 med 1`{.microbitvariables} legg du til `radio send tekst`{.microbitradio} med talet `1`.
  Då sender me beskjed til alle om kven som vann. Legg òg til `vis tall`{.microbitbasic} med
  talet `1`. Då viser me det på spelleiaren sin micro:bit.

- [ ] Så legg me til ei pause på `1` sekund mellom dei to `hvis`{.microbitlogic}-klossane før me
  går vidare til neste runde. Dette gjer du ved å leggje til klossen `pause
  (ms)`{.microbitbasic} og set den til `1000`. Tusen millisekund er det same som eitt sekund.

- [ ] Til slutt endrar me `MessageSent`{.microbitvariables} til `usann`{.microbitlogic} att.

- [ ] Viss du har gjort alt rett så vil koden din sjå slik ut:

```microbit
  radio.onReceivedNumber(function (receivedNumber) {
      if (MessageSent == true) {
          if (receivedNumber == 1) {
              Player1 += 1
              radio.sendString("1")
          }
          MessageSent = false
          basic.pause(1000)
      }
  })
```

- [ ] Utvid `hvis`{.microbitlogic}-klossen til `hvis - ellers hvis - ellers hvis - ellers hvis -
  ellers hvis`{.microbitlogic}, slik at du kan sjekke om det var nokon av dei andre spelarane
  som vann denne runden, og gjer det same for `Player2`{.microbitvariables}, `Player3`{.microbitvariables}, `Player4`{.microbitvariables} og
  `Player5`{.microbitvariables}.

- [ ] Viss du har gjort alt rett så vil koden din sjå slik ut:

```microbit
  radio.onReceivedNumber(function (receivedNumber) {
    if (MessageSent == true) {
        if (receivedNumber == 1) {
            Player1 += 1
            radio.sendString("1")
        } else if (receivedNumber == 2) {
            Player2 += 1
            radio.sendString("2")
        } else if (receivedNumber == 3) {
            Player3 += 1
            radio.sendString("3")
        } else if (receivedNumber == 4) {
            Player4 += 1
            radio.sendString("4")
        } else if (receivedNumber == 5) {
            Player5 += 1
            radio.sendString("5")
        }
        MessageSent = false
        basic.pause(1000)
    }
  })
```

# Steg 5: Overføre programmet til spelleiaren {.activity}

- [ ] Gi namnet `spelleiar` til programmet ditt. Dette gjer du ved å endre
  teksten heilt nede på midten på skjermen din.

- [ ] Koble den eine micro:biten din til datamaskina med ein USB-kabel. Denne
  micro:biten blir spelleiaren i spelet.

- [ ] Klikk på knappen `Last ned` nede til venstre på skjermen. No blir det
  lasta ned ei fil som heiter `spelleiar.hex` til datamaskina di.

- [ ] Flytt denne fila over til MICROBIT-disken på maskina di.


# Steg 6: Programmere spelarane {.activity}

*Fyrst må me syte for at spelarane koplar seg til spelleiaren og gir dei eit
spelarnummer, slik at me kan sjekke kven som vinn.*

## Sjekkliste {.check}

- [ ] Start eit nytt PXT-prosjekt.

- [ ] Finn klossen `ved start`{.microbitbasic} under `Basis`{.microbitbasic} og dra den inn i kodefeltet.

- [ ] Gå til `Radio`{.microbitradio} og finn klossen `radio sett gruppe`{.microbitradio}. Hugs at du må bruke
  det same talet her som du valte i `spelleiar`.

- [ ] Gå til `Variabler`{.microbitvariables} og vel klossen `sett variabel til`{.microbitvariables}. Denne kan du bytte
  namn på ved å klikke på _variabel_ og så på _Rename variable_. Den bør heite
  `Player`. Set verdien til `1`.

- [ ] Til slutt viser me talet vårt til skjermen, ved å hente klossen `vis tall`{.microbitbasic}
  og kople den til variabelen `Player`{.microbitvariables}.

- [ ] Viss du har gjort alt rett så vil koden din sjå slik ut:

```microbit
  radio.setGroup(37)
  let Player = 1
  basic.showNumber(Player)
```

# Steg 7: Når spelar mottek ei melding {.activity}

*Neste steg er å ta imot meldinga om kva me skal herme etter, og lagre den. Då
kan me sjekke at me har gjort rett seinare.*

## Sjekkliste {.check}

- [ ] Finn `når radio mottar receivedString`{.microbitradio} frå `Radio`{.microbitradio}.

- [ ] Vis teksten `receivedString`{.microbitvariables} på skjermen.

- [ ] Opprett ein ny variabel med namnet `Press` og set den til
  `receivedString`{.microbitvariables}. Då har me lagra det me treng til å sjekke om me har klart å
  herme etter spelleiaren.

- [ ] Viss du har gjort alt rett så vil koden din sjå slik ut:

```microbit
  radio.onReceivedString(function (receivedString) {
      basic.showString(receivedString)
      Press = receivedString
  })
```

# Steg 8: Når spelar sender ei melding {.activity}

*Siste steg er å herme etter spelleiaren og sende ein beskjed i retur.*

## Sjekkliste {.check}

- [ ] Me startar med å herme etter spelleiar viss meldinga var `A`. Fyrst må me
  finne klossen som heiter `når knapp A trykkes`{.microbitinput}. Den ligg under `Inndata`{.microbitinput}.

- [ ] Så hentar me `hvis`{.microbitlogic}-klossen frå `Logikk`{.microbitlogic} og set den saman med
  `erlik-klossen`{.microbitlogic} (`=`) frå same kategori. Her skal du sjekke om `Press` er lik
  `A`.

- [ ] Viss `Press`{.microbitvariables} er lik `A`, så skal me sende spelarnummeret vårt tilbake til
  spelleiaren. Legg til klossen `radio send tall`{.microbitradio} inni `hvis`{.microbitlogic}-klossen og kople
  den til `Player`. Legg òg til klossen `tøm skjermen`{.microbitbasic} frå `Basis`{.microbitbasic}.

- [ ] Utvid `hvis`{.microbitlogic}-klossen til `hvis - ellers`{.microbitlogic}.

- [ ] Viss `Press`{.microbitvariables} ikkje er lik `A`, så skal micro:biten vise eit surt fjes. Du
  finn klossen `vis ikon`{.microbitbasic} under `Basis`{.microbitbasic}. Vel eit passande ikon.

- [ ] Legg til `pause`{.microbitbasic} i `500` ms. Til slutt kan du finne klossen `vis tekst` og
  leggje variabelen `Press`{.microbitvariables} inni den, for å vise kva du eigentleg burde gjort.

- [ ] Viss du har gjort alt rett så vil koden din sjå slik ut:

```microbit
  input.onButtonPressed(Button.A, function () {
      if (Press == "A") {
          radio.sendNumber(Player)
          basic.clearScreen()
      } else {
          basic.showIcon(IconNames.Angry)
          basic.pause(500)
          basic.showString(Press)
      }
  })
```

- [ ] Gjer tilsvarande for `B`, `C`, `<` og `>`.

- [ ] Viss du har gjort alt rett så vil koden din sjå slik ut:

```microbit
  input.onButtonPressed(Button.A, function () {
      if (Press == "A") {
          radio.sendNumber(Player)
          basic.clearScreen()
      } else {
          basic.showIcon(IconNames.Angry)
          basic.pause(500)
          basic.showString(Press)
      }
  })input.onButtonPressed(Button.B, function () {
      if (Press == "B") {
          radio.sendNumber(Player)
          basic.clearScreen()
      } else {
          basic.showIcon(IconNames.Angry)
          basic.pause(500)
          basic.showString(Press)
      }
  })input.onButtonPressed(Button.AB, function () {
      if (Press == "C") {
          radio.sendNumber(Player)
          basic.clearScreen()
      } else {
          basic.showIcon(IconNames.Angry)
          basic.pause(500)
          basic.showString(Press)
      }
  })input.onGesture(Gesture.TiltLeft, function () {
      if (Press == "<") {
          radio.sendNumber(Player)
          basic.clearScreen()
      } else {
          basic.showIcon(IconNames.Angry)
          basic.pause(500)
          basic.showString(Press)
      }
  })input.onGesture(Gesture.TiltRight, function () {
      if (Press == ">") {
          radio.sendNumber(Player)
          basic.clearScreen()
      } else {
          basic.showIcon(IconNames.Angry)
          basic.pause(500)
          basic.showString(Press)
      }
  })
```

# Steg 9: Overføre programmet til spelarane {.activity}

*Overfør programmet til kvar av spelarane sine micro:bitar. Hugs å endre
programmet med spelarnummer mellom kvar gong, og last det ned på nytt.*

## Sjekkliste {.check}

- [ ] Gi namnet `spelar` til programmet ditt. Det gjer du ved å endre teksten
  heilt nede på midten av skjermen din.

- [ ] Kople den eine micro:biten din til datamaskina med ein USB-kabel. Denne
  micro:biten blir spelleiaren i spelet.

- [ ] Klikk på knappen `Last ned` nede til venstre på skjermen. No blir det
  lasta ned ei fil som heiter `spelar.hex` til datamaskina di.

- [ ] Flytt denne fila over til MICROBIT-disken på maskina di.

- [ ] Endre spelarnummeret i programmet, og gjer samme prosess for kvar av
  spelarane som skal vere med.

### OBS! {.protip}

Hugs å endre nummeret kvar spelar får mellom kvar nye micro:bit du koplar til og
lastar ned programmet til. Du må laste ned programmet på nytt for kvar av
spelarane med dei endringane du har gjort.

## Utfordringar {.challenge}

- [ ] Legg til fleire element som spelarane skal reagere på. Til dømes viss
  micro:biten blir rista.

- [ ] Endre koden til spelleiaren slik at micro:biten automatisk vel heilt
  tilfeldig kva spelarane skal herme etter.

- [ ] Endre koden slik at spelarane kan jukse. Kan du gjere slik at dei alltid
  svarar rett? Kan du få til at ein spelar alltid svarar raskast?

- [ ] Endre koden til spelleiaren slik at han sjekkar at spelarane faktisk har
  svara rett, for å passe på at dei ikkje har juksa. Merk at då må du endre på
  spelarane sin kode òg.

## Sikkerheit med server og klient {.protip}

No har me laga ein applikasjon med server (spelleiaren) og klientar (spelarane).
Spelarane kommuniserer gjennom kvar sin klient, men koordinerer (tel kven som
vinn) på ein server.

### Sikkerheit i spelet vårt

Kvar klient kan i prinsippet bestemme kva kode som skal køyre på si eiga eining.
Det gjer det mogleg å jukse! for å unngå at det er mogleg å jukse må me tenke
oss om for å finne ut korleis me skal kode serveren og klienten vår.

**Å la klienten sende tilbake "eg hadde rett" er ikkje sikkert.** Då kan eg lage
min eigen klient som alltid gir meg alle poenga, uansett kva eg har svart.

**Å la klienten sende tilbake "eg svarte B" er betre.** Då må eg faktisk vite
svaret for å kunne få poeng. _Kva trur du skjer viss du gjettar alle svara heile
tida? Klarar du å tenke på ein måte som gjer det umogleg?_

### Sikkerheit på Facebook

Facebook er ein annan applikasjon som er delt inn i klient og server.

**Klienten viser bileta dine og venene dine.** Du ser klienten når du går til
`facebook.com` i ein nettlesar. Når du brukar Facebook-appen på ein
mobiltelefon, brukar du ein annan klient.

**Serveren heldt styr på all informasjonen.** Serveren kan seie om du prøver å
logge inn med riktig brukarnamn og passord. Serveren veit kven som er venene
dine, og den veit kven som kan administrere kva sider og grupper.

Kva hadde skjedd viss gruppeadministrasjon vart handtert i klienten? Korleis
kunne du då ha laga din eigen klient? Kva kunne du gjort med den?
