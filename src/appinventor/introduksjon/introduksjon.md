---
title: Komme igang med App Inventor
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

# Steg 2: Starte et nytt prosjekt {.activity}

## Sjekkliste {.check}

+ Etter innlogging blir du videresendt til prosjekt-siden.
+ Trykk på **Start new project** for å komme igang.
+ Navngi prosjektet slik du ønsker selv, for eksempel `HelloWorld`.
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
Til høyre har du en meny ved navn **Properties**. I denne menyen kan du gjøre endringer på komponentene, for eksempel kan
  du endre navnet dens og posisjonen dens på skjermen.

# Steg 4: Legge til og koble sammen komponenter {.activity}

For de som allerede er kjent med programmering i Scratch, vil en del allerede være kjent. Både Scratch og MIT App Inventor er *Drag-and-drop*. Det vil si at du drar komponenter og kodeblokker fra menyen og til hvor de skal være for å lage et program. Her er et eksempel:

## Sjekkliste {.check}

+ Trykk på knappen i høyre hjørne med navnet **Blocks**.
+ En programmeringsskjerm vises.
+ Trykk på kategorien **Logic**.
+ Her ser du hvilke funksjoner du kan bruke fra **Logic** kategorien.
+ Velg en funksjon og dra den over til kode-feltet.
+ Klikk på funksjonen din og dra den over til søppelbøtta nede til høyre for å fjerne den igjen.

