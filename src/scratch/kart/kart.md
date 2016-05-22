---
title: Last ned kart
author: Geir Arne Hjelle og Lance Olav Eastgate
---

<link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css" />
<script src="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js"></script>
<script src="leaflet-image.js"></script>

# Introduksjon {.intro}

Her kommer det litt tekst som forklarer hvordan denne virker.

<div style="margin: auto; width: 480px">
  <div id="kart" style="width: 480px; height: 360px"></div>

  <p>
    <br />
    <a id="last_ned_som_bilde" class="btn btn-success btn-lg btn-block">Last ned som Scratch-bakgrunn</a>
  </p>
</div>

<script>
  var scratch_map = L.map('kart').setView([65, 14], 4);
  L.tileLayer('http://opencache.statkart.no/gatekeeper/gk/gk.open_gmaps?layers=norges_grunnkart&zoom={z}&x={x}&y={y}', {attribution: '<a href="http://www.kartverket.no/">Kartverket</a>'}).addTo(scratch_map);

  document.getElementById("last_ned_som_bilde").addEventListener("click", function() {
    leafletImage(scratch_map, downloadMapAsImage);});

  function downloadMapAsImage(err, canvas) {
    var a = document.createElement("a");
    var img = document.createElement('img');
    var dimensions = scratch_map.getSize();
    img.width = dimensions.x;
    img.height = dimensions.y;
    img.src = canvas.toDataURL();

    url = img.src.replace('image/png', 'image/octet-stream');
    a.download = 'kart.png';
    a.href = url;
    a.click();
  }
</script>

Her kommer det litt mer forklaring på hvordan man bruker kartgeneratoren.

