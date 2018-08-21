---
title: "PXT: Frustrasjon"
author: "Omsett frå [Code Club UK](https://codeclubprojects.org/en-GB/microbit/frustration/)"
translator: Stein Olav Romslo
language: nn
---


# Introduksjon {.intro}

Dette er eit enkelt koordinasjonsspel som går ut på å leie ein stav med ei løkke
langs ein bøygd ståltråd. Viss spelaren kjem borti ståltråden vil ein buzzar gi
lys, og spelaren får eit poeng. Spelaren med færrast poeng vinn!

Til dette prosjektet treng du nokre ekstra ting:

- Ståltråd

- Krokodilleklyper

- Treklossar med hol til å stikke ståltråden i.

- Buzzar

Basert på: https://codeclubprojects.org/en-GB/microbit/frustration/


# Steg 1: Lagre poeng {.activity}

## Sjekkliste {.check}

- [ ] Start eit nytt PXT-prosjekt, til dømes ved å gå til
  [makecode.microbit.org](https://makecode.microbit.org/?lang=no).

- [ ] Slett dei eksisterande blokkane.

![Bilete av "start"- og "for alltid"-blokker som kastast](slett_standard_blokker.png)

- [ ] Me vil starte eit nytt spel når spelaren trykkar på knapp A. Til det kan
  me bruke `når knapp A blir trykka`-klossen som du finn i kategorien `Inndata`.

  ![Bilete av "når knapp A blir trykka"-klossen](naar_a_trykkes.png)

- [ ] Me må opprette ein *variabel* til å ta vare på kor mange gonger spelaren
  berører ståltråden i løpet av spelet. Me opprettar variabelen `beroering` for
  å gjere det. Hugs at det er lurt å unngå `æøå` fordi det fungerer ikkje alltid
  når me programmerer.

  ![Bilete av korleis lage ein ny variabel](lag_variabel_beroeringer.png)

  ![Bilete av korleis setje variabelnamn](lag_variabel_beroeringer2.png)

  ![Bilete av den ferdige variabelen](variabel_beroeringer.png)

- [ ] Legg til at antal `beroering`ar blir vist etter at `knapp A` er trykka.

  ![Bilete av koden for å vise antal berøringar](vis_tall_beroeringer.png)


# Steg 2: Oppdatere berøringane {.activity}

## Sjekkliste {.check}

- [ ] Du skal leggje til 1 til variabelen `beroering` kvar gong kontakt `P0`
  blir trykka.

  ![Bilete av når kontakt P0 blir trykt](kontakt_p0_trykkes.png)

- [ ] Vidare skal me vise eit kryss for 1 sekund kvar gong kontakt `P1` blir
  trykka.

  ![Bilete av koden for eit kryss når kontakt P1 blir trykka](pin1_bilde.png)

  ![Bilete av Musikk-kategorien og "spill av tone"-klossen](pin1_musikk.png)

  ![Bilete av koden for kryss og tone sett saman](pin1_pause.png)

- [ ] Så må du endre verdien til `beroering` med 1.

  ![Bilete av koden med beroering endra med 1](endre_beroeringer.png)

- [ ] Så må me vise kor mange gonger me har vore borti ståltråden.

  ![Bilete av koden for å vise antal berøringar](vis_beroeringer.png)


# Steg 3: Bygg spelet {.activity}

## Sjekkliste {.check}

- [ ] Ta ein bit ståltråd og lag ei løkke i den eine enden.

- [ ] Tre løkka i ein annan bit ståltråd som du set i to treklossar med hol i.

- [ ] Fest ein kabel med krokodilleklyper i `P0` på micro:biten til det eine
  beinet på `buzzaren` og ein annan kabel frå `GND` på micro:biten til det andre
  beinet på `buzzaren`. *Det har ikkje noko å seie kva bein på buzzaren som blir
  kopla til kva kabel på buzzaren*

![Bilete av to krokodilleklemmer og ein buzzar](buzzer.png)

- [ ] Fest ein kabel med krokodilleklyper til `P1` på micro:biten og til
  ståltråden med løkka. Fest ein kabel til ståltråden som er festa til
  treklossane og til `GND` på micro:biten.

![Bilete av ein buzzwire](buzzwire.png)

![Bilete av ein micro:bit med klemmer på 1, 2 og 2 på GND](microbit.png)

## Utfordring: Leggje til eigne melodiar {.challenge}

- [ ] Klarar du å endre spelet slik at ein startar med tre liv, og mistar eitt
  for kvar gong ein kjem borti ståltråden? __Tips:__ Du kan bruke klossen `game
  over` i kategorien `Spill` for å vise ein "Game over"-animasjon når spelaren
  mistar det siste livet.
