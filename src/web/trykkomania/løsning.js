var poeng = Poeng();

var ball = Ball();
ball.onclick = poeng.øk;
setInterval(function(){
  var x = Math.random() * 80 + '%';
  var y = Math.random() * 80 + '%';
  ball.posisjon(x, y);
}, 2000);

var knapp = Knapp('Prøv en gang til!');
knapp.onclick = start;

var nedtelling = Nedtelling(stopp);
nedtelling.tellNed(10);

function start() {
  poeng.nullstill();
  nedtelling.tellNed(10);
  ball.vis();
  knapp.skjul();
}

function stopp() {
  ball.skjul();
  knapp.vis();
}

/**
 * Ball - tegner en ball på skjermen.
 *
 * Returnerer et ballen som et HTML element. Bruk:
 *
 *   var ball = Ball();  // lag ballen
 *   ball.posisjon(1, 2);  // sett posisjon til x = 1 og y = 2 i piksler
 *   ball.vis();  // viser ballen
 *   ball.posisjon('10%', '20%');  // flytter ballen til posisjon x = 10% og y = 20%
 *   ball.skjul();  // skjuler ballen
 *   ball.onclick = påKlikk;  // kjør `påKlikk()` når ballen trykkes på
 *
 * Ønsker du å endre utseende?
 * Se CSS-egenskaper på https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Properties_Reference
 *
 */
function Ball() {
  var el = document.createElement('div');
  el.style.backgroundColor = 'black';
  el.style.width = '60px';
  el.style.height = '60px';
  el.style.borderRadius = '30px';
  el.style.position = 'fixed';

  document.body.appendChild(el);

  el.posisjon = function (x, y) {
    el.style.left = x;
    el.style.top = y;
  };
  el.skjul = function () {
    el.style.display = 'none';
  };
  el.vis = function () {
    el.style.display = '';
  };

  return el;
}

/**
 * Poeng - viser poengsum nede i venstre hjørne.
 *
 * Bruk:
 *   var poeng = Poeng();  // viser poengsummen
 *   poeng.øk();  // øker poengsummen med 100
 *   poeng.nullstill();  // setter poengsummen til 0
 *
 */
function Poeng() {
  var el = document.createElement('div');
  el.style.position = 'fixed';
  el.style.bottom = '5px';
  el.style.left = '8px';
  el.style.padding = '5px';
  el.style.backgroundColor = 'black';
  el.style.color = 'white';

  var _poeng = 0;
  el.innerHTML = _poeng + ' poeng';
  document.body.appendChild(el);

  el.øk = function () {
    _poeng += 100;
    el.innerHTML = _poeng + ' poeng';
  };
  el.nullstill = function () {
    _poeng = 0;
    el.innerHTML = _poeng + ' poeng';
  };

  return el;
}

/**
 * Nedtelling - En linje som viser at tiden renner ut.
 *
 * Bruk:
 *   var nedtelling = Nedtelling(slutt);  // funksjonen `slutt` kjøres når tiden er utløpt
 *   nedtelling.tellNed(10);  // teller ned 10 sekunder
 *
 */
function Nedtelling (ferdig) {
  var el = document.createElement('div');
  el.style.position = 'fixed';
  el.style.left = '0';
  el.style.bottom = '0';
  el.style.height = '100%';
  el.style.width = '3px';
  el.style.backgroundColor = 'red';
  document.body.appendChild(el);

  function prosent (slutt, tid) {
    return (slutt - Date.now()) / tid / 10;
  }
  el.tellNed = function (tid) {
    var slutt = Date.now() + tid * 1000;
    var intervall = setInterval(tegn, 20);
    function tegn () {
      var p = prosent(slutt, tid);
      if (p < 0) {
        el.style.height = '0%';
        clearInterval(intervall);
        ferdig();
      }
      el.style.height = p + '%';
    }
  };

  return el;
}

/**
 * En knapp som ligger midt på siden.
 *
 * Bruk:
 *   var knapp = Knapp('trykk på meg');  // lager en knapp som ligger midt på siden
 *   knapp.vis();  // viser knappen
 *   knapp.skjul();  // skjuler knappen
 */
function Knapp(tekst) {
  var el = document.createElement('button');
  el.style.display = 'none';
  el.innerText = tekst;
  el.style.position = 'fixed';
  el.style.top = '50%';
  el.style.left = '50%';
  el.style.padding = '20px';
  el.style.border = 'solid 1px';
  document.body.appendChild(el);

  el.skjul = function () {
    el.style.display = 'none';
  };
  el.vis = function () {
    el.style.display = '';
    // plasser akkurat på midten
    // midten av skjermen er 50% minus halvparten av størrelsen til knappen
    var w = el.offsetWidth / 2;
    var h = el.offsetHeight / 2;
    el.style.marginLeft = '-' + w + 'px';
    el.style.marginTop = '-' + h + 'px';
  };

  return el;
}
