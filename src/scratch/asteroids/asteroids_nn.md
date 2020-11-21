---
title: Asteroids
level: 4
author: 'Geir Arne Hjelle'
translator: 'Gro Anette Vestre'
language: nn
---


# Introduksjon {.intro}

På slutten av 1970-talet ga Atari ut to spel der ein skulle kontrollera eit
romskip. Det første var Lunar Lander, men dette vart utkonkurrert av Asteroids
som Atari ga ut nokre månedar seinere. Spela var faktisk så like at dei kunne
gjenbruke mykje av teknologien. Me skal gjera det same! Du må derfor ha laga
[Lunar Lander](../lunar_lander/lunar_lander_nn.html) før du startar på dette
prosjektet. I Asteroids er målet å beskytta romskipet mot asteroidar ved å skyta
dei i småbitar.

![Illustrasjon av eit ferdig Asteroids-spel](asteroids.png)


# Oversikt over prosjektet {.activity}

*Mesteparten av kodinga av Asteroids skal du gjera sjølv (og noko har du
allereie gjort). I Asteroids vil me spesielt sjå på nokre av måtane ein kan
gjenbruke kode i Scratch.*

## Plan {.check}

- [ ] Enda eit flygande romskip

- [ ] Romskipet kan skyte!

- [ ] Pass deg for asteroidane

- [ ] .. og andre utfordringer


# Steg 1: Enda eit flygande romskip {.activity}

*I [Lunar Lander](../lunar_lander/lunar_lander_nn.html) laga me eit flott
romskip. No skal me sjå korleis me kan bruka det same romskipet i dette
prosjektet.*

Du veit sikkert at du kan *remikse* andre sine Scratch-prosjekt. Du får då
moglegheit til å laga din eigen versjon av noko andre har gjort, og spesielt kan
du gjenbruke kode andre har skrive tidlegare.

Nå skal me sjå på eit triks for å gjenbruke kode me sjølv har laga tidlegare.
Ved å bruke `Ryggsekken` kan ein kopiera figurar og kode mellom forskjellige
prosjekt. Me vil derfor først kopiera romskipet me laga i Lunar Lander.

## Sjekkliste {.check}

- [ ] Åpne [Lunar Lander](../lunar_lander/lunar_lander_nn.html)-prosjektet ditt.

- [ ] Legg merke til at det står `Ryggsekk` heilt nedst på skjermen.
  Klikk på `Ryggsekk` og eit litt større felt skal åpna seg opp.

- [ ] Dra heile romskip-figuren din til den åpne ryggsekken. Ein kopi av
romskip-figuren blir verande i ryggsekken.

- [ ] Start eit nytt prosjekt ved å velge `Ny` i `Fil`-menyen. Slett
kattefiguren og legg på ein stjernebakgrunn.

- [ ] No kan du dra romskip-kopien ut frå ryggsekken, og til figurvindauget i
det nye prosjektet.

  ![Bilete som syner korleis du dreg Romskip-kopien frå ryggsekken i Scratch](ryggsekk.png)

  Du vil no sjå at alle draktane, alle variablane og alle skripta til romskipet
  er kopiert over. Du kan rydda opp litt ved å slette skript som ikkje har noko
  med kontrollen over romskipet å gjera, til dømes om du har eit `Sjekk
  landing`-skript treng me ikkje det i dette spelet.

- [ ] Legg eit skript på scenen som sender ein melding til romskipet om at det
skal starte å fly når det grøne flaget vert klikka på. Prøv spelet ditt. Kan du
fly romskipet rundt omkring?

- [ ] Me skal gjera ein liten forandring i korleis romskipet oppfører seg.
Asteroids foregår langt ute i rommet der det ikkje er noko merkbar tyngdekraft.
Slett derfor klossen som modellerar tyngdekrafta i `gjenta for
alltid`{.blockcontrol}-løkka di, `endra [fartY v] med (-0.01)`{.b}.

- [ ] Me skal og gjera ein litt større endring i spelet. Me vil at verdsrommet
skal kjennast litt stort og uoversiktleg ved at når romskipet går ut av
skjermen på den eine sida skal det dukka opp på andre sida av skjermen.

  Dette gjer me ved ganske enkle `viss`{.blockcontrol}-testar. Det me må hugse
  på er at `x`-koordinatane på skjermen går fra `-240` til `240`, mens
  `y`-koordinatane ligg mellom `-180` og `180`. Sidan Scratch passar på at
  figurar ikkje går heilt av skjermen flyttar me dei litt innanfor skjermkanten:

  ```blocks
      når eg får meldinga [Nytt spel v]
      gjenta for alltid
          viss <(x-posisjon) < (-235)>
              endra x med (470)
          slutt
          viss <(x-posisjon) > (235)>
              endra x med (-470)
          slutt
          viss <(y-posisjon) < (-175)>
              endra y med (350)
          slutt
          viss <(y-posisjon) > (175)>
              endra y med (-350)
          slutt
      slutt
  ```


