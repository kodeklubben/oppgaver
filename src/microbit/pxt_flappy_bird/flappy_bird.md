---
title: "PXT: Flappy bird"
author: Julie Christina Revdahl
language: nb
---


# Introduksjon {.intro}
I denne opggaven skal vi lage en versjon av det populære spillet flappy bird,
slik at vi kan spille det på micro:biten vår.


# Steg 1: Starte spillet {.activity}

## Sjekkliste {.check}

- [ ] Da dette spillet krever en del kode, deler vi den inn i flere kode-blokker
for å få bedre oversikt. Nå skal vi starte med klossen `ved start`{.microbitbasic},
og bygge koden for oppstart av spillet.

- [ ] Først vil vi fortelle spilleren at spillet er på vei til å starte. Bruk en
`vis tekst`{.microbitbasic}-kloss og fortell spilleren at spillet skal starte.
Legg inn en `pause`{.microbitbasic} på `500ms`{.microbitbasic} etter denne, slik
at spilleren får litt tid til å forberede seg.

- [ ] Nå skal vi lage selve fuglen vi skal styre. Først oppretter vi en variabel
`bird`{.microbitvariables}. Denne skal vi sette til `create sprite at x: 1 y: 2`{.microbitgame}.
Det betyr at fuglen vår er ledlyset i punktet der x er 1 og y er 2. *(Ledlysene
  teller fra 0 til 4.)* Denne klossen finner vi i kategorien `Spill`{.microbitgame}.

- [ ] Etterpå må vi opprette en variabel som vi skal bruke til å styre om spillet
skal fortsette eller er over. Vi lager derfor variabelen `gameover`{.microbitvariables},
som vi setter til `usann`{.microbitlogic} ved oppstart av spillet.

- [ ] Det siste vi vil legge inn i kode-blokken for `ved start`{.microbitbasic},
er en kort pause før spillet er i gang. `300ms`{.microbitbasic} er nok, men du
kan legge inn så lang pause du vil, det betyr bare at fuglen ikke begynner å
bevege seg før denne pausen er over.

- [ ] Nå bør koden din ligne på denne:

```microbit
basic.showString("GO")
basic.pause(500)
bird = game.createSprite(1, 2)
let gameover = false
basic.pause(300)
```


# Steg 2: Få fuglen til å fly {.activity}

## Sjekkliste {.check}

- [ ] Nå skal vi lage en enkel kode for å få fuglen til å fly. Vi vil at fuglen
skal fly når vi trykker på knapp A. Vi kunne også ha brukt knapp B, det er opp
til deg. Finn klossen `når knapp A trykkes`{.microbitinput} fra kategorien
`Inndata`{.microbitinput}.

- [ ] Inne i denne klossen skal vi legge en `sprite endre x med 1`{.microbitgame}-kloss.
Vi vil endre slik at det er variabelen `bird`{.microbitvariables} som skal
endres. Da fuglen skal fly oppover, må vi endre fra x-retning til y-retning.
Y og x er null i ledlyset øverst i venstre hjørne. Endre på 1-tallet, slik at fuglen
flyr riktig vei.

- [ ] Legg inn en `pause`{.microbitbasic}-kloss på `100ms`{.microbitbasic}, slik
at knappen ikke blir for følsom.

- [ ] Koden ser nå slik ut:

```microbit
let bird: game.LedSprite = null
input.onButtonPressed(Button.A, function () {
    bird.change(LedSpriteProperty.Y, -1)
    basic.pause(200)
})
```

# Steg 3: Få fuglen til å falle {.activity}

## Sjekkliste {.check}

- [ ] At fuglen faller, er noe som skal skje hele tiden. Vi trenger derfor en
`gjenta for alltid`{.microbitbasic}-kloss.

- [ ]  Vi vil nå at fuglen skal falle så lenge vi ikke trykker knapp A. For å
få til dette bruker vi en `hvis - ellers`{.microbitlogic}-kloss. Først vil vi
sjekke om knapp A trykkes med å legge inn en `knapp A trykkes`{.microbitinput}-kloss
i `hvis`{.microbitlogic}-klossen. Vi har allerede laget koden for denne, og lar
derfor bare denne være tom.

- [ ] Inne i `ellers`{.microbitlogic} skal vi lage koden for å få fuglen til å
falle. Vi finner derfor en `sprite endre x med 1`{.microbitgame}-kloss. Også her
må vi endre slik at det er `bird`{.microbitvariables} og y-retning som endres.
Denne gangen lar vi derimot __1__ bli stående, for nå skal fuglen falle nedover.
Utenfor `hvis - ellers`{.microbitlogic}-klossen legger vi en `pause`{.microbitbasic}-kloss.
Denne bør være på minst `300ms`{.microbitbasic}, men du justerer den som du vil.
Er tallet for lite, faller fuglen for fort.

