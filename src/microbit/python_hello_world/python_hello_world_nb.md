---
title: "Python: Hello, World!"
author: "Oversatt fra [microbit-micropython.readthedocs.io](https://microbit-micropython.readthedocs.io/en/latest/tutorials/hello.html)"
translator: Øistein Søvik og Susanne Rynning Seip
language: nb
---


<!-- To get a box around the text about the playlist and to make it distinct from the rest of the exercise-->
# {.tip}

Denne oppgaven er den første i oppgavesamlingen _Programmering i micro-python_.

Vi anbefaler at du laster ned og skriver koden din i [mu editor](https://codewith.mu/){target=_blank} når du jobber med disse oppgavene. Instruksjoner for hvordan man laster ned Mu finner du på nettsiden via linken.

Når Mu er installert kan du koble micro:biten din til datamaskinen via en USB-kabel. Skriv koden din i editor-vinduet og trykk på “Flash”-knappen for å laste koden over på micro:biten. Hvis det ikke fungerer, sørg for at micro:biten har dukket opp som en USB-enhet på datamaskinen din.

# Introduksjon {.intro}

Den tradisjonelle måten å starte å programmere på i et nytt språk er å få
datamaskinen til å si, "Hello, World!" (Altså Hei, verden!).

![Bilde av en microbit som scroller texten "Hello, World!"](scroll-hello1.gif)

Dette kan gjøres som følger med MicroPython

```python
from microbit import *
display.scroll("Hello, World!")
```

Hver linje gjør noe spesielt. Den første linjen

```python
from microbit import *
```

forteller MicroPython å hente alle tingene den trenger for å sammarbeide med BBC
mico:bit. Alt disse tingene er i en modul med navn `microbit` (en modul er et
bibliotek eller sammling av eksisterende kode). Når du skriver `import` så
forteller du MicroPython at du vil bruke det, og `*` er Python's måte i si *alt*
på. Så, `from microbit import *` betyr på godt norsk, "Jeg ønsker å kunne bruke
alt fra microbit kode biblioteket".

Den andre linjen:

```python
display.scroll("Hello, World!")
```

forteller MicroPython at den skal bruke displayet sitt til å scrolle
tekststrengen av bokstaver "Hello, World" over skjermen. Biten `display` er et
*objekt* fra `microbit` modulen som representerer enhetens fysiske display. Vi
kan be displayet gjøre ting ved et punktum `.` etterfulgt av hva som ligner på
en kommando (dette er noe programmerere gjerne kaller for en *metode*). I dette
tilfellet bruker vi `scroll` metoden. Siden `scroll` trenger å vite hvilke tegn
den skal scrolle over det fysiske displayet bruker vi engelske sitat-tegn `"`
(Selv liker jeg å kalle dem for kaninører) mellom parentesene `(` og `)`. Denne
tekststrengen kalles gjerne for et *argument*. Så `display.scroll("Hello,
World!")` betyr på Norsk, "Jeg ønsker at du skal bruke displayet til å scrolle
teksten "Hello, World!". Dersom en metode ikke trenger noen argumenter gjør vi
dette klart ved å bruke tomme parenteser som dette: `()`.


# Din egen melding {.activity}

## Sjekkliste {.check}

- [ ] Kopier "Hello, World!" koden inn i editoren din og flash den til enheten.

- [ ] Endre meldingen slik at den sier hallo til deg. For eksempel, så ville jeg
  kanskje få den til å si "Hallo, Øistein!".

Her er et hint, du trenger å endre `scroll` metoden sitt argument.

## Advarsel {.tip}

Dette virker kanskje ikke. :-)

Dette er hvor ting blir gøy og MicroPython prøver å være hjelpsom. Dersom den
møter en feilmeldingen vil den scrolle en "hjelpsom" melding over micro:bit'ens
display. Dersom den kan, vil den fortelle deg linjenummerer hvor feilen kan
finnes.

Python forventer deg å skrive **akkuratt** den riktige tingen. Så, for eksempel,
`Microbit`, `microbit`, `microBit` er alle forskjellige ting til Python. Dersom
MicroPython klager på en `NameError` er det sannsynligvis fordi du har
feilstavet ett ord. Anta at du heter Bjarte og noen roper på Bjarne, du er nok
smart nok til å forstå at det kanskje var deg de ropte på, men stakkars Python
blir forvirret.

Dersom MicroPython klager på en `SyntaxError` så har du enkelt og greit skrevet
kode på en måte MicroPython ikke klarer å tolke. Sjekk at du ikke mangler noen
spesielle tegn som `"` eller `:`. Å feilplassere eller glemme disse er som å
putte ett punktum midt i en setning. Det kan være vanskelig å forstå akkurat hva
du mener da.

Dersom micro:bit'en slutter å svare: du kan ikke flashe ny kode på den eller
skrive inn kommandoer. Prøv å ta ut USB kabelen (og kabelen til batteriet om
denne og er koblet til) også koble den inn igjen. Det kan være du må avslutte og
starte på nytt programmet du skriver kode i og.

<!--To get the link to the next exercise in a box. -->
# {.tip}
Neste oppgave i samlingen er [Python: Bilder](../python_images/python_images_nb.html){target=_blank}.
Klikk videre for å fortsette gjennom samlingen.
