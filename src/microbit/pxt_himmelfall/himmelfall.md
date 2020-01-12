---
title: "PXT: Himmelfall"
author: Helene Isnes og Julie Revdahl
language: nb
---


# Introduksjon {.intro}

"Himmelfall" er et spill som går ut på å unngå det som faller ned på micro:bit
skjermen. Spilleren skal bevege seg til høyre og venstre med knappene A og B.
Selv om vi i denne oppgaven skal lage et spill, skal vi unngå `Spill`{.microbitgame}-kategorien
helt og heller bruke andre kategorier for å lage spillet vårt.

![Bilde av spillet](spill.png)

Skjermen på micro:biten består av 5x5 ledlys. Disse kan vi skru av og på med
litt kode. I denne oppgaven bruker vi klosser fra `Skjerm`{.microbitled}-kategorien
til å sette og endre hvor lysene skal være. Posisjonen til lysene blir gitt med
en x- og en y-posisjon som i et rutenett. Verdien til x angir plassen til lyset
bortover (horisontalt) og verdien til y angir plassen nedover (vertikalt), dette
er vist på bilder under. Hjørnet øverst til venstre har verdiene __(0,0)__, mens
hjørnet nederst til høyre har verdiene __(4,4)__.

![Bilde som viser hvordan rutenettet av leddlys på micro:biten fungerer](ved_start_skjerm.png)


# Steg 1: Grunnmur {.activity}

*Det første vi må gjøre er å lage litt av grunnlaget for spillet.*

## Sjekkliste {.check}

- [ ] Lag variablene `spiller`{.microbitvariables}, `poeng`{.microbitvariables},
`liv`{.microbitvariables} og `hull`{.microbitvariables} med `Lag en variabel...`{.microbitvariables}
i `Variabler`{.microbitvariables}-kategorien.

- [ ] I `ved start`{.microbitbasic}-klossen (som allerede er i kodefeltet ditt,
	ellers finner du den i `Basis`{.microbitbasic}), sett `spiller`{.microbitvariables}
	til 2. Bruk klossen `sett variabel til 0`{.microbitvariables} som du finner i
	`Variabler`{.microbitvariables}.

- [ ] Bruk `tenn`{.microbitled}-klossen fra `Skjerm`{.microbitled}-kategorien
	til å tenne x: 2 og y: 4. Dette er startposisjonen til spilleren.

- [ ] Sett `poeng`{.microbitvariables} til 0 og `liv`{.microbitvariables} til 3.

- [ ] Hvis du har gjort alt rett burde koden din se slik ut:

```microbit
let spiller = 2
led.plot(2, 4)
let poeng = 0
let liv = 3
```


# Steg 2: Det faller {.activity}

*I dette steget skal vi kode ledlysene som faller nedover og lage hullåpningen
som spilleren skal komme seg gjennom.*

## Sjekkliste {.check}

- [ ] I kategorien `Løkker`{.microbitloops} finn en `gjenta hvis sann`{.microbitloops}-kloss
	og sett den til sist i `ved start`{.microbitbasic}.

I steden for `sann`{.microbitlogic} vil vi at løkken skal kjøre så lenge `liv`{.microbitvariables}
er større enn 0.

- [ ] Bytt ut `sann`{.microbitlogic} med klossen `0 > 0`{.microbitlogic}, som du
	finner i `Logikk`{.microbitlogic}. Klikk på pilen på midten av klossen og endre
	veien tegnet står. Variabelen `liv`{.microbitvariables} skal inn i stedenfor
	den første 0-en.

```microbit
while (liv > 0) {

}
```

**All koden vi skriver videre i steg 2 og steg 3 skal inn i** `gjenta hvis liv > 0`{.microbitloops}
**-klossen.**

- [ ] Hullet spilleren skal gjennom skal settes til et tilfeldig sted for hver
	runde. Bruk en kloss fra `Variabler`{.microbitvariables} og en fra `Matematikk`{.microbitmath}
	for å få dette til. Koden skal settes i klossen fra forrige punkt.

Det vi skal gjøre nå er å gå gjennom hele rutenettet for leddlysene og se hvor
vi må tenne og etterpå slukke lys for å få det til å se ut som lysene faller
nedover.

- [ ] Lag to variabler `x-indeks`{.microbitvariables} og `y-indeks`{.microbitvariables}.
	Disse variablene vil holde styr på hvor vi er i rutenettet.