- [ ] Koden ser nå slik ut:

```microbit
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {

    } else {
        let bird: game.LedSprite = null
        bird.change(LedSpriteProperty.Y, 1)
    }
    basic.pause(400)
})
```


# Steg 4: Sjekke om fuglen flyr for høyt eller faller for lavt {.activity}

## Sjekkliste {.check}

- [ ] Denne delen av koden begynner å bli litt mer komplisert. Nå skal vi se om
fuglen flyr for høyt eller for lavt, med andre ord om fuglen kolliderer med en kant.
Dette skal vi gjøre hele tiden, og vi trenger derfor en `gjenta for alltid`{.microbitbasic}-kloss.

- [ ] Det neste som er viktig å sjekke er om spillet skal fortsette. Vi trenger
derfor en `hvis`{.microbitlogic}-kloss, hvor vi sjekker om `gameover`{.microbitvariables}
fortsatt er `usann`{.microbitlogic}. Se om du greier å sette opp dette selv.

- [ ] Etter å ha sjekket om spillet fortsatt går, skal vi sjekke om fuglen berører
en kant. Dette gjør vi med en `hvis`{.microbitlogic}-kloss, og en `is sprite touching edge`{.microbitgame}-kloss.
Denne må endres til å sjeke om `bird`{.microbitvariables} berører kanten.

- [ ] Fuglen må ha lov til å berøre kanten et lite øyeblikk for å komme seg unna
hinderet, men ikke alt for lenge. Vi vil derfor sette et starttidspunkt, slik at
vi kan lage en begrensning for hvor lenge vi kan berøre kanten. Vi lager derfor
en ny variabel `start`{.microbitvariables} og setter den til `kjøretid ms`{.microbitinput}.
Da inneholder `start`{.microbitvariables} tidspunktet den ble satt.

- [ ] Nå vil vi lage koden for hva som skal skje dersom vi fortsatt berører kanten.
Vi trenger derfor en `gjenta hvis`{.microbitloops}-kloss, med samme krav som tidliger:
`is bird touching edge`{.microbitgame}.

- [ ] Inne i denne klossen lager vi den nye variabelen `slutt`{.microbitvariables},
som skal settes til det nåværende tidspunktet på samme måte som `start`{.microbitvariables}.

- [ ] Etter dette er satt, vil vi sjekke om tiden vi har berørt kanten
overskrider kravet vårt. Vi trenger en `hvis`{.microbitlogic}-kloss, hvor vi
må sjekke om slutt minus start er større eller lik kravet vårt. Vi bestemmer at
vi kan berøre kanten i maks 1 sekund. Se om du finner klosser i kategoriene
`Matematikk`{.microbitmath}, `Logikk`{.microbitlogic} og `Variabler`{.microbitvariables}
til å sette opp kravet på egenhånd.

- [ ] Inne i `hvis`{.microbitlogic}-klossen skal vi lage koden for hva som skjer
når vi har berørt kanten for lenge. Da er spillet over. Først vil vi vise
poengsummen ved å bruke `vis tall`{.microbitbasic}- og `poengsum`{.microbitgame}-klossene.
Deretter setter vi inn `game over`{.microbitgame}-klossen for å avslutte spillet.

- [ ] Nå har vi fullført hele kode-blokken for å sjekke om fuglen kolliderer
med kantene. Koden ser nå slik ut:

```microbit
basic.forever(function () {
    if (gameover == false) {
        let bird: game.LedSprite = null
        if (bird.isTouchingEdge()) {
            start = input.runningTime()
            while (bird.isTouchingEdge()) {
                slutt = input.runningTime()
                if (slutt - start >= 1000) {
                    gameover = true
                    basic.showNumber(game.score())
                    game.gameOver()
                }
            }
        }
    }
})
```


# Steg 5: Lage et hinder som forflytter seg over skjermen {.activity}

## Sjekkliste {.check}

- [ ] Vi skal nå lage hinderet som fuglen vår skal prøve å unngå. Vi starter på
samme måte som i steg 4, og setter opp `gjenta for alltid`{.microbitbasic}-kloss.
Vi trenger også en lik `hvis`{.microbitlogic}-kloss som igjen sjekker om
`gameover`{.microbitvariables} fortsatt er `usann`{.microbitlogic}. Du kan kopiere
disse klossene fra koden fra forrige steg.

