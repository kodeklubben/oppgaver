---
title: "CSS: Style nettsider"
author: Arve Seljebu
language: nb
---


# Introduksjon {.intro}

Nå skal vi lære å endre på stilen til nettsider. I denne oppgaven forventer vi
at du har gjort HTML-oppgavene (i oppgavesamlingen _Intro til web_) eller er litt kjent med HTML fra før av.

I denne og neste leksjon skal vi lære oss hvordan å __endre farge, tekst,
størrelse og mer__! Dette gjør vi ved å lære oss å bruke et språk som heter
__CSS__ (som står for __Cascading Style Sheets__). Det er et veldig enkelt språk
å lære. La oss begynne.

Resultatet kommer til å se noe sånt ut:

![Bilde av nettsiden om Felix](ressurser/bilde1.png)

![Tekst om den savnede katten](ressurser/bilde2.png)


# Steg 1: Hvordan fungerer CSS? {.activity}

Det finnes mange måter å lage stiler på. En av dem er __inline__ hvor du skriver
stilen rett i en tag, om dette:

```html
<p style="color:red">Tekst som er rød</p>
```

En annen måte er å lage en egen `.css`-fil og referere til den i `<head>`:

```html
<head>
    <link rel="stylesheet" type="text/css" href="navn_på_css_filen_din.css">
</head>
```

Men i dag skal vi bruke den siste metoden hvor vi legger stilene i `<head>`
slik:

```html
<head>
    <style>
        <--! Her skal vi skrive CSS-en -->
    </style>
</head>
```

På denne måten slipper vi å håndere flere filer, vi kan ha alt vi trenger i én
fil.

- [ ] Åpne index.html fra mappen Felix som vi lagde i oppgaven [Forvunnet
  katt](../forsvunnet_katt/forsvunnet_katt.html) eller last ned filen ved å
  høyreklikke og trykk `lagre som`:
  [index.html](../forsvunnet_katt/ressurser/index.html). Lag en mappe som heter
  `Felix` og legg `index.html` i den.

- [ ] I seksjonen `<head>` trenger vi en __style-tag__.

```html
 <style>
 </style>
```

Alle stiler skal legges mellom disse elementene. Generelt ser css-kode slik ut:

```css
selector {
  property: value;
}
```

Selektorer kan være html-element som `h1`, `p`, `img`, `a`, eller `id-er` og
`klasser`, men disse skal vi se på senere. Selektorer brukes for å fortelle
CSS-en hvilke HTML-objekter vi skal sette stil på. Hvilken stil selektoren får
avheniger av hva man setter på `property` og `value`.

`Property` eller `attributt` er gjerne en egenskap man kan tilegne selektoren,
sammen med en verdi, `value`. Eksempler på `property` og `value` kan være
`color: blue;`, `background-color: red;` og ` font-family: "Times New Roman",
Serif;`.

- [ ] Kan du finne knappene for `{` og `}` på ditt tastatur

- [ ] Hva med `:` og `;`?

Finner du dem ikke, så få hjelp av noen til å finne dem for deg, fordi disse er
viktige. Dersom du ikke har med `{ }`, `:`eller `;` på de riktige stedene, så
vil ikke HTML-en din få stil. Derfor er det viktig å allerede nå å vite hvor man
finner `{ }`, `:`eller `;` på tastaturet.


# Steg 2: Legg til farge {.activity}

Visste du at CSS er faktisk oppfunnet av en norsk gutt? Det er litt kult!

La oss endre `h1` til å være `rød` istedenfor `svart` ved hjelp av property-en
`color`:

```html
<style>
  h1 {
      color:red;
    }
</style>
```

__NB! Husk å sette `;` etter `value`.__

## __LAGRE__ filen og __VISE__ den i nettleseren din {.save}

