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
  var csvJson = Papa.parse(csvStr, {skipEmptyLines: true});
  console.log('Parsing JSON: ' +  JSON.stringify(csvJson.meta));

  var headers = csvJson.data[0];
  var rows = csvJson.data.slice(1);

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

  var jsonObj = JSON.parse(jsonStr);
  jsonObj['lists'] = children;
  return JSON.stringify(jsonObj);
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
