---
title: 'Lunar Lander'
level: 4
author: 'Geir Arne Hjelle'
translator: 'Gro Anette Vestre'
language: nn
---


# Introduksjon {.intro}

Lunar Lander vart opprinneleg utvikla på slutten av 1970-tallet. Målet med
spelet er å landa eit romskip på månen. Sjølve kontrollen av romskipet vart
vidareført i spelet Asteroids som vart utgitt året etter.

![Illustrasjon av eit ferdig Lunar Lander-spel](lunar_lander.png)


# Oversikt over prosjektet {.activity}

*Mesteparten av kodinga av Lunar Lander skal du gjera sjølv. I Lunar Lander vil
me spesielt bruka litt tid på gjera den fysiske modelleringa av romskipet ganske
realistisk.*

## Plan {.check}

- [ ] Eit flygande romskip

- [ ] Me kjem til månen

- [ ] Klar for landing

- [ ] Begrensa drivstoff, fleire landingsplasser og andre utfordringer


# Steg 1: Eit flygande romskip {.activity}

Me skal nå programmera eit romskip som flyr rundt på skjermen. For å ha kontroll
på bevegelsen vil me bruka to variable, `fartX`{.blockdata} og
`fartY`{.blockdata}, som beskriv kor raskt romskipet bevegar seg henholdsvis
sidelengs og opp-og-ned. Ved å bruka begge desse samtidig vil romskipet kunna
bevega seg i alle retningar.

Utfordringa i programmeringa av spelet er at romskipet kan rotera uavhengig av
kva retning det faktisk flyr. Når spelaren trykker pil-opp for å bruka motoren
vil me gi romskipet ekstra fart i den retninga det peikar. Det betyr at me må
fordela farten i romskipet sin retning i kor mykje sidelengs fart det får, og
kor mykje av farten som går opp eller ned.

Dette virkar umiddelbart kanskje litt vanskelig, men det er akkurat dette dei
matematiske funksjonene `sinus` og `cosinus` gjer. I funksjonen nedanfor fortel
for eksempel `cosinus(vinkel)` oss kor lang den vannrette streken er i forhold
til den skrå streken.

![Bilete som syner samanhengen mellom vinkel, sinus og cosinus](sinus_cosinus.png)

## Sjekkliste {.check}

- [ ] Start eit nytt prosjekt. Slett kattefiguren.

- [ ] Legg til ein romskip-figur. Du kan gjerne bruke `Romfart/Spaceship`.

- [ ] Lag romskipet ganske lite. Du kan for eksempel bruke

  ```blocks
      set storleik til (20) %
  ```

  rett etter at det grønne flagget er klikket.

- [ ] Lag to nye variable, `fartX`{.blockdata} og `fartY`{.blockdata} som gjeld
      kun for denne romskip-figuren.

- [ ] Me lagar først hovedløkka som lar romskipet falle, kun påvirka av
      tyngdekrafta. Skriv denne koden:

  ```blocks
      når eg får meldinga [Nytt spel v]
      gå til x: (0) y: (175)
      peik i retning (90 v)
      set [fartX v] til (0)
      set [fartY v] til (0)
      gjenta for alltid
          endra [fartY v] med (-0.01)
          endra x med (fartX)
          endra y med (fartY)
      slutt
  ```

  Om du prøver spelet ditt nå skal romskipet falle stadig raskare nedover
  skjermen. Prøv å endre litt i klossen

  ```blocks
      endra [fartY v] med (-0.01)
  ```

  Det er denne som modellerer tyngdekraften. Om du forandrar verdien her vil
  romskipet falle raskare eller tregare, eller det kan til og med falle oppover
  om du lar tyngdekraften vera positiv.

- [ ] Me vil nå programmera kontrollen av romskipet. Først og fremst vil me at
      romskipet vender seg når me trykker på piltastene mot høgre og venstre.

  Legg til to `viss`{.blockcontrol}-blokker inne i `gjenta for
  alltid`{.blockcontrol}-løkken hvor du `vender`{.blockmotion} romskipet for
  eksempel `5` grader mot høgre eller venstre avhengig av kva piltast du trykker
  på.

- [ ] Når du trykker pil opp-tasten vil me at romskipet skal få litt ekstra fart
      i den retninga romskipet peikar. Som me snakka om tidlegare kan me bruke
      dei matematiske funksjonane sinus og cosinus for å få til dette. Legg og
      til denne blokken inne i `gjenta for alltid`{.blockcontrol}-løkken din.

  ```blocks
      viss <tasten [pil opp v] er trykt?>
          endra [fartX v] med ((0) - ([cos v] av (retning)))
          endra [fartY v] med ([sin v] av (retning))
      slutt
  ```

  Du finn både sinus og cosinus-funksjonene som valg på klossen

  ```blocks
      ([kvadratrot v] av (9))
  ```

  Me må bruke `((0) - ([cos v] av (retning)))`{.b} i stadenfor `([cos v] av
  (retning))`{.b} fordi `retning`{.blockmotion} i Scratch måles motsatt veg av
  korleis ein målar vinklar i matematikk.

- [ ] Prøv spelet ditt. Kan du styra romskipet rundt på skjermen? Dersom du
      synes romskipet flyr for raskt eller sakte kan du justera `endra
      fart`{.blockdata}-klossene, for eksempel slik,

  ```blocks
      endra [fartX v] med ((0.3) * ((0) - ([cos v] av (retning))))
      endra [fartY v] med ((0.3) * ([sin v] av (retning)))
  ```

  Pass på at du justerar begge klossane med det same tallet.


