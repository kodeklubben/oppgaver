---
title: Komme i gang med App Inventor
level: 1
author: Basert på MITs ["Getting Started"-guide](http://appinventor.mit.edu/explore/get-started.html)
translator: Tjerand Silde
license: "[cc-by-sa 3.0](http://creativecommons.org/licenses/by-sa/3.0/)"
---

# Introduksjon {.intro}
Dette er en introduksjon til *MIT App Inventor*, hvor du skal lære å lage applikasjoner til Android. Å lage apps i App Inventor er ganske enkelt, men vi anbefaler at du er godt kjent med programmering i Scratch, samt kan litt engelsk. Før du kan lage egne apps, må du sette opp App Inventor og bli kjent med hvordan det fungerer.


# Steg 1: Logge inn på App Inventor {.activity}

## Sjekkliste {.check}
+ Gå til [ai2.appinventor.mit.edu](http://ai2.appinventor.mit.edu/).
+ Logg inn med en Google-konto, for eksempel en gmail-adresse. Dersom du lurer på om epost-adressen din er en Google-konto, [kan du sjekke det her](https://support.google.com/accounts/answer/40560?hl=no).
+ Når du har logget inn vil App Inventor be om tillatelse til å åpne kontoen din.
+ Trykk **Tillat** for å gi App Inventor tilgang.
+ *Terms of service* kommer nå opp, som må godtas.


# Steg 2: Starte et nytt prosjekt {.activity}

## Sjekkliste {.check}
+ Etter innlogging blir du videresendt til prosjekt-siden.
+ Trykk på **Start new project** for å komme igang.
+ Navngi prosjektet slik du ønsker selv, for eksempel `Test`.
+ Du blir nå videresendt til programmeringen.


# Steg 3: Bli kjent med menyene {.activity}

#### Palette
Til venstre har du en meny som heter **Palette**. Her finner du alle de ulike komponentene du kan bruke til å
  lage en app. Du vil se at det er 9 forskjellige kategorier som du kan trykke på for å få tilgang til komponentene.

#### Viewer
I midten har du en mobil-skjerm med navn **Viewer** som viser deg hvordan appen din ser ut til en hver tid.

#### Components
Den tredje menyen heter **Components**. I denne menyen kan du velge hvilken komponent du vil endre.

#### Properties
Til høyre har du en meny ved navn **Properties**. I denne menyen kan du gjøre endringer på komponentene, for eksempel kan du endre navnet dens og posisjonen dens på skjermen.


# Steg 4: Legge til og koble sammen komponenter {.activity}
For de som allerede er kjent med programmering i Scratch, vil en del allerede være kjent. Både Scratch og MIT App Inventor er *drag-and-drop*. Det vil si at du drar komponenter og kodeblokker fra menyen og til hvor de skal være for å lage et program. Her er et eksempel:

## Sjekkliste {.check}
+ Trykk på knappen **Blocks** i høyre hjørne.
+ En programmeringsskjerm vises.
+ Trykk på kategorien **Logic**.
+ Her ser du hvilke klosser du kan bruke fra **Logic** kategorien.
+ Velg en kloss og dra den over til kode-feltet.
+ Lek deg og se hva som passer i lag.
+ Når du er ferdig, dra all koden til søppelkurven og gå tilbake til **Designer**.

[Her](http://appinventor.mit.edu/explore/designer-blocks.html) kan du se bilder over menyene med beskrivelse på engelsk.


# Steg 5: Lage en test-app {.activity}
For å se hvordan dette fungerer skal vi lage en test-app som sier *Hello World* når man trykker på en knapp. Du har alleredet opprettet prosjektet og gitt det navn, da kan du gå rett på programmeringen.

## Sjekkliste {.check}
+ Legg til en knapp ved å dra `Button` over til skjermen. Om du ikke finner `Button`, ligger den i menyen **Palette** under kategorien **User Interface**.
+ Legg merke til at knappen nå vises på skjermen og at den er valgt under **Components**.
+ Du kan nå bestemme egenskapene til knappen under **Properties**. La oss endre teksten og størrelsen.
+ Endre `FontSize` til `60`.
+ Endre `Height` til `100 pixels`.
+ Endre `Width` til `Fill parent`.
+ Endre `Text` til `Talk to me`.
+ For å sentrere knappen til midten av skjermen, velg `Screen1` under **Components**. + Endre `AlignVertical` til `center`.
+ Inne på egenskapene til `Screen1` kan du også endre navn på appen (`AppName`) og tittel på vinduet (`Title`).
+ Legg til lyd ved å trekke `TextToSpeech` fra **Palette** > **Media** over til skjermen. Legg merke til at `TextToSpeech` ikke vises på skjermen, men legger seg i **Non-visible components** under skjermen.

I neste steg får du se hvordan appen ser ut, selv om den ikke er ferdig.


# Steg 6: Teste appen mens du programmerer {.activity}
Det kan være veldig nyttig å teste appen din mens du lager den for å sjekke at den fungerer. I App Inventor kan du teste appen din på to måter, ved å bruke en Android-telefon eller ved å bruke en Android-emulator på PC-en din. Begge metodene er beskrevet under.

## På en mobiltelefon
Denne metoden lar deg teste appen på din egen Android-telefon.

## Sjekkliste {.check}
+ Installer appen *MIT AI2 Companion* på Google Play.
+ Koble telefonen din til samme trådløsnett som PC-en din er på.
+ Gå til App Inventor og trykk på **Connect** og velg **AI Companion**.
+ Åpne MIT AI2 Companion på telefonen din og scan QR-koden.
+ Nå kan du teste appen.

## På en emulator
For å teste appen din på en emulator trenger du en datamaskin. Første steg er å installere *App Inventor Setup Software*. Hvert operativsystem har sin egen guide for installasjonen:

+ [Windows](http://appinventor.mit.edu/explore/ai2/windows.html)
+ [Mac OS X](http://appinventor.mit.edu/explore/ai2/mac.html)
+ [GNU/Linux](http://appinventor.mit.edu/explore/ai2/linux.html)

Når programmet er installert gjør du følgende:

## Sjekkliste {.check}
+ Åpne **aiStarter**.
    + **Windows:** Du finner aiStarter i startmenyen eller på skrivebordet.
    + **Mac:** aiStarter åpnes automatisk når du slår på maskinen. Hvis det ikke er åpent kan du bruke spotlight (cmd+mellomrom).
    + **Linux:** Skriv inn denne kommandoen i en terminal:

        ```sh
        /usr/google/appinventor/commands-for-appinventor/aiStarter &  
        ```

+ Gå til App Inventor og trykk på **Connect** og velg **Emulator**. Du kan se at "aiStarter" begynner å arbeide, dette kan ta en stund.
+ Etterhvert blir emulatoren klar. Først vises en svart skjerm, så dukker en mobil-bakgrunn opp, før du til slutt får opp appen.

Nå kan du teste appen på emulatoren.

## Problemer {.tip}
Dersom du har problemer, så kan du sjekke ut den [en mer detaljert veiledning på engelsk](http://appinventor.mit.edu/explore/ai2/setup.html).

## {.slaa-av-tip-sekjson}
Nå ser du at du har en knapp på skjermen din som du kan trykke på. Det vil ikkje skje noe når du trykker på den, rett og slett fordi du ikke har skrevet noe kode for det enda. Det kommer du snart til, men aller først må du teste hva som skjer når du legger til ting samtidig som du er koblet til appen.

## Test prosjektet {.flag}
+ Endre egenskapen `BackgroundColor` til `Screen1` under **Components**.
+ Skjer det noe med appen på telefonen eller i emulatoren?
+ Prøv å endre `Title`, `AlignHorizontal` og `AlignVertical`. Hva skjer?


# Steg 7: Fullføre test-appen {.activity}
Nå er vi klar for å programmere komponentene som skal. Det kan du gjøre på følgende måte:

## Sjekkliste {.check}
+ Trykk på "Blocks" i høyre hjørne. Da kommer du til programmeringsskjermen.
+ Trykk på "Button1" under "Blocks" i menyen til venstre. Da kommer en ny meny opp. Velg øverste blokk som heter "when Button1.Click - do",
  og dra den over i "Viewer".
+ Trykk så på "TextToSpeech1" under "Blocks", og velg "call TextToSpeech1.Speak - message". Dra denne inn i blokken som allerede er der.
+ Til slutt kan du trykke på "Text" under "Blocks". Velg den øverste blokken, som er en tom streng, og koble den til "message" i kodeblokken din.
  Klikk inni den tomme strengen og skriv "Hello world!".

Nå er appen din kodet ferdig, men det er lurt å sjekke at den fungerer som den skal.

## Test prosjektet {.flag}
+ Dersom du sjekker appen på telefonen eller emulatoren din, sier den "Hello world!" når du trykker på knappen?


# Steg 8: Bygge en app {.activity}
Når appen din er ferdig, så kan du bygge den. Det vil si at koden din blir pakket sammen til en .apk-fil som du kan installere på en Android-telefon. Du kan også laste filen ned og kjøre den i en emulator. For å bygge appen må du gjøre følgende:

## Sjekkliste {.check}
+ For å laste appen inn på en Android-telefon så må du trykke på "Build" i hovedmenyen øverst, også trykke på "App (provide QR code for .apk)".
  Da vil den bygge appen, også vise deg en QR-kode på skjermen som du kan scanne med telefonene din, for eksempel via "MIT AI2 Companion App".
+ For å laste appen ned til datamaskinen din trykker du på "Build", også på "App (save .apk to my computer)". Da vil du laste ned appen,
  slik at du kan åpne den i en Android-emulator eller sende filen til noen andre.

## Problemer {.tip}
Dersom du ønsker en mer detaljert veiledning for å laste ned og dele appen din så kan du [lese denne siden](http://appinventor.mit.edu/explore/ai2/share.html).


# Steg 9: Lære mer {.activity}
For å lære mer om App Inventor så kan det være lurt å sjekke ut følgende lenker:

## Sjekkliste {.check}
+ [App Inventor på Youtube](https://www.youtube.com/results?search_query=app+inventor).
+ [Veiledninger for å lage apps](http://appinventor.mit.edu/explore/ai2/tutorials.html).
+ [Sjekke ut hvordan alle blokkene fungerer](http://appinventor.mit.edu/explore/ai2/support/blocks.html).
+ [Sjekke ut App Inventor sitt bibliotek](http://appinventor.mit.edu/explore/library.html).
