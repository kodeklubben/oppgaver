---
title: "JS: Partikkel-gravitasjon"
author: Lars Klingenberg
language: nb
---


# Introduksjon {.intro}

I denne oppgaven skal vi ta utgangspunkt i animasjone vi lagde i oppgaven
[Partikkel-animasjon](https://oppgaver.kidsakoder.no/web/partikkel_animasjon/partikkel_animasjon){target=_blank}.
Dersom du ikke har gjort denne oppgaven anbefaler vi deg om å gå tilbake å gjøre
den før du fortsetter her.

Oppgaven her går ut på å legge til gravitasjon på `Partikkel`-objektet. Du vil
få presentert hva du skal gjøre, så du må selv finne ut hvordan man skriver kode
for å få det til. Til slutt kommer det til å se noe slik ut:

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

Det første vi skal gjøre er å få partikkelen til å falle, for å få det til å
skje må du programmere følgende:

- [ ] Legg til to attributter i `particle` som skal holde styr på
  `gravitasjonen` og `hastigheten` den faller med. `Gravitasjons`-attributtet
  bør være et lite tall, som for eksempel `0.01`. `Hastigheten` bør være `0` fra
  starten av

- [ ] Sett et passende startsted for `particle`, helst høyt oppe

For hver gang `draw()` kjører, skal følgende skje:

- `hastighets`-attributtet skal endres med `gravitasjons`-attributtet

- `particle` sin `y`-posisjon blir endret med `hastighets`-attributtet

<toggle>
    <strong> Hint </strong>
    <hide>
    objekt.hastighet += objekt.gravitasjon eller
    objekt.hastighet = objekt.hastighet + objekt.gravitasjon
    </hide>
</toggle>

Faller partikkelen nå? Nå som partikkelen faller ser du kanskje også at det
faller igjennom skjermen, derfor må vi legge til en sjekk om gjør at den stopper
nederst.


# Steg 2: Stopp nederst på skjermen {.activity}

For at partikkelen vårt skal stoppe nederst på skjermen trenger vi enkelt og
greit en sjekk hver gang vi kjører `draw()`

- [ ] Lag en sjekk som sjekker om `particle` sin `y`-verdi er større enn høyden
  på `canvas`-objektet. OBS! Du vil sikkert merke at den "rister" helt nederst,
  derfor må du også ta hensyn til størrelsen på partikkel-objektet når du
  sjekker hvor langt ned den er.

<toggle>
    <strong> Hint </strong>
    <hide>
    Lag en variabel som holder på verdien til `canvas.height - particle.size`.
    </hide>
</toggle>

- [ ] I sjekken må du stoppe partikkelen ved å sette `y`-verdien. Kan du tenke
  deg til hva `y`-verdien bør være?

Nå har du et fallende objekt!

## Utfordringer {.challenge}

- [ ] Når partikkelen treffer kanten, snu gravitasjonen sånn at partikkelen går
  oppover

- [ ] Klarer du å få partikkelen til å gå til venster eller høyre også

- [ ] "Steng" alle kantene i `canvas` ved hjelp av flere `if`-setninger


# Steg 3: Få partikkelen til å fly! {.activity}

Nå som vi har fått gravitasjon på partikkelen vårt kan vi legge til styring på
partikkelen ved hjelp av knapper. Vi skal nå programmere slik at når du trykker
`pil opp` så gir vi partikkelen negativ akselerasjon og når vi slipper så blir
den påvirket av gravitasjonen. Får å gjøre dette bruker vi noe som heter
`onkeyup`, `onkeydown` og `keyCode`.

For å kunne utføre en operasjon når vi trykker på en knapp må vi ha denne koden:

```js
window.onkeydown = function(inputKey) {
    var key = inputKey.keyCode ? inputKey.keyCode : inputKey.which;

    if (key == //knapp-koden) {
        // Kode som skal utføres
    }
}
```

- [ ] Bruk [keycode.info](http://keycode.info) til å finne ut hvilke
  `knapp-kode` knappen du vil bruke har.

## Forklaring {.challenge}

- `window.onkeydown` er en funksjon som sjekker om en knapp trykkes ned, dersom
  den gjør det, så kjøres funksjonen med `knapp-kode` `inputKey`.

- `var key = inputKey.keyCode ? inputKey.keyCode : inputKey.which;` er en
  enklere måte å skrive dette på:

```js
if(inputKey.keyCode) {
    var key = inputKey.keyCode;
} else {
    var key = inputKey.which;
}
```

Grunnen til at du må bruke `keyCode` og `which` er fordi ikke alle nettlesere
støtter `keyCode`, men bruker `which` istedet.

+ I `if (key == //knapp-kode)` må du skrive kode for at gravitasjonen skal være
  negativ, prøv med forskjellige tall.

##

- [ ] For at du skal få gravitasjonen tilbake når du slipper knappen må du lage
  en funksjon for `window.onkeyup`.

- [ ] Les mer om `window.onkeyup` osv her: [w3school](http://www.w3schools.com/jsref/event_onkeydown.asp){target=_blank}

Dersom du står bomfast: [Forslag til
kode](https://jsbin.com/sezumakiyo/edit?html,output){target=_blank}