- [ ] Finn en `gjenta for indeks 0 til 4`{.microbitloops}-kloss i kategorien
	`Løkker`{.microbitloops}, denne skal settes under klossen fra forrige punkt.
	Endre variablen til `y-indeks`{.microbitvariables}.

- [ ] Sett en `gjenta for indeks 0 til 4`{.microbitloops}-kloss inn i den
	forrige og bytt ut variabelen med `x-indeks`{.microbitvariables}.

```microbit
while (liv > 0) {
    for (let yindeks = 0; yindeks <= 4; yindeks++) {
        for (let xindeks = 0; xindeks <= 4; xindeks++) {

        }
    }
}
```

Programmet skal gå gjennom hele raden bortover (alle x indeksene) og tenne alle
ledlysene på raden utenom der hullet skal være.

- [ ] Hvis `x-indeks`{.microbitvariables} er ulik `hull`{.microbitvariables}
	skal lyset tennes ved x: `x-indeks`{.microbitvariables} og y: `y-indeks`{.microbitvariables}.
	Kod dette ved bruk av klossene `hvis`{.microbitlogic} (fra kategorien `Logikk`{.microbitlogic}),
	`tenn`{.microbitled} (fra kategorien `Skjerm`{.microbitled}) og `0 ulik 0`{.microbitlogic}  
	(som du finner i `Logikk`{.microbitlogic} ved å endre på `=`{.microbitlogic}
	klossen). Disse klossene skal sammen settes i `gjenta for x-indeks 0 til 4`{.microbitloops}-klossen.

- [ ] Sett så en `pause`{.microbitbasic}-kloss til 300 etter `gjenta for x-indeks
	0 til 4`{.microbitloops}-blokken.

- [ ] Kopier `gjenta for x-indeks 0 til 4`{.microbitloops}-blokken (høyreklikk
	og trykk på __Lag kopi__). Sett blokken under `pause`{.microbitbasic}-klossen
	og endre `tenn`{.microbitled}-klossen til en `slukk`{.microbitled}-kloss.


# Steg 3: Poeng og antall liv {.activity}

*Nå skal vi lage kode som holder orden på antall poeng og liv!*

## Sjekkliste {.check}

- [ ] Sett inn en `hvis-eller`{.microbitlogic}-kloss under `gjenta for y-indeks
	fra 0 til 4`{.microbitloops}-blokka. `Hvis-ellers`{.microbitlogic}-klossen
	finner du i `Logikk`{.microbitlogic}.

- [ ] Hvis `spiller`{.microbitvariables} er lik `hull`{.microbitvariables} så
	skal `poeng`{.microbitvariables} endres med 1. Se om du kan klare å kode dette
	til ved å bytte ut `sann`{.microbitlogic} med klosser fra `Variabler`{.microbitvariables}
	og `Logikk`{.microbitlogic}, og sette inn en kloss i område til `hvis`{.microbitlogic}
	som skal være fra `Variabler`{.microbitvariables}.

## {.tip}
`hvis-ellers`{.microbitlogic}-klossen fungerer slik at hvis spilleren kommer seg
gjennom hullet, så vil programmet kjøre koden som hører til `hvis`{.microbitlogic}-delen
av klossen. Hvis dette ikke er sant (spilleren klarte ikke å komme gjennom hullet),
vil programmet kjøre koden som hører til `ellers`{.microbitlogic}-delen av klossen.
##

Hvis spilleren ikke klarer å komme seg gjennom hullet, skal et liv går tapt.

- [ ] I `ellers`{.microbitlogic}-området til `hvis-ellers`{.microbitlogic}-klossen,
	endre liv med -1.

Hvis vi har tapt et liv, og alle liv er brukt opp, skal spillet være over. Hvis
vi fortsatt har liv igjen, skal vi tenne spilleren på nytt.

- [ ] Sett in en `hvis-ellers`{.microbitlogic}-kloss under `endre liv med 1`{.microbitvariables}.

- [ ] Bytt ut `sann`{.microbitlogic} med klossen `liv = 0`{.microbitlogic}.

- [ ] Når alle liv er tapt (liv = 0) er spillet over. Det første vi skal gjøre,
	er å vise dette klart å tydelig med et bilde. Gå til kategorien `Basis`{.microbitbasic}
	og bruk klossen `vis ikon`{.microbitbasic}. Du kan selv velge hvilket bilde du
	vil bruke, men et forslag er hodeskallen.

- [ ] Legg på en `pause`{.microbitbasic}-kloss som du finner i `Basis`{.microbitbasic},
	og endre tallet til 500.

