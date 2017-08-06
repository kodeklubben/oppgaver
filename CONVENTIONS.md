---
title: Kodekonvensjoner
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

- Bryt avsnitt på 80 tegn.

  Foretrukket:

  ```markdown
  Stilguiden er lite streng. Du trenger ikke finkjemme stilguiden før du foreslår
  noe. Om noe er viktig å få med seg, får du tilbakemelding på det når du legger
  inn _pull request_.
  ```

  Ikke foretrukket:

  ```markdown
  Stilguiden er lite streng. Du trenger ikke finkjemme stilguiden før du foreslår noe. Om noe er viktig å få med seg, får du tilbakemelding på det når du legger inn _pull request_.
  ```

  - Automatisk brytning av linjer i Emacs: `M-q` eller `M-x auto-fill-mode`
  - Automatisk brytning av linjer i Atom: `C-S-q` med
    [Autoflow](https://github.com/atom/autoflow) (innebygget)
  - Automatisk brytning av linjer i Vim: `gqq`

# Tekstfiler generelt

Dette er typisk ting du kan sette opp teksteditoren din til å gjøre for deg.

- Bruk **mellomrom** til inntrykk heller enn tab
- Bruk **to mellomrom** for hvert nivå innrykk
- Avslutt filen med en tom linje
- Unngå mellomrom til høyre for teksten eller på tomme linjer

# Versjonskontroll med Git

Arbeidsflyt for å legge til nye oppgaver med Git:

1. Sjekk ut siste versjon av branchen `master` på
   `git@github.com:kodeklubben/oppgaver.git`
2. Lag en ny branch med navn som beskriver temaet du skal legge til
3. Spor endringene dine i én eller flere commits
4. Lag pull request. Start gjerne navnet med `WIP - ` (work in progress) om du
   vil ha tilbakemeldinger før du er helt ferdig.

## En god branch

Vi bør gjøre så lite som mulig i hver feature branch / pull request. Da er det
lett å se hva som er gjort og unngå at det sniker seg inn feil.

**Gode navn på brancher:**

- `scratch-ny-felix-herbert`
- `elm-ny-prov-i-nettleser`
- `python-fiks-fargespill-lenke`

En branch bør altså ha navn etter _temaet_ for endringen.

Du kan endre navnet på branchen din med `git branch -m <gammeltnavn> <nyttnavn>`.

## En god commit

En commit bør være liten, men "koden skal kompilere". Det bør være mulig å komme
tilbake til tidligere commits uten at alt er ødelagt, og se rekkefølgen ting er
blitt gjort i.

Commits bør ha sammendrag etter _hva som er gjort_. Sammendraget står på første
linje.

```text
Skrevet ny Elm-oppgave om HTML
```

Det er også mulig å utdype sammendraget. Videre tekst skal skrives under én tom
linje.

```text
Skrevet ny Elm-oppgave om HTML

Oppgaven bruker `elm-lang.org/try` til å vise hvordan vi kan gjøre
HTML-generering med Elm. Oppgaven gir innsikt i

- Hvordan HTML er strukturer som et tre
- Hvordan vi leser feilmeldinger
- Hvordan vi kan se på andre eksempler.
```
