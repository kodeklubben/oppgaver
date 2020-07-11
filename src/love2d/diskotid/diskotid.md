---
title: Diskotid!
level: 1
author: Abdur-Raheem Idowu
language: nb
---


# Diskotid! {.intro}

I denne oppgaven skal skjermen din bli diskolys!
Vi skal bruke variabler og Love2D funksjoner for å lage kule, tilfeldige
farger når du trykker på mellomromstasten.
Du skal lære hvordan datamaskiner representerer forskjellige farger, og hvordan
du kan bruke Love2D for å reagere når tastaturet blir brukt.

# Steg 1: Digitale farger {.activity}

Før vi begynner med koding, må vi lære hvordan datamaskiner lager/representerer
farger.

Skjermer klarer å lage så mange utallige farger med å kombinere noen få
grunnfarger sammen.
Disse grunnfarger er rød, grønn og blå.
For eksempel, for å lage fargen gul, kombinerer skjermen rød og grønn sammen.
For fargen lilla, kan skjermer bruke rød og blå.
Denne modellen klarer å lage mer enn 16 millioner farger,
og den heter **RGB** for **R**ød, **G**rønn, og **B**lå.

Når du vil at skjermen skal vise et farge, må du si hvor mye rød, hvor mye blå
og hvor mye grønn den fargen har.
Dette kan gjøres i to forksjellige måter:

Et måte å gjøre dette bruker et skala fra 0 til 255:
255 betyr at så masse som mulig av den fargen blir brukt i blandingen,
og 0 betyr at det blir ikke brukt i det hele tatt.

Et annet måte, som Love2D , bruker et skala fra 0 - 1.
Dette systemet er helt lik den forrige, bortsett fra at den bruker desimaltall
i stedet.

Hvis du har et farge, for eksempel "turkis", og du vil vite hvor mye av hvert
grunnfarge du trenger, kan du bruke denne nettsiden:
[https://www.colorhexa.com/](https://www.colorhexa.com/).
Vi finner ut at RGB-"koden" for turkis er (64, 224, 208).
I Love2D, kan du representere turkis med (0.251, 0.878, 0.816).

Ok, nok teori.
Ta et titt på oppgavene nedover, og da kan vi starte med selve diskoen.

## Lære mer om farger {.check}

- [ ] Hva er RGB koden til favorittfargen din? Du kan søke det på Google,
eller bruke nettsiden nevnt ovenfor.

- [ ] Du kan lese mer om fargeblanding her på
[SNL](https://snl.no/farge#-Fargeblanding) (Store Norske Leksikon).
Hvilken fargeblanding modell bruker printere?

# Steg 2: Sette opp variabler og tegne på skjermen {.activity}

## Oppsett {.check}

- [ ] Sette opp farge variablene

For ett farge, trenger vi tre "tall" variabler:
et for rød-komponenten, grønn-komponenten og blå-komponenten.
La oss lage disse i `love.load()`:

```lua
function love.load()
    rød = 0
    grønn = 0
    blå = 0
end
```

- [ ] Tegne skjermen med denne fargen

Her kan vi bruke funksjonen `love.graphics.setBackgroundColor()`.
Den tar tre argumenter: rød, grønn og blå (NB. i den rekkefølgen! Husk på *RGB*)
komponentene av fargen vi vil at skjermen skal være.
Denne funksjonen går i `love.draw()`:

```lua
function love.draw()
    love.graphics.setBackgroundColor(rød, grønn, blå)
end
```

## Teste koden {.flag}

Kjøre koden med Love2D. Du bør se et svart skjerm.
Dette er fordi vi valgt 0,0,0 for alle komponentene sist, som betyr at ingen
farger blir blandet sammen - dette er jo svart!

Prøv å endre på disse tallene å lage flere farger!

# Steg 3: Reagere på trykk på tastaturet {.activity}

Love2D er et supert spillmotor siden den har så mange funksjoner som gjør det
enkelt for oss å lage hva som helst vi vil.
For å sjekke om et knapp er trykket
eller ikke, kan vi bruke `love.keyboard.isDown()`.
Denne funksjonen tar et
argument: hvilken knapp vi vil sjekke, og gir oss tilbake et Boolean -
`true` hvis knappen blir trykket, og `false` hvis ikke.
La oss bruke mellomrom knappen.

Da kan vi bruke et "IF" statement for å kjøre kode basert på om ett knapp er
trykket eller ikke. I andre ord, kode i et IF-blokk kjøres bare om kondisjonen
er `true`.

Men hva er det vi vil gjøre? Det skal være et disko, så hva med om vi bytter
fargen på skjermen, helt tilfeldig (som på et ekte disko)?
Da er det enda et Love2D funksjon som kan hjelpe oss her: `love.math.random()`.
Dette gir oss et tilfeldig desimal tall fra 0 til 1.

Denne funksjonen kan gi oss nye RGB komponenter, så nye farger!

## Koding {.check}

- [ ] Sjekke om mellomroms knappen er trykket eller ikke

Vi vil skjekke dette kontinuerlig(over og over igjen), og vi tegner ikke på
skjermen, så dette koden bør gå inn i `love.update()`:

```lua
function love.update()
    if love.keyboard.isDown("space") then -- space er mellomrom på engelsk
        --koden her kjøres om knappen er trykket
    end
end
```

- [ ] Endre på farge variablene

Denne koden skal gå inne i IF statementen vi nettop lagde.

```lua
rød = love.math.random()
blå = love.math.random()
grønn = love.math.random()
```

## Teste koden {.flag}

Kjøre koden med Love2D, og trykke på mellomroms knappen.
Fargen på skjermen skal skiftes! Du kan også holde knappen ned for ekte diskolys!

Hvis det funker ikke, dobbeltsjekk koden din. Hele koden bør se sånn ut:

```lua
function love.load()
    rød = 0
    blå = 0
    grønn = 0
end

function love.update()
    if love.keyboard.isDown("space") then
        rød = love.math.random()
        blå = love.math.random()
        grønn = love.math.random()
    end
end

function love.draw()
   love.graphics.setBackgroundColor(rød, blå, grønn)
end
```

Da er diskolysene ferdig! Bra jobbet! Hvis du ønsker mer utfordring kan du prøve
ekstra oppgavene nedover.

## Ekstraoppgaver {.check}

- [ ] Legge til favoritt musikken din.

- [ ] Animere et karakter og la den danse med lyset!

- [ ] Noen av fargene som blir valgt er ikke veldig pen ut/er ikke særlig disco
farger. Er det et måte vi kan bare generere "fine farger"?

- [ ] Hvis du holder ned på mellomroms knappen, så bytter programmet veldig fort
gjennom farger, og det ser ikke veldig bra ut. Er det mulig vi kan gjøre det
litt saktere? Hint: Bruk [delta time](https://love2d.org/wiki/dt) og
en [debounce](https://www.google.com/search?q=debounce) variabel.