# Steg 2: Me kjem til månen {.activity}

*Nå skal me leggje til eit månelandskap der spelaren skal prøva å landa.*

## Sjekkliste {.check}

- [ ] Lag ein ny bakgrunn, der du teiknar eit passande månelandskap. Gjer det så
      lett eller vanskelig som du sjølv vil. Teikn og inn ein eller fleire
      landingsplasser der romskipet skal landa. Me vil bruka `rører
      fargen`{.blocksensing}-klosser for å sjekka landinga seinare, så det
      enklaste er å bruka ein farge for landskapet og ein annan for
      landingsplassen.

- [ ] For at romskipet skal slutta å fly når det treff bakken kan du byte ut
      `gjenta for alltid`{.blockcontrol}-løkk med ein `gjenta
      til`{.blockcontrol}-løkke der du testar på om romskipet `rører
      fargen`{.blocksensing} du har brukt på landskapet eller på
      landingsplassen.

- [ ] Legg og til ein `send meldinga [Sjekk landing v]`{.b} rett etter `gjenta
      til`{.blockcontrol}-løkken.

- [ ] Prøv spelet ditt igjen. Du skal nå kunne fly rundt heilt til romskipet
      kjem nær bakken.


# Steg 3: Klar for landing {.activity}

*Me vil til slutt sjekka kor og korleis romskipet landa.*

## Sjekkliste {.check}

- [ ] Når me sjekkar landinga til romskipet vil me skilje mellom tre
      forskjellige tilfeller:

  __1__: Romskipet landa utanfor landingsplassen (kræsjet).

  __2__: Romskipet landa på landingsplassen, men landa enten på skrå (eller
  opp-ned) eller for raskt.

  __3__: Romskipet landa perfekt på landingsplassen.

  Lag eit nytt skript på romskipet som starter når det mottar meldingen `Sjekk
  landing`. Under denne klossen må du bruke `viss`{.blockcontrol}- og `viss
  elles`{.blockcontrol}-klosser som tester for dei tre tilfella. Du kan for
  eksempel sei at landinga er perfekt dersom romskipet lander på
  landingsplassen, `fartY`{.blockdata} er større enn `-1.5` og
  `retning`{.blockmotion} er mellom `80` og `100`.

- [ ] Finn ein måte å fortelje spelaren korleis romskipet landa. Det enklaste er
      kanskje å berre bruka ein `sei`{.blocklooks}-kloss. Men du kan og bruka
      lydeffekter, forskjellige draktar eller kanskje ein tekstplakat som dukkar
      opp.


# Steg 4: Vidareutvikling av spelet {.activity}

*Du har nå laga ein enkel variant av Lunar Lander. Men prøv å gjera spelet
kjekkare ved å vidareutvikla det. Du bestem sjølv korleis du vil jobba vidare,
men nedanfor er nokre idear som kanskje kan vera til inspirasjon?*

## Idear til vidareutvikling {.check}

- [ ] Lag fleire landingsplasser. Kanskje nokon kan vera vanskeligare enn andre
      å lande på (enten på grunn av terrenget eller fordi sjølve landingsplassen
      er mindre).

- [ ] Lag fleire bakgrunnar eller brett. Du kan enten la spelaren velje seg ein
bakgrunn å spela på i starten av spelet, eller gå vidare frå brett til brett
etterkvart som spelaren klarar å landa.

- [ ] Du kan og bruka fleire bakgrunnar som eit brett. Dersom romskipet flyr ut
      av skjermen på høgre sida kan du la det dukke opp igjen på venstre sida av
      ein annan bakgrunn, og motsatt.

- [ ] Prøv å animera bruken av motoren. For eksempel, kan du laga ein kopi av
      den flyvande romskip-drakten, og endre den som følger. Klikk først på
      romskipet, og deretter på den nye knappen som dukker opp nederst i
      knapperekka (markert med rødt i figuren til venstre). Denne vil dela opp
      romskip-figuren i mindre deler. Vel ein passande flammefarge, og bruk
      malingsspannet til å fargeleggje dei tre finnane på romskipet slik at det
      ser ut som flammer som kjem frå motoren.

  ![Bilete av ein kopi av romskipet med flammer på](animer_romskip.png)

- [ ] Ein av utfordringane i det originale Lunar Lander-spelet var at spelaren
      berre hadde begrensa drivstoff tilgjengeleg. Du kan leggje til dette i
      ditt spel ved å laga ein `Drivstoff`{.blockdata}-variabel som du lar bli
      stadig mindre etterkvart som spelaren trykker på piltastane. Dersom
      romskipet går tomt for drivstoff kan du ignorere tastetrykka frå spelaren
      og berre la romskipet sveva til det til slutt kræsjer.

- [ ] Du kan laga forskjellige bonusting som spelaren kan plukka opp. For å
      gjøre det litt utfordrande kan du la desse liggje på måneoverflaten slik
      at spelaren må manøvrera forsiktig for å få tak i dei. Eksempler på slike
      bonusting kan vera ekstra drivstoff, bonuspoeng, større landingsplass og
      så vidare.

- [ ] Ein større endring i spelet kan vera at landingsplassen er skjult under
      bakken når spelet startar og spelaren må grave denne fram ved å sleppe
      bomber frå romskipet. Du kan implementera dette for eksempel ved bruk av
      nokre av klossane under `Penn`{.blockpen}-kategorien.
