---
title: "HTML: Legg til lyd og video"
author: "Omsett frå [Code Club UK](//codeclub.org.uk)"
translator: Stein Olav Romslo
language: nn
---


# Introduksjon {.intro}

Lær å leggje til lyd og video på nettsida di!

Det finst fleire måtar å leggje til lyd, bilete og video på nettsidene dine. La
oss sjå på dei saman.


# Legg til video frå YouTube {.activity}

Å leggje til ein video frå YouTube er veldig lett.

- [ ] Gå til sida med videoen på YouTube.

- [ ] Under videospelaren finn du ein `Del`/`Share`-knapp. Trykk på den.

- [ ] For å få kode du kan bruke på nettsida di, trykk `Bygg inn`/`Embed`.

Koden vil likne på dette:

```
<iframe width="560" height="315" src="//www.youtube.com/embed/FjgQbPwkljQ"
  frameborder="0" allowfullscreen></iframe>
```

Denne kodesnutten vil leggje til ein kodeklubbvideo på sida di. Kopier koden og
lim den inn der du vil at videoen skal visast. Legg merke til attributtane
`width` (breidde) og `height` (høgde). Dei gjer at du kan bestemme kor stort
videoen skal visast på nettsida. Gjerne prøv å forandre på dei.


# Legg til ein video frå Vimeo. {.activity}

- [ ] Gå til sida med videoen på Vimeo.

- [ ] Klikk på `Del`/`Share`-knappen i videospelaren.

- [ ] Nedst ser du ein boks med _Embed_. Klikk på den og kopier koden. Koden vil
  likne på dette:

```
<iframe src="http://player.vimeo.com/video/44738167?title=0&amp;byline=0&amp;portrait=0&amp;badge=0" width="600" height="338" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>
```

- [ ] Kopier koden og lim den inn der du vil at videoen skal visast. Legg merke
  til attributtane `width` (breidde) og `height` (høgde). Dei gjer at du kan
  bestemme kor stort videoen skal visast på nettsida. Gjerne prøv å forandre på
  dei.


# Legge til ein video frå datamaskina di {.activity}

Viss du har ein video du har laga sjølv kan du leggje den til på sida utan å
laste den opp på YouTube eller Vimeo.

- [ ] For å leggje til ein video på sida di må du leggje til ein `video`-tagg.

- Akkurat som `img`-taggen har video ein `src`-attributt som peikar på fila:

```
  <video src="romskip_landing.mp4">
  </video>
```

Det som er keisamt når me legg til video er at ikkje alle nettlesarane klarar å
spele av alle videoformata. Formata `.mp4` og `.ogv` fungerer i dei fleste
nettlesarane, så det kan løne seg å lagre videoen din i eitt av desse formata.

- [ ] For å la nettlesaren vite at me har fleire format tilgjengeleg, så kan me
  skrive følgjande kode:

```
  <video>
    <source src="romskip_landing.ogv" type="video/ogg">
    <source src="romskip_landing.mp4" type="video/mp4">
  </video>
```

- [ ] For å leggje til eit bilete som visast før videoen blir spelt av kan du
  bruke `poster`-attributten på videotaggen:

```
  <video poster="romskip_landing.jpg">
    <source src="romskip_landing.ogv" type="video/ogg">
    <source src="romskip_landing.mp4" type="video/mp4">
  </video>
```

- [ ] Viss du vil at videoen skal starte automatisk kan du leggje til
  `autoplay`-attributten. Det gjer du slik:

```
  <video poster="romskip_landing.jpg" autoplay>
    <source src="romskip_landing.ogv" type="video/ogg">
    <source src="romskip_landing.mp4" type="video/mp4">
  </video>
```

- [ ] For å vise knappar til å styre videoen med, som spel av, pause, volum og
  så bortetter, kan du leggje til `controls`-attributten:

```
  <video poster="romskip_landing.jpg" controls>
    <source src="romskip_landing.ogv" type="video/ogg">
    <source src="romskip_landing.mp4" type="video/mp4">
  </video>
```

- [ ] Du kan òg styre storleiken på videoen med `width` (breidde) og `height`
  (høgde) på følgjande måte:

```
  <video poster="romskip_landing.jpg" width="600" height="400">
    <source src="romskip_landing.ogv" type="video/ogg">
    <source src="romskip_landing.mp4" type="video/mp4">
  </video>
```


# Legg til ei lydfil frå datamaskina di {.activity}

Måten ein legg til lydfiler på nettsida er veldig lik måten ein legg til videoar
på.

- [ ] For å leggje til ei lydfil kan du skrive dette:

```
  <audio src="romskip.mp3">
  </audio>
```

Legg merke til `src`-attributten som peikar på fila.

Akkurat som med video er det ikkje alle nettlesarar som kan spele alle typer
lydfiler. For å la flest mogleg få tilgang til å høyre på fila bør du leggje den
til i fleie format. Formata flest nettlesarar klarar å spele av er `.mp3` og
`.oga`.

```
  <audio>
     <source src="romskip.mp3" type='audio/mp3'>
     <source src="romskip.ogg" type='audio/ogg; codecs=vorbis'>
  </audio>
```

- [ ] For å leggje til knappar for å styre lydavspelinga må du leggje til
  `controls`-attributten:

```
  <audio controls>
     <source src="romskip.mp3" type='audio/mp3'>
     <source src="romskip.ogg" type='audio/ogg; codecs=vorbis'>
  </audio>
```

- [ ] Viss du ynskjer at lyden skal starte å spelast av med ein gong nokon går
  inn på nettsida kan du leggje til `autoplay`-attributten på denne måten:

```
  <audio controls autoplay>
     <source src="romskip.mp3" type='audio/mp3'>
     <source src="romskip.ogg" type='audio/ogg; codecs=vorbis'>
  </audio>
```
