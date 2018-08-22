---
title: "HTML: Me byggjer heimeside"
author: "Omsett frå [Code Club UK](//codeclub.org.uk)"
translator: Stein Olav Romslo
language: nn
---


# Introduksjon {.intro}

I oppgåva [Introduksjon til
Web](../introduksjon_til_web/introduksjon_til_web_nn.html) kan du lære om
*HTML*-taggar, og i denne oppgåva skal du bruke dei i den fyrste heimesida di!
La oss starte med ein gong!


# Steg 1: Åpne sida som heiter "Om meg" {.activity}

## Aktivitetar {.check}

- [ ] Åpne eit __tekstprogram__.

- [ ] Last ned [internett.zip](../introduksjon_til_web/internett.zip) viss du
  ikkje allereie har gjort det gjennom oppgåva [Introduksjon til
  Web](../introduksjon_til_web/introduksjon_til_web_nn.html)

- [ ] Åpne fila som heiter `om_meg.html`. Fila inneheldt bittelitt HTML-kode for
  å hjelpe deg med å kome i gang, men du må skrive reisten sjølv.


# Steg 2: Lag ei heimeside om deg sjølv {.activity}

### Om å gjere feil

Feil skjer ofte. Det er veldig lett å gjere dei i HTML fordi du må hugse å lukke
kvar tag, og åpnings-taggen og avslutnings-taggen er litt ulike. La oss prøve å
gjere nokre feil for å sjå korleis nettlesaren handterer det. Den kjem til å
prøve å forstå meininga av koden vår, sjølv om me ikkje har skrive den perfekt.

## Aktivitetar {.check}

- [ ] La oss ta lista over ting me likar som eit døme. Ein av feila som ofte
  skjer er å gløyme avslutnings-taggen, så la oss fjerne `</ul>` for å sjå
  korleis det påverkar sida. Lagre fila og oppdater den i nettlesaren.

