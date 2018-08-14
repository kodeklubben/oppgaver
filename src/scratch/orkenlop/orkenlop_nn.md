---
title: Ørkenløp
level: 2
author: 'Omsett frå [Code Club UK](//codeclub.org.uk)'
translator: 'Stein Olav Romslo'
language: nn
---


# Introduksjon {.intro}

Dette er eit spel for to, der ei papegøye og ei løvinne kjempar om å kome fyrst
gjennom ørkenen. Kvar spelar må trykke ein tast så fort og så ofte som mogleg
for å flytte figuren sin, og den som kjem fyrst til kanten av skjermen vinn.

![Illustrasjon av eit ferdig ørkenløp-spel](orkenlop.png)


# Steg 1: Lag ei scene og legg til figurar {.activity}

*Me startar med å få på plass bakgrunnen og figurane.*

## Sjekkliste {.check}

- [ ] Klikk på Scene og vel ein ferdig bakgrunn,
  ![vel ein ferdig bakgrunn](../bilder/bakgrunn-fra-bibliotek.png). Vel
  `Natur/desert`.

- [ ] Fjern katten ved å høgreklikke på figuren og vel `slett`.

- [ ] Legg til ein ny figur ved å trykke på
  ![vel figur frå biblioteket](../bilder/hent-fra-bibliotek.png). Vel
  `Dyr/Lionness`.

- [ ] Legg til endå ein ny figur: vel `Dyr/Parrot`. Krymp figuren slik
  at den er omlag like stor som løvinna ved å bruke
  ![krymp](../bilder/krymp.png).


# Steg 2: La løvinna og papegøya bevege seg {.activity}

*Me vil at figurane skal bevege seg når du trykkar på ein knapp.*

## Sjekkliste {.check}

- [ ] Vel løvefiguren og få den til å `gå 4 steg`{.blockmotion} når du trykkar
  `L`-tasten.

  ```blocks
  når [l v] vert trykt
  gå (4) steg
  ```

- [ ] Vel papegøyefiguren og la den `gå 4 steg`{.blockmotion} når du trykkar
  `A`-tasten.

  ```blocks
  når [a v] vert trykt
  gå (4) steg
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Beveger løvinna og papegøya seg over skjermen når du trykkar på
  `A`- og `L`-tastane?


# Steg 3: Start kappløpet {.activity}

*No må me starte kappløpet og kåre ein vinnar! Me startar med å lage ein
 startknapp.*

## Sjekkliste {.check}

- [ ] Legg til ein ny figur. Vel `Ting/Button3`. Flytt den til midten av
  scena.

- [ ] Klikk på `Drakter`-fana og verktøyet `T` for å leggje til tekst. Trykk på
  venstre kant av knappen for å leggje til eit tekstfelt og skriv inn teksten
  `Start`. Du kan flytte på teksten ved å trykkje på den ein gong, og du endrar
  innhaldet ved å dobbeltklikke.

- [ ] Legg til eit skript som viser figuren når spelet startar:

  ```blocks
  når @greenFlag vert trykt på
  vis
  ```

- [ ] I tillegg vil me at når du klikkar på knappen skal den fyrst telje ned frå
  3, seie `SPRING!` og så bli gøymt. Dette ordnar du med følgjande skript:

  ```blocks
  når denne figuren vert trykt på
  sei [3] i (1) sekund
  sei [2] i (1) sekund
  sei [1] i (1) sekund
  sei [SPRING!] i (1) sekund
  gøym
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget, og så på startknappen.__

- [ ] Tel knappen ned?

- [ ] Seier den `SPRING!`?

- [ ] Blir den borte?

Me vil at figurane berre skal bevege seg etter at kappløpet har starta, og me
vil vite når kappløpet er over.

## Sjekkliste {.check}

- [ ] For å vite når kappløpet har starta og slutta lagar me ein variabel
  med namnet `kappløp`{.blockdata}. Variabelen skal vere tilgjengeleg
  `for alle figurar`. Fjern avhukinga framfor variabelen slik at den
  ikke visast på scena.

- [ ] Set `kappløp`{.blockdata} til `0` når spelet startar ved å forandre `når
  grønt flagg vert trykt på`{.blockevents}-skriptet slik:

  ```blocks
  når @greenFlag vert trykt på
  vis
  set [kappløp v] til [0]
  ```

