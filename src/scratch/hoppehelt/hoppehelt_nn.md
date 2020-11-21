---
title: Hoppehelt
level: 4
author: 'Geir Arne Hjelle'
translator: 'Stein Olav Romslo'
language: nn
---


# Introduksjon {.intro}

Hoppehelt er eit spel som er litt inspirert av musikkspelet Guitar Hero. I
Hoppehelt skal du kontrollere fleire heltar samstundes medan dei hoppar over
farga boksar som lagar lyd. Gjennom spelet Hoppehelt skal me sjå korleis klonar
blir brukt til programmering i Scratch. Me skal også sjå på klonar av klonar!

![Illustrasjon av eit ferdig Hoppehelt-spel](hoppehelt.png)


# Steg 1: Streken {.activity}

*Me startar bygginga av spelet med å lage ein veldig enkel bakgrunn.*

## Sjekkliste {.check}

- [ ] Start eit nytt prosjekt, og slett kattefiguren.

- [ ] Teikne ein ny bakgrunn som består av ein einsfarga rett strek ganske langt
  ned på skjermen. Bruk vektorgrafikk. Dette er bakken som helten vår skal
  springe på.

- [ ] For at det skal bli enklare å legge til ein tittel seinare, så lagar me ei
  melding med `Nytt spel` på scena:

  ```blocks
  når @greenFlag vert trykt på
  send meldinga [Nytt spel v]
  ```


# Steg 2: Ein hoppande helt {.activity}

*No skal me introdusere helten for spelet vårt.*

## Sjekkliste {.check}

- [ ] Teikne ein enkel liten strekfigur som ser ut som han spring mot venstre.
  Gi figuren namnet `Helt 1`.

  Seinare kan du lage fleire drakter slik at spelet ser betre ut, men me skal
  ikkje bruke tid på det no.

- [ ] Lag ein ny variabel som du kallar `sprett`{.blockdata}. Det er viktig at
  denne berre gjeld for denne figuren.

  Me skal bruke `sprett`{.blockdata}-variabelen til å beskrive rørsla til helten
  når han hoppar.

- [ ] I hovudløkka til helten skal gravitasjonen virke slik at den stadig skal
  gjere `sprett`{.blockdata} mindre, samstundes som me seier at viss helten
  rører bakken skal han ikkje dette lengre ned.

  ```blocks
  når eg får meldinga [Nytt spel v]
  gå til x: (210) y: (-120)
  gjenta for alltid
      endra [sprett v] med (-1)
      viss <rører fargen [#00cc00] ?>
          neste drakt
          set [sprett v] til [0]
      slutt
      endra y med (sprett)
  slutt
  ```

  Set farga i `rører fargen`{.blocksensing}-klossen til same farge som
  streken du teikna på bakgrunnen i Steg 1.

- [ ] Prøv å endre startposisjonen til helten, særleg y-koordinaten. Får du
  helten til å falle mot bakken?

- [ ] Legg til ein ny `viss`{.blockcontrol}-test inne i
  `viss`{.blockcontrol}-testen du allereie har. Viss tasten `m` blir trykka set
  du `sprett`{.blockdata} til eit positivt tal. Prøv deg fram slik at du finn
  ein verdi som gjer at helten hoppar passe høgt.

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Står eller spring helten på bakken? Figuren skal ikke bevege seg
  sidelengs.

- [ ] Hoppar helten når du trykkar på `m`-tasten?


# Steg 3: Boksar med lyd {.activity}

*No skal me lage boksar som helten vår kan hoppe over.*

## Sjekkliste {.check}

- [ ] Lag ein ny figur ved å teikne ein liten fargelagt boks som helten kan
  hoppe over. Kall figuren `Boks`. Bruk ![Velg
  senterpunkt](../bilder/velg_senterpunkt.png) til å setje senterpunktet nedst
  til venstre på boksen.

