---
title: "JS: Partikkel-fest"
level: 3
---

# Introduction {.intro}
I denne oppgaven skal vi bruke JavaScript til å få figurer vi å bevege seg. Vi skal altså lære å animere ved hjelp av JavaScript og noe som heter `Canvas`. 

![gif](ressurser/out.gif)

I denne oppgaven vil du få bruk for det du har lært i oppgaven [Grunnleggende JavaScript](../grunnleggene_js/grunnleggende_js.html). 

# Steg 1: Canvas-elementet {.activity}
I HTML bruker vi `<canvas>` til å tegne figurer ved hjelp av JavaScript. Selve `<canvas>`-elementet gjør ikke så stor nytte for seg, så derfor bruker vi JavaScript til å fortelle hva slags grafikk `<canvas>`-elementet skal inneholde. La oss prøve det ut:

+ Åpne favoritt teksteditoren din
+ Lag en ny HTML-fil som heter `partikler.html`
+ Kopier koden under inn i `partikler.html`:

```html
<html>
<head>
    <meta charset="UTF-8">
    <title>Partikkel-fest</title>
    <style>
        body {
            background-color:#666;
        }

        #canvas {
            background-color:#000;
            margin-left:100px;
        }
    </style>

</head>
<body>
    <canvas id="canvas" width="500" height="500"></canvas>
</body>
</html>

```

## Forklaring {.tip}
+ `<canvass id="canvas" width="500" height="500"></canvas>` er selve `Canvas`-elementet. Den har en gitt høyde og bredde `500px x 500px`. Vi skal bruke JavaScript til å lage andre elementer inne i `canvas`-elementet. 
+ I CSSen er det lagt til en `grå` bakgrunnsfarge til `<body>` og sort bakgrunnsfarge til `<canvas>`. 
##

# Steg 2: Tegn et objekt {.activity}
Nå som vi vet hvordan `canvas` ser ut er det på tide å prøve det ut:

+ Sett inn `<script> </script>` i koden din
+ Lag en variabel som henter ut `canvas`-elementet på nettsiden vår:
```js
var canvas = document.getElementById("canvas");
```
+ Lag en variabel som skal holde på grafikken vi tegner på `canvas`-elementet:
```js
var ctx = canvas.getContext("2d");
```