# Steg 2: Romskipet kan skyte {.activity}

*Romskipet vårt vil snart fly inn i ein asteroidesverm, så me må montera
rakettar som kan sprengje unna asteroidane.*

## Sjekkliste {.check}

- [ ] Lag ein ny figur som du kallar `Skot`. Denne teiknar du greit sjølv.
Eventuelt finst det til dømes nokre ball-figurar som kan brukast som kuler.
Bruk ein `set storleik`{.blocklooks}-kloss for at figuren skal verta passe
stor. Legg også på ein kloss for å `gøyme`{.blocklooks} figuren.

- [ ] Me vil bruka kloner slik at me kan skyte fleire skot. Først treng me
koden som lagar ein ny skotklone når du trykkjer mellomromtasten:

  Lag eit skript på skot-figuren som starter på `Nytt spel`-meldingen.
  Skriptet kan bestå av ein `gjenta for alltid`{.blockcontrol}-løkke, der du
  testar om mellomromtasten er trykka. Dersom eit skot skal avfyrast kan du
  først la skotet `gå til`{.blockmotion} romskipet og deretter peike i same
  retning som romskipet. Dette siste kan du gjera med ein kombinasjon av `peik i
  retning`{.blockmotion}, `retning av`{.blocksensing} og
  `vend`{.blockmotion}-klosser. Til slutt kan du `lage ein klon`{.blockcontrol}
  av figuren.

- [ ] For å passa på at berre éi melding vert sendt ut kvar gong du trykkjer
mellomromtasten kan me starta `viss`{.blockcontrol}-testen med å venta til
mellomromtasten er slept opp att. Dette trikset ser omtrent slik ut:

  ```blocks
      viss <tasten [mellomrom v] er trykt?>
          vent til <ikke <tasten [mellomrom v] er trykt?>>
          ...
      slutt
  ```

- [ ] No skal me kode oppførselen til skotet etter at det er avfyrt. Det kan
vera ganske enkelt. Når skotfiguren `startar som klon`{.blockcontrol} må den
`visast`{.blocklooks}, og deretter kan den flyttast i ei løkkje før den til
slutt vert sletta. Eksperimentér med farta og rekkjevidda på skotet ved å endre
på kor mange gonger løkkja blir gjenteke og kor mange steg figuren går inne i
løkkja.

- [ ] Til slutt vil me og at skota skal kunne forsvinne ut på den eine sida av
skjermen og dukke opp att på den andre. Til dette vil me bruke omtrent same
kode som for romskipet.

  For å kopiere skript mellom figurar kan du bruka ryggsekken på same måte som
  tidlegare. Ein litt raskare metode er å berre dra skriptet du vil kopiere til
  den figuren du vil kopiere til.

  Kopier koden for å *warp'e* rundt skjermen fra romskipet til skot-figuren.

- [ ] Me kan nesten bruka denne koden som den er. Den eineste endringa me treng
å gjera er at den skal starte på `når eg startar som klon`{.b} i staden for på
`når eg får meldinga [Nytt spel v]`{.b}, sidan denne oppførselen skal gjelde for
alle skotklonene.

- [ ] Prøv spelet ditt. No skal du kunne fly rundt i verdsrommet medan du skyt.


# Steg 3: Pass deg for asteroidane {.activity}

*Då er det på tide å laga ein asteroidesverm. Noko av det som er kult med
Asteroids er at asteroidane blir skutt i småbiter når du skyt på dei, og ein må
fortsatt passa seg for og skyte desse mindre asteroidane. Me vil kode dette ved
å bruke kloner i forskjellige storleikar.*

## Sjekkliste {.check}

- [ ] Lag ein asteroidefigur. Ein måte å gjera dette på er å teikne ein ny
figur med vektorgrafikk. Start med ein enkel firkant, og bruk deretter
`Bøy`-verktøyet for å leggje til fleire hjørnepunkt og flytta dei rundt som i
figuren under.

  ![Bilete av ein asteroidefigur i Scratch](flyttpunkt.png)