- [ ] Inspiser med [X-Ray Goggles](https://goggles.mozilla.org/). Forstår du kva
  som kan ha skjedd? Etter at me fjerna avslutnings-taggen forstår ikkje
  nettlesaren at lista er avslutta, og difor skjer det som skjedde no.

- [ ] Legg til avslutnings-taggen `</ul>` att og lagre sida. Oppdater sida og
  alt skal vere tilbake til normalt.

- [ ] Taggar må vere stava riktig for at nettlesaren skal forstå dei. Kva skjer
  om me gjer ein skrivefeil?

- [ ] Finn `<h1>`-taggen. La oss sjå kva som skjer viss me forandrar den til
  `<d1>`. Lagre fila og oppdater sida i nettlesaren.

__Kva skjedde?__ Sidan nettlesaren ikkje veit kva du meiner med taggen, så kan
den ikkje forstå at det er ei overskrift. Då brukar den heller ikkje større
tekst til å vise kor viktig akkurat denne teksten er.

- [ ] Bytt `<d1>` attende til `<h1>` og lagre att.

- [ ] Finn ein av `<img>`-taggane. Me har akkurat prøvd å feilstave ein tagg,
  slik at nettlesaren ikkje visste kva den skulle gjere med det. Men kva om me
  feilstavar attributten?

Inne i `<img>`-taggen har me `src`- og `alt`-attributtar:

```html
<img src="katt.png" alt="Katt">
```

`src` er der biletet blir henta frå og kva det heiter. I dette tilfellet ligg
biletet på same stad som `om_meg.html`. Hadde biletet vore i ei anna mappe måtte
me ha spesifisert det, til dømes slik: `bilete/katt.png`.

`alt` er ein tekst som kjem til syne viss biletet ikkje visast. Dette gjer at
til dømes blinde kan få lest opp kva det er bilete av ved hjelp av ein
skjermlesar. Bileteteksten kan òg hjelpe deg å finne feil viss eit bilete ikkje
kjem til syne på nettsida di.

- [ ] Prøv å endre `src` til noko anna. Lagre dokumentet og oppdater i
  nettlesaren.

- [ ] Kva skjedde? __Kattungen er borte!__ Plutseleg veit ikkje nettlesaren kor
  den skal sjå etter biletet den skal vise. Den leitar nemleg fyrst etter
  `src`-attributten som ikkje er der lengre.

- [ ] Endre det attende til `src` så me kan sjå kattungen att.

- [ ] Fjern det andre hermeteiknet (`"`) frå `alt`-attributten for biletet,
  altså det etter teksten, slik at du ender opp med dette:

```html
<img src="katt.png" alt="Katt />
```

- [ ] Lagre og oppdater i nettlesaren.

Den neste taggen forsvann. Kvifor? Nettlesaren vil tru at alt etter `alt ="` og
før neste hermeteikn er ekstra tekst for dette biletet, inkludert slutten av
biletekoden og den neste åpnings-taggen.

- [ ] Rett opp feilen slik at alt fungerer att.

<toggle>
  <strong>Hint</strong>
  <hide>

alt="Katt"

  </hide>
</toggle>

No har me gjort nokre vanlege feil, og me har sett at nokre gonger kan ein enkel
feil gjere at nettlesaren ikkje forstår kva me vil. Men mesteparten av tida vil
nettlesaren prøve å vise oss noko likevel. Me såg at nettlesaren viste oss tekst
sjølv om den ikkje forsto at det skulle vere ei overskrift. Så den hjelper oss
litt undervegs og prøver å vise det me lagar så godt den kan. Men me har òg sett
at enkelte feil gjer den veldig forvirra.


# Steg 3: Lag ei ny side og lenk til den {.activity}

La oss lage ei ny side. Åpne `om_meg_side_2.html`. Den har litt mindre kode enn
den andre sida du jobba med, men du kan heilt sikkert leggje til meir kode sjølv
no.

## Utfordringar til deg: {.challenge}

- [ ] Legg til ei overskrift som vil fungere som tittelen på denne sida.

- [ ] Denne sida kan handle om kjæledyret ditt, favoritthobbyen din eller venene
  dine og hobbyane deira.

- [ ] Lag ei liste over ting kjæledyret likar viss sida er om eit kjæledyr.

## <!-- Utfordring slutt -->

__Er du ferdig? Flott! No skal me lenke saman dei to sidene du har laga.__

Når me har lenka til delar av den same sida har me berre lenka til ein bestemt
ID på sida, slik som dette:

```html
<a href="#kattunge"> Klikk for å sjå ein kattunge </a>
```

som då tok deg til noko som dette:

```html
<div id="kattunge">
  <img src="kattunge.jpg" alt="Dette er ein kattunge." />
</div>
```

Viss du vil lenke til ei anna side treng du ikkje å ta med `#`, men du må seie
kva fil du vil lenka skal ta oss til.

Så for å lenke frå `om_meg_side_2.html` til `om_meg.html` skriv me dette:

```html
<a href="om_meg.html"> Gå til "Om meg"-sida </a>
```

Du kan endre ankerteksten til noko anna, til dømes tittelen på sida viss du
endra den.

For å lenke tilbake frå `om_meg.html` til `om_meg_side_2.html` må du skrive det
slik:

```html
<a href="om_meg_side_2.html"> Gå til den andre sida mi </a>
```

__Gratulerer! Du har laga din eigen nettstad!__

## Ting du kan prøve {.challenge}

- [ ] Korleis kan du lenke til ei anna side på nettet? __Hint:__ Prøv å leggje
  til `http://` og så adressa til nettstaden du vil lenke til.

- [ ] På same måte som over, korleis ville du lagt til eit bilete frå ein stad
  på nettet i staden for frå datamaskina? __Hint:__ Prøv å legg til `http://` og
  adressa til biletet.

- [ ] Prøv å publisere nettsida di på Internett: [Publiser nettsida
  di!](../publiser/publiser_nn.html)