Samme framgangsmåte brukes for å legge til og fjerne komponenter i appen. Trykk [her](http://appinventor.mit.edu/explore/designer-blocks.html) for å se hvordan det ser ut.

# Steg 5: Lage en test-app {.activity}

For å se litt på hvordan dette fungerer, skal du lage en test-app. Du har alleredet opprettet prosjektet og gitt det navn. Da kan du gå rett på programmeringen. Appen skal ha en knapp med teksten `Hello world`. Når knappen trykkes så skal appen si `Hello world`. Dette kan du få til ved å gjøre følgende:

## Sjekkliste {.check}

+ Det første du gjør er å legge inn en knapp på skjermen. Det gjør du ved å gå til **Palette** og **User Interface**.
  Der velger du **Button**, og drar den over til skjermem i **Viewer**. Legg merke til at knappen vises på skjermen.
+ Neste steg er å legge inn lyd. Dette gjør du ved å gå til **Palette** og **Media**. Der velger du **TextToSpeech**,
  og drar den over til skjermer vår i **Viewer**. Legg merke til at den ikke vises på skjermen, men legger seg
  under **Non-visible components**.
+ Så vil du endre litt på designet. Det første du gjør da er å trykke på **Screen1** på **Components**,
  hvor du går til **AlignHorizontal** og velger **Center**. Du kan også gå til **AlignVertical** og velge **Center**.
  Til slutt kan du gå til **Title** og skrive inn `Hello world`.
+ Vi vil også endre litt på knappen. Dette gjør vi ved å trykke på **Button1** under **Components**. Der endrer vi **FrontSize** til `60`,
  **Height** til `100 pixels`, **Width** til `Fill parent` og **Text** til `Hello world`.

I neste steg får du se hvordan appen ser ut, selv om den ikke er ferdig.

# Steg 6: Teste appen mens du programmerer {.activity}

Det kan være veldig nyttig å teste appen din mens du lager den, for å sjekke at alt fungerer som det skal. I App Inventor kan du teste appen din på to forskjellige måter. Den ene måten å teste appen din på er ved å koble telefonen din til App Inventor. Dette krever at operativsystemtet på mobiltelefonen din er Android. Den andre måten å teste appen din på er ved å laste ned en Android-emulator og laste inn appen din der. Begge disse to metodene er beskrevet under. Dersom du har en Android-telefon, så er det den letteste måten å teste på. **Det er ikke nødvendig å teste både på telefonen og i en emulator, velg en av delene.**

## Problemer {.tip}

Legg merke til at når du tester appen din live, så vil ikke alltid alt fungere optimalt. Eksempler på ting som ikke
alltid fungerer som det skal er berøring, tid og lyd. Det første som kan være lurt å gjøre er å opprette en ny kobling
mellom telefonen og MIT App Inventor. Dette kan du gjøre ved å trykke **Connect**, også **Reset Connection**,
før du så oppretter koblingen på nytt slik som du pleier. Dersom du mener at du har programmert appen slik som den skal
være, men at den fremdeles ikke fungerer som den skal, så kan det være lurt å bygge appen som en .apt-fil.
Da kan du teste appen på telefonen din som et fullverdig program istedetfor. Dette er beskrevet lengre nede.

## Steg 6.1: Teste appen på mobiltelefonen

For å kunne teste appen din på en telefon mens du programmerer så trenger du tre ting:

## Sjekkliste {.check}

+ En datamaskin til å bygge appen.
+ En Android-telefon.
+ Tilgang til WIFI.

For å kunne teste appen må du gjøre følgende:

## Sjekkliste {.check}

+ Last ned *MIT AI2 Companion App* til telefonen din. Den finner du på Google Play.
+ Koble telefonen din og datamaskinen din til det samme WIFI-nettverket.
+ Når du er i App Inventor er det en meny helt øverst, hvor det blant annet er mulig å trykke på **Connect**.
  Trykk på **Connect**, og velg **AI Companion**.
+ I ruten som dukker opp på skjermen så står det to ting; en QR-kode og en bokstav-kode. Åpne MIT AI2 Companion App
  på telefonen din. Der kan du velge om du vil scanne QR-koden eller skrive inn bokstav-koden manuelt. Begge deler fungerer
  helt fint, så du kan velge hva du ønsker å gjøre.

Nå kan du teste appen på telefonen din.

## Problemer {.tip}

[Dersom du har problemer, så kan du sjekke ut en mer detaljert veiledning på engelsk her](http://appinventor.mit.edu/explore/ai2/setup-device-wifi.html).

## Steg 6.2: Teste appen på en emulator

For å kunne teste appen din på en emulator mens du programmerer så trenger du en datamaskin med tilgang til Internett. Første steg er å installere *App Inventor Setup Software*, hvor det finnes en guide for hvert av operativsystemene her:

## Sjekkliste {.check}

+ [Windows](http://appinventor.mit.edu/explore/ai2/windows.html).
+ [Mac OS X](http://appinventor.mit.edu/explore/ai2/mac.html).
+ [GNU/Linux](http://appinventor.mit.edu/explore/ai2/linux.html).

Når "App Inventor Setup Software" er installert gjør du følgende:

## Sjekkliste {.check}

+ Åpne "aiStarter", det er viktig at dette kjører i bakgrunnen. Dette vil skje automatisk på Mac ved installasjon,
  og i noen tilfeller på Windows også. Dersom du har Linux må du skrive inn følgende i kommandolinjen.

  ```sh
  /usr/google/appinventor/commands-for-appinventor/aiStarter &
  ```
+ Når du er i MIT App Inventor er det en meny helt øverst, hvor det blant annet er mulig å trykke på "Connect".
  Trykk på "Connect", og velg "Emulator". Da vil du se at "aiStarter" begynner å arbeide. Dette kan ta en stund.
+ Etterhvert vil emulatoren bli klar, ved å først vise en svart skjerm. Så vil en mobil-bakgrunn dukke opp, før du
  til slutt får opp appen du har laget.

Nå kan du teste appen på emulatoren din.

## Problemer {.tip}

[Dersom du har problemer, så kan du sjekke ut en mer detaljert veiledning på engelsk her](http://appinventor.mit.edu/explore/ai2/setup-emulator.html).

# Steg 7: Fullføre test-appen {.activity}

Nå ser du at du har en knapp på skjermen din som du kan trykke på. Det vil ikkje skje noe når du trykker på den, rett og slett fordi du ikke har skrevet noe kode for det enda. Det kommer du snart til, men aller først må du teste litt hva som skjer når du legger til ting samtidig som du er koblet til appen.

## Test prosjektet {.flag}

+ Dersom du trykker på "Screen1" under "Components", da kan du skifte "BackgroundColor" under "Properties".
  Hva skjer med appen din på telefonen eller i emulatoren din da?
+ Hva skjer om du skifter "Title"?
+ Hva skjer om du endrer på "AlignHorizontal"?
+ Hva skjer om du endrer "AlignVertical"?

Nå er du klar for å programmere komponentene i appen vår. Det kan du gjøre på følgende måte:

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

[Dersom du ønsker en mer detaljert veiledning for å laste ned og dele appen din så kan du klikke her](http://appinventor.mit.edu/explore/ai2/share.html).

# Steg 9: Lære mer {.activity}

For å lære mer om App Inventor så kan det være lurt å sjekke ut følgende lenker:

## Sjekkliste {.check}

+ [App Inventor på Youtube](https://www.youtube.com/results?search_query=app+inventor).

+ [Veiledninger for å lage apps](http://appinventor.mit.edu/explore/ai2/tutorials.html).

+ [Sjekke ut hvordan alle blokkene fungerer](http://appinventor.mit.edu/explore/ai2/support/blocks.html).

+ [Sjekke ut App Inventor sitt bibliotek](http://appinventor.mit.edu/explore/library.html).