- [ ] Når nedteljinga er ferdig og løpet startar forandrar me
  `kappløp`{.blockdata}-verdien til 1. Dette gjer du ved å leggje til klossen
  `Set kappløp til 1`{.blockdata} under `sei 1 i 1 sekund`{.blocklooks} i
  skriptet som startar med `når denne figuren vert trykt på`{.blockevents}.

- [ ] No må me lage ein regel som seier at figurane berre får lov til å bevege
  seg etter at løpet har starta – det vil seie når `kappløp`{.blockdata} har
  verdien 1. Klikk på papegøya og endre:

  ```blocks
  når [a v] vert trykt
  viss <(kappløp) = [1]>
      gå (4) steg
  slutt
  ```

- [ ] Gjenta det same for løvinna.

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Kan løvinna og papegøya berre flytte seg når nedteljinga er ferdig?


# Steg 4: Avslutte kappløpet {.activity}

*No vil me finne ut kven som vinn kappløpet, og i tillegg gjere klart for ein ny
 runde.*

## Sjekkliste {.check}

- [ ] Legg til ein kloss i papegøya sitt skript som seier `set kappløp til
  0`{.blockdata} viss figuren er borti kanten av skjermen:

  ```blocks
  når [a v] vert trykt
  viss <(kappløp) = [1]>
      gå (4) steg
      viss <rører [kant v]?>
          set [kappløp v] til [0]
      slutt
  slutt
  ```

- [ ] Spel inn ein lyd som skal spelast av viss papegøya vinn.

  Trykk på `Lyder`-fana og så mikrofon-ikonet og spel inn ein morosam lyd!
  Opptaket startar når du har klikka på disken slik at den blir raud. Klikk
  stopp (firkanten) når du er ferdig, og gi lyden eit namn - til dømes `Polly`.
  Nokre nettlesarar kan be deg om lov til å spele inn lyd. Viss du ikkje vil
  godta det kan du bruke lydane som følgjer med figurane.

- [ ] Så legg du til klossane som speler av lyden og let papegøya
  fortelje at den vann:

  ```blocks
  når [a v] vert trykt
  viss <(kappløp) = [1]>
      gå (4) steg
      viss <rører [kant v]?>
          set [kappløp v] til [0]
          spel lyden [Polly v]
          sei [Polly vann!] i (3) sekund
      slutt
  slutt
  ```

- [ ] Gjer tilsvarande for løvinna.

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Kan du trykkje på startknappen og så bevege dyra med tastane `A` og `L`?

- [ ] Kjem den riktige vinnarlyden og riktig melding opp på skjermen?


# Steg 5: Nullstill spelet {.activity}

*Når kappløpet er over må me fortelje dei andre figurane at spelet er over og
 nullstille spelet, slik at det er klart for ein ny runde.*

## Sjekkliste {.check}

- [ ] Klikk på papegøyefiguren og legg til ein kloss som sender melding
  `Avslutt` etter at figuren seier den har vunne.

  ```blocks
  når [a v] vert trykt
  viss <(kappløp) = [1]>
      gå (4) steg
      viss <rører [kant v]?>
          set [kappløp v] til [0]
          spel lyden [Polly v]
          sei [Polly vann! v] i (3) sekund
          send meldinga [Avslutt v]
      slutt
  slutt
  ```

- [ ] Me treng eit nytt skript som lyddar etter denne avslutningsmeldinga og
  flyttar papegøya attende til start.

  ```blocks
  når jeg mottar [Avslutt v]
  set x til (-170)
  ```

- [ ] Gjer det same for løvinna. Test ulike `x`-verdiar for å vere sikker på at
  løvinna og papegøya startar frå same stad.

- [ ] For at figurane skal stå på startstreken når kappløpet startar den aller
  fyrste gongen må me leggje til følgjande klossar på begge figurane:

  ```blocks
  når @greenFlag vert trykt på
  set x til (-170)
  ```

