---
title: "JS: Partikkel-gravitasjon"
author: Lars Klingenberg
translator: Stein Olav Romslo
language: nn
---


# Introduksjon {.intro}

I denne oppgåva tek me utgangspunkt i animasjonen me laga i oppgåva
[Partikkel-animasjon](https://oppgaver.kidsakoder.no/web/partikkel_animasjon/partikkel_animasjon_nn){target=_blank}.
Viss du ikkje har gjort den oppgåva anbefalar me at du gjer den før du fortset her.

Denne oppgåva går ut på å leggje til gravitasjon på `partikkel`-objektet. Du får
presentert kva du skal gjere, men du må sjølv finne ut korleis du skriv kode for
å få det til. Til slutt kjem det til å sjå ut omlag som dette:

<script>
        var canvas, ctx;

        var particle = {
            x: 125,
            y: 0,
            gravity: 0.05,
            gravitySpeed: 0,
            size: 10

        };

        window.onload = function() {
            canvas = document.getElementById("canvas");
            ctx = canvas.getContext("2d");
            setInterval(draw, 30);
        };


        function draw() {
            ctx.clearRect(0,0,250,250);

            ctx.fillStyle = 'red';
            ctx.fillRect(particle.x, particle.y,particle.size,particle.size);

            particle.gravitySpeed += particle.gravity;
            particle.y += particle.gravitySpeed;

            kant = canvas.height - particle.size;
            if(particle.y > kant){
                particle.y = kant;
                particle.gravitySpeed = 0;

                setTimeout(function() { particle.y = 0; }, 2000);
            }

        }

</script>

<canvas id="canvas" width="250" height="250"></canvas>


# Steg 1: Få partikkelen til å falle {.activity}

Det fyrste me skal gjere er å få partikkelen til å falle, og for å få til det må
du programmere det følgjande:

- [ ] Legg til to attributtar i `particle`: `gravitasjon` som styrer
  akselerasjonen nedover, og `hastigheit` som er farta den fell med. Du bør
  velje eit lite tal for `gravitasjon`, til dømes `0.01`. Frå starten bør
  `hastigheit` vere `0`.

- [ ] Set ein passande startstad for `particle`, helst høgt oppe.

For kvar gong `draw()` køyrer, skal følgjande skje:

- Attributten `hastigheit` skal endrast med `gravitasjon`-attributten.

- `y`-posisjonen til `particle` blir endra med `hastigheit`-attributten.

<toggle>
    <strong> Hint </strong>
    <hide>
    objekt.hastigheit += objekt.gravitasjon eller
    objekt.hastigheit = objekt.hastigheit + objekt.gravitasjon
    </hide>
</toggle>

Fell partikkelen no? Når partikkelen fell ser du kanskje òg at den fell gjennom
skjermen. Difor må me leggje til ein sjekk som gjer at den stoppar nedst.


# Steg 2: Stopp nedst på skjermen {.activity}

For at partikkelen vår skal stoppe nedst på skjermen treng me enkelt og greit
ein sjekk kvar gong me køyrer `draw()`

- [ ] Lag ein sjekk som kontrollerer om `particle` sin `y`-verdi er større enn
  høgda på `canvas`-objektet. OBS! Du vil sikkert merke at den "ristar" heilt
  nedst, difor må du òg ta omsyn til storleiken på partikkel-objektet når du
  sjekkar kor langt ned den er.

<toggle>
    <strong> Hint </strong>
    <hide>
    Lag ein variabel som heldt på verdien til `canvas.height - particle.size`.
    </hide>
</toggle>

- [ ] I sjekken må du stoppe partikkelen ved å setje `y`-verdien. Kan du tenke
  deg kva `y`-verdien bør vere?

No har du eit fallande objekt!

## Utfordringar {.challenge}

- [ ] Når partikkelen treff kanten, snu gravitasjonen slik at partikkelen går
  oppover.

- [ ] Klarar du å få partikkelen til å gå til venstre eller høgre òg?

- [ ] "Steng" alle kantane i `canvas` ved hjelp av fleire `if`-setningar.


# Steg 3: Få partikkelen til å flyge! {.activity}

No som me har fått gravitasjon på partikkelen vår kan me leggje til styring på
partikkelen ved hjelp av tastar. Me skal programmere slik at når du trykkar `pil
opp` så gir du partikkelen negativ akselerasjon, og når me slepp att blir den
påverka av gravitasjonen ned att. For å gjere det brukar me noko som heiter
`onkeyup`, `onkeydown` og `keyCode`.

For å kunne utføre ein operasjon når me trykkar på ein tast må me ha denne
koden:

```js
window.onkeydown = function(inputKey) {
    var key = inputKey.keyCode ? inputKey.keyCode : inputKey.which;

    if (key == TAST) {
        // Kode som skal utførast når TAST blir trykka.
      }
}
```

- [ ] Bruk [keycode.info](http://keycode.info) til å finne ut kva `tastekode`
  tasten du vil bruke har.

## Forklaring {.challenge}

- `window.onkeydown` er ein funksjon som sjekkar om ein tast blir trykka ned, og
  viss den gjer det blir funksjonen køyrt med `tastekode` lik `inputKey`.

- `var key = inputKey.keyCode ? inputKey.keyCode : inputKey.which;` er ein
  enklare måte å skrive dette på:

```js
if(inputKey.keyCode) {
    var key = inputKey.keyCode;
} else {
    var key = inputKey.which;
}
```

Grunnen til at du må bruke `keyCode` og `which` er fordi ikkje alle nettlesarar
støttar `keyCode`, men dei brukar `which` i staden.

- I `if (key == TAST)` må du skrive kode for at gravitasjonen skal vere negativ.
  Prøv med ulike tal.

##

- [ ] For at du skal få att gravitasjonen når du slepp tasten må du lage ein
  funksjon for `window.onkeyup`.

- [ ] Les meir om `window.onkeyup` og meir her: [w3school](http://www.w3schools.com/jsref/event_onkeydown.asp){target=_blank}

Viss du står heilt bom fast kan du sjå her: [Forslag til
kode](https://jsbin.com/sezumakiyo/edit?html,output){target=_blank}.
