---
title: "CSS: Animasjon"
author: Lars Klingenberg
translator: Stein Olav Romslo
language: nn
---


# Introduksjon {.intro}

I denne oppgåva skal du lære å animere HTML-objekt ved hjelp av CSS. Under ser
du korleis resultatet vil bli til slutt:

![Viser ein animasjon av teksten "Minecraft" som dukkar opp og ei hakke som
treff ein kloss](ressurser/out.gif)

Før me startar å lage animasjonen over må me lære om korleis animasjon fungerer
ved hjelp av CSS. Så la oss starte med det grunnleggjande!

__For å lære mest mogleg bør du åpne ei tom `.html`-fil og skrive koden for hand
når du les oppgåva, då kjem du til å bli ein racer i CSS-animasjon!__


# Steg 1: Animasjons-attributten {.activity}

Animasjon i CSS er ganske enkelt. I utgangspunktet har animasjonen to stadium:
`start` og `slutt`. Mellom `start` og `slutt` kan du leggje inn ulike faser, det
skal me sjå på seinare. Animasjonen vil heller ikkje få i `loop` (altså gjenta
seg sjølv) med mindre du fortel at den skal gjere det.

Før me skal sjå på eit enkelt døme skal me sjå på `animation`-attributtar. Me
skal bruke desse:

```css
#id {
    animation-name: eit-namn;
    animation-duration: 1s;
    animation-timing-function: linear|ease|ease-in|ease-out|ease-in-out|step-start|step-end;
    animation-delay: 1s;
    animation-iteration-count: nummer|infinite;
    animation-direction: normal|reverse|alternate|alternate-reverse;
    animation-fill-mode: none|forwards|backwards|both;
}
```

- `name`: Namnet på animasjonen.

- `duration`: Kor lenge (i sekund) skal animasjonen vare.

- `timing-function`: Korleis mellom-fasane er berekna.

- `delay`: Kor lang forseinking det skal vere før animasjonan startar. Standard
  er 0 sekund.

- `iteration-count`: Kor mange gonger animasjonen skal bli gjenteke.

- `direction`: Bestemmer om animasjonen skal gå baklengs eller ikkje.

- `fill-mode`: Kva stilar som er lagt til før og etter start av animasjonen.

Her er eit enkelt døme på ein boks som går frå venstre til høgre:

<style>
    #boks {
        height: 50px;
        width: 50px;
        background-color: blue;
        position: relative;
        animation-name: fram-og-tilbake;
        animation-duration: 2s;
        animation-iteration-count: infinite;
        animation-direction: alternate;
    }
    @keyframes fram-og-tilbake {
        0% { left:0; }
        100% { left:100px; }
    }
</style>

<div id="boks"></div>

<br>

```html
<!DOCTYPE html>
<html>
<head>
<style>
    #boks {
        height: 50px;
        width: 50px;
        background-color: blue;
        position: relative;
        animation-name: fram-og-tilbake;
        animation-duration: 2s;
        animation-iteration-count: infinite;
        animation-direction: alternate;
    }
    @keyframes fram-og-tilbake {
        0% {
            left: 0px;
        }
        100% {
            left: 100px;
        }
    }
</style>
</head>
<body>
    <div id="boks"></div>
</body>
</html>
```

__La oss sjå nærare på koden over:__

Me har ein `<div>` med ID `boks`, den er `50x50px` med blå bakgrunnsfarge.
Posisjonen er `relative`, som vil seie at me har moglegheita til å flytte på
den.

`animation`-attributtane:

- `name`: fram-og-tilbake

- `duration`: 2s (sekund)

- `timing-function`: Ikkje gjeve, er `ease` som standard.

- `delay`: Ikkje gjeve, sidan me vil at animasjonen skal starte med ein gong og
  standard er `0s`.

- `iteration-count`: infinite (uendeleg, så den vil ikkje stoppe).

- `direction`: alternate (for at den skal gå fram og tilbake)

- `fill-mode`: Ikkje gjeve, sidan animasjonen startar med ein gong og aldri
  sluttar treng me ikkje ein `fill-mode` før eller etter animasjonen.

