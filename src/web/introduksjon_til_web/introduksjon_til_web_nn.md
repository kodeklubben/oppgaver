---
title: "HTML: Introduksjon til Web"
author: "Omsett frå [Code Club UK](//codeclub.org.uk)"
translator: Stein Olav Romslo og Susanne Rynning Seip
language: nn
---


# Introduksjon {.intro}

I denne oppgåva skal du få ein enkel introduksjon til Internett og korleis
nettsider og HMTL fungerer. I denne oppgåva er det viktig at du tek deg god tid
og les oppgåvene nøye.

Har du nokon gong lurt på korleis Internett fungerer? Klart du har! I dag skal
du lære korleis ein lagar nettsider slik at du kan hjelpe til med å byggje det.
Nettsider blir skrive ved å bruke **HTML**, som er ei forkorting for **HyperText
Markup Language**. Du kjem til å finne ut meir om dette etter kvart som du
byggjer sida di.

Filene du blir bedt om å åpne i denne oppgåva finn du i
[internett.zip](internett.zip). Last ned fila og pakk den ut før du startar.
Viss du ikkje får til å pakke ut fila kan du laste ned programmet
[7zip](http://www.7-zip.org/) som pakkar ut zip-filer.


# Steg 1: Kva er nettsider? {.activity}

## Aktiviteter {.check}

- [ ] Åpne ein **teksteditor**, til dømes teksteditoren [Atom](http://atom.io),
  [Brackets](http://brackets.io/), NotePad eller
  [NotePad++](https://notepad-plus-plus.org/).

- [ ] Lag eit nytt dokument.

- [ ] Skriv noko! Til dømes `Hei! Eg heiter ...`.

- [ ] Lagre fila med filnamnet `hei.txt`.

- [ ] Finn fila di i filhandsamaren og åpne den. Den blir åpna i eit
  tekstprogram, og det er jo ikkje så spanande.

- [ ] Lagre fila på nytt til filnamnet `fil.html` med *Lagre som*.

- [ ] Åpne fila på nytt.

Kva program vart fila åpna i denne gonger? Nettlesaren er eit speselt program
som veit korleis tekstfiler skrive ved hjelp av HTML skal lesast. Me har ikkje
skrive noko HTML endå, men me har laga ei HTML-fil. Førebels er det berre vanleg
tekst i fila, men det bryr ikkje nettlesaren seg om! Så lenge du gir den ei
`.html`-fil, så vil den gjere sitt beste for å vise deg kva som er i fila. Det
same gjeld når ei HTML-fil inneheldt feil, då vil nettlesaren prøve å finne ut
korleis fila skal visast uansett.

### Korleis kan me sjå desse filene?

Når du skriv inn ei adresse i nettlesaren din blir førespurnaden sendt vidare
til ei datamaskin som alltid står på og er innstilt for å la deg sjå nettsidene
som bur i den. Denne datamaskina kallast ein *server*. Når den får ein
førespurnad frå datamaskina di ser den etter alle dei nødvendige filene, til
dømes `.html`-fila, og sender deg den saman med alt det andre nettsida treng,
som bilete og videoar.

### Kan eg få denne sida, takk?

![Illustrasjon av korleis datamaskina di ber serveren om å få sjå ei side, og så
får alle filene som trengst.](webdialog.png)


# Steg 2: Kva er HTML? {.activity}

HTML er eit **markeringsspråk** - det tyder at det brukast til å beskrive kva
ting er. Sjølv om nettlesaren prøver å gjere sitt beste for å vise ting, så
hjelper det at den veit kva tinga er frå før. For å fortelje det til nettlesaren
brukar me **taggar**. Dei ser slik ut:

```html
<p>Dette er litt tekst.</p>
```

`<p>` er ein forkorting for **paragraph**, som er det engelske ordet for
_paragraf_ eller _avsnitt_. Den har ei åpning, som er `<p>`, og ei tilsvarande
avslutning med skråstrek, `</p>`. Då veit nettlesaren at alt mellom dei to
taggane er eit avsnitt med tekst.

Taggar kan òg ha **attributtar**, som er informasjon om elementet. La oss sjå på
link-taggen:

```html
<a href="http://kodeklubben.no/">Besøk nettsida til Kodeklubben</a>
```

`<a>` står for **anchor**, som tyder _anker_, det lenker vart kalla før. Den har
åpninga `<a>` og avslutninga `</a>`. I åpningstaggen legg me til attributten
`href` med verdien `http://kodeklubben.no/`. `href` står for
*hypertekst-referanse*. Ein tekst som lenka til andre tekstar vart før kalla
*hypertekst*, fordi den kunne peike til bilete, lyd og andre tekstar. Det gjorde
*anker* annleis enn vanleg tekst. `href` fortel nettlesaren kor lenka skal føre
deg, og teksten mellom taggane blir synleg som ei lenke.

## Aktivitetar {.check}

- [ ] Åpne fila `side.html` frå [internett.zip](internett.zip) i nettlesaren (Chrome).

- [ ] Høgreklikk på sida og velg "Inspiser" ("Inspect" på engelsk). Då åpnar utviklarverktøyet til nettlesaren din.

- [ ] Klikk på ikonet øvst til venstre som ser ut som ei pil i ein firkant (![Bilete av "Pick element" ikon](pickelement.png)).

- [ ] Beveg så musa rundt på sida. Då kan du sjå delar av sida lyse opp og sjå kva
  taggar delane er laga av.

- [ ] Trykk på noko for å sjå kodesnutten det er laga av.

- [ ] Trykk på knappen **ESC** når du er ferdig.


# Steg 3: Fleire taggar {.activity}

Me har allereie prata om taggane `<p>` og `<a>`, men det finst mange fleire. Her
er nokre taggar som ofte brukast:

- `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`: Overskrifter med ulik
  storleik.

- `<ol>`: Sortert liste.

- `<ul>`: Usortert liste.

- `<li>`: Eit punkt i ei liste.

- `<hr>`: Horisontal linje.

- `<div>`: Ein boks for å gruppere ting.

- `<img>`: Eit bilete. Bilete er litt spesielle, fordi i motsetnad til dei
  fleste andre taggane har **ikkje** `<img>` ein avslutning `</img>`. For å vise
  eit bilete brukar me ein attributt `src="lenke til biletet"`, men dette skal
  me sjå nærare på i ei anna oppgåve.

Det finst nokre taggar me alltid må ha med i HTML-dokument:

- `<html>`: Fortel nettlesaren at her kjem det HTML-kode.

- `<head>`: Inne i `<head>` skriv me ting som er nyttig for nettlesaren, men som
  ikkje skal dukke opp som tekst på sjølve nettsida. Til dømes kan me bruke
  taggen `<title>`:

  ```html
  <head>
    <title>Heimesida mi</title>
  </head>
  ```

  `Heimesida mi` blir då tittelen på heimesida, og vil visast i vindauget til
  nettlesaren.

- `<body>`: Her ser me inn det som skal dukke opp på nettsida.

## Aktivitetar {.check}

- [ ] Åpne fila `side.html` i teksteditoren din.

- [ ] Legg merke til korleis taggar kan stå på innsida av andre taggar. Me har
  `<a>`-taggen, som er inni `<p>`-taggen, som igjen er inni `<div>`, som er
  plassert i `<body>`. Når ein tagg er på innsida av ein annan seier me at
  taggen som er inni er **bornet** og taggen som er rundt er **forelder**. Det
  er litt som eit slektstre.

- [ ] For nettlesaren er taggar av same type like, men du kan skilje dei frå
  kvarandre ved å bruke klasser. Til dømes kan nokre avsnitt vere
  introduksjonar, og då kan me bruke klassa `introduksjon` for å skilje desse
  avsnitta frå andre avsnitt. Finn taggane som har klasser i fila `side.html`.

- [ ] ID-ar brukast for å markere unike element på sida di. Finn `div`-taggen
  som har `id="kattunge"`.

- [ ] Kva skjer viss du flyttar på ting? Finn ein `<ol>` tagg i koden og vel den
  og alt inni, slik som dette:

  ```html
  <ol>
    <li>Kattungar</li>
    <li>Universet</li>
    <li>Å sove lenge</li>
    <li>Å spele spel</li>
  </ol>
  ```

- [ ] Kopier teksten og flytt den til ein annan stad.

- [ ] Lagre sida og åpne den i nettlesaren.

- [ ] Korleis påverkar rekkefølgja av koden rekkefølgja på det som blir vist i
  nettlesaren?

## Ting du kan prøve {.challenge}

- [ ] Lag ditt eige avsnitt med tekst.

- [ ] Lag ei lenke som peikar til ein annan del av sida. **Hint:** Det har noko
  med ID å gjere, sjå etter ei lenke som peikar til katten.

- [ ] Legg til dine eigne overskrifter der du synest dei passar. Kva skjer viss
  du endrar talet i overskrift-taggen, til dømes frå `<h3>` til `<h4>`?

- [ ] Kva må du gjere for å lenke til ei anna side?

- [ ] Bruk utviklarverktøyet og dobbeltklikk på litt kode som ser interessant
  ut. Endre koden. Då får du ei førehandsvising av kva som kjem til å skje, utan
  at du må byte mellom nettlesaren og teksteditoren. Kult, ikkje sant? Oppdater
  sida. Kva skjedde?

  Når du redigerer kode på denne måten blir det ikkje lagra, så du kan teste kva
  som skjer utan å øydeleggje fila. Slik kan du eksperimentere mykje, men alltid
  ha moglegheita til å gå attende.
