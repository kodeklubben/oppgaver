---
title: 'PXT: Frustrasjon'
level: 2
author: dagfs
language: nb
---

# Introduksjon {.intro}

Dette er et enkelt kordinasjonspill som går ut på å lede en stav med en løkke langs en bøyd ståltråd. Hvis spilleren kommer borti ståltråden vil en buzzer gi lyd og såilleren får et poeng. Spilleren med færrest poeng vinner!

Til dette prosjektet trengs det et par ekstra ting:

- Ståltråd
- Krokkodilleklyper
- Treklosser med hull til å stikke ståltråden i.
- Buzzer

Basert på: https://codeclubprojects.org/en-GB/microbit/frustration/

# Steg 1: Lagre poeng {.activity}

## Sjekkliste {.check}

- [ ] Start et nytt PXT-prosjekt, for eksempel ved å gå til
  [makecode.microbit.org](https://makecode.microbit.org/?lang=no).

- [ ] Slett de eksisterende blokkende.

 ![Bilde av start og for alltid blokker som kastes](slett_standard_blokker.png)

- [ ] Vi ønsker å starte et nytt spill når spilleren trykker på knapp A. Til dette kan vi bruke `når knapp A trykkes`-klossen som finnes i kategorien `Inndata`.

 ![](naar_a_trykkes.png)


  - [ ] Vi må opprette en `variabel` til å ta vare på hvor mange ganger spilleren berører ståltråden i løpet av spillet. Vi oppretter variabelen `beroering` til dette. Husk det er lurt å unngå `æøå` fordi det fungerer ikke i alle tilfeller.

   ![](lag_variabel_beroeringer.png)

   ![](lag_variabel_beroeringer2.png)

   ![](variabel_beroeringer.png)



   - [ ] Legg til at antall `beroeringer` vises etter at `knapp a` er trykket.

  ![](vis_tall_beroeringer.png)  

# Steg 2: Oppdatere berøringene {.activity}

## Sjekkliste {.check}

- [ ] Du skal legge til 1 til variabelen `beroeringer` hver gang kontakt `P0` trykkes.

	![](kontakt_p0_trykkes.png)

- [ ] Videre skal vi vise et kryss for 1 sekund hver gang kontakt `P1` trykkes.

  ![](pin1_bilde.png)

  ![](pin1_musikk.png)

  ![](pin1_pause.png)

- [ ] Så må du endre verdien til `beroeringer` med 1.

![](endre_beroeringer.png)

- [ ] Så må vi vise hvor mange ganger  vi har berørt.

![](vis_beroeringer.png)


# Steg 3: Bygg spillet {.activity}


## Sjekkliste {.check}

- [ ] Ta en bit ståltråd og lag en løkke i den ene enden.

- [ ] Tre løkken i en annen bit ståltråd som du setter i to treklosser med hull i.

- [ ] Fest en kabel med ktrokkodilleklyper i `P0` på Microbiten til det ene beinet på `buzzeren` og en annen kabel fra `GND` på Microbiten til det andre beinet på `buzzeren`. *Det har ikke noe å si hvilket bein på buzzeren som kobles til hvilken kabel på buzzeren*

![](buzzer.png)

- [ ] Fest en kabel med krokkodilleklyper til `P1` på Microbiten og til ståltråden med løkke. Fest en kabel til ståltråden som er festet til treklossene og til `GND` på Microbiten.

![](buzzwire.png)

![](microbit.png)

## Utfordring : Legge til egne melodier {.challenge}

- [ ] Klarer du å endre spillet slik at en starter med 3 liv og for hver gang en kommer borte i ståltråden reduseres liv med 1?
Tips: Det er mulig å bruke blokken `game over` i kategorien `Spill` for å vise en Game over annimasjon når spilleren mister det siste livet.
