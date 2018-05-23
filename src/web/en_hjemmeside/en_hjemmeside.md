---
title: 'HTML: Vi bygger hjemmeside'
level: 1
logo: ../../assets/img/ccuk_logo.png
author: 'Oversatt fra [Code Club UK](//codeclub.org.uk)'
translator: 'Marius Krakeli'
license: '[Code Club World Limited Terms of Service](https://github.com/CodeClub/webdev-curriculum/blob/master/LICENSE.md)'
language: nb
---

# Introduksjon {.intro}

I oppgaven [Introduksjon til Web](../introduksjon_til_web/introduksjon_til_web.html) kan du lære om *HTML*-tagger, og i denne oppgaven skal du bruke HTML-taggene i din første hjemmeside. La oss begynne med en gang!

# Steg 1: Åpne siden som heter om meg {.activity}

## Aktiviteter {.check}

- [ ] Åpne et __tekstprogram__.
- [ ] Last ned [internett.zip](../introduksjon_til_web/internett.zip) hvis du ikke har gjort det allerede igjennom [Introduksjon til Web](../introduksjon_til_web/introduksjon_til_web.html).
- [ ] Åpne filen som heter `om_meg.html`. Filen inneholder bittelitt HTML kode for å hjelpe deg med å komme igang, men du må skrive resten selv.


# Steg 2: Lag en hjemmeside om deg selv {.activity}

### Om å gjøre feil

Feil skjer ofte. Det er veldig lett å gjøre dem i HTML fordi du må huske å lukke hver tag, og åpnings-taggen og avslutnings-taggen er litt annerledes. La oss prøve å gjøre noen feil for å se hvordan nettleseren prøver å forstå meningen av koden vår, selv om vi ikke har skrevet den perfekt.

## Aktiviteter {.check}

- [ ] La oss ta listen av ting vi liker som et eksempel. En av feilene som ofte skjer, er å glemme __avslutnings-taggen__, så la oss fjerne `</ul>` for å se hvordan det påvirker siden. Lagre filen og oppdater den i nettleseren.

