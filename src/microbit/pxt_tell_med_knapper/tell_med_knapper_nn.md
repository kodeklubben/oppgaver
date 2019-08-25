---
title: "PXT: Tel med knappar"
author: Helene Isnes
translator: Stein Olav Romslo
language: nn
---


# Introduksjon {.intro}

I denne oppgåva skal me få micro:bit-en til å telje både oppover og nedover ved
å trykkje på knappane A og B.


# Steg 1: Lage ein variabel {.activity}

Før me startar å telje må me finne ein måte for micro:bit-en å hugse talet me
har kome til. Viss me ikkje gjer det, så vil den gløyme kor langt me har kome!

## Sjekkliste {.check}

- [ ] Gå til `Variablar`{.microbitvariables} og klikk på `Lag ein variabel`{.microbitvariables} heilt øvst.

- [ ] Skriv inn eit namn på variabelen, til dømes `Tal`{.microbitvariables} og klikk OK.

Ser du at det dukka opp ein raud kloss som heiter `Tal`{.microbitvariables}? Den har du laga! I
denne klossen skal me lagre talet me har kome til i teljinga. Den kallast ein
variabel fordi me kan variere kva tal me lagrar i den.

- [ ] Finn `set variabel til`{.microbitvariables}-klossen i `Variablar`{.microbitvariables} og set den inni ein `ved
  start`{.microbitbasic}-kloss (den ligg allereie i kodefeltet ditt, elles finn du den i
  `Basis`{.microbitbasic}). Så klikkar du på den vesle pila og vel variabelen du laga i stad.

```microbit
let Tall = 0
```

Når programmet startar blir talet __0__ lagra i variabelen `Tal`{.microbitvariables}.


# Steg 2: Teljing {.activity}

No er det på tide å byrje å telje. Når me trykkar på knappen A ynskjer me å auke
verdien i `Tal`{.microbitvariables} med éin. Slik kan me telje oppover kvar gong me trykkar på
knappen.

- [ ] Prøv å lage ei kodeblokk som aukar variabelen `Tal`{.microbitvariables} med __1__ når knapp A
  vert trykt. Koden din bør sjå slik ut:

  ```microbit
  input.onButtonPressed(Button.A, function () {
      Tall += 1
  })
  ```

## {.tip}

`Når knapp A vert trykt`{.microbitinput}-klossen finn du i menyen under `Inndata`{.microbitinput}. `Endre
variabel med 1`{.microbitvariables}-klossen finn du i `Variablar`{.microbitvariables}. Hugs å endre `variabel`{.microbitvariables} til
`Tal`{.microbitvariables}.


# Steg 3: Vis tal {.activity}

Men me ser jo ingenting! Det er fordi me ikkje har bedt programmet om å faktisk
vise oss verdien av `Tal`{.microbitvariables}. Den eksisterer, men er usynleg for oss.

- [ ] For å vise den fram, legg til ein `vis tal`{.microbitbasic}-kloss under klossen `endre Tal med 1`{.microbitvariables}. Erstatt `0`{.microbitbasic} me `Tal`{.microbitvariables}.

- [ ] Viss du vil sjå talet __0__ i starten kan du leggje den til nedst i `ved
  start`{.microbitbasic}-klossen.

## {.tip}

Hugs at du finn `Tal`{.microbitvariables}-klossen i `Variablar`{.microbitvariables}.


# Steg 4: Siste bit {.activity}

- [ ] No skal me gjere noko smart. Høgreklikk på den lilla ramma til `når knapp
  A vert trykt`{.microbitinput} i koden din og vel "Lag kopi" frå menyen som dukkar opp. No får
  du ein kopi av heile den seksjonen med kode. Dette er lurt når ein skal lage
  kode som er heilt lik eller nesten heilt lik den koden ein allereie har laga,
  fordi det går så fort!

- [ ] Endre kopien din slik at koden ser ut som den under. Me har gjort om __A__
  til __B__ og __1__ til __-1__.

```microbit
input.onButtonPressed(Button.B, function () {
    Tall += -1
    basic.showNumber(Tall)
})
```

Å endre `Tal`{.microbitvariables} med __-1__ tyder at verdien av `Tal`{.microbitvariables} minkar med 1 kvar gong me
trykkar på B.

## Test prosjektet {.flag}

- [ ] Test programmet ved å trykkje på knappane A og B i simulatoren. Tel den
  oppover og nedover som den skal?

- [ ] Last ned koden til micro:bit-en viss du er ferdig, og test ut knappane.

## Utfordring {.challenge}

- [ ] La oss lage ein ny måte å nullstille telljaren vår på. Gå til `Inndata`{.microbitinput} og
  finn klossen `når ristast`{.microbitinput}. Legg inn `set Tal til 0`{.microbitvariables}-klossen.

```microbit
input.onGesture(Gesture.Shake, function () {
    Tall = 0
})
```

- [ ] Last ned koden til micro:bit-en. Kva skjer når du ristar micro:bit-en? Kva
  anna enn risting kan du velje i denne klossen?

- [ ] Klarar du å finne fleire måtar å endre `Tal`{.microbitvariables} med i programmet ditt?
  Kanskje skal me auke med __2__ når du heller micro:bit-en mot høgre? Eller skal
  `Tal`{.microbitvariables} setjast til __10__ når både knapp A og B vert trykt inn samstundes? Prøv
  deg fram, og leik med alle moglegheitene!
