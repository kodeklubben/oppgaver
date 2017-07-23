---
title: Asteroids
level: 4
author: Geir Arne Hjelle
translator: Gro Anette Vestre
language: nn
tags:
    topic: [block_based, game, animation]
    subject: [arts_and_crafts, mathematics, programming]
    grade: [secondary, junior]
---

# Introduksjon {.intro}

På slutten av 1970-talet ga Atari ut to spel der ein skulle kontrollera eit romskip. Det første var Lunar Lander, men dette vart utkonkurrert av Asteroids som Atari ga ut nokre månedar seinere. Spela var faktisk så like at dei kunne gjenbruke mykje av teknologien. Me skal gjera det same! Du må derfor ha laga [Lunar Lander](../lunar_lander/lunar_lander_nn.html) før du startar på dette prosjektet. I Asteroids er målet å beskytta romskipet mot asteroidar ved å skyta dei i småbitar.

![](asteroids.png)

# Oversikt over prosjektet {.activity}

*Mesteparten av kodinga av Asteroids skal du gjera sjølv (og noko har du allereie gjort). I Asteroids vil me spesielt sjå på nokre av måtane ein kan gjenbruke kode i Scratch.*

## Plan {.check}

- [ ] Enda eit flygande romskip

- [ ] Romskipet kan skyte!

- [ ] Pass deg for asteroidane

- [ ] .. og andre utfordringer

# Steg 1: Enda eit flygande romskip {.activity}

*I [Lunar Lander](../lunar_lander/lunar_lander_nn.html) laga me eit flott romskip. Nå skal me sjå korleis me kan bruka det same romskipet i dette prosjektet.*

Du veit sikkert at du kan *Remikse* andre sine Scratch-prosjekter. Du får då mulegheit til å laga din eigen versjon av noko andre har gjort, og spesielt kan du gjenbruke kode andre har skrevet tidlegare.

Nå skal me sjå på eit triks for å gjenbruke kode me sjølv har laga tidlegare. Ved å bruke `Ryggsekken` kan ein kopiera figurar og kode mellom forskjellige prosjekt. Me vil derfor først kopiera romskipet me laga i Lunar Lander.

## Sjekkliste {.check}

- [ ] Åpne [Lunar Lander](../lunar_lander/lunar_lander_nn.html)-prosjektet ditt.

- [ ] Legg merke til at det står `Ryggsekk` heilt nederst på skjermen.
  Klikk på `Ryggsekk` og et litt større felt skal åpna seg opp.

- [ ] Dra heile romskip-figuren din til den åpne ryggsekken. Ein kopi av romskip-figuren blir verande i ryggsekken.

- [ ] Start eit nytt prosjekt ved å velge `Ny` i `Fil`-menyen. Slett kattefiguren og legg på ein stjernebakgrunn.

- [ ] Du kan nå dra romskip-kopien ut frå ryggsekken, og til figurvinduet i det nye prosjektet.

  ![](ryggsekk.png)

  Du vil nå sjå at alle draktane, alle variablane og alle skripta til romskipet er kopiert over. Du kan rydda opp litt ved å slette skript som ikkje har noko med kontrollen over romskipet å gjera, for eksempel   om du har eit `Sjekk landing`-skript treng me ikkje det i dette spelet.

- [ ] Legg eit skript på scenen som sender ein melding til romskipet om at det skal starte å fly når det grøne flaget vert klikka på. Prøv spelet ditt. Kan du fly romskipet rundt omkring?

- [ ] Me skal gjera ein liten forandring i korleis romskipet oppfører seg. Asteroids foregår langt ute i rommet der det ikkje er noko  merkbar tyngdekraft. Slett derfor klossen som modellerar tyngdekrafta i `for alltid`{.blockcontrol}-løkka di, `endre [fartY v] med (-0.01)`{.b}.

- [ ] Me skal og gjera ein litt større endring i spelet. Me vil at verdsrommet skal følas litt stort og uoversiktlig ved at når romskipet går ut av skjermen på den eine sida skal det dukka opp på andre sida av skjermen.

  Dette gjør me ved ganske enkle `hvis`{.blockcontrol}-testar. Det me må hugse på er at `x`-koordinatene på skjermen går fra `-240` til `240`, mens `y`-koordinatene ligg mellom `-180` og `180`. Sidan Scratch passar på at figurar ikkje går heilt av skjermen flyttar me dei litt innafor skjermkanten:

  ```blocks
      når jeg mottar [Nytt spill v]
      for alltid
          hvis ((x-posisjon) < (-235))
              endre x med (470)
          slutt
          hvis ((x-posisjon) > (235))
              endre x med (-470)
          slutt
          hvis ((y-posisjon) < (-175))
              endre y med (350)
          slutt
          hvis ((y-posisjon) > (175))
              endre y med (-350)
          slutt
      slutt
  ```

