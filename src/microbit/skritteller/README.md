---
title: Skritteller
author: Erik Sagatun
language: nb
---
# Om oppgaven {.activity}

I denne oppgaven lager elevene en skritteller med micro:bit. De bruker akselerometeret (hendelsen `når ristes`{.microbitinput}) til å telle skritt, lagrer antallet i en variabel, og bygger videre med knapper, nullstilling og et mål med lyd. Oppgaven gir en konkret sammenheng mellom kode og kropp: elevene kan gå, telle selv og sammenligne med det micro:biten viser.

## Oppgaven passer til: {.check}

**Fag**: Matematikk, Naturfag, Programmering, Teknologi

**Anbefalte trinn**: 5.-7. klasse

**Tema**: Blokkbasert, Elektronikk, Stegbasert

**Tidsbruk**: Ca. 60 minutter for steg 1–4, pluss 15–30 minutter til utfordringene.

## Kompetansemål {.challenge}

- [ ] **Naturfag, 7. trinn**: utforske, lage og programmere teknologiske systemer som består av deler som virker sammen

- [ ] **Naturfag, 7. trinn**: designe og lage et produkt basert på brukerbehov

- [ ] **Matematikk, 5. trinn**: lage og programmere algoritmer med bruk av variabler, vilkår og løkker

## Forslag til læringsmål {.challenge}

- [ ] Elevene kan bruke en variabel til å telle og vise et antall.

- [ ] Elevene kan bruke hendelser fra sensorer og knapper til å styre et program.

- [ ] Elevene kan bruke en betingelse (`hvis`{.microbitlogic}) til å sjekke om et mål er nådd.

- [ ] Elevene kan forklare hvordan et akselerometer brukes i en skritteller, og hvorfor den ikke alltid teller helt riktig.

## Forslag til vurderingskriterier {.challenge}

Det er mange ulike måter man kan vurdere et programmeringsprosjekt på, og her må en selv vurdere hva som er den beste måten ut ifra hvilket fag man jobber i, hvilken aldersgruppe og hvilket nivå elevene er på, hva man ønsker å teste og hvor mye tid man har til rådighet. I vårt [lærerdokument](https://github.com/kodeklubben/oppgaver/wiki/Hvordan-undervise-i-og-vurdere-programmering){target=_blank} har vi blant annet beskrevet ulike måter dette kan gjøres på, i tillegg til en del andre nyttige tips til hvordan man underviser i programmering.

## Forutsetninger og utstyr {.challenge}

- [ ] **Forutsetninger**: Elevene bør ha prøvd MakeCode før, for eksempel med en enkel oppgave som viser navnet deres på skjermen. Det er en fordel om de har laget en variabel tidligere, men det er ikke nødvendig.

- [ ] **Utstyr**: En datamaskin med nettleser, én micro:bit med USB-kabel per elev eller elevpar, og en batteripakke (2 × AAA). Teip eller strikk for å feste micro:biten på skoen.

## Fremgangsmåte

Her er tips, erfaringer og vanlige utfordringer til de ulike stegene i oppgaven.

# Steg 1: Tell skritt {.activity}

- [ ] Noen elever legger `vis tall`{.microbitbasic} utenfor `når ristes`{.microbitinput}. Da vises tallet bare én gang. Be dem se på hvilken blokk koden ligger inni.

- [ ] I simulatoren må elevene klikke på RIST-knappen over micro:biten for å teste.

# Steg 2: Vis tallet bare når du vil {.activity}

- [ ] Dette er et godt sted å snakke om at micro:biten gjør én ting om gangen: mens `vis tall`{.microbitbasic} ruller, kan nye ristinger gå tapt. Ta gjerne en kort felles prat om hvorfor.

- [ ] Koordinatene på skjermen starter på 0, så midten er x = 2 og y = 2. Mange gjetter 3.

# Steg 3: Nullstill telleren {.activity}

- [ ] Elevene forveksler ofte `sett`{.microbitvariables} og `endre`{.microbitvariables}. `sett skritt til 0` gir en fast verdi, mens `endre skritt med 1` legger til.

# Steg 4: Sett deg et mål {.activity}

- [ ] Be elevene sette `mål` til 5 mens de tester. Det sparer tid og støy i klasserommet.

- [ ] Bruker elevene større enn eller lik i stedet for lik, spilles melodien for hvert skritt etter målet. Det kan bli en fin diskusjon om forskjellen.

- [ ] Gå gjerne ut og la alle gå nøyaktig 20 skritt. Samle resultatene i en tabell på tavla. Det gir en naturlig kobling til feilkilder og måleusikkerhet i naturfag.

## Variasjoner {.challenge}

- [ ] Elevene kan måle sin egen skrittlengde og regne om skritt til meter.

- [ ] Elevene kan bruke `radio`{.microbitradio} til å sende antall skritt til en felles micro:bit og lage en klassekonkurranse.

- [ ] Elevene kan registrere antall skritt i friminuttet hver dag i en uke og lage et diagram i matematikktimen.

## Eksterne ressurser {.challenge}

- [ ] [MakeCode for micro:bit](https://makecode.microbit.org){target=_blank}

- [ ] [Læreplan i naturfag (NAT01-04) på udir.no](https://www.udir.no/lk20/NAT01-04){target=_blank}
