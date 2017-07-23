---
title: 3D-Flakser, Del 1
level: 4
author: Gudbrand Tandberg og Geir Arne Hjelle
translator: Gro Anette Vestre
language: nn
tags:
    topic: [block_based, game, animation]
    subject: [arts_and_crafts, mathematics, science]
    grade: [secondary, junior]
---

# Introduksjon {.intro}

I dette prosjektet skal me laga ein versjon av Flaksefugl (som er ein kopi av Flappy Bird) i *tre dimensjonar*! Spelet går ut på at du styrer ein flygande figur gjennom ringar som kjem mot deg. Du må styra figuren opp og ned og side til side. Hovedutfordringen i dette spelet er å få det til å virka som om ringane faktisk kjem mot flaksaren, og så forsvinn forbi. Prosjektet er delt inn i to deler sidan det er ganske mykje me skal igjennom. I denne første delen skal me få ringane til å fungera som dei skal. La oss sette i gong!

![](3d_flakser.png)

# Steg 1: Lag ringar, og få dei til å kome mot deg {.activity}

Spelet skal bestå av tre figurar: __Ring__, __Flakser__ og __Bakken__.

Me startar med å laga ringfiguren. Du kan enkelt teikne den sjølv som to sirklar inni kvarandre, fylt med ein farge imellom.

## Sjekkliste {.check}

- [ ] Teikn figuren __Ring__. Jo enklare jo betre.

- [ ] Gi ringfiguren desse skriptene:

    ```blocks
        når jeg mottar [Nytt spill v]
        skjul
        for alltid
            lag klon av [meg v]
            vent (1) sekunder
        slutt

        når jeg starter som klon
        gå til x: (0) y: (0)
        vis
        gjenta (10) ganger
            endre størrelse med (5)
            vent (0.1) sekunder
        slutt
        slett denne klonen
    ```

Du må og laga eit skript som sørger for at meldinga `Nytt spill` sendes når du klikkar på det grøne flaget.

## Test prosjektet {.flag}

- [ ] Kva gjer dei to skripta over? Ser det ut som om ringene kjem mot deg?

## Sjekkliste {.check}

Dei to skripta me har foreløpig er ein OK start, men dei er ikkje gode nok til å verkeleg kallas 3D! Tenk litt på korleis det virkar som om noko veks i størrelse når det kjem mot deg. Når det er langt unna så veks det ganske sakte, mens når det er nærare så veks det mykje fortere. Dette skal me få til ved hjelp av ein *variabel* som me kallar `distanse`{.blockdata}. Når `distanse`{.blockdata} er stor, så er ringen langt borte, og skal vekse sakte. Når `distanse`{.blockdata} er lita så betyr det at ringen er nære, og den skal vekse fort.

- [ ] Lag ein variabel som heiter `distanse`{.blockdata}. Pass på at den kun gjeld for denne figuren.

- [ ] Endre skriptet over til dette:

    ```blocks
        når jeg starter som klon
        gå til x: (0) y: (0)
        vis
        sett [distanse v] til (10)
        gjenta til ((distanse) < (1))
            sett størrelse til ((150) / (distanse)) %
            endre [distanse v] med (-0.5)
            vent (0.1) sekunder
        slutt
        slett denne klonen
    ```

- [ ] Det kan hende du må endra litt på tala i skriptet over for at det skal sjå bra ut. Prøv deg fram!

## Utfordring: Gjennomsiktig effekt {.challenge}

Dette er ikkje viktig for å kunne fortsetje med spelet, men prøv hvis du vil. For at det skal sjå endå mer ut som at ringene først er langt borte og så nære, så kan du bruke klossen

```blocks
    sett [gjennomsiktig v] effekt til ((100)-((150)/(distanse))
```

for å gjera ringane meir gjennomsiktig når dei er langt borte. Kva tal må du putta i denne klossen for at det skal sjå bra ut?

# Steg 2: Få ringane til å dukka opp tilfeldige stader {.activity}

*For at spelet skal bli mest mogleg utfordrande så burde ringane dukka opp på forskjellige stader kvar gong.*

Å først få dei til å dukka opp på forskjellige stader er ikkje så vanskeleg, men å få dei til å vekse på rett måte er litt vanskeleg.

## Sjekkliste {.check}

- [ ] Prøv først å endra på blokka som plasserar ring-klonane til

    ```blocks
        gå til x: (tilfeldig tall fra (-100) til (100)) y: (tilfeldig tall fra (-100) til (100))
    ```

    Det ser ganske bra ut, men ikkje helt rett, eller kva? Det er fordi *midtpunktet* til ringen er på same stad heile tida medan ringen er på veg mot deg. For at det skal sjå ut som at den susar *forbi deg* så må du heile tida flytta på ringen medan den er på veg mot deg. For å få det til å fungera må ringklonen hugsa kor den dukka opp til å begynne med.

