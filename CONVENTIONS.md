---
title: Stilguide til Markdown
author: Teodor Heggelund
---

# Hvorfor kodekonvensjoner?

Det er lettere å jobbe med kode (og tekst) som ser lik ut over hele prosjektet.
Dette er noe de fleste er enige om. Med en stilguide skriver vi dette ned, så vi
kan gjøre det samme alle sammen.

Vi kan også ta hensyn til at vi alle bruker forskjellige verktøy. For eksempel
er det mange som kjører verktøy i terminaler. Disse er typisk 80 tegn brede. Det
er derfor svært vanlig å bruke linjeskift (som vi setter inn med Enter) for å
holde linjebredden nede. Dette gjør det mer behagelig å redigere tekst i mange
editorer, og lettere å sammenlikne filer.

Stilguiden er lite streng. Du trenger ikke finkjemme stilguiden før du foreslår
noe. Om noe er viktig å få med seg, får du tilbakemelding på det når du legger
inn _pull request_.

# Formatering av Markdown-filer

- Bruk `-` for punktlister

- Bruk `- [ ]` for lister av sjekkpunkter

- Bruk `1.`, `2.`, ... for lister av tall

- Ha én tom linje før og etter overskrifter.

  Foretrukket:
  
  ```markdown
  _pull request_.
  
  # Formatering av Markdown-filer
  
  - Bruk `-` for punktlister
  ```
  
  Ikke foretrukket:
  
  ```markdown
  _pull request_.


  # Formatering av Markdown-filer  
  - Bruk `-` for punktlister
  ```  

# Tekstfiler generelt

Dette er typisk ting du kan sette opp teksteditoren din til å gjøre for deg.

- Bruk **mellomrom** til inntrykk heller enn tab
- Bruk **to mellomrom** for hvert nivå innrykk
- Avslutt filen med en tom linje
- Unngå mellomrom til høyre for teksten eller på tomme linjer

