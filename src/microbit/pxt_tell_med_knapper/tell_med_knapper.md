---
title: "PXT: Tell med knapper"
author: Helene Isnes
language: nb
---


# Introduksjon {.intro}
I denne oppgaven skal vi få micro:biten til å telle både oppover og nedover ved
å trykke på knappene A og B.


# Steg 1: Lage en variabel {.activity}

Før vi begynner å telle, må vi finne en måte for micro:biten å huske tallet vi
har kommet til. Hvis vi ikke gjør dette, så vil den glemme hvor langt vi har
kommet!

## Sjekkliste {.check}

- [ ] Gå til `Variabler`{.microbitvariables} og klikk på `Lag en variabel`{.microbitvariables}
	helt øverst.

- [ ] Skriv inn ønsket navn, f.eks. "Tall" og klikk Ok.

Ser du at det nå finnes en rød kloss som heter "Tall"? Den har du laget! I denne
klossen skal vi lagre tallet vi har kommet til i tellingen. Den kalles en
variabel fordi vi kan variere hvilket tall vi lagrer i den.

- [ ] Finn `sett variabel til`{.microbitvariables}-klossen i `Variabler`{.microbitvariables}
	og sett den inni en `ved start`{.microbitbasic}-kloss (denne ligger allerede i
	kodefeltet ditt eller så finner du den i `Basis`{.microbitbasic}). Så klikker
	du på den vesle pila og velger variabelen du lagde på forrige steg, "Tall".

```microbit
let Tall = 0
```

Når programmet starter blir nå tallet 0 lagret i variabelen/klossen som heter
"Tall".


# Steg 2: Telling {.activity}

Nå er det på tide å begynne å telle. Når vi trykker på knappen A så ønsker vi å
øke verdien av "Tall" med en. Slik kan vi telle oppover hver gang knappen
trykkes.

- [ ] Prøv å lage en kodeblokk som øker variabelen "Tall" med 1 når knapp A
	trykkes. Koden din burde se slik ut:

```microbit
input.onButtonPressed(Button.A, function () {
    Tall += 1
})
```

## {.tip}

`Når knapp A trykkes`{.microbitinput}-klossen finner du i menyen under `Inndata`{.microbitinput}.
`Endre variabel med 1`{.microbitvariables}-klossen finner du i `Variabler`{.microbitvariables}.
Husk å endre `variabel`{.microbitvariables} til `Tall`{.microbitvariables}.


# Steg 3: Vis tall {.activity}

Men vi ser jo ingenting! Det er fordi vi ikke har bedt programmet om å faktisk
vise oss verdien av "Tall". Den eksisterer, men er usynlig for oss.

- [ ] For å vise den fram, legg til en `vis tall 0`{.microbitbasic}-kloss under
	klossen `endre Tall med 1`{.microbitvariables}. Erstatt __0__ med variabelen
	`Tall`{.microbitvariables}.

- [ ] Hvis du vil se tallet 0 i begynnelsen kan du også legge den til nederst i
	`ved start`{.microbitbasic}-klossen.

## {.tip}

Husk at du finner "Tall"-klossen i `Variabler`{.microbitvariables}.


# Steg 4: Siste bit {.activity}

- [ ] Nå skal vi gjøre noe smart. Høyreklikk på den lilla rammen til
	`når knapp A trykkes`{.microbitinput} i koden din og velg "Lag kopi" fra
	menyen som dukker opp. Nå får du en kopi av hele den seksjonen med kode. Dette
	er lurt når man skal lage kode som er helt lik eller nesten helt lik den koden
	man allerede har laget, fordi det går så fort!

- [ ] Endre kopien din slik at koden ser ut som den under. Vi har gjort om A til
	B og 1 til -1.

```microbit
input.onButtonPressed(Button.B, function () {
    Tall += -1
    basic.showNumber(Tall)
})
```

Å endre "Tall" med -1 betyr at verdien av "Tall" minker med 1 hver gang vi
trykker på B.


## Test prosjektet {.flag}

- [ ] Test programmet ved å trykke på knappene A og B i simulatoren. Teller den
	oppover og nedover som den skal?

- [ ] Last ned koden til micro:biten hvis du er ferdig og test ut knappene.


## Utfordring {.challenge}

- [ ] La oss lage en ny måte å nullstille telleren vår på. Gå til `Inndata`{.microbitinput}
	og 	finn klossen `når ristes`{.microbitinput}. Legg inn `sett Tall til 0`{.microbitvariables}-klossen.

```microbit
input.onGesture(Gesture.Shake, function () {
    Tall = 0
})
```

- [ ] Last ned koden til micro:biten. Hva skjer når du rister micro:biten? Hva
	annet kan du velge i denne klossen enn risting?

- [ ] Klarer du å finne flere måter å endre Tall med i programmet ditt? Kanskje
	skal "Tall" økes med 2 når du heller micro:biten til høyre? Eller kanskje skal
	"Tall" settes til 10 når både knapp A og B trykkes samtidig? Prøv og lek deg
	med mulighetene!