- [ ] Lag variabler `ringX`{.blockdata} og `ringY`{.blockdata} som *kun gjeld for ringfiguren*.

- [ ] Erstatt blokka som først plasserar ringen med dette:

    ```blocks
        sett [ringX v] til (tilfeldig tall fra (-100) til (100)
        sett [ringY v] til (tilfeldig tall fra (-100) til (100)
        gå til x: (ringX) y: (ringY)
    ```

    Forhåpentligvis har ikkje oppførselen til ringane endra seg ennå. For å få midtpunktet til ringane til å flytta på seg medan ringane kjem mot deg kan du putte følgjande blokk ein stad inni løkka kor ringen veks:

    ```blocks
        gå til x: ((ringX) / (distanse)) y: ((ringY) / (distanse))
    ```

## Test prosjektet {.flag}

Trykk på det grøne flaget. Nå burde det sjå ut som om ringane verkeleg kjem mot deg! Nå kan du ta ein pust i bakken og sjå over det du har skrevet så langt.

# Steg 3: Styr ein flaksefigur med piltastane {.activity}

*I neste del av dette kurset skal me få ein figur til å fly gjennom ringane. I dette steget skal me laga den figuren, men ikkje koda all flygeoppførselen dens.*

## Sjekkliste {.check}

- [ ] Lag ein ny figur. Det er best om den er symmetrisk, slik at det kan sjå ut som om den flyr innover i skjermen utan at det ser teit ut, bruk for eksempel flaggermus-figuren. Kall den __Flakse__.

- [ ] Lag to nye variablar, `x`{.blockdata} og `y`{.blockdata}. La dei gjelde *for alle figurer*.

- [ ] Gi Flakse følgende skript:

    ```blocks
        når jeg mottar [Nytt spill v]
        sett [x v] til [0]
        sett [y v] til [0]
        for alltid
            hvis (tast [pil høyre v] trykket)
                endre [x v] med (10)
                vent (0.05) sekunder
            slutt
            hvis (tast [pil venstre v] trykket)
                endre [x v] med (-10)
                vent (0.05) sekunder
            slutt
            hvis (tast [pil opp v] trykket)
                endre [y v] med (10)
                vent (0.05) sekunder
            slutt
            hvis (tast [pil ned v] trykket)
                endre [y v] med (-10)
                vent (0.05) sekunder
            slutt
        slutt
    ```

    Nå endres `x`{.blockdata} og `y`{.blockdata} når du styrer med piltastane. me venter litt inni kvar `hvis`{.blockcontrol}-test slik at `x`{.blockdata} og `y`{.blockdata} ikkje plutseleg veks over alle grenser. Test gjerne kva som skjer dersom me ikkje ventar.

- [ ] Nå vil me at posisjonen til ringane skal endra seg når me styrer. Det kan me få til ved å endra klossen

    ```blocks
        gå til x: ((ringX) / (distanse)) y: ((ringY) / (distanse))
    ```

    til dette:

    ```blocks
        gå til x: (((ringX)-(x)) / (distanse)) y: (((ringY) - (y)) / (distanse))
    ```

    Ser det rett ut nå? Nå er me igrunn ferdig med det som trengs for å gå vidare til del 2. I del 2 skal me få det til å virke som om Flakse flakser når me trykkjer på mellomromstasten, akkurat som i Flappy Bird og Flaksefugl. Prøv deg på desse utfordringane hvis du har meir tid igjen.

## Ting å prøve {.try}

- [ ] Er det mogleg å styra figuren gjennom alle ringane? Husk at spelet skal vera akkurat passe vanskeleg, og iallfall ikkje umogleg. Gå gjennom alle skripta og endra på verdiane slik at spelet er kjekt å spela, og slik at det ser bra ut. Kanskje du må endre på størrelsen til ringen, kor mykje ringane skal veksa, kor mykje `x` og `y` endrar seg når du trykkjer på pilane, kor lenge me ventar eller nokon av dei andre verdiane.

- [ ] Teikn din eigen figur! Flaggermusfiguren er kanskje ikkje heilt perfekt. Prøv å sjå om du kan finna nokre bilete på nettet du kan bruka, eller teikn din heilt eigen figur (den burde vera eit fugleliknande dyr). Hugs at det ser mykje betre ut om figuren er symmetrisk. Det er lurt å gi figuren to draktar; ein med vingene ned og ein med vingene opp. Då kan me seinere få Flakse til å flaksa!
