---
title: "Lærerveiledning - JS: Trykkomania"
author: Lars Klingenberg og Susanne Rynning Seip
language: nb
---


# Om oppgaven {.activity}

Denne oppgaven viser deg hvordan du kan lage et spill med JavaScript og dele det
med vennene dine. Spillet kalles *Trykkomania* fordi det handler om å trykke på
en ball flest mulig ganger før tiden renner ut.

Oppgaven henter ideer fra utvikling av web-applikasjoner med bibliotek som
[React](https://facebook.github.io/react/) og [Mithril](http://mithril.js.org/),
der elementer i spillet lages som inviduelle komponenter. Komponentene ligner på
objektorientert programmering, men bruker teknikken "closures" (funksjoner som
husker konteksten de ble laget i).

## Oppgaven passer til: {.check}

__Fag__: Matematikk, Programmering, Kunst og håndverk, IT1

__Trinn__: 4. trinn - VG3

__Tema__: Javascript, Web, Spill, Variabler, Funksjoner, Closures, Objekter

__Nivå__: Nybegynner

__Tidsbruk__: Dobbeltime eller mer.

## Kompetansemål {.challenge}

- [ ] __Kunst og håndverk, 7. trinn__: bruke programmering til å skape interaktivitet og visuelle uttrykk

- [ ] __Matematikk, 7. trinn:__ representere og bruke brøk, desimaltall og prosent på ulike måter og utforske de matematiske sammenhengene mellom disse representasjonsformene

- [ ] __Matematikk, 8. trinn:__ lage og forklare regneuttrykk med tall, variabler og konstanter tilknyttet praktiske situasjoner

- [ ] __Fordypning i matematikk, 10. trinn:__ diskutere, planlegge, lage og vurdere spilldesign og egne spill

- [ ] __Programmering, 10. trinn:__ bruke flere programmeringsspråk, deriblant minst ett som er tekstbasert

- [ ] __IT1, VG2:__ lage og bruke egne og andres funksjoner med og uten parametre og returverdier

- [ ] __IT1, VG2:__ lese, strukturere, analysere og kommentere programkode

- [ ] __IT2, VG3:__ lage objektorienterte programmer som benytter klasser med metoder

## Forslag til læringsmål {.challenge}

- [ ] Eleven kan bruke enkle matematiske uttryksmåter for å øke eller minke
  variabler i JavaScript.

- [ ] Eleven kan bruke JavaScript til å tegne en sirkel.

- [ ] Eleven kan plassere et element i på en nettside ved hjelp av koordinater
  på x- og y-aksen.

- [ ] Eleven kan skrive kommentarer til sin egen kode i JavaScript.

- [ ] Eleven kan bruke variabler, løkker og funksjoner til å manipulere
  elementer i JavaScript.

- [ ] Eleven kan videreutvikle sitt ferdige produkt ved hjelp av egenprodusert
  JavaScript-kode.

## Forslag til vurderingskriterier {.challenge}

- [ ] Eleven oppnår middels måloppnåelse ved å fullføre oppgaven.

- [ ] Eleven oppnår høy måloppnåelse ved å videreutvikle egen kode basert på
  oppgaven.

## Forutsetninger og utstyr {.challenge}

- [ ] __Forutsetninger__: Oppgaven er *kun* javascript, men det lønner seg å ha
  kjennskap til HTML og CSS.

- [ ] __Utstyr__: Datamaskin med internett.

## Konsepter brukt i oppgaven {.challenge}

- [ ] [Variabler]

- [ ] [Objekter]

- [ ] [Funksjoner]

- [ ] [Closures], funksjoner som husker konteksten de ble laget i.

- [ ] [HTML-elementer] via javascript

- [ ] [CSS-stil] via javascript

- [ ] [`onclick`]

- [ ] [`setInterval`]

[Variabler]:https://developer.mozilla.org/en-US/docs/Glossary/Variable
[Objekter]:https://developer.mozilla.org/en-US/docs/Glossary/Object
[Funksjoner]:https://developer.mozilla.org/en-US/docs/Glossary/Function
[Closures]:https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures
[HTML-elementer]:https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement
[CSS-stil]:https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style
[`onclick`]:https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onclick
[`setInterval`]:https://developer.mozilla.org/en-US/docs/Web/API/WindowTimers/setInterval


# Løsning {.challenge}

[Her er en full løsning av oppgaven.](losning.js)

<!--A workaround to get "Fremgangsmåte" out from the challenge box-->
# {.intro}

## Fremgangsmåte

Her kommer tips, erfaring og utfordringer til de ulike stegene i den faktiske
oppgaven. [Klikk her for å se oppgaveteksten.](trykkomania.html){target=_blank}


# Generelt i oppgaven {.activity}

- [ ] Elevene bør ha god og oversiktelig kode sånn at det er enkelt å finne
  feil. Dette oppnås ved å kommentere koden, samt bruke inntrykk og mellomrom
  mellom funksjoner og annen kode.

- [ ] Elevene må passe på at variabelnavn og tegnsetting er riktig.


# Steg 2: Lage en ball {.activity}

- [ ] Elevene kjenner kanskje igjen CSS-elementer når de skal lage funksjonen
  `Ball()`. Her vises det at HTML og CSS kan programmeres gjennom JavaScript.


# Steg 3: Flytte ballen {.activity}

- [ ] Elevene kan lure på hvor de skal legge til koden i dette steget, den skal
  legges til i funksjonen `Ball()` fordi `el` er en lokal varibel til funksjonen
  `Ball()`.


# Steg 4: Flytte ballen med en funksjon {.activity}

- [ ] Elevene kan være forvirret hva `x` og `y` er i denne oppgaven så her er
  det viktig å poengtere at dette er verdier som blir sendt inn senere i
  programmet, som vi ser rett før _Steg 5_.


# Steg 5: Velg en tilfeldig plassering {.activity}

- [ ] Her ser vi at vi kan legge til _strenger_ bak tall som er blitt regnet ut:
  `Math.random() * 100 + '%';`. Dette kan være svært nyttig for elevene å vite i
  senere oppgaver.

- [ ] Elever kan lure på hva `Math.random()` er. Og ved å si `Math.random()` så
  kaller vi på et bibliotek (_Math_), altså en innebygget JavaScript-fil, som
  inneholder funksjonen `random()`.


# Steg 7: Poeng {.activity}

- [ ] Elevene må kopiere koden akkurat som den står oppført, hvis ikke blir det
  fort feil.

- [ ] __Merk:__ Det er en liten forskjell i koden gitt i dette steget og koden som det er linket til i fasitene.

  `el.style.bottom` er satt til `50px` (i motsettning til `5px`). Dette er for at den ikke skal ende opp bak reklamen som kan dukke opp på bunnen av editoren.


# Steg 8: Begrense tiden {.activity}

- [ ] Elevene må kopiere koden akkurat som den står oppført, hvis ikke blir det
  fort feil.


# Steg 9: Omstarte spillet {.activity}

- [ ] Elevene må kopiere koden akkurat som den står oppført, hvis ikke blir det
  fort feil.

## Variasjoner {.challenge}

- [ ] _Vi har dessverre ikke noen variasjoner tilknyttet denne oppgaven enda._