- [ ] Når boksen mottek meldinga `Nytt spel` vil me at den plasserer seg på
  bakken heilt til venstre på skjermen. Bruk ein `gå til`{.blockmotion}-kloss og
  lag dette skriptet sjølv. Pass på at boksen ikke er borti kanten av skjermen.

- [ ] Etter at du har funne ein bra plassering for boksen kan du utvide skriptet
  ved å `gøyme`{.blocklooks} figuren og lage ei løkke som gjer at boksen lagar
  ein klone av seg sjølv annakvart sekund.

- [ ] Gå til scena og lag ein variabel du kallar `hastigheit`{.blockdata}. Lag
  eit skript på scena som set denne variabelen til `3` når meldinga `Nytt spel`
  blir motteke.

- [ ] Gå tilbake til boksfiguren. No vil me at boksklonane flyttar seg mot
  helten. Lag eit nytt skript som startar når boksen startar som klon. I dette
  skriptet må du `vise`{.blocklooks} boksen. Så kan du starte ei løkke som blir
  gjenteke til boksen er borti kanten. Inne i løkka vil du endre x med
  `hastigheit`{.blockdata}. Etter løkka kan du slette denne klonen.

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Kjem det ein jamn straum av boksar mot helten.

- [ ] Kan du bruke `m` til å hoppe over boksane?

- [ ] Kva skjer viss helten spring inn i ein boks?

## Sjekkliste {.check}

- [ ] Me vil at spelet skal stoppe når helten spring inn i ein boks. Gå til
  `Helt 1`. Bytt ut `gjenta for alltid`{.blockcontrol}-løkka med ei `gjenta
  til`{.blockcontrol}-løkke som du gjentek til helten kjem borti `Boks`.

- [ ] Etter den nye `gjenta til`{.blockcontrol}-løkka kan du sende ut ei ny
  melding `Spel slutt`.

- [ ] Klikk på boks-figuren. Legg til eit skript som stoppar andre skript i
  figuren, og så slettar denne klonen etter at `Spel slutt` blir motteke.

  Prøv spelet ditt att. Kva skjer viss helten spring inn i ein boks no?

- [ ] Me kan spele ein liten lyd kvar gong me har hoppa over ein boks. Legg til
  følgande kloss etter løkka som flyttar boksen, men før klonen blir sletta:

  ```blocks
  spel tonen (60) i (0.5) takter
  ```

  Du kan gjerne bruke `bruk instrument`{.blocksound}-klossen til å velje eit
  passande instrument før spelet startar.

- [ ] Viss du testar dette ser du at boksane heng litt medan lyden blir spelt
  av. Ein enkel måte å unngå dette på er å leggje til ein
  `gøym`{.blocklooks}-kloss rett før `spel tonen`{.blocksound}-klossen.

## Prøv sjølv {.challenge}

Før me går vidare skal me sjå på eit par måtar me kan gjere kvar enkelt boks
litt spesiell og ulik dei andre. Prøv å eksperimentere med desse og dei andre
innstillingane i spelet ditt.

Heilt fyrst i skriptet der boksen startar som klon, før den blir vist, kan du
prøve å legge til ulike effektar. Til dømes kan du endre storleiken tilfeldig
med klossen

```blocks
set storleik til (tilfeldig tal frå (30) til (100)) %
```

På same måte kan du bruke

```blocks
set [farge v]-effekt til (tilfeldig tal frå (-100) til (100))
```

for å endre farga på boksane tilfeldig. Finn på andre effektar, kanskje med å
bruke fleire drakter?

Me kan gjere lydane som kjem når me har hoppa over boksane individuelle. Prøv
til dømes å la lengda av tona vere avhengig av storleiken på boksen.

Til slutt kan du prøve å endre på kor ofte det kjem nye boksar. Bruk gjerne den
følgande klossen:

```blocks
tilfeldig tal frå (1.2) til (3.2)
```

Du kan godt eksperimentere med verdiane i klossen.


# Steg 4: Fleire strekar og boksar {.activity}

