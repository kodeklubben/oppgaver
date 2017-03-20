---
title: Fraktaler
level: 3
language: nb-NO
author: Teodor Heggelund
---

# Introduksjon {.intro}

En fraktal er en geometri med et mønster som gjentar seg selv inne i seg selv.
Høres ikke det rart ut? I denne oppgaven skal vi lage våre egne.

Her er Sierpinski-teppet, som er en fraktal:

![](sierpinski.png)

# Steg 1: Hvordan fungerer Sierpinski? {.activity}

Fraktaler følger tre regler:

- **Startregelen** gir hvor vi skal starte. Med en firkant? En trekant? En
  strek?
- **Tegneregelen** gir hvordan vi skal tegne på nivået vi er. Fargelegge en bit
  av firkanten? Splitte en strek i to?
- **Rekursjonsregelen** deler opp figuren vår i mindre biter, som vi kjører på
  nytt i. Lager firkanten vi tegnet nye firkanter? Lager streken vi tegnet nye
  streker? Gjenta for hver strek.

## Sjekkliste {.check}

Gå til [Wikipedia-artikkelen](https://en.wikipedia.org/wiki/Sierpinski_carpet)
til Sierpinski-teppet. Se på animasjonen.

- Hvordan er teppet før det begynner å bli fargelagt? Dette er **startregelen**.
- Hva tegner vi i hver firkant? Dette er **tegneregelen**.
- Hvordan gjentas regelen? Dette er **rekursjonsregelen**.

Se på figurene under avsnittet **Process**. Ser du at noe gjentar seg?

# Steg 2: Tegne firkanter med SVG {.activity}

```elm
type alias Square =
  { corner : Point
  , width : Float
  }


start =
  { corner = { x = 0.0
             , y = 0.0
             }
  , width = 27.0
  }

main =
    div []
      [ h1 [] [ text (toString start) ]
      , svg
        [ width "500", height "500", viewBox "0 0 27 27" ]
        [ rect [ x "0", y "0", width "27", height "27", fill "blue" ] [ ]
        , rect [ x "3", y "3", width "3", height "3", fill "green" ] [ ]
        ]
      ]

```

## Sjekkliste {.check}

- Juster på `x`, `y` og `width` i `start`. Ser du endringene i toppen av siden?
