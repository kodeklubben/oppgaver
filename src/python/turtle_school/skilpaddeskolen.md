---
title: Skilpaddeskolen
level: 2
logo: ../../assets/img/ccuk_logo.png
author: Oversatt fra [Code Club UK](//codeclub.org.uk)
translator: Bjørn Einar Bjartnes
license: "[Code Club World Limited Terms of Service](https://github.com/CodeClub/scratch-curriculum/blob/master/LICENSE.md)"
---

# Steg 1: Flere firkanter {.activity}

## Sjekkliste {.check}

+ Åpne IDLE-editoren, og åpne en ny fil ved å trykke `File > New File`,
og la oss begynne.

  Husk at du skal ha to vinduer åpne. Det ene er 'Python Shell' og det andre er for å skrive kode i.

  Som sist vil den første linjen alltid være `from turtle import *` for å fortelle Python at vi vil tegne ved hjelp av skilpadde-biblioteket!

  ```python
  from turtle import *

  for n in range(4):
      forward(100)
      right(90)
  ```

+ Lagre det som en ny fil, og kjør programmet fra menyen ved å trykke `Run > Run Module`.

  Husk at `for n in range(4)` gjentar koden, og at koden må grupperes med mellomrom (innrykk) for å være en del av for-løkken. Bruk *tab* (knappen rett over *caps lock*) for å flytte kode.

# Steg 2: Forskjellige firkanter {.activity}

La oss bruke variabler for å gjøre programmet vårt lettere å lese og lettere å endre, akkurat som vi gjorde i forrige modul.

## Sjekkliste {.check}

+ Endre programmet så det ser slik ut:

  ```python
  from turtle import *

  sides = 4
  length = 100
  angle = 360/sides

  for n in range(sides):
      forward(length)
      right(angle)
  ```

+ Kjør det ved å trykke `Run > Run Module` fra menyen. Får du den samme firkanten som før? Sjekk at det virker før du går videre.

Dette er et litt langt program, men nå kan vi endre det til å tegne hvilken figur vi vil. Problemet er bare at vi er nødt til å klippe og lime programmet for å få det til. Som tidligere kan vi skrive kode for å slippe å gjenta oss selv (programmerere anstrenger seg gjerne litt slik at de kan være late etterpå!). Denne gangen skal vi lage en *funksjon*. En funksjon er en enkel måte for å gjenbruke en kodeblokk (eller oppskrift om du vil) mange ganger. Funksjonen får et navn, og dette navnet kan vi senere bruke.

# Steg 3: Vi lager en funksjon {.activity}

## Sjekkliste {.check}

+ Vi endrer koden og legger til `def poly():`. `def` betyr definer, altså å lage. Pass på at koden har riktig innrykk og bruk den nye funksjonen. For å få innrykk på flere linjer kan man merke linjene og deretter trykke *tab* (knappen rett over *caps lock*). Dersom du vil ha mindre innrykk, bruk *shift + tab*.

  ```python
  from turtle import *

  def poly(): # vi lager funksjonen
      sides = 4
      length = 100
      angle = 360/sides

      for n in range(sides):
          forward(length)
          right(angle)

  pencolor('red')
  poly() # vi kaller på funksjonen
  right(180)
  poly()
  ```

+ Kjør programmet. Hvis det virker skal to røde firkanter bli tegnet.

Vi sparte litt tid ved å lage en ny funksjon i Python, og nå kan vi tegne en rød firkant to ganger, uten å skrive hele greia to ganger. Den nye funksjonen `poly()` er fin for å slippe å skrive så mye.

# Steg 4: Hvorfor stoppe med firkanter? {.activity}

Vi er ikke ferdige ennå - hva med å endre funksjonen så den kan tegne hvilken som helst form? Som med `forward` og `right`, kan vi sende verdier inn i funksjonen istedenfor å endre koden hver gang.

## Sjekkliste {.check}

+ Endre koden så den ser slik ut:

  ```python
  from turtle import *

  def poly(sides, length):
      angle = 360/sides

      for n in range(sides):
          forward(length)
          right(angle)

  pencolor('red')
  poly(4, 100)
  right(180)
  pencolor('blue')
  poly(3, 150)
  ```

+ Kjør den og se hva som skjer.

  La oss ta dette litt sakte, for dette er ganske kule greier. Istedenfor å bestemme variablene i funksjonen, sier vi at funksjonen tar noen verdier som har navn, og så bruker vi verdiene der vi trenger dem.

  Vi flyttet noen verdier ut av funksjonen, og flyttet dem til den delen av koden som bruker dem. Nå kan vi, med en eneste funksjon, tegne *hvilken som helst* form, med *hvilken som helst farge*. Jeg vet ikke hva du tenker, men dette imponerer meg hver gang jeg tenker på det: Vi kan lære datamaskinen nye triks, og så få den til å gjøre triksene.

Å være i stand til å lage nye funksjoner som kan oppføre seg forskjellig basert på verdiene vi gir inn er et av de kraftigste verktøyene i programmering.

### Tips {.protip}
I python finnes det funksjoner, mens i andre programmeringsspråk finnes det også noe som blir kalt prosedyrer. Disse begrepene går litt inn i hverandre, så det er ikke så farlig om dere ikke ser forskjellen. En funksjon skal gjerne returnere noe, og den skal helst ikke gjøre noe annet enn å regne ut returverdien. I tillegg burde funksjonen alltid returnere det samme når den får samme innputt. Prosedyrer ligner veldig på funksjoner, men de får lov til å returnere forskjellige ting avhenging av andre ting enn innputt. I tillegg er det lov for en prosedyre å gjøre noe annet enn å returnere noe. For eksempel kan en prosedyre tegne på skjermen. I python er det ingen forskjell på funksjoner og prosedyrer, så det er vanlig å bare kalle begge deler for funksjoner.

# Steg 5: Skilpaddestreker {.activity}

## Sjekkliste {.check}

+ Selv om skilpadden er en liten robot som kan tegne, kan den også flytte seg uten å tegne. Husk at vi kan bruke `penup()` og `pendown()` for å slå av og på at skilpadden setter spor. Åpne en ny Python-fil, og skriv inn koden under:

  ```python
  from turtle import *

  length = 200
  for num in range(8):
      forward(length/16)
      penup()
      forward(length/16)
      pendown()
  ```

+ Dette programmet tegner en stiplet linje over skjermen. Kjør det og sjekk!

# Steg 6: Tegne figurer {.activity}

Vi kan koble figur-programmet og stiplet-linje-programmet sammen ved å bytte ut funksjonen `forward` med koden vi har for stiplete linjer. Vi bruker koden for å tegne figurer ytterst, og inni der bruker vi koden for å lage stiplete linjer istedenfor hele streker.

## Sjekkliste {.check}

+ Endre koden så den ser ut som følgende:

  ```python
  from turtle import *
  speed(11)
  shape("turtle")

  def dashpoly(sides, length):
      angle = 360/sides

      for n in range(sides):
          for num in range(8):
              forward(length/16)
              penup()
              forward(length/16)
              pendown()
          right(angle)

  pencolor('red')
  dashpoly(4, 100)
  right(180)
  pencolor('blue')
  dashpoly(3, 150)
  ```
+ Kjør koden og se hva den gjør.

  Vi har to for-løkker inni hverandre, en ytre og en indre. Den ytre løkken `for n in range(sides)` tegner hver kant av figuren, og hver gang kjører den indre løkken `for num in range(8)` som tegner stiplete linjer.

  Den ytre løkken bruker variabelen `n` for å holde styr på hvor mange ganger den har gjentatt seg selv, og den indre løkken bruker variabelen `num` på tilsvarende måte. Du må bruke forskjellige variabelnavn inni løkken, ellers roter du det bare til.

# Steg 7: Byggeklosser for figurer {.activity}

## Sjekkliste {.check}

+ La oss bruke funksjoner igjen for å rydde opp i koden. Endre koden fra steg 6 og la oss dele koden i biter.

  ```python
  from turtle import *
  speed(11)
  shape("turtle")

  def dashforward(length):
      for num in range(8):
          forward(length/16)
          penup()
          forward(length/16)
          pendown()

  def dashpoly(sides, length):
      angle = 360/sides

      for n in range(sides):
          dashforward(length)
          right(angle)

  pencolor('red')
  dashpoly(4, 100)
  right(180)
  pencolor('blue')
  dashpoly(3, 150)
  ```

+ Kjør koden og se at den gjør akkurat det samme som før.

### Tips {.protip}

Trikset er at istedenfor å bygge programmer ved å klippe og lime, kan vi lage nye funksjoner og gjenbruke dem. Da blir koden kortere og litt lettere å forstå.

# Steg 8: Litt tilfeldigheter {.activity}

Hva om vi gjør litt tilfeldige sprell rett før vi er ferdige?  Vi kan be datamaskinen velge et tall for oss, eller velge en farge for oss, litt som om vi kaster terning. Scratch kan dette også, da brukte vi `pick`.

## Sjekkliste {.check}

+ I en ny fil, skriv inn følgende:

  ```python
  from turtle import *
  from random import randrange, choice
  colors = ['red', 'blue', 'green']


  def poly(sides, length):
      angle = 360/sides

      for n in range(sides):
          forward(length)
          right(angle)

  for count in range(10):
      pencolor(choice(colors))
      right(randrange(0,360))
      poly(randrange(3,9), randrange(10,30))
  ```

+ Lagre og kjør koden

  Programmet skal tegne ti figurer i forskjellige farger med forskjellig størrelse. Linjen  `from random import randrange, random` henter inn funksjonene `randrange()` og `choice()`.

  `randrange()` plukker ut et tall mellom det laveste og det høyeste tallet vi gir inn, så `randrange(1, 10)` velger et tall mellom 1 og 9 (Python begynner med 1, og stopper rett før 10).

  `choice()` velger en ting fra listen vi gir inn. En liste er en samling av verdier, for eksempel `[1, 2, 3]`. I koden ovenfor bruker vi listen `colors`, som har verdiene `'red'`, `'blue'`, and `'green'`.

  Ved å bruke `choice()` og `randrange()` kan vi be datamaskinen om å velge farge, størrelse og form for oss, og det kommer til å bli forskjellig resultat nesten hver eneste gang du kjører programmet.

## Flere ting å prøve {.try}

Hva med å prøve flere farger, eller å endre tallene? Hva skjer?
