// List of layers
var baseLayers = {
  'Kartverkets grunnkart': L.tileLayer('http://opencache.statkart.no/gatekeeper/gk/gk.open_gmaps?layers=norges_grunnkart&zoom={z}&x={x}&y={y}', {attribution: '&copy; <a href="http://www.kartverket.no/Kart/Gratis-kartdata/Lisens/">Kartverket</a>'}),
  'Kartverkets topografiske kart': L.tileLayer('http://opencache.statkart.no/gatekeeper/gk/gk.open_gmaps?layers=topo4&zoom={z}&x={x}&y={y}', {attribution: '&copy; <a href="http://www.kartverket.no/Kart/Gratis-kartdata/Lisens/">Kartverket</a>'}),
  'OpenStreetMap': L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {maxZoom: 19, attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> bidragsytere'}),
  'Stamens vannfargekart':  L.tileLayer('http://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.{ext}', {attribution: 'Design av <a href="http://stamen.com">Stamen</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Kartdata &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> bidragsytere', subdomains: 'abcd', minZoom: 1, maxZoom: 16, ext: 'png'}),
  'Thunderforests pioneerkart': L.tileLayer('http://{s}.tile.thunderforest.com/pioneer/{z}/{x}/{y}.png', {attribution: '&copy; <a href="http://www.thunderforest.com/">Thunderforest</a>, &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> bidragsytere'}),
  'Thunderforests togkart':  L.tileLayer('http://{s}.tile.thunderforest.com/transport-dark/{z}/{x}/{y}.png', {attribution: '&copy; <a href="http://www.thunderforest.com/">Thunderforest</a>, &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> bidragsytere', maxZoom: 19})
}

// Set up map with default layer and control to switch layers
var scratchMap = L.map('kart').setView([65.4, 21], 4);
baseLayers['Kartverkets grunnkart'].addTo(scratchMap);
L.control.layers(baseLayers, null, {collapsed: true, position: 'bottomright'}).addTo(scratchMap)

// Use leaflet-image.js to download map as an image file
document.getElementById("last_ned_som_bilde").addEventListener("click", function() {
  leafletImage(scratchMap, downloadMapAsImage);});

function downloadMapAsImage(err, canvas) {
  var a = document.createElement('a');
  document.body.appendChild(a);
  a.setAttribute('type', 'hidden');
  var img = document.createElement('img');
  var dimensions = scratchMap.getSize();
  img.width = dimensions.x;
  img.height = dimensions.y;
  img.src = canvas.toDataURL();

  var url = img.src.replace('image/png', 'image/octet-stream');
  a.download = 'kart.png';
  a.href = url;
  a.click();
}
