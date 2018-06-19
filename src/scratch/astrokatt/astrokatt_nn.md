---
title: Astrokatt
level: 1
author: 'Geir Arne Hjelle'
translator: 'Gro Anette Vestre'
language: nn
---

# Introduksjon {.intro}

Katten vår har så lyst å vera ein astronaut, la oss sjå om me kan hjelpa han? Undervegs vil me læra korleis me flyttar figurar rundt på skjermen, og korleis kattar blir påvirka av gravitasjonskreftene frå jorda.

![](astrokatt.png)

# Steg 1: Ein flygande katt {.activity}

Me begynner prosjektet vårt med å få katten til å fly!

## Sjekkliste {.check}

- [ ] Start eit nytt prosjekt. Du vil sjå ein katt som ventar på å bli programmert!

- [ ] Prøv å klikk på dei blå klossane midt på skjermen. For eksempel, om du klikkar på

    ```blocks
        gå (10) steg
    ```

    skal du sjå at katten flyttar litt på seg, og om du klikkar på

    ```blocks
        vend høyre (15) grader
    ```

    vil den snu seg! Desse klossane er kommandoer me kan gi til katten!

- [ ] Legg merke til at over dei blå klossane er det fleire kategoriar av  kommandoar i forskjellige fargar, for eksempel `Utseende`{.blocklooks} og `Lyd`{.blocksound}. Klikk på desse kategoriane og prøv nokre av klossane du finn!

- [ ] For å setje saman fleire kommandoar til eit skript kan du dra klossar til det store tomme området til høgre på skjermen.

    Prøv å pusla saman desse klossane (bruk fargane for å finne rett kategori):

    ```blocks
        når grønt flagg klikkes
        for alltid
            gå (10) steg
            vend høyre (15) grader
        slutt
    ```

## Test prosjektet {.flag}

Legg merke til at den første klossen seier at noko skal skje når me klikkar på eit grønt flag. Over vindauga med katten til venstre er det eit grønt flag. __Klikk på det!__

- [ ] Du skal sjå at katten flyttar seg rundt i ein sirkel. Les koden du laga ein gong til. Forstår du kvifor katten går i sirkel?

- [ ] Prøv å endra tala i koden din. Kan du få katten til å gå saktere? I større sirkler?

## Sjekkliste {.check}

- [ ] Nå skal me endra litt på koden slik at me kan kontrollera korleis katten bevegar seg. I kategorien `Sansning`{.blocksensing} fins ein kloss som reagerar når ein tast er trykka på. Den kan me bruka til å styra katten med piltastene.

    Bytt ut klossene i koden din slik at den blir sjåande slik ut:

    ```blocks
        når grønt flagg klikkes
        for alltid
            hvis (tast [pil høyre v] trykket?)
                vend høyre (5) grader
            slutt
            hvis (tast [pil venstre v] trykket?)
                vend venstre (5) grader
            slutt
            hvis (tast [pil opp v] trykket?)
                gå (5) steg
            slutt
        slutt
    ```

## Test prosjektet {.flag}

__Klikk på det grøne flaget.__

- [ ] Kan du styra katten rundt ved å bruke piltastane?

- [ ] Forstår du korleis katten vert kontrollert?

- [ ] Kan du få katten til å fly raskare eller saktare ved å endre i koden?

# Steg 2: Ut i verdsrommet! {.activity}

Nå skal me senda den flygande katten ut i verdsrommet.

## Sjekkliste {.check}

- [ ] Klikk på ![Velg ny bakgrunn](../bilder/velg-bakgrunn.png) nedst til venstre på skjermen for å henta inn ein ny bakgrunn. Vel bakgrunnen `stars` som du finn i kategorien `Romfart`.

- [ ] Me skal og gi katten ein liten oksygentank, sidan den flyr rundt ute i rommet. Klikk på katten i figurvinduet og deretter på fana `Drakter` øvst på skjermen.

- [ ] Vel først ein litt lys farge. Klikk deretter på Ellipse-verktøyet til høgre på skjermen, og teikn ein ellipse rundt hovudet på katten.

    ![](katt_oksygentank.png)

Til slutt lagar me og ein jordklode, som katten kan fly rundt.

- [ ] Klikk på fana `Skript` og deretter på
  ![Velg figur fra biblioteket](../bilder/hent-fra-bibliotek.png). Vel jordklodefiguren `Romfart/Earth`. Plasser denne litt på sida av skjermen.

## Test prosjektet {.flag}

__Klikk på det grøne flaget.__

- [ ] Flyr katten rundt omkring i verdsrommet?

# Steg 3: Litt meir ekte ... {.activity}

Me skal nå legge på nokre effektar som gjer at spelet virkar litt meir realistisk.

## Sjekkliste {.check}

- [ ] Først kan me få jordkloden til å rotera. Dette er enkelt, me har jo allereie gjort det for katten! Pass på at jordkloden er merka i figurlista, og lag deretter dette skriptet:

    ```blocks
        når grønt flagg klikkes
        for alltid
            vend høyre (1) grader
        slutt
    ```

