---
title: "Hvor er HTML? Jeg ser den ikke!"
level: 1
language: nb-NO
---

# Introduksjon {.intro}

Målet med denne oppgaven er å _vise_ hvor HTML finnes i virkelige nettsider, uten først å måtte pugge navnet på tags. Vi skal prøve å gi en intuitiv forståelse av HTML som trestruktur, uten alt for mye distraksjoner.

Denne oppgaven er demonstrert med nettleseren Google Chrome. Bruk Google Chrome hvis du har den.

# Steg 1: Se {.activity}

Hvor er da all HTML-koden bak nettsidene vi ser til vanlig? Den er gjemt bakk nettleseren! La oss ta en titt.

## Aktiviteter {.check}

- Gå til [kodeklubben.github.io](http://kodeklubben.github.io) i Chrome eller Firefox
- Høyreklikk på katten og trykk `Inspisér` (norsk) eller `Inspect` (engelsk).

  ![](inspiser_katten.png)

  Når vi klikker på `Inspiser`, får vi se en meny til hjelp for utviklere. Denne er svært nyttig til webutvikling.

  ![](kattens_kildekode.png)

  Ser du den fargede teksten, du også? Det er HTML, slik Chrome leser den! Nettsidens kildekode.

  Kildekoden til katten ser slik ut:

  ```html
  <img src="scratch/logo-black.png">
  ```

- Se om du finner igjen `scratch/logo_black.png` i kildekoden. Hold pekeren over filnavnet. Ser du filen dukker opp?

- Inspiser slangen. Hva er filnavnet til slangen? Ser du det samme som meg?

  ![](slangens_kildekode.png)

  Kildekoden til slangen ser slik ut:

  ```html
  <img src="python/logo-black.png">
  ```

## Hva har vi lært? {.protip}

**Høyreklikk og inspect** finner HTML-koden til elementet vi ser på.

**HTML-kode for bilder** ser slik ut:
```html
<img src="fil.png">
```

# Steg 2: Fjern {.activity}

Nettleseren lar og tulle med HTML-koden til alle nettsider vi er på. Vi ødelegger ikke nettsidene, altså! Når vi gjør noe med nettsidene, er det bare i vår egen nettleser det skjer noe. Alle andre som ser på nettsiden ser en *helt vanlig* nettside.

## Alt borte vekk? {.protip}

Tips: Skulle du fjerne alt for mye, last siden på nytt med oppdater-knappen. Da blir alt som det var. Prøv!

## Aktiviteter {.check}

Jeg er glad i Minecraft. Men Minecraft er ikke først! La oss gjøre noe med det. Vi fjerner alt som er foran!

- Høyreklikk på katten og inspiser. Finn elementet med katten. Fjern elementet med knappen `delete`!

  ![](katten_er_borte.png)

- Yes! Katten ble borte!

  ... men. Vent litt. Slangen gikk ikke til venstre. Hva skjedde nå, mon tro? Og det står fremdeles `Scratch` under den tomme plassen?

  ![](kattens_usynlige_boks.png)

  Ha! Det er en usynlig boks igjen, den som tidligere hadde katten i seg! Den heter `<a>`, og er en link:

  ```html
  <a href="scratch/index.html" id="scratch" data-original-title="" title="" aria-describedby="popover162945">
    <div class="logo-wrapper">
    </div>
    <div class="name">
      <span>Scratch</span>
    </div>
  </a>
  ```

- Trykk på den lille pilen ved siden av linken  `<a>`. Da gjemmer vi hva som er inni linken!

  ![](liten_a.png)

- Fjern teksten `Scratch`. Merk den som under, og trykk `delete`:

  ![](teksten_scratch.png)

  Simsalabim!

  ![](simsalabim.png)

  La oss fjerne litt mer.

- Fjern elementet som inneholder alle kursene:
  ```html
  <div class="courses">
  ```

  ![](class_courses.png)

  Poff!

  ![](alt_borte.png)

  Å nei! Nå ble alt borte!

  Last siden på nytt for å få den gamle tilbake.

  Nå må du hjelpe meg å få Minecraft først i køen.

- Finn elementet som er den usynlige boksen rundt katten. Fjern det!

- Finn elementet som er den usynlige boksen rundt slangen. Fjern det!

- Gjør det samme for `Lego Mindstorms`, `Web`, `App Inventor` og `CodeStudio`.

  ![](minecraft_yay.png)

  Sånn skal det se ut!

## Hva har vi lært? {.protip}

**HTML** kan inneholde usynlige koder!

Disse kan være lenker (`<a>`) eller bokser (`<div>`)

Vi kan fremdeles finne alle de usynlige kodene når vi bruker `Inspisér!`

# Steg 3: Skap {.activity}

Nå skal vi leke! La oss putte denne rakkeren

![](schnauzer.jpg)

på **alle kursene**!

![](schnauzere.png)

## Aktiviteter {.check}

- Finn et bilde du liker på internett. Hent bildeadressen ved høyreklikke på bildet:

  ![](bildeadresse.png)

- Endre alle bildene ved å redigere `src`-attributten til `<img>`-taggen:

  ![](ny_og_bedre_src.png)

# Steg 4: Masse moro! {.activity}

Gratulerer! Du er har kommet ett skritt på vei til å bli Webutvikler!

![](schnauzer_web_developer.jpg)
