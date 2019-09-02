---
title: "PXT: Micro:bit repeater"
author: Julie Christina Revdahl
language: nb
---


# Introduksjon {.intro}

En micro:bit kan sende en melding fra én micro:bit til en annen, men ikke over
store avstander. Nå skal vi lage et program som tar i mot en beskjed via radioen
og sender den videre til en annen, slik at vi kan sende en melding enda lengre.


# Steg 1: Oppsett av radio {.activity}

## Sjekkliste {.check}

- [ ] Start et nytt PXT-prosjekt, for eksempel ved å gå til
  [makecode.microbit.org](https://makecode.microbit.org/?lang=no){target=blank}.

- [ ] Micro:biter som tilhører samme radiogruppe, bruker samme frekvens og kan
derfor kommunisere med hverandre. Vi må derfor sette opp radioen vår til en
radiogruppe.

- [ ] Opprett en variabel som skal inneholde radiogruppe-tallet. Da kan vi enklere
endre det senere.

- [ ] Sett variabelen du lagde til en verdi. Det kan være hvilket som helst tall
mellom 0 og 255.

- [ ] Bruk deretter klossen `radio sett gruppe`{.microbitradio} fra kategorien
`Radio`{.microbitradio} til å sette radiogruppe-tallet. Husk at du lagret dette
i variabelen du akkurat opprettet.

- [ ] Legg inn en `vis tall`{.microbitbasic}-kloss slik at tallet vises på skjermen ved oppstart.

- [ ] Nå ligner nok koden din på dette:
```microbit
  let radiogruppe = 5
  radio.setGroup(radiogruppe)
  basic.showNumber(radiogruppe)
```


# Steg 2: Vise hvilken radiogruppe vi er innstilt på {.activity}

## Sjekkliste {.check}

- [ ] Lag en kode slik at `når knapp A trykkes`{.microbitinput}, vises radiogruppen
på skjermen til micro:biten.


# Steg 3: Endre radiogruppe {.activity}

For å slippe å lage egen kode til hver enkelt micro:bit, lager vi en kode som
gjør at vi kan endre radiogruppen vi er på når begge knappene trykkes.

## Sjekkliste {.check}

- [ ] Lag en kode som endrer radiogruppen `når knapp A+B trykkes`{.microbitinput}.

- [ ] Vis deretter på skjermen hvilken radiogruppe vi er på.

- [ ] Koden for endring av radiogruppe ser nå slik ut:
```microbit
  input.onButtonPressed(Button.AB, function () {
      radiogruppe += 1
      basic.showNumber(radiogruppe)
      })
```


# Steg 4: Når vi mottar meldinger {.activity}

## Sjekkliste {.check}

- [ ] Bruk klossen `når radio mottar`{.microbitradio} til å lage en kode som
viser den mottatte meldingen på skjermen.

- [ ] I variabelen `receivedString`{.microbitvariables} lagres beskjeden du
mottok, det er denne du vil vise på skjermen.


# Steg 5: Sende videre på en annen radiogruppe {.activity}

## Sjekkliste {.check}

- [ ] Etter å motta en melding, skal vi sende den videre på en kanal høyere
enn den vi selv lytter på.

- [ ] Inne i `når radio mottar`{.microbitradio}-klossen må vi først endre
radiogruppen med 1, sette den nye radiogruppen og sende teksten vi mottok videre
før vi går tilbake til kanalen vi opprinnelig var på. *En annen micro:bit lytter
på kanalen vi hopper opp til slik at denne personen kan sende meldingen videre
igjen.* Se om du finner de riktige klossene og bygg koden på egenhånd!

- [ ] Når bør koden din ligne på dette:
```microbit
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
    basic.pause(1000)
    radiogruppe += 1
    radio.setGroup(radiogruppe)
    radio.sendString(receivedString)
    radiogruppe += -1
    radio.setGroup(radiogruppe)
})
```


# Sender {.activity}

*Nå lager vi startkoden som en av micro:bitene må sende. Én micro:bit laster
derfor kun ned denne koden.*

## Sjekkliste {.check}

- [ ] Én micro:bit må sende beskjeden som skal videresendes. Bruk en `ved start`{.microbitbasic}-kloss
til  sette radiogruppen til en verdi. Pass på at den neste micro:biten du sender
til er innstilt på samme radiogruppe.

- [ ] Lag en kodesnutt som sender en tekst `når knapp A trykkes`{.microbitinput}.

- [ ] Lag en kodesnutt som sender en tekst `når knapp B trykkes`{.microbitinput}.

## Test prosjektet {.flag}


- [ ] Nå kan du teste programmet ditt. Last ned startkoden på én micro:bit, og
den andre koden på de andre micro:bitene dere bruker.

- [ ] Bruk A+B-knappene til å stille inn slik at radiogruppene blir riktige. *Husk
at koden endrer opp én radiogruppe før den videresender meldingen. Med andre ord:
Dersom den første micro:biten sender på radiogruppe 5, må den neste være innstilt
på radiogruppe 5. Denne vil sende videre på radiogruppe 6, så den tredje micro:biten
som skal motta må være innstilt på gruppe 6 osv.*

- [ ] Hvor langt greier dere å sende en melding uten at det stopper opp?