`@keyframes fram-og-tilbake` er det me brukar for å spesifisere kva som skal
skje under animasjonen. I dette tilfellet har me sett namnet til animasjonen med
`animation-name: fram-og-tilbake`, så me brukar `@keyframes fram-og-tilbake` for
å beskrive animasjonen.

No kan me spesifisere kva me vil at animasjonen skal gjere. Det gjer me innanfor
`@keyframes`. Me har to fasar, ein start og ein slutt. `0%` er starten på
animasjonen og `100%` er slutten. Difor vil boksen vår starte til venstre
(`left: 0px`) og slutte lengre til høgre (`left: 100px`).

__NB!__ Verdiane i `animation`-attributtane kan òg skrivast som ei eiga linje,
men då er det litt vanskelegare å finne ut kva som er kva:

```css
#boks {
    animation: fram-og-tilbake 2s ...;
}
```

## Utfordring {.challenge}

- [ ] Skriv koden inn i favoritt-teksteditoren din, lagre den som ei `.html`-fil
  og gjer oppgåvene under.

- [ ] Få animasjonen til å byte farge frå blå til raud undervegs.

- [ ] Klarar du å få boksen til å flytte seg nedover og oppover?

- [ ] Prøv å få boksen til å bevege seg i ein firkant.


# Steg 2: @keyframes {.activity}

La oss sjå nærare på `@keyframes`. `@keyframes` er CSS som fortel kva steg ein
animasjon består av.

Her kjem nokre døme:

<style>
    #diagonalt {
        height: 50px;
        width: 50px;
        background-color: green;
        position: relative;
        margin-bottom: 100px;
        animation: diagonalt 2s 0s infinite;
    }
    @keyframes diagonalt {
        0% { top: 0px; left: 0px; }
        100% { top: 100px; left: 100px; }
    }
</style>

<div id="diagonalt"></div>

```css
@keyframes diagonalt {
    0% {
      top: 0px;
      left: 0px;
    }
    100% {
      top: 100px;
      left: 100px;
    }
}
```

Dette dømet får eit objekt til å gå diagonalt sidan det startar på `top: 0px;
left: 0px;` og ender på `top: 100px; left: 100px;`.

<style>
    #ned {
        height: 50px;
        width: 50px;
        background-color: red;
        position: relative;
        margin-bottom: 100px;
        animation: ned 2s 0s infinite;
    }
    @keyframes ned {
        0% { top: 0px; }
        100% { top: 100px; }
    }
</style>

<div id="ned"></div>

```css
@keyframes ned {
    0% {
      top: 0px;
    }
    100% {
      top: 100px;
    }
}
```

Her går HTML-objektet nedover ved hjelp av `top`-attributten.

<style>
    #skifte_farge {
        height: 50px;
        width: 50px;
        background-color: blue;
        position: relative;
        animation: skifte_farge 5s 0s infinite;
    }
    @keyframes skifte_farge {
        0% { background-color: blue; }
        50% { background-color: yellow; }
        100% { background-color: red; }
    }
</style>

<div id="skifte_farge"></div>

<br>

```css
@keyframes skifte-farge {
    0% {
      background-color: blue;
    }
    50% {
      background-color: yellow;
    }
    100% {
      background-color: red;
    }
}
```

Merk at i dette dømet har me lagt inn `50%`. Dette er eit døme på at du kan dele
inn animasjonen i fasar mellom `0%` og `100%`. Du kan leggje til så mange fasar
du vil ved å bruke `%`.

**Merk** at du ikkje kan endre på kor lenge animasjonen varar med `@keyframes`
og `%`, då må du endre på `animation-duration`.


# Steg 3: Pakke ut filene {.activity}

No skal me animere øksa og Minecraft-logoen:

![Viser ein animasjon av teksten "Minecraft" som dukkar opp og ei hakke som
treff ein kloss](ressurser/out.gif)

- Last ned og pakk ut [minecraft_animasjon.zip](minecraft_animasjon.zip).

- Åpne `index.html` i favoritt-teksteditoren din og i ein nettlesar.

No vil du ha ei nettside som ser slik ut:

![Minecraft](ressurser/minecraft_1.png){width=100%}

I koden til `index.html` har me eit bakgrunnsbilete og 3 div-ar med følgjande
ID: `pickaxe`, `minecraft` og `block`. Alle desse ID-ane er eit bilete på
nettsida, bakgrunnsbiletet ligg i CSS-en under `body`.

