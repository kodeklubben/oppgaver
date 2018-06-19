---
title: 'HTML: Forsvunnet katt'
level: 2
language: nb
---

# Introduksjon {.intro}

Katten Felix har forsvunnet. Eieren hans har laget en plakat for å henge opp i nabolaget, men du innser at å lage en webside gjør at mange fler kan se den.

![screenshot](missingcat.png)

# Steg 1: Felix har forsvunnet! {.activity}

- [ ] Lag en ny mappe som du kaller Felix.

- [ ] Lag et nytt dokument med navnet `index.html` og lagre det i mappen du kalte Felix.
- [ ] Nå kan du sette opp dokumentet ditt slik som du lærte i [Introduksjon til web](../introduksjon_til_web/introduksjon_til_web.html).

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
  </body>
</html>
```

- [ ] Lag en tittel og en overskrift. Husk at tittelen skal plasseres i `<head>` og overskriften skal plasseres i `<body>`.

- [ ] Bruk "Katten Felix er forsvunnet" som tittel, og "Forsvunnet" som `<h1>`.

- [ ] Rett under `<h1>` kan vi lage en `<h2>` hvor det står "Katten Felix".


<toggle>
  <strong>Hint</strong>
  <hide>

```html
<!doctype html>
<html>
  <head>
    <title> Katten Felix er forsvunnet </title>
  </head>
  <body>
    <h1>Forsvunnet</h1>
    <h2>Katten Felix</h2>
  </body>
</html>
```
  </hide>
</toggle>

# Steg 2: Legg til bilde av Felix {.activity}

Vi trenger også et bilde av Felix, slik at folk vet hva de skal se etter. Vi har tidligere lært hvordan å legge inn et bilde som er lagret et annet sted på Internett, men denne gangen skal vi bruke et bilde på vår egen datamaskin.

- [ ] Finn et bilde på nettet av en katt.
- [ ] Lagre bildet i mappen Felix og la bildet hete `felix.jpg` eller `felix.png` avhengig av om bilde du laster ned har `.jpg` eller `.png` bak navnet sitt.
- [ ] Viktig at bildet blir lagt i samme mappe som `index.html`.

- [ ] Nå kan du skrive `<img>` taggen som du vanligvis ville gjort, men i scr attributten, istede for å skrive en URL skriver vi bare `felix.jpg` eller `felix.png`. Ikke glem å legge inn en `alt` attributt!

```html
<img src="felix.jpg" alt="bilde av Felix">
```

- [ ] Lagre filen din og vis den i nettleseren.

Dersom bildet er litt for stort, så kan vi gjøre det mindre ved hjelp av attributtet `width`. Vi spesifiserer ikke bredden i centimeter eller meter eller tommer eller fot, men i noe som kalles `pixler`. Jeg velger å gå for 400 pixler for dette bildet, du kan selv velge hvor stort det skal være, så prøv deg frem med forskjellige tall.

```html
<img src="felix.jpg" alt="bilde av Felix" width="400">
```

# Steg 3: Legg til beskrivelse av Felix {.activity}

Under bildet vil vi skrive en beskrivelse av Felix, og gi noen detaljer om når og hvor han forsvant. For dette kan vi skrive noen paragrafer.

```html
<p>Felix er en veldig snill katt. Han liker å kose, sitte foran varmepumpa og lekemusa si. Pelsen hans er oransje. </p>
<p>Han forsvant fra hagen i går.</p>
```

Vi trenger også informasjon om hvordan å kontakte eieren hvis noen har sett eller funnet Felix.

```html
<p>Har du sett Felix? Vennligst kontakt eieren hans på eierentilfelix@email.com</p>
```

Dette er bare en leke-epostadresse, men la oss gjøre det sånn at når noen klikker på den, så åpnes epostprogrammet deres. Vi gjør dette på nesten samme måten som vi lager en lenke, men istede for en __url__ bruker vi `mailto` sånn som dette:

```html
<p>Har du sett Felix? Vennligst kontakt eieren hans på <a href="mailto:eierentilfelix@email.com">eierentilfelix@email.com</a></p>
```

## Lagre dokumentet ditt og se om det fungerer i nettleseren! {.save}

# Step 4: Legge til fet tekst og trykk {.activity}

Vi vil virkelig at folk skal finne Felix, så vi vil legge litt *trykk* på `vennligst`. Dette gjør vi ved å bruke em taggen.

```html
<p>Har du sett Felix? <em>Vennligst</em> kontakt eieren hans på eierentilfelix@email.com</p>
```
Vi vil også at ´Tusen takk´ skal vises skikkelig, som vi oppnår ved å bruke strong taggen.

```html
<p><strong>Tusen takk!</strong></p>
```

## Lagre dokumentet ditt og vis det i nettleseren. {.save}

- [ ] Ser du nå hvordan vennligst vises i *skrå* og Tusen takk i **fet**?

# Step 5: Legge til kommentarer i koden {.activity}

Noen ganger er det lønnsomt å skrive kommentarer i selve html-filen. Med kommentarer mener vi ting som er ment for at mennesker skal lese hvis de åpner og ser filen, og ikke for nettleseren å lese og vise. Vi gjør dette ved å bruke den spesielle koden:

```html
<!-- skriv hva som helst her -->
```

Alt som skrives mellom pilene er kommentaren.
La oss legge en kommentar i filen som sier at dette er et Kodeklubb-prosjekt og at Felix ikke er ekte.

```html
<!-- Dette er et Kodeklubb-prosjekt. Felix er ikke ekte og er egentlig ikke forsvunnet. -->
```


# Steg 6: Mer metadata (Det er bare ting som legges i head) {.activity}

La oss legge til hvem som har skrevet websiden til websiden, slik at de som ser filen vet at det er deg.

```html
<meta name="author" content="#">
```

Erstatt `#` med navnet ditt.

Det er også vanlig å legge til hvilket språk websiden er på. Vi gjør dette ved å legge til en attributt til `<html>` taggen.

```html
<html lang="no">
```

`no` står for norsk.

Det er også god praksis å legge til tegnsettet (eller alfabet) dokumentet er skrevet i. Vi bruker vanligvis __UTF-8__.

```html
<meta charset="UTF-8">
```

Vi kan også legge til en beskrivelse av websiden.

```html
  <meta name="description" content="En side laget for å finne katten Felix">
```

Og noen nøkkelord, separert med komma

```html
<meta name="keywords" content="Felix, katt, forsvunnet">
```


Siden vår vil nå se ca slik ut:

![screenshot](screenshot_jsbin.png)

Til venstre har vi HTML-koden og til høyre har vi hvordan nettleseren viser siden vår.

## Hva kan du gjøre videre? {.challenge}

- [ ] Er det noe annet du kan legge til websiden som vil hjelpe folk å finne Felix? Mer informasjon? Hvordan ville du lagt til et kart over hvor han forsvant?

- [ ] Mer gøy med bilder. Legg til et bilde som beveger seg. Prøv å legge til bildet `catswithhats.gif` til websiden. Last ned gifen eller bruk lenken her: [catswithhats.gif](../forsvunnet_katt/ressurser/catswithhats.gif). Åpne det i nettleseren og se hva som skjer.

- [ ] Hvis Felix blir funnet. Bruk taggen `<del>` for å streke over informasjon som ikke lenger er sant, som foreksempel forsvunnet. Bruk taggen `<ins>` for å sette inn ny informasjon istede, som foreksempel __Funnet__!
