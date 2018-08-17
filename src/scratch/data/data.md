---
title: Bruk data i Scratch
author: Geir Arne Hjelle og Lance Olav Eastgate
language: nb
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.0.0/jszip.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2014-11-29/FileSaver.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/es6-promise/3.2.2/es6-promise.min.js"></script>
<!--<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/4.1.2/papaparse.min.js"></script>-->
<script type="text/javascript" src="papaparse.min.js"></script> <!-- Using local copy because CDN contains a bug in guessDelimiter, should disappear when they bump version -->


# Introduksjon {.intro}

Her kan du gjøre om regneark og datafiler til lister som du kan bruke i
Scratchprosjektene dine.

<div style="margin: auto; width: 480px">
  <button id="hent_fil" class="btn btn-default btn-lg btn-block">Last opp datafil</button>
  <input type="file" id="csv_fil" style="display:none">

  <div id="feilmelding"></div>
</div>


# Hvordan laste opp en datafil {.activity}

_Denne tjenesten lager Scratchprosjekter fra såkalte **CSV-filer**. Dette er et
vanlig format for datalagring. Du kan finne mange CSV-filer på nettet, eller
lage dine egne med regnearkprogrammer som Excel, Numbers eller Libre Office._

## Sjekkliste {.check}

- [ ] Legg en CSV-fil lokalt på harddisken din. Du kan enten laste denne ned fra
  nettet eller lage den selv.

- [ ] Klikk på knappen **Last opp datafil** lenger opp på denne siden.

Dette vil lage et Scratchprosjekt av datafilen din. Om du ikke får velge filnavn
selv vil prosjektet hete `data.sb2` og sannsynligvis ligge i en katalog som
heter `Nedlastinger`.


# Hvordan laste dataene inn i Scratch {.activity}

_Vi skal nå se hvordan du kan laste dataene dine inn i Scratch._

## Sjekkliste {.check}

- [ ] Start et nytt Scratchprosjekt.

- [ ] Klikk på **Fil**-menyen og velg **Last opp fra maskinen**.

- [ ] Velg filen du lastet ned i forrige steg. Sannsynligvis heter den `data.sb2` og
  ligger i katalogen `Nedlastinger`.

- [ ] Si **OK** til å slette innholdet i det eksisterende prosjektet (du startet et
  nytt Scratchprosjekt, ikke sant?)

- [ ] Dataene dine er nå tilgjengelige som **lister** i Scratch. For å programmere
  med disse bruker du klosser fra `Data`{.blocksdata}-kategorien.

<script type="text/javascript" src="data.js"></script>

