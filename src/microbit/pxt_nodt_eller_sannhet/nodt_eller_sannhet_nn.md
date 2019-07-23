---
title: "PXT: Nødt eller sannheit"
author: Helene Isnes
translator: Stein Olav Romslo
language: nn
---


# Introduksjon {.intro}

I denne oppgåva skal du lage spelet nødt eller sannheit. Når knapp A vert trykt
skal ei tilfeldig utfordring visast på micro:bit-en, og når knapp B vert trykt
skal eit tilfeldig spørsmål bli vist.


# Steg 1: Lag listene {.activity}

*Det fyrste du må gjere er å lage to lister - ei med utfordringar og ei med
 spørsmål. Me brukar lister sidan dei kan innehalde mange element (her er kvar
 utfordring og kvart spørsmål eitt element), og dette kan me bruke seinare når
 me skal hente ut ei tilfeldig utfordring eller eit tilfeldig spørsmål.*

## Sjekkliste {.check}

- [ ] Lag to lister og lagre dei i variablar. Den eine lista skal innehalde
  utfordringar og den andre skal innehalde spørsmål. Du må finne ut korleis du
  skal gjere dette sjølv. Tips: Du kjem til å trenge klossen under, den finn du
  i `Avansert` -> `Lister`:

![Bilete for å vise klossen me brukar for å lage ei liste](lage_liste.png)

## {.tip}

Døme på spørsmål: Er du redd for edderkoppar?

Døme på utfordring: Syng ein song.


# Steg 2: Vel ei utfordring {.activity}

*Det neste me skal gjere er å lage kode som vel ei utfordring når knapp A vert
 trykt.*

## Sjekkliste {.check}

- [ ] Når knapp A vert trykt skal eit tilfeldig element frå lista med
  utfordringar bli valt, og den valte utfordringa skal visast på skjermen. Til
  dette kan du få bruk for følgjande kloss:

![Bilete for å vise kva kloss ein kan bruke for å finne eit element i ei
liste](element_i_liste.png)

- [ ] Erstatt `list` med variabelen lista di er lagra i, og `0` med nummeret til
  elementet du vil hente ut frå lista. Det fyrste elementet i ei liste er nummer
  `0`, det andre er nummer `1` og så bortetter.


# Steg 3: Vel eit spørsmål {.activity}

*Dette er siste steg før koden din er ferdig. Her skal me lage kode for å velje
 eit spørsmål.*

## Sjekkliste {.check}

- [ ] Gjenta steg 2 for knapp B og lista med spørsmål.

## {.tip}

Det er sannsynlegvis raskare å kopiere (høgreklikk på den ytste ramma) og endre
koden enn å lage den frå grunnen av.


# Steg 4: Testing {.activity}

*No er koden din ferdig, men du kan framleis teste og forbetre koden din slik du
 vil.*

- [ ] Test og gjer forbetringar i koden din til du er fornøgd.

- [ ] Last ned koden på micro:bit-en og spel med nokon andre.