- [ ] Inspiser med [X-Ray Goggles](https://goggles.mozilla.org/). Skjønner du hva som kan ha skjedd? Etter at vi fjernet avslutnings-taggen vet nettleseren rett og slett ikke at listen er avsluttet og derfor skjer det som skjedde nå.

- [ ] Legg til avslutnings-taggen `</ul>` igjen og lagre siden. Oppdater siden og alt skal være tilbake til normalt.

- [ ] Tagger må være stavet riktig for at nettleseren skal forstå dem. Hva skjer hvis vi gjør en skrivefeil?

- [ ] Finn `<h1>` taggen. La oss se hva som skjer hvis vi forandrer den til `<d1>`. Lagre filen og oppdater siden i nettlesern.

__Hva skjedde?__ Siden nettleseren ikke vet hva du mener med denne taggen så kan den ikke lenger forstå at det skal være en overskrift, så den bruker ikke lenger en større tekst til å vise hvor viktig akkurat den teksten er.

- [ ] Bytt `<d1>` tilbake til `<h1>` og lagre igjen.


- [ ] Finn en av `<img>` taggene. Vi har akkurat prøvd å feilstave en tagg og nettleseren var ikke sikker på hva den skulle gjøre med det. Men hva hvis vi feilstaver attributtet?

Inne i `<img>` taggen har vi `src` og `alt` attributter:

```html
<img src="katt.png" alt="Katt">
```
`src` er hvor bildet blir hentet fra og hva det heter. I dette tilfellet ligger bildet på samme sted som `om_meg.html`. Hadde bildet ligget i en annen mappe måtte vi ha spesifisert det, for eksempel slik: `bilder/katt.png`.

`alt` er en tekst som kommer tilsyne dersom bildet ikke vises. Dette gjør at, for eksempel, blinde kan få lest opp hva det er bilde av via en skjermleser. Bildeteksten kan også hjelpe deg med å finne feil dersom et bilde ikke vises på nettsiden din.

- [ ] Prøv å endre `src` til noe annet. Lagre dokumentet og oppdater i nettleseren.

- [ ] Hva skjedde? __Kattungen er borte!__ Plutselig vet ikke nettleseren hvor den skal se etter bildet den skal vise - den ser etter filnavnet i `src` attributten som ikke lenger er der.

- [ ] Endre det tilbake til `src` så vi kan fortsette å se på kattungen.

- [ ] Nå fjern det andre anførselstegnet (`" `) fra `alt` attributtet av dette bildet: den etter teksten, slik at du ender opp med dette:

```html
<img src="katt.png" alt="Katt />
```

- [ ] Lagre og oppdater i nettleseren.

Den neste taggen forsvant. Hvorfor? Nettleseren vil tro at alt etter `alt ="` og før neste sitatmerke (` "`) er ekstra tekst for dette bildet, inkludert slutten av bildekoden og neste åpnings-taggen.

- [ ] Rett opp feilen slik at alt fungerer igjen.

<toggle>
  <strong>Hint</strong>
  <hide>

alt="Katt"

  </hide>
</toggle>


Vi har nå gjort noen vanlige feil og vi har sett at noen ganger kan en enkelt feil gjøre at nettleseren ikke forstår hva vi vil. Men mesteparten av tiden vil nettleseren prøve å vise oss noe uansett. Vi så at nettleseren viste oss tekst selvom den ikke forstod at det var en overskrift vi prøve å vise. Så den hjelper oss litt underveis og prøver å vise det vi lager så godt den kan. Men vi har sett at enkelte feil gjør det veldig forvirret.

# Steg 3: Lag en ny side og link til den {.activity}

La oss lage en ny side. Åpne `om_meg_side_2.html`.  Den har litt mindre kode en den andre siden du jobbet med, men jeg er sikker på at du kan legge til mer kode selv nå.


## Utfordringer til deg: {.challenge}
- [ ] Legg til en overskrift som vil fungere som tittelen på denne siden.
- [ ] Denne siden kan handle om kjæledyret ditt, din favoritt hobby eller vennene dine og deres hobbyer.
- [ ] Lag en liste over ting kjæledyret liker, hvis siden er om et kjæledyr.
## <!-- Challenge slutt -->

__Er du ferdig? Flott! La oss nå linke de to sidene du har laget sammen.__

Når vi har linket til deler av den samme siden, kunne vi bare peke linken til en bestemt id på siden, som dette:

```html
<a href="#kattunge"> Klikk for å se en kattunge </a>
```

Som da tok deg til noe sånt som dette:

```html
<div id="kattunge">
  <img src="kattunge.jpg" alt="Dette er en kattunge." />
</div>
```
Hvis du vil koble til en annen side, trenger vi ikke å inkludere hashsymbolet (`#`), men i stedet må vi si hvilken fil vi vil linken skal ta oss til.

Så for å linke fra `om_meg_side_2.html` til `om_meg.html` skriver vi slik:

```html
<a href="om_meg.html"> Gå til Om Meg siden </a>
```

Du kan endre anker teksten til noe annet, som tittelen på siden hvis du har endret det.

For å linke tilbake fra `om_meg.html` til `om_meg_side_2.html` må du skrive det slik:

```html
<a href="om_meg_side_2.html"> Gå til min andre side </a>
```

__Gratulerer! Du har laget ditt eget nettsted.__

## Ting du kan prøve {.challenge}

- [ ] Hvordan kan du linke til en annen side på nettet? (Hint: prøv å legge til `http://` og deretter adressen til nettstedet du vil koble til)
- [ ] I likhet med forslaget ovenfor, hvordan ville du legge til et bilde fra et sted på nettet i stedet for fra datamaskinen? (Hint: igjen, prøve å legge til `http://` og adressen til bildet)
- [ ] Prøv å publiser nettsiden din på internett: [Publiser nettsiden din!](../publiser/publiser.html)