Overskriften skal nå være `rød`! Det finnes forskjellige måter å representere en
farge på. Det er 16 grunnleggende fargenavn: aqua, black, blue, fuchsia, gray,
green, lime, maroon, navy, olive, purple, red, silver, teal, white, og yellow.

- [ ] Prøv og endre fargen til noe annet!

De fleste nettlesere støtter i tillegg 130 andre fargenavn, hele listen i
alfabetisk rekkefølge kan dere finne på
[http://www.w3.org/TR/css3-color/#svg-color](http://www.w3.org/TR/css3-color/#svg-color).
Er din favorittfargen i listen?

- [ ] Men vi kan bruke enda flere farger gjennom å bruke den heksadesimale koden
  istedenfor navnet. En heksadesimal kode er en `#` fulgt av 6 tegn der tegnene
  kan være sifferne 0-9 eller bokstavene A, B, C, D, E, F. Gjennom å bruke
  heksadesimale koder kan vi representere mer enn 16 millioner farger.

- [ ] Kodeklubben sin favorittfarge er `#58AB57`. Kan du gjette hvilken farge
  det er? Prøv å endre noen tekst til den fargen og se hvordan det ser ut i en
  nettleser.

- [ ] Prøve å endre teksten, `<p>`, på siden til denne fargen: `#58AB57`.

<toggle>
 <strong>Hint</strong>
 <hide>

  ```css
   p{
     color: #58AB57;
   }
   ```
   </hide>
</toggle>

- [ ] Bruk [www.colorpicker.com](http://www.colorpicker.com) til å finne en
  farge du liker. Colorpicker genererer det nummer du trenger, så kan du enkelt
  klippe og lime det inn i koden din.

- [ ] Finn en farge du liker med `Colorpicker` og endre teksten på siden til den
  fargen du fant.

## __LAGRE__ filen og __VISE__ den i nettleseren din {.save}


# Steg 3: Gi farge til spesifikke elementer {.activity}

Hva om vi vil gjøre sånn at ordet `oransje` i setningen `Pelsen hans er oransje`
får oransje farge? Ikke hele setningen, men akkurat det ordet. Da bruker vi en
tag som heter `<span>`. Vi legger taggen rundt ordet vi vil sette farge på slik:

```html
<span>oransje</span>
```

I `<head>` kan vi nå gjøre at alle `<span>`-taggene blir oransje slik:

```css
span {
  color:orange;
}
```

## __LAGRE__ filen og __VISE__ den i nettleseren din {.save}


# Steg 4: La oss endre bakgrunnen {.activity}

Vi kan legge til farge på bakgrunnen også, ikke bare på tekst. For eksempel:

```css
body {
  background-color: #D2FAFC;
}
```

Dette vil gjøre at hele bakgrunnen blir blå.

Prøve nå:

```css
h1 {
  background-color:black;
}
```

Siden vi allerede hadde en `h1` deklarert i filen kan vi bare putte inn
property-en `background-color` sammen med `color`, vi trenger ikke å skrive alt
om igjen.

```css
h1 {
  color:red;
  background-color: black;
}
```

## Nå skal du __LAGRE__ filen og se hvordan det ser ut. {.save}

Legg merke til at kun bakgrunnen til `h1` blir svart og ikke hele siden. For å
få hele siden bruker må vi legge til bakgrunnsfarge på `body`, som vist over.


# Steg 5: Morro med tekst {.activity}

Kanskje skulle tittelen være __større__ og med store bokstaver. Vi kan
spesifisere størrelsen på teksten gjennom å bruke `font-size`. Verdiene kan være
forskjellige, men de mest brukte er 12, 14, 16, 32, 48 og 72 piksler.

- [ ] La oss prøve ut `72px` for nå. (px betyr piksel)

```css
h1 {
  color:red;
  background-color:black;
  font-size:72px;
}
```

- [ ] Nå skal du forsøke å endre tittelen til å være kun i store bokstaver bare
  gjennom å bruke `text-transform:uppercase;` Vi kan også gjøre den understreket
  gjennom å bruke `text-decoration:underline;`

## Nå skal du __LAGRE__ filen og se hvordan den ser ut. {.save}

Er det ikke mye større forskjell nå?

### For de som bruker Firefox eller Chrome som nettleser. {.challenge}

Det finnes faktisk også en annen verdi for `text-decoration` som er `blink`. Jeg
kommer ikke til å fortelle deg hva det gjør. Du må teste det.
`text-decoration:blink;` (det blir litt masete etterhvert, men det er lov å gå
tilbake til “underline” hvis du vil).


# Steg 6: Sentrere tekst (og bilder) horisontalt {.activity}

All vår tekst vises helt borte til venstre. Vi kan endre det gjennom å bruke
`text-align:center` (man kan også bruke `right`(høyre) og `left`(venstre)).

1. For denne nettsiden vil vi at all vår tekst skal være sentrert, og da kan vi
  skrive: (Merk deg at den engelske måten å stave senter på er center.)

```css
body {
  background-color: #F8FAF4;
  text-align: center;
}
```

La du merke til at alt på nettsiden ble sentrert når vi har lagt til
`text-align:center` i seksjonen `<body>`? Det er fordi alt innenfor elementet
`<body>` arver stilen. Dette skjer når et element er innenfor et annet, som
dette her:

```html
<p>Har du sett Felix? <em>Vennligst</em> kontakt eieren hans</p>
```

Teksten *“Vennligst”* vil ha stilen fra elementet `<p>` med stilen fra elementet
`<em>` lagt på. Dette er grunnen til at man kaller det __cascading__ - stilene
blir videreført fra et element til alle ene som er innenfor dem. Men vær
forsiktig, det finnes noen stiler som ikke blir videreført.

## Nå skal du __LAGRE__ filen og åpne den i en nettleser {.save}


# Steg 7: Koden vi har til nå {.activity}

## Resultat:

![Bilde av nettsiden om Felix](ressurser/bilde1.png)

![Tekst om den savnede katten](ressurser/bilde2.png)

## Koden:

```html
<!doctype html>
<html lang="no">
<head>
    <meta name="author" content="#">
    <meta charset="UTF-8">
    <meta name="description" content="En side laget for å finne katten Felix">
    <meta name="keywords" content="Felix, katt, forsvunnet">
    <title>Katten Felix er forsvunnet</title>

  <!---CSS-stilen til siden --->
  <style>

    body{
      background-color: #F8FAF4;
      text-align: center;
    }

    h1{
      color:red;
      background-color:black;
      font-size:72px;
      text-decoration: uppercase;
    }

    span {
      color:orange;
    }


  </style>

</head>

<body>
<!-- Dette er et Kodeklubb-prosjekt. Felix er ikke ekte og er egentlig ikke forsvunnet. -->
    <h1>Forsvunnet</h1>
    <h2>Katten Felix</h2>
    <img src="http://kodeklubben.github.io/web/forsvunnet_katt/missingcat.png" alt="bilde av Felix" width="400">
    <p>Felix er en veldig snill katt. Han liker å kose, sitte foran varmepumpa og lekemusa si. Pelsen hans er <span>oransje</span>. </p>
    <p>Han forvant fra hagen i går.</p>
    <p>Har du sett Felix? Vennligst kontakt eieren hans på <a href="mailto:eierentilfelix@email.com">eierentilfelix@email.com</a></p>
    <p><strong>Takk!</strong></p>
</body>
</html>
```

## Videre studier {.challenge}

- [ ] Hvordan ville du endret på siden for å få den til å se bedre ut? Hvorfor
  ikke prøve å bruke alle dine favorittfarger? Finnes din farge som et navn
  eller må du bruke en heksadesimal kode

- [ ] Hvis du blir fort ferdig kan du gå tilbake å legge på stiler for tidigere
  leksjoner.