- [ ] Også for asteroidane vil me bruka kloner. Lag eit skript som
`gøymer`{.blocklooks} figuren og lager eit par asteroide-kloner tilfeldige
stader på skjermen når det mottek `Nytt spel`-meldingen.

- [ ] Når figuren `starter som klon`{.blockcontrol} vil me først at den
`peker`{.blockmotion} i ein tilfeldig retning og deretter `visast`{.blocklooks}.
Vidare kan den gå inn i ei løkkje med `gjenta til`{.blockcontrol} figuren
`rører romskipet`{.blocksensing}. Inne i løkkja let du først asteroiden `gå
nokre steg`{.blockmotion}. Deretter må du teste om asteroiden `rører eit
skot`{.blocksensing}. Viss den gjer det kan du laga asteroiden mindre med ein
kloss som liknar

  ```blocks
      set storleik til ((storleik) / (2)) %
  ```

  `Viss`{.blockcontrol} `storleiken`{.blocklooks} framleis er større enn til
  dømes 10 kan du laga eit par nye kloner av denne mindre asteroiden. Til slutt
  kan du `slette denne klonen`{.blockcontrol} uansett kor stor den er.

- [ ] Legg på ei melding eller ein `stopp`{.blockcontrol}-kloss slik at spelet
kan avsluttast etter at `gjenta til`{.blockcontrol}-løkka er ferdig, sidan
romskipet då har krasja i ein asteroide.

- [ ] Også asteroidane skal kunne fly ut av skjermen på ei side og dukke opp på
ei anna. Kopier derfor skriptet som fiksar dette frå skot-figuren på same måte
som tidlegare.

- [ ] Til slutt vil me og slette skot-klonene når dei treff asteroidane. Her må
me vera litt forsiktige så me ikkje slettar skot-klonene før asteroidane merkar
at dei er truffe. Dette kan me fiksa ved å leggje inn ei ørlita forseinking. Du
kan til dømes leggje inn kode som dette i løkkja som flyttar skot-figuren:

  ```blocks
      viss <rører [Asteroide v] ?>
          vent (0.01) sekund
          slett denne klonen
      slutt
  ```


# Steg 4: Vidareutvikling av spelet {.activity}

*Du har no laga ein enkel variant av Asteroids. Men prøv å gjere spelet
kjekkare ved å vidareutvikle det. Du bestemmer sjølv korleis du vil jobba
vidare, men nedanfor er nokre idear som kanskje kan vera til inspirasjon?*

## Idear til vidareutvikling {.check}

- [ ] Gi poeng når spelaren treff ein asteroide. Ein burde kanskje få fleire
poeng for å treffe dei små asteroidane? Det kan du fikse med ei utrekning
omtrent som

  ```blocks
      rund av ((100) / (storleik))
  ```

- [ ] Dersom du plasserar asteroidane heilt tilfeldig når eit nytt spel startar
er det ganske sannsynleg at romskipet krasjar i ein asteroide allereie før
spelet har starta. Det er ikkje noko kjekt. Ein måte å fikse det på vil vera å
først la asteroideklonen `gå til romskipet`{.blockmotion}, men deretter peike i
ein tilfeldig retning og `gå 100 til 200 steg`{.blockmotion} før det til slutt
`visast`{.blocklooks}.

- [ ] Spelet ser litt kulare ut om du teiknar fleire asteroidedrakter, og vel
ein av dei tilfeldig når ein klon vert laga.

- [ ] Dersom du klarar å skyte ned alle asteroidane burde ein kome vidare til
eit vanskeligare nivå. Kanskje med fleire asteroidar? Eller med asteroidar som
bevegar seg raskare? Eller deler seg i fleire deler når dei vert skotne?

  For å vite når du kan gå vidare til eit nytt nivå må du telje kor mange
  asteroidar som flyr rundt. Lag derfor ein variabel `Antal
  asteroider`{.blockdata} som du aukar med 1 når ein asteroide `startar som
  klon`{.blockcontrol}. Deretter må variabelen minka med 1 når klonen vert
  sletta.

  Vidare brukar du ein `Nivå`{.blockdata}-variabel som held styr på kva nivå
  spelaren har kome til.

- [ ] I det originale Asteroids-spelet dukka det og opp ein flygande tallerken
(UFO) innimellom. Denne måtte ein også passe seg for, men i motsetnad til
asteroidane kunne UFO-en skyte tilbake. Prøv å legg til ein slik UFO i spelet
ditt!