*Me skal gjere spelet mykje vanskelegare ved å lage tre rader med boksar.*

## Sjekkliste {.check}

- [ ] Sjå på skripta til `Boks`. Ser du at du har ei *generator-løkke* som lagar
  nye bokser omkring annakvart sekund? Ser du *flytte-løkka* som flyttar boksane
  mot høgre?

  Riv laus begge desse løkkene og legg dei til sides. Me skal bruke dei att
  snart, så ikkje slett noko.

- [ ] Lag ein ny variabel som du kallar `er generator`{.blockdata}. Denne må
  gjelde kun for denne figuren. Me skal bruke variabelen til å identifisere
  generator-løkka.

- [ ] No legg me på ei ny løkke som lagar tre uavhengige generator-løkker. Endre
  skriptet som køyrast for `Nytt spel` til dette:

  ```blocks
  når eg får meldinga [Nytt spel v]
  gå til x: (-239) y: (-161)
  set [er generator v] til [ja]
  gøym
  gjenta (3) gongar
      lag klon av [meg v]
      endra y med (110)
  slutt
  ```

  Bruk den same utgangsposisjonen som før. Dette lagar tre *generator-klonar*
  med ulike y-verdier.

- [ ] Me skal bygge opp at skriptet som køyrer når ein boks startar som klone.
  Lag fyrst det følgande:

  ```blocks
  når eg startar som klon
  viss <(er generator) = [ja]>
      set [er generator v] til [nei]
  elles
  slutt
  ```

- [ ] Flytt generator-løkka du la til sides inn i `viss`{.blockcontrol}-testen
  rett under `set er generator`{.blockdata}-klossen.

- [ ] Tilsvarande legg du flytt-løkka frå tidlegare inn i
  `elles`{.blockcontrol}-testen.

Prøv spelet ditt. No skal du ha tre rader med boksar som blir flytta over
skjermen.

- [ ] Klikk på `Scene` heilt til venstre på skjermen. Gå til
  `Bakgrunnar`{.blocklightgrey}. Teikne to nye strekar i same farge som den
  fyrste. Test spelet og flytt strekane slik at boksane flyttar seg naturleg
  oppå dei.

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Har du tre rader med boksar som sklir over skjermen?

- [ ] Er det framleis berre ein hoppehelt på den nedste rada?


# Steg 5: Kor er alle heltane hen? {.activity}

*No skal me lage dei to siste hoppeheltane!*

## Sjekkliste {.check}

- [ ] Lag ein kopi av `Helt 1`-figuren. Det skjer automatisk at kopien får
  namnet `Helt 2`.

- [ ] Klikk på `Helt 2`. Det einaste me må endre på er y-posisjonen og kva tast
  som skal trykkast for å hoppe.

  Endre y-posisjonen i `gå til`{.blockmotion}-klossen med 110.

  Endre `m` til `k` i `tast trykt`{.blocksensing}-testen.

Prøv spelet ditt att. Har du to hoppeheltar? Virkar dei som dei skal?

- [ ] Lag endå ein kopi av `Helt 1`. Endre kopien slik at den har posisjon 110
  høgare enn `Helt 2`, og slik at den hoppar når du trykkar på `o`.

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] No skal du ha tre hoppeheltar som må hoppe over boksane som kjem. Spelet
  er ganske vanskeleg og krever konsentrasjon og koordinasjon!

## Prøv sjølv {.challenge}

Her er oppgåva ferdig, men det er framleis mange spanande ting du kan gjere med
spelet ditt for å gjere det endå betre.

Til dømes kan du leggje til poeng ved å lage ein `Poeng`{.blockdata}-variabel
som aukar kvar gong ein av heltane hoppar over ein boks. Du kan også auke
hastigheita etter kvart som spelet varar.

Prøv å gjere tona som blir spelt avhengig av y-posisjonen til boksen. Det er
litt vanskeleg, men blir veldig kult sidan du høyrer at hoppeheltane speler ein
slags sang ved å hoppe over boksane.
