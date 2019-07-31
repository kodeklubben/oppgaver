---
title: "Python: Retningar"
author: "Omsett frå [microbit-micropython.readthedocs.io](https://microbit-micropython.readthedocs.io/en/latest/tutorials/direction.html)"
translator: Stein Olav Romslo
language: nn
---


# Introduksjon {.intro}

Visste du at micro:bit-en inneheldt eit kompass? Viss du nokon gong skal lage
ein værstasjon kan du bestemme vindretninga, eller du kan navigere deg gjennom
Amazonas.


# Kompass {.activity}

Eit bruksområde for kompasset er å fortelje deg kva retning som er nord:

```python
from microbit import *

compass.calibrate()

while True:
    needle = ((15 - compass.heading()) // 30) % 12
    display.show(Image.ALL_CLOCKS[needle])
```

## Merk {.tip}

**Du må kalibrere kompasset før det kan gjere målingar.** Viss du gløymer å
gjere dette vil kompasset berre vise tull. Metoden `calibration` køyrer eit
kjekt lite program som hjelper micro:bit-en å finne ut kor den er i høve til
jorda sitt magnetfelt.

For å kalibrere kompasset må du snu rundt på micro:bit-en til ein sirkel av
pikslar er teikna på kanten av displayet.

##

I reisten av oppgåva skal me prøve å bryte ned kva koden over gjer, sidan det
kan vere vanskeleg å forstå detaljane i ein gong.

## Activity checklist {.check}

- [ ] Køyr koden over og bestem retninga til nord, aust, sør og vest.

![Viser dei fire himmelretningane](Brosen_windrose_no.svg)

No skal me sjå nærare på kva `compass.calibrate()` gjer.

- [ ] Køyr koden under

```python
from microbit import *

compass.calibrate()

while True:
    display.scroll(str(compass.calibrate()))
```

- [ ] Kva verdi viser koden over når du peikar micro:bit-en i kvar av dei fire
  himmelretningane? Bruk denne informasjonen til å bestemme kva
  `compass.calibrate()` gjer.

<toggle>
  <strong>Hint</strong>
  <hide>

Funksjonen `compass.calibrate()` viser altså kor mange grader unna nord me står.
Med andre ord gir funksjonen ut eit tal slik at `0 ≤ compass.calibrate() < 360`.

</hide>
</toggle>

- [ ] Endre verdien for `A` til ulike heiltal. Kva heiltal er lovlege, og kva
  viser displayet?

```python
from microbit import *

display.show(Image.ALL_CLOCKS[A])
```

<toggle>
  <strong>Hint</strong>
  <hide>

Som du kanskje har funne ut er `ALL_CLOCKS` ei liste som inneheldt 12 ulike
bilete, desse kan veljast frå og med `0` til og med `11`.

</hide>
</toggle>

- [ ] Test ut koden under og varier `A` frå og med `0` til og med `360`. Kva
  skjer?

```python
from microbit import *

display.show((15 - A // 30) % 12)
```

Gratulererer! Viss du har klart å løyse oppgåvene over er du klar til å gå ut og
utforske verda med kompasset ditt!