__Dette skal me programmere:__

1. `pickaxe`-a skal kome flygande inn og treffe blokkene.

2. Når øksa har treft blokkene skal logoen kome inn.


# Steg 4: Flygande øks {.activity}

No skal me få `pickaxe`-a til å fly. Me startar med å beskrive animasjonen med
`keyframes`.

## Sjekkliste {.check}

- [ ] Lag ein `@keyframes` med animasjonsnamnet `move-pickaxe`.

- [ ] La figuren starte utanfor skjermen. **Hint:** bruk ein negativ verdi av
  `left`.

- [ ] La `pickaxe`-biletet bevege seg bort til blokkene. Klarar du å finne ut
  kor langt det er? **Hint:** positiv verdi av `left`.

- [ ] Legg til rotasjon med `transform: rotate(antall grader)`.

- [ ] Kan du tenke deg kor `transform: rotate()` bør vere? I `0%` eller `100%`?

- [ ] Prøv deg fram med kor mange gradar du treng for at den skal bli riktig.
  **Hint:** 360 gradar er ein gong, og 720 gradar er to gonger, rundt seg sjølv.

Så legger me til animasjonen til øksa.

## Sjekkliste {.check}

- [ ] Finn `#pickaxe` i CSS-en.

- [ ] Legg til animasjonsnamnet frå `keyframes` med `animation-name`.

- [ ] Legg til `animation-duration` på `2s`.

- [ ] Legg til eit `animation-delay` på `1s`.

- [ ] Set `animation-timing-function` til `linear`.

- [ ] Set `animation-fill-mode` til `forwards`.

<style>
    #pickaxe {
        background-image: url("ressurser/pickaxe.png");
        z-index: 1;
        width: 150px;
        height: 150px;
        position: relative;
        animation: move-pickaxe 2s;
        animation-timing-function: linear;
        animation-fill-mode: forwards;
        animation-iteration-count: infinite;
    }
     @keyframes move-pickaxe {
        0% {
            left:0px;
        }
        100% {
            left: 800px;
            transform: rotate(720deg);
        }
    }
</style>

<div id="pickaxe"></div>

<toggle>
<strong>Forslag til kode så langt</strong>
<hide>

```css
#pickaxe {
    background-image: url("pickaxe.png");
    z-index: 1;
    width: 150px;
    height: 150px;
    position: absolute;
    bottom: 150px;
    left: -150px;
    animation: move-pickaxe 2s;
    animation-delay: 1s;
    animation-timing-function: linear;
    animation-fill-mode: forwards;
}
@keyframes move-pickaxe {
    0% {
        left:-150px;
    }
    100% {
        left: 800px;
        transform: rotate(720deg);
    }
}
```

</hide>
</toggle>


# Steg 5: Flygande logo {.activity}

No som du har klart å få `pickaxe` til å flyge inn med rotasjon er den neste
oppgåva di å få `#minecraft` til kome flygande inn etter at `pickaxe` har
stoppa.

- Bruk det du har lært i oppgåva til no, og prøv å få logoen til å kome inn når
  `pickaxe` er ferdig med animasjonen sin.

<style>
    #minecraft {
        background-image: url("ressurser/minecraft.png");
        width: 616px;
        height: 154px;
        position: relative;
        left: -900px;
        animation: move_minecraft 4s; /* Chrome, Safari, Opera */
        animation-delay: 1s;
        animation-fill-mode: forwards;
        animation-iteration-count: infinite;
    }
    @keyframes move_minecraft {
        0% {
            left: -900px;
        }
        100% {
            left:250px;
        }
    }
</style>

<div id="minecraft"></div>

<toggle>
<strong>Forslag til kode for Minecraft-logo</strong>
<hide>

```css
#minecraft {
    background-image: url("minecraft.png");
    z-index: 1;
    width: 616px;
    height: 154px;
    position: absolute;
    left: -900px;
    animation: move_minecraft 4s;
    animation-delay: 3s;
    animation-fill-mode: forwards;
}
@keyframes move_minecraft {
    0% {
        left: -900px;
    }
    100% {
        left:400px;
    }
}
```

</hide>
</toggle>

__Gratulerer!__ Du har laga din fyrste animasjon!