- [ ] For at spelarane skal kunne klikke i gang nye runder må me passe på at
  start-knappen kjem til syne att etter kvar avslutta runde. Klikk på
  startknapp-figuren og legg til eit skript som viser knappen når
  avslutningsmeldinga blir motteke.

  ```blocks
  når jeg mottar [Avslutt v]
  vis
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Kan du spele mot ein ven? Ein av dykk styrer papegøya ved å trykke `A`, og
  den andre løvinna ved å trykke `L`.

## Lagre prosjektet {.save}

Spelet er ferdig! Viss du vil kan du velje `Legg ut` slik at venene og familien
din kan prøve det.

Under finn du nokre framlegg og idear til korleis du kan utvide spelet og gjere
det meir interessant.

## Utfordring 1: Legg til ein rakett! {.challenge}

- [ ] __Legg til ein rakett__ som kan brukast ein gong per kappløp og som
  flyttar papegøya eller løvinna __30 steg på ein gong.__

- [ ] __Legg til ei ny drakt__ med ild som kjem ut bak figurane. La denne bli
  aktivert når raketten avfyrast.

- [ ] __Lag ein lyd__ som figuren kan gi frå seg når raketten avfyrast.

Under er eit framlegg til korleis eit rakett-skript kan sjå ut. Du må leggje til
nokre lydar og variablar på eiga hand.

```blocks
når [q v] vert trykt
viss <<(kappløp) = [1]> og <(rakett_brukt) = [0]>>
    bytt drakt til [parrot-rakett v]
    set [rakett_brukt v] til [1]
    gå (30) steg
    spel lyden [motorcycle passing v]
    viss <rører [kant v]?>
        set [kappløp v] til [0]
        spel lyden [Polly v]
        sei [Polly vann! v] i (3) sekund
        send meldinga [Avslutt v]
    slutt
    bytt drakt til [parrot-a v]
slutt
```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Fungerer raketten slik du hadde planlagt?

- [ ] Kva skjer viss ein prøver å bruke raketten to gonger?

- [ ] Kva skjer viss ein brukar raketten for å kome heilt til mål?

## Utfordring 2: Bruk eigendefinerte klossar for å forenkle skriptet ditt {.challenge}

Koden som brukast for å sjekke om kappløpet er over brukast to stader for kvar
figur: både når den beveger seg normalt og når den beveger seg med rakett. Me
kan forenkle skriptet vårt ved å lage ein eigendefinert kloss. Dette er ei
samling kode som brukast fleire stader. Det er nesten som å lage vår eigen
Scratch-kodekloss!

- [ ] Vel papegøya sitt skript.

- [ ] Vel `Flere klosser`{.blockmoreblocks}-paletten og klikk på `Lag
  en kloss`-knappen.

- [ ] Kall klossen din `ferdig` og trykk OK.

- [ ] No får du ein `definer ferdig`{.blockmoreblocks}-kloss i
  skriptvindauget ditt. Flytt den litt for seg sjølv.

- [ ] Riv laus heile `viss`{.blockcontrol}`rører
  kant?`{.blocksensing}-klossen og dra den til `definer
  ferdig`{.blockmoreblocks}-klossen.

- [ ] Kan du dra `ferdig`{.blockmoreblocks}-klossen frå paletten og bruke
  den på same måte som andre kodeklossar?

- [ ] Slett den andre `viss`{.blockcontrol}`rører
  kant?`{.blocksensing}-klossen frå skriptet ditt og erstatt den med ein
  `ferdig`{.blockmoreblocks}-kloss.

  ```blocks
  definer ferdig
  viss <rører [kant v]?>
      set [kappløp v] til [0]
      spel lyden [Polly v]
      sei [Polly vann! v] i (3) sekund
      send meldinga [Avslutt v]

  når [a v] vert trykt
  viss <(kappløp) = [1]>
      gå (4) steg
      ferdig

  når [q v] vert trykt
  viss <<(kappløp) = [1]> og <(rakett_brukt) = [0]>>
      bytt drakt til [parrot-rakett v]
      set [rakett_brukt v] til [1]
      gå (30) steg
      spel lyden [motorcycle passing v]
      ferdig
      bytt drakt til [parrot-a v]
  ```

- [ ] Gjer dette koden din enklare å lese? Kan du lage ein tilsvarande
  eigendefinert kloss for løvinna?

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- Virkar spelet framleis slik det skal?

- Er spelet ferdig når papegøya eller løvinna kjem til kanten av skjermen?

## Lagre prosjektet {.save}

Veldig bra! No er du ferdig og kan kose deg med spelet du har laga!
