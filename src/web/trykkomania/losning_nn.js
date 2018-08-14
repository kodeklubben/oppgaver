var poeng = Poeng();

var ball = Ball();
ball.onclick = poeng.auk;
setInterval(function(){
  var x = Math.random() * 80 + '%';
  var y = Math.random() * 80 + '%';
  ball.posisjon(x, y);
}, 2000);

var knapp = Knapp('Prøv ein gong til!');
knapp.onclick = start;

var nedteljing = Nedteljing(stopp);
nedteljing.telNed(10);

function start() {
  poeng.nullstill();
  nedteljing.telNed(10);
  ball.vis();
  knapp.skjul();
}

function stopp() {
  ball.skjul();
  knapp.vis();
}

/**
 * Ball - teiknar ein ball på skjermen.
 *
 * Returnerer ballen som eit HTML-element. Bruk:
 *
 *   var ball = Ball();  // lag ballen
 *   ball.posisjon(1, 2);  // set posisjon til x = 1 og y = 2 i pikslar
 *   ball.vis();  // viser ballen
 *   ball.posisjon('10%', '20%');  // flyttar ballen til posisjon x = 10% og y = 20%
 *   ball.skjul();  // skjuler ballen
 *   ball.onclick = påKlikk;  // køyr `påKlikk()` når ballen blir trykka på
 *
 * Vil du endre korleis det ser ut?
 * Sjå CSS-eigenskapar på https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Properties_Reference
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
 *   poeng.auk();  // aukar poengsummen med 100
 *   poeng.nullstill();  // set poengsummen til 0
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

  el.auk = function () {
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
 * Nedteljing - Ei linje som viser at tida renn ut.
 *
 * Bruk:
 *   var nedteljing = Nedteljing(slutt);  // funksjonen `slutt` køyrast når tida er ute
 *   nedteljing.telNed(10);  // tel ned 10 sekund
 *
 */
function Nedteljing (ferdig) {
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
  el.telNed = function (tid) {
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
 * Ein knapp som ligg midt på sida.
 *
 * Bruk:
 *   var knapp = Knapp('trykk på meg');  // lagar ein knapp som ligg midt på sida
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
    // midten av skjermen er 50 % minus halvparten av storleiken til knappen
    var w = el.offsetWidth / 2;
    var h = el.offsetHeight / 2;
    el.style.marginLeft = '-' + w + 'px';
    el.style.marginTop = '-' + h + 'px';
  };

  return el;
}
