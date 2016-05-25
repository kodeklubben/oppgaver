---
title: Lyd og bilde på nettsider
level: 3
language: nb-NO
---

# Introduksjon {.intro}

Det finnes flere måte å legge til lyd og bilde på nettsidene dine. La oss ta en titt på de sammen.

# Legg til video fra YouTube {.activity}

Å legge til enn video fra YouTube er veldig lett.

+ Gå til videoen sin side på YouTube
+ Under videospilleren finner du en `Del`/`Share` knapp. Trykk på den.
+ For å få kode du kan bruke på nettsiden din, trykk `Embed`.

Koden vil ligne på dette:
```
<iframe width="560" height="315" src="//www.youtube.com/embed/FjgQbPwkljQ" frameborder="0" allowfullscreen></iframe>
```

Denne kodesnutten vil legge til en kodeklubbvideo på siden din. Kopier koden og lim din der du vil at videoen skal vises. Legg merke til `width`(bredde) og `height`(høyde) attributtene. De gjør at du kan bestemme hvor stort videoen skal  vises på nettsiden. Forsøk gjerne å forandre på de.


# Legg til en video fra Vimeo. {.activity}

+ Gå på videosiden på Vimeo.
+ Klikk på `Del`/`Share` knappen i videospilleren.
+ Nederst vises det en boks med _Embed_. Klikk på den og kopiere koden. Koden vil ligne på dette:

```
<iframe src="http://player.vimeo.com/video/44738167?title=0&amp;byline=0&amp;portrait=0&amp;badge=0" width="600" height="338" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>
```

+ Lim inn koden der du vil at videoen skal vises på siden. Legg merke til `width`(bredde) og `height`(høyde) attributtene. De gjør at du kan bestemme hvor stort videoen skal  vises på nettsiden. Forsøk gjerne å forandre på de.

# Legge til en video fra datamaskinen din {.activity}

Hvis du har en video du har laget kan du legge den til på siden din uten å laste den opp på YouTube eller Vimeo.

+ For å legge til en video på siden din må du legge til en `video` tag. Akkurat som `img` taggen har også video en `src` attributt som peker på filen:

```
  <video src="romskip_landing.mp4">
  </video>
```

Det som er kjedelig når man legger til video er at ikke aller nettleserene klarer å spille av alle videoformatene. `.mp4` og `.ogv` fungere i de fleste nettleserene, så det kan lønne seg å lagre videoen din i et av de formatene.

For å la nettleseren vite at vi har flere formater tilgjengelig, kan vi skrive følgende kode:

```
  <video>
    <source src="romskip_landing.ogv" type="video/ogg">
    <source src="romskip_landing.mp4" type="video/mp4">
  </video>
```

+ For å legge til et bilde som vises før videoen spilles av, kan du bruke 'poster' attributtet på videotaggen:

```
  <video poster="romskip_landing.jpg">
    <source src="romskip_landing.ogv" type="video/ogg">
    <source src="romskip_landing.mp4" type="video/mp4">
  </video>
```

+ Hvis du vil at videoen automatisk skal start å spilles av kan du legge til `autoplay` attributtet. Det gjøres på denne måten:

```
  <video poster="romskip_landing.jpg" autoplay>
    <source src="romskip_landing.ogv" type="video/ogg">
    <source src="romskip_landing.mp4" type="video/mp4">
  </video>
```

+ For å vise knapper til å styre videoen med, sånn som spill av, pause, volum og så videre kan du legge til `controls` attributtet:

```
  <video poster="romskip_landing.jpg" controls>
    <source src="romskip_landing.ogv" type="video/ogg">
    <source src="romskip_landing.mp4" type="video/mp4">
  </video>
```

+ Du kan også styre størrelsen på videoen med `width`(bredde) og `height`(høyde) attributtene på følgende måte:

```
  <video poster="romskip_landing.jpg" width="600" height="400">
    <source src="romskip_landing.ogv" type="video/ogg">
    <source src="romskip_landing.mp4" type="video/mp4">
  </video>
```

# Legg til en lydfil fra datamaskinen din {.activity}

Måten man legger lydfiler til på nettsiden din er ganske lik måten man legger til videoer på.

+ For å legge til en lydfil kan du skrive dette:

```
  <audio src="romskip.mp3">
  </audio>
```

Legg merke til `src` attributtet som peker på filen.

Akkurat som med video er det ikke alle nettlesere som kan spille alle type lydfiler. For å sørge for at flest mulig kan høre på filen bør du legge den til i flere formater. `.mp3` og `.oga` er formatene som flest nettlesere klarer å spille av.

```
  <audio>
     <source src="romskip.mp3" type='audio/mp3'>
     <source src="romskip.ogg" type='audio/ogg; codecs=vorbis'>
  </audio>
```

+ For å legge til knapper for å styre lydavspillingen må du legge til `controls` attributtet:

```
  <audio controls>
     <source src="romskip.mp3" type='audio/mp3'>
     <source src="romskip.ogg" type='audio/ogg; codecs=vorbis'>
  </audio>
```

+ Hvis du ønsker at lyden skal starte å spilles av med en gang man går inn på nettsiden kan du legge til `autoplay` attributten på denn måten:

```
  <audio controls autoplay>
     <source src="romskip.mp3" type='audio/mp3'>
     <source src="romskip.ogg" type='audio/ogg; codecs=vorbis'>
  </audio>
```
