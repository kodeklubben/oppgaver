---
title: 'Rotasjon rundt eigen akse'
level: 1
author: 'Carl A. Myrland'
translator: 'Stein Olav Romslo'
language: nn
---


# Introduksjon {.intro}

I denne oppgaven skal vi importere en geometrisk figur og deretter
`rotere`{.blockmotion} den.

![Bilde av en trollmann hatt](Geometri.png)


# Steg 1: Vi roterer en likebeint trekant {.activity}

*For å gjere det enkelt å kome i gang skal me hente inn ein figur frå
 Scratch-biblioteket. Denne figuren er tilnærma lik ein likebeint trekant.*

## Sjekkliste {.check}

- [ ] Start eit nytt prosjekt.

- [ ] Slett kattefiguren ved å høgreklikke på den og velje `slett`.

- [ ] Legg til ein ny figur. Klikk på ![Vel figur frå
  biblioteket](../bilder/hent-fra-bibliotek.png)-knappen og vel
  trollmannshatten. Me har brukt `Ting/Wizard Hat`-figuren.

- [ ] Gi den nye figuren namnet `Hattulf` ved å klikke på `i`.

- [ ] Før me startar med sjølve oppgåva skal me leggje inn ein hjelpefunksjon i
  tilfelle noko uventa skjer:

  ```blocks
  når [n v] vert trykt
  vis
  peik i retning [90 v]
  gå til x: (0) y: (0)
  ```

- [ ] Viss noko uventa skjer kan du berre trykke på `N`-tasten, så vil Hattulf
  gå tilbake til utgangspunktet slik at du kan prøve på nytt.

No skal me gi Scratch beskjed om å `rotere`{.blockmotion} hatten 90 gradar.

- [ ] Legg til følgjande skript på `Hattulf`-figuren din.

  ```blocks
  når @greenFlag vert trykt på
  snu @turnRight (90) gradar
  ```

## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

- [ ] Kva skjer når du trykkar på det grøne flagget?

- [ ] Roterer hatten som forventa?

- [ ] Kva trur du skjer om du trykker på det grøne flagget ein gong til? I kva
  retning vil toppen av hatten peike?

- [ ] Kor mange gonger må du be hatten om å rotere før den er tilbake til
  utgangspunktet?

## Sjekkliste {.check}

Rotasjon er jo morosamt! Men at ting roterer med 90 gradar om gongen er jo litt
keisamt og unaturleg.

- [ ] Halver talet på gradar hatten skal rotere kvar gong:

  ```blocks
  når @greenFlag vert trykt på
  snu @turnRight (45) gradar
  ```

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Kor mange gonger må du trykkje på hatten for at den skal rotere heile
  vegen rundt no?

- [ ] Fortset å halvere talet på gradar hatten skal rotere. Prøv å finne ein
  samanheng mellom kor mange gradar den roterast og kor mange gonger du må
  trykkje på det grøne flagget for at den skal rotere heilt rundt.

Du oppdagar kanskje at det begynner å bli veldig mange klikk etter kvart?


# Steg 2: Litt meir action, takk! {.activity}

Heldigvis kan me bruke ligg programmeringsmagi og få datamaskina til å gjere
jobben for oss!

## Sjekkliste {.check}

- [ ] Me legg til ein `styring`{.blockcontrol}-kloss som ber hatten om å rotere
  eit bestemt antal gonger:

  ```blocks
  når @greenFlag vert trykt på
  gjenta (8) gongar
  snu @turnRight (45) gradar
  ```

- [ ] Tips: For kvar gong du halverer vinkelen, så må du doble talet på
  repetisjonar for at hatten skal rotere like langt.


# Steg 3: The final countdown {.activity}

- [ ] Du veit kanskje at ein rotasjon heilt rundt er 360 gradar. Viss du fortset
  å halvere talet på gradar forbi `1,40625`, så vil du oppdage at gradene blir
  mindre enn `1`, og rotasjonen må bli repetert `512` gonger. Sjølv om det
  sjølvsagt er mogleg, og absolutt nødvendig i nokre samanhengar, er det ikkje
  nødvendig no. Me tek ein snarveg, og vil få Hattulf til å rotere `1` grad
  `360` gonger.

  ```blocks
  når @greenFlag vert trykt på
  gjenta (360) gongar
  snu @turnRight (1) gradar
  ```

## Test prosjektet {.flag}

__Klikk på det grønet flagget.__

- [ ] Roterer hatten heile vegen om seg sjølv når du trykkar på det grøne
  flagget?

- [ ] Me har sett talet på gradar hatten roterer per gong til `1`. Kor mange
  gonger må Hattulf rotere for å gjere to fulle rotasjonar? Kva med tre og ein
  halv? Ser tala kjent ut?

## Avslutning

- [ ] Lagre prosjektet ved å gi det eit namn, til dømes `Geometri 1`.
