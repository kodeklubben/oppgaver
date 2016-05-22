---
title: Konverter CSV-data til Scratch
author: Geir Arne Hjelle og Lance Olav Eastgate
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.0.0/jszip.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2014-11-29/FileSaver.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/es6-promise/3.2.2/es6-promise.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/4.1.2/papaparse.min.js"></script>

# Introduksjon {.intro}

Her kommer det litt tekst som forteller hva du skal gjøre!

<div style="margin: auto; width: 480px">
  <button id="hent_fil" class="btn btn-success btn-lg btn-block">Konverter CSV-fil</button>
  <input type="file" id="csv_fil" style="display:none">

  <div id="feilmelding"></div>
</div>

Og her kommer det litt mer tekst som forteller hvordan du får dette inn i Scratch

<script>
function loadFile(url, type) {
  var p = new Promise(function(resolve, reject) {
    var req = new XMLHttpRequest();
    req.open('GET', url, true);
    req.responseType = type;
    req.onload = function(e) {
      resolve(req.response);
    }
    req.onerror = function(err) {
      reject(err);
    }

    req.send();
  });

  return p;
}

function logError(e) {
  console.error(e);
}

function manipulateJson(csvStr, jsonStr){
  console.log(jsonStr);
  console.log(csvStr);
  var csvJson = Papa.parse(csvStr, {skipEmptyLines: true});
  console.log(csvJson);

  var headers = csvJson.data[0];
  var rows = csvJson.data.slice(1);
  console.log(rows)

  var children = [];
  for (var i=0; i < headers.length; ++i) {
    children.push({
      'listName': headers[i],
      'contents': rows.map(function(r) {
        return r[i];
      }),
      'isPersistent': false,
      'x': 5 + i * 10,
      'y': 5,
      'width': 100,
      'height': 200,
      'visible': true
    });
  }
  console.log(children);

  var jo = JSON.parse(jsonStr);
  jo['lists'] = children;
  return JSON.stringify(jo);
}

var fileUpload = document.getElementById('csv_fil');

document.getElementById('hent_fil').onclick = function() {
  fileUpload.click();
};

fileUpload.onchange = function() {
  var loadedCsv = new Promise(function(resolve, reject) {
    var file = fileUpload.files[0];
    fr = new FileReader();
    fr.onload = function() {
      resolve(fr.result);
    };
    fr.onerror = function(err) {
      reject(err);
    };
    fr.readAsText(file);
  });

  var zip = new JSZip();
  var loadedZip = loadFile('empty_project.sb2', 'blob');
  var gotJsonContent = new Promise(function(resolve, reject) {
    loadedZip.then(function(response){
      zip.loadAsync(response).then(function() {
        zip.file('project.json').async('string').then(function(content) {
          resolve(content);
        }, reject);
      }, logError);
    });
  });

  function all_success(values) {
    var csvResponse = values[0];
    var jsonStr = values[1];
    zip.file('project.json', manipulateJson(csvResponse, jsonStr));
  }

  function saveZip() {
    zip.generateAsync({type: 'blob'}).then(function(content) {
      saveAs(content, 'data.sb2');
    }, logError);
  }

  Promise.all([loadedCsv, gotJsonContent]).then(all_success, logError).then(saveZip, logError);

};
</script>

