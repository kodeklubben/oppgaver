---
title: 'Felix og Herbert'
level: 1
logo: ../../assets/img/ccuk_logo.png
author: 'Oversatt fra [Code Club UK](//codeclub.org.uk)'
translator: 'Gro Anette Vestre'
language: nn
license: '[Code Club World Limited Terms of Service](https://github.com/CodeClub/scratch-curriculum/blob/master/LICENSE.md)'
---

# Introduksjon {.intro}

Me skal laga eit spel der katten __Felix__ skal fanga musa __Herbert__. Du styrer Herbert med musepeikaren og skal prøva å unngå å bli tatt av Felix. Jo lenger du unngår han jo fleire poeng får du, men blir du tatt, går poengsummen din ned.

![](felix_og_herbert.png)

# Steg 1: Felix føl musepeikaren {.activity}

*Me ynskjer at katten Felix skal følge etter musepeikaren.*

## Sjekkliste {.check}

- [ ] Start eit nytt prosjekt.

- [ ] Trykk på `i`{.blockmotion} i hjørna av ![Sprite1](sprite1.png) og byt navn på figuren til `Felix`.

- [ ] Sørg for at Felix kun ser til høgre og venstre ved å setje
  rotasjonsmåte til ![Høyre/Venstre](../bilder/rotasjonsmate-hv.png).

- [ ] Klikk på scenen ved sida av Felix i vinduet for figurar. Vel fana `Bakgrunnar`{.blocklightgrey} og trykk på ![Vel ein ferdig bakgrunn](../bilder/velg-bakgrunn.png) for å importera ein ferdig bakgrunn. Vel den bakgrunnen du vil.

- [ ] Klikk på Felix, vel `Skript`{.blocklightgrey}-fana og lag dette skriptet:

    ```blocks
        Når grønt flagg klikkes
        for alltid
            pek mot [musepeker v]
            gå (10) steg
            neste drakt
            trommeslag (3 v) som varer (0.25) takter
        slutt
    ```

## Test prosjektet {.flag}

__Klikk på det grøne flaget.__

- [ ] Føl Felix musepeikaren?

- [ ] Ser det ut som han går når han bevegar seg?

- [ ] Bevegar han seg med rett hastighet?

- [ ] Klikk det raude stopp-symbolet for at Felix skal slutta å følgje etter musepeikaren.

## Lagre prosjektet {.save}

Scratch lagrar alle prosjekta dine automatisk med jevne mellomrom. Det kan allikevel vera lurt å lagra manuelt innimellom.

- [ ] I filmenyen, vel `Lagre nå`.

# Steg 2: Felix jagar Herbert {.activity}

*Nå ynskjer me at Felix skal jaga musa Herbert istadenfor musepeikaren.*

## Sjekkliste {.check}

- [ ] Lag ein ny figur ved å trykke på ![Vel figur frå biblioteket](../bilder/hent-fra-bibliotek.png) og vel figuren `Dyr/Mouse1`.

- [ ] Byt namn på figuren til `Herbert`.

- [ ] Gjer Herbert mindre enn Felix ved å trykke på ![krymp](../bilder/krymp.png) (øvst mot midten av vindauga). Prøv seks klikk.

- [ ] Gje Herbert dette skriptet:

    ```blocks
        Når grønt flagg klikkes
        for alltid
            gå til [musepeker v]
            pek mot [Felix v]
        slutt
    ```

## Test prosjektet {.flag}

__Klikk på det grøne flaget.__

- [ ] Flyttar Herbert seg med musepeikaren?

- [ ] Jagar Felix Herbert?

# Steg 3: Felix seier når han har fanga Herbert {.activity}

*Me vil at Felix skal veta når han har fanga Herbert og fortelje det til oss.*

## Sjekkliste {.check}

- [ ] Endre skriptet til Felix til dette:

    ```blocks
        Når grønt flagg klikkes
        for alltid
            pek mot [musepeker v]
            gå (10) steg
            neste drakt
            trommeslag (3 v) som varer (0.25) takter
            hvis (berører [Herbert v]?)
                si [Tok deg!] i (1) sekunder
            slutt
        slutt
    ```

