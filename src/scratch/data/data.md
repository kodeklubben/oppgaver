---
title: Bruk data i Scratch
author: Geir Arne Hjelle og Lance Olav Eastgate
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.0.0/jszip.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2014-11-29/FileSaver.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/es6-promise/3.2.2/es6-promise.min.js"></script>
<!--<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/4.1.2/papaparse.min.js"></script>-->
<script type="text/javascript" src="papaparse.min.js"></script> <!-- Using local copy because CDN contains a bug in guessDelimiter, should disappear when they bump version -->

# Introduksjon {.intro}

Her kan du gjøre om regneark og datafiler til lister som du kan bruke i Scratchprosjektene dine.

<div style="margin: auto; width: 480px">
  <button id="hent_fil" class="btn btn-success btn-lg btn-block">Last opp datafil</button>
  <input type="file" id="csv_fil" style="display:none">

  <div id="feilmelding"></div>
</div>

# Hvordan laste opp en datafil og bruke den i Scratch

Og her kommer det litt mer tekst som forteller hvordan du får dette inn i Scratch

<script type="text/javascript" src="data.js"></script>

