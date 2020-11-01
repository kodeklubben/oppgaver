---
title: "PXT: Fjernstyr en venn"
author: Julie Christina Revdahl
language: nb
---


# Introduksjon {.intro}

I denne oppgaven skal vi sette opp radiokommunikasjon mellom to micro:biter slik
at vi kan sende instruksjoner for å navigere en venn i blinde.

*Obs: Følg med på overskriftene. Du skal gjennomføre steg for enten sender eller
mottaker.*


# Sender og mottaker: oppsett {.activity}
*I denne delen av oppgaven, skal vi sette opp senderen slik at den kan kommunisere
med en annen micro:bit.*

## Sjekkliste {.check}

- [ ] Start et nytt PXT-prosjekt, for eksempel ved å gå til
  [makecode.microbit.org](https://makecode.microbit.org/?lang=no){target=blank}.

- [ ] Micro:bitene skal sende beskjeder til hverandre med mikrobølger. Alle micro:biter
som tilhører samme radiogruppe, bruker samme frekvens, og kan derfor kommunisere
med hverandre. Klossen `radio sett gruppe 1`{.microbitradio} finnes under kategorien
`Radio`{.microbitradio}. For å ikke kommunisere med nabogruppa, erstatt `1`{.microbitradio}
med et tall dere tror er ledig. Pass på at dere er i samme radiogruppe.


# Sender {.activity}

*Vi skal nå lage en kode som lar senderen sende et tall for å representere
pilretningen mottakeren skal gå i.*

## Sjekkliste {.check}

- [ ] Pilnummeret du skal sende refererer til en av fire piler: 0 = opp (Nord),
2 = høyre (Øst), 4 = ned (Sør) eller 6 = venstre (Vest). Lag en kode som bestemmer
hvilken av disse du skal sende. Du kan selv velge hvordan du vil gjøre dette,
men her er noen forslag:
  - Bruk innebygd funksjon for helning av micro:bit til å bestemme hvilken pil
  som skal sendes.
  - Bruk målt akselerasjon i x-og y-retning til å avgjøre retningen (høyre: x>0,
    venstre: x<0, opp: y<0, ned: y>0) .
  - La trykk på kontaktene P0, P1 og P2 representere pilene venstre, høyre og opp,
  mens knapp A representerer pil ned.
  - Når du trykker på A vises neste pil.

- [ ] Lag kode som sender pilnummeret til mottakeren. Dersom du lagret dette i
en variabel kalt `pilnummer`{.microbitvariables} kan koden din se slik ut:

```microbit
input.onButtonPressed(Button.B, function () {
    let pilnummer = 0
    radio.sendNumber(pilnummer)
})
```
*Her har vi ikke brukt knapp B til noe annet*

- [ ] Noen ganger mottar ikke mottakeren beskjeden som sendes. Dette kan skyldes
at man for eksempel har stått for langt unna hverandre. For å unngå misforståelser
kan mottakeren sende en bekreftelse tilbake til senderen, for å fortelle at han
eller hun har mottatt beskjeden.

- [ ] Lag et enkelt bilde eller lignende som vises en kort stund etter du har
mottatt bekreftelse. Til det kan du bruke denne klossen:

```microbit
radio.onReceivedNumber(function (receivedNumber) {
})
```
*I variabelen receivedNumber (på norsk:mottatt tall) lagres teksten du mottar.
For vår del er ikke dette viktig. Vi kan motta hva som helst som bekreftelse.*

- [ ] Nå er senderens del av koden ferdig og klar til å lastes ned!

# Mottaker {.activity}

*Denne delen av koden er for den som skal lage mottakeren. Vi skal nå sette opp
micro:biten slik at tallet vi mottar blir til en pil på skjermen vår.*

## Sjekkliste {.check}

- [ ] Senderen skal sende deg et pilnummer. Når du mottar dette tallet, lagres
det i en variabel. Bruk `når radio mottar`{.microbitradio}-klossen fra `Radio`{.microbitradio}-
kategorien, og opprett en variabel du vil lagre tallet i. Det automatiske navnet
er `receivedNumber`{.microbitvariables}, men lag gjerne ditt eget navn, for
eksempel `pilnummer`{.microbitvariables}.

- [ ] Pilnummeret du mottar refererer til en av fire piler: 0 = opp (Nord),
2 = høyre (Øst), 4 = ned (Sør) eller 6 = venstre (Vest). Den enkleste måten å
vise pilen på, er å sette pilnummeret inn i en `vis pil`{.microbitbasic}-kloss.
Du kan også lage en kode-blokk med `hvis`{.microbitlogic}-klosser.

- [ ] Noen ganger mottar man ikke alle beskjeder som blir sendt, for eksempel
fordi man har stått for langt unna hverandre. For å unngå misforståelser bør du
sende en bekreftelse tilbake til senderen om at du har mottat et `pilnummer`{.microbitvariables}.
Legg til en kodesnutt som sender en tekst tilbake.

- [ ] Du vil med stor sannsynlighet motta flere like piler etter hverandre.
Oppdater koden din slik at du tydelig ser når du har mottatt en ny pil. Dette
kan du gjøre på flere ulike måter, så her er noen forslag:
  - Tøm skjermen, og vent et halvt sekund før du viser den nye pila.
  - Vis noe annet bilde på skjermen mellom hver pil.
  - Få microbiten til å lage en lyd når du mottar en ny pil. *Til dette trenger du
  2 ledninger og 1 buzzer. Koble GND til - på buzzeren og kontakt 0 til + på buzzeren.*

- [ ] Nå er mottakerens del av koden ferdig og klar til å lastes ned!



# Sender og mottaker: Testing {.activity}

- [ ] Dersom samarbeidspartneren din også er ferdig med koden sin, er det nå
på tide å teste koden.

- [ ] Last ned hver deres kode til hver deres micro:bit. Mottar dere pilene som
blir sendt?

- [ ] Når dere er fornøyd med at programmet fungerer, kan mottakeren ta et pledd
eller en jakke over hode slik at han eller hun kun ser micro:biten. Senderen skal
nå gi mottakeren beskjed om hvor han skal gå kun ved å sende piler.

- [ ] Bytt på slik at begge får prøvd å styre ved å sende piler til den andre.