- [ ] Vidare skal me gjera det slik at det ser ut som om katten flyr mot jorda. Det gjør me ved å endra størrelsen slik at katten blir mindre jo nærmere den kjem jordkloden.

    Klikk på katten i figurlista. Legg `sett størrelse til`{.blocklooks} nederst i `for alltid`{.blockcontrol}-løkka, slik at størrelsen på katten er avhengig av avstanden til jordkloden:

    ```blocks
        når grønt flagg klikkes
        for alltid
            hvis (tast [pil høyre v] trykket?)
                vend høyre (5) grader
            slutt
            hvis (tast [pil venstre v] trykket?)
                vend venstre (5) grader
            slutt
            hvis (tast [pil opp v] trykket?)
                gå (5) steg
            slutt
            sett størrelse til (avstand til [Earth v])%
        slutt
    ```

## Test prosjektet {.flag}

__Klikk på det grøne flaget.__

- [ ] Blir katten mindre når den nærmar seg jorda?

- [ ] Ser det ut som om den flyr ned mot jorda, og kjem tilbake til oss?

## Sjekkliste {.check}

- [ ] For å gjera det enda meir realistisk vil me forandra kor langt katten flyttar seg med. Når den er langt unna oss flyttar den seg ikkje like mange steg. Byt ut

    ```blocks
        gå (5) steg
    ```

    med

    ```blocks
        gå ((avstand til [Earth v]) / (50)) steg
    ```

    Denne klossen er litt komplisert fordi den er satt saman av tre forskjellige klossar. Sjå på fargane så finn du dei rette klossane.

- [ ] Av og til vil katten fly bak jordkloden. For å sleppe det kan du legge klossen `legg øverst`{.blocklooks} først i katten sitt skript.

## Test prosjektet {.flag}

__Klikk på det grøne flaget.__

- [ ] Flyr katten rundt omkring i verdsrommet? Kan du få den til å lande på jorda?

- [ ] Prøv også å flytte jordkloden til andre stader på skjermen. Blir det annleis å fly med katten nå?

# Steg 4: Gravitasjon {.activity}

Gravitasjon er krafta som jorda trekker på alle katter og mennesker med. Me kan la astrokatten vår bli påverka av gravitasjonen og.

## Sjekkliste {.check}

- [ ] Lag eit nytt skript på katten. Du kan berre legge klossane ved sida av det skriptet du allereie har laga. Skriptet skal sjå slik ut:

    ```blocks
        når grønt flagg klikkes
        gå til x: (-200) y: (150)
        for alltid
            pek mot [Earth v]
            gå (1) steg
        slutt
    ```

- [ ] Når du testar programmet ditt ved å klikke på det grøne flaget, vil du sjå at katten svevar mot jordkloden. Gravitasjonen trekker på den!

- [ ] MEN, me har eit problem: Me kan ikkje lengre styra katten! Kva har skjedd?

    I det nye skriptet seier me at katten `for alltid`{.blockcontrol} skal `peke mot`{.blockmotion} jordkloden. Då hjelper det jo ikkje at me i det andre skriptet seier at katten skal snu seg.

- [ ] Det er ingen kommando i Scratch for å flytta ein figur mot ein annan. Derfor må me peika katten mot jordkloden og deretter flytta den. Men me kan få programmet til å virka igjen, om me berre hugsar kva retning katten peikte før me snudde den.

    For at programmer skal hugsa ting bruker me variablar. Lag ein
 variabel ved å klikke på `Data`{.blockdata}-kategorien og deretter på `Lag en variabel`. Kall variabelen `katteretning`.

- [ ] Me kan nå bruke denne variabelen til å hugsa kva retning katten peikte. Endra skriptet ditt ved å legge til to nye klossar:

    ```blocks
        når grønt flagg klikkes
        gå til x: (-200) y: (150)
        for alltid
            sett [katteretning v] til (retning)
            pek mot [Earth v]
            gå (1) steg
            pek i retning (katteretning)
        slutt
    ```

## Test prosjektet {.flag}

__Klikk på det grøne flaget.__

- [ ] Kan du styra katten igjen?

- [ ] Dersom du ikkje trykker på nokon tastar, vil katten då falle ned mot jorda?

- [ ] Legg merke til at dersom katten har kome veldig nær jorda klarar den ikkje å fly tilbake til oss. Det er fordi gravitasjonen er kraftigare jo nærare jorda ein er. Og når katten kjem nær jorda har den ikkje nok hastighet til å unnsleppe jordas gravitasjon.

    Korleis kan du endra på jordas gravitasjon og kattens hastighet?

## Lagre spillet {.save}

Då har me ein katt som kan fly rundt i verdsrommet. Eksperimenter gjerne med å utvide spelet ditt. Når du er ferdig kan du klikke på `Legg ut`-knappen. Då vil spelet bli lagt ut på Scratch-heimesida din slik at andre kan spele det.