- [ ] Vi legger inn en `pause`{.microbitbasic} på 1-2 sekunder. På den måten får
spilleren tid til å teste flygingen før hinderet kommer på skjermen.

- [ ] Nå må vi opprette hinderet på samme måte som vi lagde fuglen i det første
steget. Lag variabelen `hinder`{.microbitvariables}, og sett denne til
`create sprite at x:4 y: velg tilfeldig 0 til 4`{.microbitgame}. Klossen
`velg tilfeldig 0 til 4`{.microbitmath} finner du under kategorien `Matematikk`{.microbitmath}.
Vi velger tilfeldig mellom tall fra 0 til 4 fordi ledlysene har indeks fra 0 til 4.
Det betyr at fuglen alltid vil havne på en tilfeldig rad, og ikke på samme sted
hver runde.

- [ ] Neste oppgave er å lage koden for å få hinderet til å forflytte seg. Vi
må derfor lage en kode som skal `gjentas for indeks fra 0 til 4`{.microbitloops},
altså skal vi flytte ledlyset gjennom alle indeksene.

- [ ] Deretter må vi inn i kategorien `Spill`{.microbitgame} og finne klossen `sprite
endre x med 1`{.microbitgame}. Vi må endre slik at det er `hinder`{.microbitvariables}
som endres, og den skal endres med __-1__. Da vil hinderet bevege seg fra høyre
mot venstre over skjermen vår.

- [ ] Legg inn en `pause`{.microbitbasic}-kloss slik at hinderet ikke beveger
seg for raskt.

- [ ] Nå må vi lage koden som avslutter spillet dersom fuglen kolliderer med
hinderet. Vi bruker klossene `hvis`{.microbitlogic} og `bird touching hinder`{.microbitgame}.
Se om du finner de på egenhånd!

- [ ] Dersom fuglen og hinderet kolliderer skal vi avslutte spillet på samme måte
som tidligere. Vi setter `gameover`{.microbitvariables} til `sann`{.microbitlogic},
viser `poengsum`{.microbitgame} på skjermen og avslutter spillet med `game over`{.microbitgame}-klossen.

- [ ] Til slutt må vi legge til at poengsummen vår skal øke for hver gang vi
greier å unngå hinderet. Vi må også slette hinderet hver gang det fullfører én
runde over skjermen slik at vi ikke får uendelig mange hinder. Du finner begge
klossene under kategorien `Spill`{.microbitgame}. Disse må settes utenfor de
innerste løkkene, men inne i `hvis gameover = sann`{.microbitlogic}-blokken.
Se om du greier å plassere disse på riktig sted.

- [ ] Denne kodeblokken bør nå se ut som dette:

```microbit
basic.forever(function () {
    if (gameover == false) {
        basic.pause(1000)
        let bird: game.LedSprite = null
        let hinder: game.LedSprite = null
        hinder = game.createSprite(4, Math.randomRange(0, 4))
        for (let indeks = 0; indeks <= 4; indeks++) {
            hinder.change(LedSpriteProperty.X, -1)
            basic.pause(200)
            if (bird.isTouching(hinder)) {
                gameover = true
                basic.showNumber(game.score())
                basic.pause(1000)
                game.gameOver()
            }
        }
        if (hinder.get(LedSpriteProperty.X) == 0){
        game.addScore(1)
        hinder.delete()
        }
    }
})
```
- [ ] Vi har nå lagd alle blokkene for koden vår, og den er klar til å testes!

## Test prosjektet {.flag}

Det er to måter du kan teste spillet ditt på:

- [ ] Bildet av micro:biten til venstre på skjermen din er faktisk en simulator
hvor du kan teste koden din. Når du trykker på knapp A skal du greie å styre
fuglen så den kommer seg unna hinderet. Fungerer det som det skal?

- [ ] Du kan også teste spillet ved å laste det ned på micro:biten. For å laste
ned koden må du først ha koblet micro:biten til datamaskinen med en USB-kabel.
Klikk deretter på knappen `Last ned` nede til venstre på skjermen. Det lastes nå
ned en fil som heter `microbit-Uten-navn.hex` til datamaskinen din. Samtidig
dukker det opp et vindu som sier at du må flytte denne filen til MICROBIT-disken
på datamaskinen din.


## Utfordring {.challenge}

- [ ] Prøv å endre på pause-klossene dersom fuglen faller for fort eller hinderet
beveger seg for raskt.
