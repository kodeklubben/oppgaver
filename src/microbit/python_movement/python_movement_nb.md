---
title: "Python: Tilfeldig"
level: 2
author: "Oversatt fra [microbit-micropython.readthedocs.io](https://microbit-micropython.readthedocs.io/en/latest/tutorials/random.html)"
license: "[The MIT License (MIT)](https://github.com/bbcmicrobit/micropython/blob/master/LICENSE)"
translator: "Øistein Søvik"
language: nb
---


# Introduksjon {.intro}

Er du lei av at enheten din gjør det samme hver gang, ønsker du kanskje å gjøre utfallet mer spennende? I denne oppgaven skal vi lære hvordan vi kan få enheten til å oppføre seg tilsynelatende tilfeldig.

MicroPython har en `random` modul som gjør det enkelt å inkludere tilfeldigheter og litt kaos inn i koden din. For eksempel, her er hvordan en kan scrolle et tilfeldig navn over displayet:

```python
from microbit import *
import random

navn = ["Mari", "Yolanda", "Jakob", "Sofie", "Kushal", "Mei Xiu", "William" ]

display.scroll(random.choice(names))
```

Listen (`navn`) inneholder syv navn som er definert som tekststrenger. Den siste
linjen er en nøstet (Tenk på lagene på en "løk" som vi nevnte tidligere):
metoden `random.choice` tar inn listen `navn` som et argument og returnerer et
tilfeldig element. Dette elementer er argumentet til `display.scroll`.

## Prøv det ut selv {.check}

- [ ] Endre på listen og inkluder dine egne navn. 

- [ ] Hva kan bruksområdet til en slik liste være? Tenk ut 2 tilfeller hva du kan bruke en slik liste til. ()

- [ ] Inkluder samme navnet flere ganger i listen. Hva skjer?


# Tilfeldige tall {.activity}

Tifleldige tall er veldig nyttige og er vanlige i spill. Vet du om andre plasser vi bruker terninger?

MicroPython kommer utrustet med en rekke nyttige metoder få 