# Steg 2: Romskipet kan skyte {.activity}

*Romskipet vårt vil snart fly inn i ein asteroidesverm, så me må montera rakettar som kan sprengje unna asteroidane.*

## Sjekkliste {.check}

- [ ] Lag ein ny figur som du kallar `Skudd`. Denne teiknar du greit sjølv. Eventuelt fins det for eksempel nokre ball-figurar som kan brukast som kuler. Bruk ein `sett størrelse`{.blocklooks}-kloss for at figuren skal verta passe stor. Legg også på ein kloss for å `skjule`{.blocklooks} figuren.

- [ ] Me vil bruka kloner slik at me kan skyte fleire skudd. Først treng me koden som lagar ein ny skuddklone når du trykkjer mellomromtasten:

  Lag eit skript på skudd-figuren som starter på `Nytt spill`-meldingen. Skriptet kan bestå av ein `for alltid`{.blockcontrol}-løkke, der du testar på om mellomromtasten er trykka. Dersom eit skudd skal avfyres kan du først la skuddet `gå  til`{.blockmotion} romskipet og deretter peike i same retning som  romskipet. Dette siste kan du gjera med ein kombinasjon av `pek i  retning`{.blockmotion}, `retning av`{.blocksensing} og  `vend`{.blockmotion}-klosser. Til slutt kan du `lage en  klon`{.blockcontrol} av figuren.

- [ ] For å passa på at berre ein melding vert sendt ut kvar gong du trykkjer mellomromtasten kan me starta `hvis`{.blockcontrol}-testen med å venta til mellomromtasten er sluppet igjen. Dette trikset ser  omtrent slik ut:

  ```blocks
      hvis (tast [mellomrom v] trykket?)
          vent til (ikke (tast [mellomrom v] trykket?))
          ...
      slutt
  ```

- [ ] Nå skal me kode oppførselen til skuddet etter at det er avfyrt. Det kan vera ganske enkelt. Når skuddfiguren `starter som klon`{.blockcontrol} må den `vises`{.blocklooks}, og deretter kan den flyttas i ei løkke før den til slutt vert sletta. Eksperimenter med hastigheta og rekkevidden på skuddet ved å endre på kor mange gonger løkka gjentas og kor mange steg figuren går inne i løkka.

- [ ] Til slutt vil me at og skudda skal kunne forsvinne ut på den eine sida av skjermen og dukke opp igjen på den andre. Til dette vil me bruke omtrent samme kode for romskipet.

  For å kopiere skript mellom figurar kan du bruka ryggsekken på same måte som tidlegare. Ein litt raskare metode er å berre dra skriptet du vil kopiere til den figuren du vil kopiere til.

  Kopier koden for å *warp'e* rundt skjermen fra romskipet til skudd-figuren.

- [ ] Me kan nesten bruka denne koden som den er. Den eineste endringa me treng å gjera er at den skal starte på `når jeg starter som klon`{.b} i stadenfor på `når jeg mottar [Nytt spill v]`{.b}, siden denne oppførselen skal gjelde for alle skuddklonene.

- [ ] Prøv spelet ditt. Nå skal du kunne fly rundt i verdsrommet medan du skyt.

# Steg 3: Pass deg for asteroidane {.activity}

*Då er det på tide å laga ein asteroidesverm. Noko av det som er kult med Asteroids er at asteroidane blir skutt i småbiter når du skyt på dei, og ein må fortsatt passa seg for og skyte desse mindre asteroidane. Me vil kode dette ved å bruke kloner i forskjellige størrelser.*

## Sjekkliste {.check}

- [ ] Lag ein asteroidefigur. Ein måte å gjera dette på er å teikne ein ny figur med vektorgrafikk. Start med ein enkel firkant, og bruk deretter `Bøy`-verktøyet for å leggje til fleire hjørnepunkt og flytta dei rundt som i figuren under.

  ![](flyttpunkt.png)