## Test prosjektet {.flag}

__Klikk på det grøne flaget.__

- [ ] Seier Felix frå når han har fanga Herbert?

# Steg 4: Herbert blir eit spøkelse når han vert fanga {.activity}

*I tillegg til at Felix seier noko, vil me nå at Herbert blir forvandla til eit spøkelse når han vert fanga.*

## Sjekkliste {.check}

- [ ] Endra skriptet til Felix slik at det sender ein melding og lagar ein lyd når han fangar Herbert:

    ```blocks
        Når grønt flagg klikkes
        for alltid
            pek mot [musepeker v]
            gå (10) steg
            neste drakt
            trommeslag (3 v) som varer (0.25) takter
            hvis (berører [Herbert v]?)
                send melding [Fanget!]
                trommeslag (1 v) som varer (0.25) takter
                si [Tok deg!] i (1) sekunder
                vent (1) sekunder
            slutt
        slutt
    ```

- [ ] Vel Herbert og gå til `Drakter`{.blocklightgrey}-fana.

- [ ] Hent ein ny drakt ved å trykke på ![Vel drakt frå biblioteket](../bilder/hent-fra-bibliotek.png) og vel `Fantasi/ghost2-a`

- [ ] Gjer drakta mindre ved å velgje ![Krymp](../bilder/krymp.png) og trykke seks gonger på spøkelsesdrakta.

- [ ] Endra namna på Herberts draktar slik at musedrakten heiter `levande` og spøkelsesdrakten heiter `død`.

- [ ] Gå til `Skript`{.blocklightgrey}-fana, og lag eit nytt skript for Herbert for å gjera han om til eit spøkelse. Ikkje slett det gamle skriptet:

    ```blocks
        når jeg mottar [Fanget! v]
        bytt drakt til [død v]
        vent (0.5) sekunder
        bytt drakt til [levende v]
    ```

## Test prosjektet {.flag}

__Klikk på det grøne flaget.__

- [ ] Forvandlas Herbert til eit spøkelse når han vert fanga?

- [ ] Spelar Felix dei rette lydane til rett tid?

- [ ] Står Felix stille lenge nok til at Herbert kjem seg unna?

# Steg 5: Telje poeng {.activity}

*La oss legge til ein poengsum slik at me kan sjå kor flink ein er til å halde Herbert i live. Me startar med poengsummen null og auker den med ein for kvart sekund. Hvis Felix fangar Herbert, minker me poengsummen med ti.*

## Sjekkliste {.check}

- [ ] På `Skript`{.blocklightgrey}-fana under kategorien `Data`{.blockdata}, lag ein ny variabel. Kall variabelen for `Poeng`{.blockdata}, og la den gjelde for alle figurar.

    ![](ny-variabel-poeng.png)

    Legg merke til at variabelen `Poeng `{.blockdata} dukka opp øvst til venstre i spelet ditt.

- [ ] Klikk på `Scene` til venstre på skjermen, ved sida av `Figurer`. Lag disse to skripta på scenen:

    ```blocks
        Når grønt flagg klikkes
        sett [Poeng v] til (0)
        for alltid
            vent (1) sekunder
            endre [Poeng v] med (1)

        når jeg mottar [Fanget! v]
        endre [Poeng v] med (-10)
    ```

## Test prosjektet {.flag}

__Klikk på det grøne flaget.__

- [ ] Aukar poengsummen med ein kvart sekund?

- [ ] Går poengsummen ned med ti når Herbert vert fanga?

- [ ] Kva skjer dersom Herbert vert fanga før du har ti poeng?

- [ ] Går poengsummen tilbake til null når du starter spelet på nytt?

## Lagre prosjektet {.save}
*Du er ferdig. Godt gjort. Nå kan du spele spelet!*

Du kan dele spelet med familie og venner ved å trykke `Legg ut` på menylinjen.