## {.tip}
Vi legger på en `pause`{.microbitbasic}-kloss under `vis ikon`{.microbitbasic}
fordi vi vil at bildet skal vises en stund før resten av koden kjøres.
##

- [ ] Til slutt vil vi at poengsummen vår skal vises. Dette gjør vi ved å bruke
	en `hvis sann`{.microbitlogic}-kloss siden koden i klossen vil kjøre helt til
	vi vil starte spillet på nytt. Sett inn koden nedenfor under `pause`{.microbitbasic}-klossen.

```microbit
while (true) {
    basic.showNumber(poeng)
    basic.showString("")
}
```

## {.tip}
Klossene `vis tall`{.microbitbasic} og `vis tekst`{.microbitbasic} kan begge
finnes i `Basis`{.microbitbasic}-kategorien.
##

## {.tip}
Hvis man vil starte spillet på nytt kan man trykke på den sorte __RESET__-knappen
på baksiden av micro:biten.
##

Det eneste vi vil gjøre hvis vi fortsatt har liv igjen, er å tenne `spiller`{.microbitvariables}.

- [ ] I `ellers`{.microbitlogic}-området til `hvis-ellers`{.microbitlogic}-klossen,
	sett inn en `tenn`{.microbitled}-kloss som skal tenne x: `spiller`{.microbitvariables}
	og y: 4.

- [ ] Hvis du har gjort alt rett burde koden din se slik ut:

```microbit
if (spiller == hull) {
    poeng += 1
} else {
    liv += -1
    if (liv == 0) {
        basic.showIcon(IconNames.Skull)
        basic.pause(500)
        while (true) {
            basic.showNumber(poeng)
            basic.showString("")
        }
    } else {
        led.plot(spiller, 4)
    }
}
```


# Steg 4: Beveg spilleren {.activity}

*Vi vil at spilleren skal bevege seg mot venstre når knapp A trykkes, og mot
høyre når knapp B trykkes.*

## Sjekkliste

- [ ] Finn en `når knapp A trykkes`{.microbitinput}-kloss i `Inndata`{.microbitinput}-kategorien.

- [ ] Bruk `slukk`{.microbitled}- og `tenn`{.microbitled}-klossene som du
	finner i `Skjerm`{.microbitled}-kategorien til å først slukke og så tenne lyset til
	spilleren. X-verdien er det vi har kalt `spiller`{.microbitvariables}, mens
	y-verdien er 4 siden spilleren bare skal bevege seg på nederste rad.

- [ ] Mellom `slukk`{.microbitled}- og `tenn`{.microbitled}-klossene trenger
	vi en `hvis`{.microbitlogic}-kloss. Her skal koden inni kjøre om `spiller`{.microbitvariables}
	er over 0. `spiller`{.microbitvariables} skal da endres med -1.

## {.tip}
Grunnen til at vi bruker en `hvis`{.microbitlogic} kloss og ikke endrer
`spiller`{.microbitvariables} uansett er fordi vi ikke vil at spilleren skal
bevege seg mer mot venstre enn det rutenettet med leddlys tillater. Hvis
spilleren allerede står på x: 0, skal den ikke få lov til å bevege seg mot venstre.
##

- [ ] Kopier hele `når knapp A trykkes`{.microbitinput}-blokka ved å høyreklikke
	på den og trykk __Lag kopi__.

- [ ] Endre den kopierte blokka slik at den er for når knapp B trykkes (trykk på
	pilen ved siden av __A__.

Det er to ting som må endres fra `når knapp A trykkes`{.microbitinput}-blokka
til `når knapp B trykkes`{.microbitinput}. Det ene er veien spilleren skal gå
når knappen blir trykket, og det andre er det som hindrer spilleren i å gå ut av
brettet.

- [ ] Endre fra `spiller > 0`{.microbitlogic} til `spiller < 4`{.microbitlogic}.
	Da vil ikke spilleren få lov til å gå utenfor spillebrettet mot høyre.

- [ ] Endre tallet i `endre spiller med ...`{.microbitvariables} slik at
	spilleren går mot høyre når knapp B trykkes (du trenger bare å ta bort en
	minus (__-__)).

## Test prosjektet {.flag}

*Koden din er nå ferdig!*

- [ ] Sjekk simulatoren og se til at alt fungerer som det skal.

- [ ] Last ned spillet til micro:biten og spill i vei!

## Utfordringer {.challenge}

- [ ] Sett på lyd ved starten av spillet og når spillet er over

- [ ] Klarer du å endre koden slik at spillet blir litt vanskeligere eller
	enklere å spille?
