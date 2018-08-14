---
title: Bruk data i Scratch
author: Geir Arne Hjelle og Lance Olav Eastgate
translator: 'Stein Olav Romslo'
language: nn
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.0.0/jszip.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2014-11-29/FileSaver.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/es6-promise/3.2.2/es6-promise.min.js"></script>
<!--<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/4.1.2/papaparse.min.js"></script>-->
<script type="text/javascript" src="papaparse.min.js"></script> <!-- Using local copy because CDN contains a bug in guessDelimiter, should disappear when they bump version -->


# Introduksjon {.intro}

Her kan du gjere om rekneark og datafiler til lister som du kan bruke i
Scratchprosjekta dine.

<div style="margin: auto; width: 480px">
  <button id="hent_fil" class="btn btn-default btn-lg btn-block">Last opp datafil</button>
  <input type="file" id="csv_fil" style="display:none">

  <div id="feilmelding"></div>
</div>


# Korleis laste opp ei datafil {.activity}

*Denne tenesta lagar Scratchprosjekt frå såkalla __CSV-filer__. Dette er eit
vanleg format for datalagring. Du kan finne mange CSV-filer på Internett, eller
lage dine eigne med reknearkprogram som Excel, Numbers eller Libre Office.*

## Sjekkliste {.check}

- [ ] Lag ei CSV-fil lokalt på harddisken din. Du kan anten laste ned ei frå
  Internett, eller lage ho sjølv.

- [ ] Klikk på knappen __Last opp datafil__ lengre opp på denne sida.

Dette lagar eit Scratchprosjekt av datafila di. Viss du ikkje får velje
filnamnet sjølv heiter prosjektet `data.sb2` og ligg sannsynlegvis i ein katalog
som heiter `Nedlastingar`.


# Korleis laste dataane inn i Scratch {.activity}

*No skal me sjå korleis du laste inn dataane i Scratch.*

## Sjekkliste {.check}

- [ ] Start eit nytt Scratchprosjekt.

- [ ] Klikk på __Fil__-menyen og vel __Last opp frå maskina__.

- [ ] Vel fila du lasta ned i førre steg.

- [ ] Si __OK__ til å slette innhaldet i det eksisterande prosjektet (du starta eit nytt Scratchprosjekt, ikkje sant?).

- [ ] Dataane dine er tilgjengelege som __lister__ i Scratch. For å programmere
  med desse brukar du klossar frå `Data`{.blocksdata}-kategorien.

<script type="text/javascript" src="data.js"></script>
