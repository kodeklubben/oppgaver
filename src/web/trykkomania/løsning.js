// Poengsum nede i hjørnet.
var poeng = Poeng()

// Når ball klikkes, kjør `poeng.ink`.
var ball = Ball(poeng.ink)

// Nedtelling på ti sekunder. Når ferdig, kjør stopp.
var nedtelling = Nedtelling(10, stopp)

// Omstartsknapp. Kjør `start` når knappen klikkes.
var omstart = Omstart(start)

// Start spillet.
start()



/**
 * Starter spillet.
 */
function start () {
  omstart.skjul()
  poeng.nullstill()
  ball.hoppTilfeldig()
  nedtelling.start()
}

/**
 * Stopper spillet.
 */
function stopp () {
  ball.stopp()
  omstart.vis()
}

/**
 * En knapp som kjører `handterKlikk` når den klikkes.
 */
function Omstart(handterKlikk) {
  var el = document.createElement('button')
  el.style.display = 'none'
  el.innerText = 'Prøv en gang til'
  el.style.position = 'fixed'
  el.style.top = '50%'
  el.style.left = '50%'
  el.style.padding = '20px'
  el.onclick = handterKlikk
  document.body.appendChild(el)

  return {
    skjul: function () {
      el.style.display = 'none'
    },
    vis: function () {
      el.style.display = ''
      var w = el.offsetWidth / 2
      var h = el.offsetHeight / 2
      el.style.marginLeft = '-' + w + 'px'
      el.style.marginTop = '-' + h + 'px'
    }
  }
}

/**
 * Ball - tegner en ball på skjermen.
 *
 * `handleClick` kjøres hver gang ballen trykkes.
 *
 * Returnerer et objekt med funksjonene
 *   `hoppTilfeldig()` og
 *   `stopp()`.
 *
 * Ballen vises ikke før `hoppTilfeldig` kjøres for første gang.
 *
 * Ønsker du å endre utseende?
 * Se CSS-egenskaper på https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Properties_Reference
 *
 */
function Ball (handtereKlikk) {
  var el = document.createElement('div')
  el.style.display = 'none'
  el.style.backgroundColor = 'black'
  el.style.width = '60px'
  el.style.height = '60px'
  el.style.borderRadius = '30px'
  el.style.position = 'fixed'
  el.onclick = handtereKlikk
  document.body.appendChild(el)

  var intervall

  function tegn () {
    var x = tilfeldig()
    var y = tilfeldig()
    el.style.display = ''
    el.style.left = x
    el.style.top = y
  }
  function hoppTilfeldig () {
    tegn()
    intervall = setInterval(tegn, 1500)
  }
  function stopp () {
    clearInterval(intervall)
    el.style.display = 'none'
  }

  return { hoppTilfeldig: hoppTilfeldig, stopp: stopp  }
}

/**
 * Poeng - viser poengsum nede i venstre hjørne.
 *
 * Returnerer et objekt med funksjonen `ink(i)` som øker poengsummen.
 *
 */
function Poeng () {
  var el = document.createElement('div')
  el.style.position = 'fixed'
  el.style.bottom = '5px'
  el.style.left = '8px'
  el.style.padding = '5px'
  el.style.backgroundColor = 'black'
  el.style.color = 'white'

  var poeng = 0
  el.innerHTML = poeng + ' poeng'
  document.body.appendChild(el)

  function ink () {
    poeng += 100
    el.innerHTML = poeng + ' poeng'
  }
  function nullstill () {
    poeng = 0
    el.innerHTML = poeng + ' poeng'
  }

  return { ink: ink, nullstill: nullstill }
}

/**
 * Nedtelling - Viser en linje som visualiserer at tiden renner ut.
 *
 * Bruk: Nedtelling(tid, slutt)
 *   `tid` i sekunder.
 *   `slutt` funksjon som kjøres når
 *
 */
function Nedtelling (tid, ferdig) {
  var el = document.createElement('div')
  el.style.position = 'fixed'
  el.style.left = '0'
  el.style.bottom = '0'
  el.style.height = '100%'
  el.style.width = '3px'
  el.style.backgroundColor = 'red'
  document.body.appendChild(el)

  function prosent (slutt) {
    return (slutt - Date.now()) / tid / 10
  }

  function start () {
    var slutt = Date.now() + tid * 1000
    var intervall = setInterval(function () {
      var p = prosent(slutt)
      if (p < 0) {
        el.style.height = '0%'
        clearInterval(intervall)
        ferdig()
      }
      el.style.height = p + '%'
    }, 20)
  }

  return { start: start }
}

/**
 * Tilfeldig x/y-koordinat mellom 10% og 90%.
 */
function tilfeldig () {
  var prosent = (0.1 + Math.random() * 0.8) * 100
  return prosent + '%'
}
