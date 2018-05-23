---
title: 'Eget prosjekt'
level: 4
language: nb
author: 'Teodor Heggelund'
---

# Introduksjon {.intro}

Har du noe du har hatt lyst til å lage en stund? Nå er sjansen! Under er noen
forslag for å komme i gang.

# Idé 1: spill {.activity}

Her er en måte å sjekke hva brukeren trykker på av knapper:

```elm
module Main exposing (..)

import Html exposing ( text )
import Keyboard

type Msg = Down Int
         | Up Int

model =
    { lastDown = 0
    , lastUp = 0
    }

main =
    Html.program
       { init = ( model, Cmd.none )
       , view = view
       , update = update
       , subscriptions = subscriptions
       }

update msg model =
    let
        newmodel =
            case msg of
                Down d -> { model | lastDown = d }
                Up u -> { model | lastUp = u}
    in
        ( newmodel, Cmd.none )

view model = text ( "Last down: " ++ toString model.lastDown
                    ++ ", last up: " ++ toString model.lastUp )

subscriptions model =
    Sub.batch
        [ Keyboard.downs Down
        , Keyboard.ups Up
        ]
```

## Modulen `Keyboard` {.protip}

`Keyboard` fungerer ikke i **Try Elm**.

Muligheter:

- Prøv [Ellie](https://ellie-app.com/P7GZ5mV9Lja1/0)!

- Kjør lokalt:

  Installer `Keyboard` med `elm package install elm-lang/keyboard`

  Se siden med `elm reactor`.

## Sjekkliste {.check}

- [ ] Hvilke tall (tastekoder) har vi for pil opp? Venstre? Høyre? Ned?

- [ ] Hvilke tall har vi for WASD?

- [ ] Hvilket tall er A?

- [ ] Hvilket tall er B?

Hmm, men nå skjer det ikke så mye. Skal vi ha noe i sanntid, trenger vi en
klokke.

## Sjekkliste {.check}

Ta en titt tilbake
til [Tell sekunder](../07_tell_sekunder/07_tell_sekunder.html).

- [ ] Hvordan fikk vi tiden til å gå her?

- [ ] Klarer du å kombinere oppgavene? Få tiden til å gå _mens_ du sjekker hva
  brukeren trykker på?

Her er det mange muligheter videre! Vi kan for eksempel lage oss koordinater for
noe vi vil tegne, og flytte det rundt med piltastene.
