---
title: "PXT: Send ein hemmeleg beskjed"
author: Helene Isnes
translator: Stein Olav Romslo
language: nn
---


# Introduksjon {.intro}

I denne oppgåva skal du sende og motta hemmelege beskjedar til/frå ein annan
micro:bit ved å bruke radiosignal. Du treng nokon å utveksle hemmelege beskjedar
med! Finn nokon som har lyst å gjere denne oppgåva saman med deg.


# Steg 1: Set opp ei radiogruppe {.activity}

## Sjekkliste {.check}

- [ ] Finn ein `ved start`-kloss (den ligg allereie i kodefeltet, elles finn du
  den nedst i `Basis`).

- [ ] Gå til `Radio` og klikk på `radio sett gruppe`-klossen.

- [ ] Vel eit gruppenummer mellom `0` og `255` som de trur ingen andre her. Alle
  micro:bit-ar i same gruppe kan kommunisere, og du vil ikkje at nokon andre
  skal høyre den hemmelege beskjeden!

![Bilete som viser `radio sett gruppe til 42`-kloss inni `ved start`-klossen](radiogruppe.png)


# Steg 2: Send ein hemmeleg beskjed {.activity}

## Sjekkliste {.check}

- [ ] Gå til `Inndata` og finn klossen `når knapp A vert trykt`. Me brukar denne
  fordi me vil sende den hemmelege beskjeden når me trykkar på A.

- [ ] Finn klossen `radio send tekst` i `Radio`. Legg den inni `når knapp A vert
  trykt` og skriv inn den hemmelege beskjeden du vil sende.

![Bilete som viser at når A vert trykt så skal radio sende teksten "Hemmelig beskjed"](hemmelig_beskjed.png)

### OBS! {.protip}

Micro:bit-en klarar ikkje å vise Æ, Ø eller Å. Bruk heller AE, OE og AA.

Beskjeden burde heller ikke vere for lang sidan micro:bit-en berre klarar å
sende nokre få ord kvar gong.


# Steg 3: Lag sendar og mottakar {.activity}

No er du klar til å sende hemmelege beskjedar. Men fyrst må me skrive kode slik
at dei hemmelege beskjedane kan bli motteke og lese.

- [ ] Gå til `Radio` att og finn `når radio mottek recievedString`-klossen:

![Bilete som viser `når radio mottar recievedString`-klossen](naar_radio_mottar.png)

"RecievedString" tyder "Motteke tekst" på norsk, og beskjeden som blir motteke
blir lagra i klossen som heiter dette.

- [ ] Legg til ein `vis tekst`-kloss (frå `Basis`) og `recievedString`-kloss
  (frå `Variablar`). Legg dei slik at koden din for å motta beskjedar ser slik
  ut:

![Bilete som viser `vis tekst recievedString`-klossen inni `når radio mottar recievedString`-klossen](vis_mottat_beskjed.png)

## Test prosjektet {.flag}

No er me klare til å både sende og motta beskjedar!

- [ ] Last ned koden til micro:bit-en og send dei hemmelege beskjedane til
  kvarandre ved å trykke på A.

## {.tip}

For å laste ned koden må du fyrst ha kopla micro:bit-en til datamaskina med ein
USB-kabel. Klikk på knappen `Last ned` nede til venstre på skjermen. No blir det
lasta ned ei fil som heiter `microbit-Uten-navn.hex` til datamaskina di.
Samstundes dukkar det opp eit vindauge som seier at du må flytte denne fila til
MICROBIT-disken på datamaskina di.


# Ekstra testing {.activity}

Det er mogleg å justere styrken på sendaren til micro:bit-en ved å bruke klossen
`radio sett sendareffekt` som du finn viss du trykkar på `Radio` og så `more`
(meir) rett under. Den høgste styrken sendaren kan ha er 7. Prøv fleire ulike
styrkar når du går gjennom punkta under.

## Sjekkliste {.check}

- [ ] Test kor langt unna kvarandre de kan stå og framleis klare å motta
  beskjedar.

- [ ] Klarar de å sende beskjedar gjennom eit pledd?

- [ ] Kva med veggar?