- [ ] Også for asteroidane vil me bruka kloner. Lag eit skript som `skjuler`{.blocklooks} figuren og lager eit par asteroide-kloner tilfeldige stader på skjermen når det mottar `Nytt spill`-meldingen.

- [ ] Når figuren `starter som klon`{.blockcontrol} vil me først at den `peker`{.blockmotion} i ein tilfeldig retning og deretter `vises`{.blocklooks}. Vidare kan den gå inn i ei løkke som `gjentas til`{.blockcontrol} figuren `berører romskipet`{.blocksensing}. Inne i løkka lar du først asteroiden `gå noen steg`{.blockmotion}. Deretter må du teste om asteroiden `berører et skudd`{.blocksensing}. Hvis den gjer det kan du laga asteroiden mindre med ein kloss som liknar

  ```blocks
      sett størrelse til ((størrelse) / (2)) %
  ```

  `Hvis`{.blockcontrol} `størrelsen`{.blocklooks} fortsatt er større enn for eksempel 10 kan du laga eit par nye kloner av denne mindre asteroiden. Til slutt kan du `slette denne klonen`{.blockcontrol} uansett kva størrelsen er.

- [ ] Legg på ei melding eller ein `stopp`{.blockcontrol}-kloss slik at spelet kan avsluttas etter at `gjenta til`{.blockcontrol}-løkka avsluttes, sidan romskipet då har krasjet i ein asteroide.

- [ ] Også asteroidane skal kunne fly ut av skjermen på ei side og dukke opp på ei anna. Kopier derfor skriptet som fiksar dette frå skudd-figuren på same måte som tidlegare.

- [ ] Til slutt vil me og slette skudd-klonene når dei treff asteroidane. Her må me vera litt forsiktig så me ikkje slettar skudd-klonene før asteroidane merker at dei er truffet. Dette kan me fiksa ved å leggje inn ein ørliten forsinkelse. Du kan for eksempel legge inn kode som dette i løkka som flyttar skudd-figuren:

  ```blocks
      hvis (berører [Asteroide v] ?)
          vent (0.01) sekunder
          slett denne klonen
      slutt
  ```

# Steg 4: Vidareutvikling av spelet {.activity}

*Du har nå laga ein enkel variant av Asteroids. Men prøv å gjer spelet kjekkare ved å vidareutvikle det. Du bestemmer sjølv korleis du vil jobba vidare, men nedanfor er nokre idear som kanskje kan vera til inspirasjon?*

## Idear til vidareutvikling {.check}

- [ ] Gi poeng når spelaren treff ein asteroide. Ein burde kanskje få fleire poeng for å treffe dei små asteroidane? Det kan du fikse med ei utrekning omtrent som

  ```blocks
      avrund ((100) / (størrelse))
  ```

- [ ] Dersom du plasserar asteroidane heilt tilfeldig når eit nytt spel startar er det ganske sannsynleg at romskipet krasjar i ein asteroide allereie før spelet har starta. Det er ikkje noko kjekt. Ein måte å fikse det på vil vera å først la asteroideklonen `gå til romskipet`{.blockmotion}, men deretter peike i ein tilfeldig retning og `gå 100 til 200 steg`{.blockmotion} før det til slutt `vises`{.blocklooks}.

- [ ] Spelet ser litt kulare ut om du teiknar fleire asteroidedrakter, og vel ein av dei tilfeldig når ein klon vert laga.

- [ ] Dersom du klarar å skyte ned alle asteroidane burde ein kome vidare til eit vanskeligare nivå. Kanskje med fleire asteroider? Eller med asteroider som bevegar seg raskare? Eller deler seg i fleire deler når dei vert skutt?

  For å veta når du kan gå vidare til eit nytt nivå må du telje kor mange asteroidar som flyr rundt. Lag derfor ein variabel `Antall asteroider`{.blockdata} som du aukar med 1 når ein asteroide `starter som klon`{.blockcontrol}. Deretter må variabelen minka med 1 når klonen vert sletta.

  Vidare brukar du ein `Nivå`{.blockdata}-variabel som held styr på kva nivå spelaren har kome til.

- [ ] I det originale Asteroids-spelet dukka det og opp ein flygande tallerken (UFO) innimellom. Denne måtte ein og passe seg for, men i motsetning til asteroidane kunne UFOen skyte tilbake. Prøv å legg til ein slik UFO i spelet ditt!
