---
title: Tetris
level: 1
author: Kine Gjerstad Eide
language: nb
---

# Introduksjon {.intro}

Lag starten på ditt eget tetris spill! 

Det du skal gjøre i denne oppgava er først å sette opp bakgrunnen til spillet og så rett og slett å få firkanter til å falle over skjermen. 

Slik vil det se ut når du er ferdig med oppgava:

![](preview.PNG)

For hvert steg kommer det en forklaring og litt eksempler, på slutten av hvert steg kommer et bilde av hele koden som er forklart, bruk bilde dersom du trenger det, men forsøk å skriv koden på egenhånd først.

# Steg 1: Lag dine første to metoder {.activity}

La oss starte med å sette opp et vanlig vindu, dersom du ikke har åpna Processing, så må du gjøre det nå. 

Lagre programmet ditt, dette gjør du ved å velge `File` og deretter `Save As`, det anbefales at du gir koden din et navn som har noe med spillet å gjøre, slik at det er lett å finne igjen. Det er også lurt å lagre koden på et sted som er lett å huske. 

Processing er en kode editor, det betyr at du kan skrive kode i den. Den første koden du skal skrive er en kodesnutt som setter opp to metoder. Alt som skrives i den første metoden skjer en gang, mens det som står i den andre metoden skjer på nytt og på nytt helt til programmet avsluttes. Navnet på de to metodene er `setup` og `draw`, nå viser vi hvordan vi skriver setup metoden og så kan du forsøke å skive draw metoden selv. De to metodene skal være helt like bortsett fra navnet:

```processing
void setup(){

}
```

Nå må du kjøre koden for å sjekke at metodene fungerer. For å kjøre koden trykker du på `play` knappen opp til venstre i Proccesing programmet. Dersom all koden din er riktig skal du få opp et lite vindu som ser slik ut:

![](steg0vin.PNG)

Her er hele koden slik den skal se ut nå, dobbelsjekk at du har skrevet alt riktig før du går videre:

![](steg0.png)


# Steg 2: Bestem størrelsen på vinduet og sett en egen bakgrunsfarge {.activity}

Nå skal du bestemme størrelsen på vinduet, det gjør du ved å bruke en metode som noen allerede har skrevet ferdig. Når vi bruker en metode, så skriver vi navnet på metoden, deretter må vi ha parenteser, og til sist legger vi til semikolon. Når man bruker en metode som allerede er ferdigskrevet, så sier man at man `kaller på en metode`.

### Forklaring av parametre {.protip}

Inni parentesene må man ofte sette inn informasjon, dette kalles parametere eller argumenter. Parameterne som må oppgis når man setter størrelsen på et vindu er rett og slett hvor stor man vil ha vinduet. 

Når man kaller på en metode er det ikke alltid man vet nøyatktig hvilke parametre som skal legges ved. Da kan man enten søke etter svaret på internett, eller man kan gjøre et metodekall uten parametre. Gjør du sistnevnte, vil du få opp en feilmelding neders på skjermen. Feilmeldingen forteller hvor mange og hvilken type parametre som skal skrives i parentesene. Hvert parameter skilles av kommategn.  
#

Parametrene til metodekallet som bestemmer størrelsen på vinduet er oppgitt i piksler, så det kommer litt ann på skjermen din hvor mange piksler du ønsker at vinduet skal være. Prøv for eksempel med 600 og 900, og så kan du endre ett og ett tall helt til du får et vindu som du synes har riktig størrelse. 

Slik kaller du på metoden som bestemmer størrelsen på vinduet:

```processing
    size(600, 900);
``` 

Denne kodelinja må skrives inni setup metoden din, det betyr mellom de to krøllparentesene som står etter parentesene til setup. Krøllparentesene er `{` og `}`. 



## Prøv selv {.check}
- [ ] Lag et vindu som er kvadratisk.
- [ ] Lag et vindu som når helt fra høyre til venstre side av skjermen din.
- [ ] Lag et vindu som er ca. like stort som et russekort.
- [ ] Lag et vindu som du synes er passelig for å spille tetris i.

### Forklaring av `background` {.protip}

På samme måte som `size` så er det også en ferdigskrevet metode som gjør at man kan bestemme hvilken bakgrunnsfarge man ønsker. Denne heter `background` og trenger enten ett eller tre parametre for å fungere. Alle parameterne må være heltall, eller `int` som det heter når man programerer. I tillegg må de være mellom 0 og 255. 

Dersom man bare har ett parameter, så får man hvit farge ved å skrive 255, svart ved å skrive 0 og grå i forskjellige nyanser ved å variere mellom 0 og 255. Tallene bestemmer hvor sterk lyspærene inni pc-skjermen skal lyse. 

Det brukes RGB farger, altså rød, grønn, blå. Det betyr at det første tallet bestemmer styrken på det røde lyset, det andre på det grønne det siste på det blå, så kan man blande farger og variere lysstyrken slik at man får akkurat den fargen man ønsker. 
#

Her er de to måtene å kalle på metoden som setter bakgrunnsfargen:

```processing
    background(20, 255, 170);`
```
og
```processing
    background(70);`
```

Husk å avslutt metodekallet med semikolon. Dette metodekallet skal også inn i setup metoden din. 

## Prøv selv {.check}
- [ ] Test med å først bare ha ett tall inni parentesen og endre på tallet, hva får du? Endre tallet minst 4 ganger og sjekk hvilken farge du får.
- [ ] Få bakgrunnsfargen til å bli svart. 
- [ ] Få bakgrunnsfargen til å bli helt lysegrå.
- [ ] Få bakgrunnsfargen til å bli hvit.
- [ ] Prøv å sett inn tre forskjellige tall, og så endrer du på ett og ett av disse, hva skjer?
- [ ] Hvilken farge får du dersom alle parametrene til `background` er 0?
- [ ] Få bakgrunnsfargen til å bli rød.
- [ ] Få bakgrunnsfargen til å bli gul.
- [ ] Prøv tilfeldige tall og se hvilken farge du får.
- [ ] Finn en bakgrunnsfarge du liker og gå videre.

Her er et bilde av hvordan koden din skal se ut nå, (husk at du sikkert har funnet litt andre tall enn vi har som parameter i metodekallene inni setup).

![](steg2.png) 

# Steg 3: Lag en firkant {.activity}

Nå skal du lage firkanten som senere skal falle over skjermen. For å lage en firkant bruker vi metodekallet `rect`. Dette trenger fire parameter, som bestemmer hvor firkanten skal plasseres og hvor stor den skal være. Metodekallet på `rect` skal du skrive inni draw metoden. 

Start for eksempel med disse tallene:

```processing 
    rect(275, 10, 50, 50);
```

## Prøv selv {.check}

- [ ] Finn ut hva de forskjellige tallene står for ved å endre ett og ett av de.
- [ ] Få firkanten til å nå fra toppen av vinduet til bunnen av vinduet ditt.
- [ ] Tegn firkanten slik at den står midt i vinduet.
- [ ] La firkanten dekke hele vinduet ditt (du kan bruke minus forran tallene).

Sett en farge på firkanten ved å gjøre et metodekall på `fill`, denne tar tre parameter. slik som background, men den fargelegger figurer i stede for hele bakgrunnen. Denne må skrives inni `draw` og den må stå på linja over firkanten.

## Prøv selv {.check}
- [ ] Førsøk å gjøre firkanten lilla.
- [ ] La firkanten få en fage du liker.

Her er vår kode så langt, husk at du sikkert har valgt andre parametre.

![](Steg3.png)

# Steg 4: Lag en variabel {.activity}

For å få firkanten til å falle må vi gjøre to ting. Vi må opprette en variabel som endrer seg og så må vi bruke variabelen i firkanten.

### Forklaring av variabel {.protip}

En variabel er noe som kan endre seg. Vi vil jo gjerne at firkanten skal bevege seg nedover skjermen, altså at firkanten skal endre posisjonen. Dette gjør vi ved å putte inn en variabel i stede for tallet som bestemmer posisjonen til firkanten. 

I den virkelige verden finnes det også variabler som man må endre og så har vi andre tall som alltid er de samme. For eksempel i en håndballkamp har man mange tall. Alle spillerne har sitt eget nummer på drakta. Ingen av spillerne skal bytte nummer under kampen, så derfor er nummeret trykka rett på skjorta. Det er også tall som viser hva stillingen i kampen er. Dette er ofte vist på ei svær tavle. Her endres tallene. Det hadde ikke funka å trykka stillingen på ei skjorte før kampen. Derfor har de laga tavler, slik at stillingen kan oppdateres etterhvert som lagene får poeng. På samme måte, så lager vi variabler i programmering, slik at vi kan oppdatere de etterhvert som noe skjer i programmet. Alle variabler har sitt eget navn, slik som "poeng", "liv", "fart" eller lignende. Når de skal oppdateres, skriver vi for eksempel: `liv = 2`. 

For å lage en variabel, så må vi først sette av plass i minnet til pcen, slik at den tar vare på et tall. Da trenger ikke pcen å vite hva tallet er, men den har satt av plassen slik at det er ledig når vi begynner å bruke det. 

Når vi skal lage en variabel i Processing, så må vi si hvilken datatype variabelen skal inneholde. Eksempler på datatyper kan være `int` for heltall, `float` for desimaltall, eller `String` for tekst. 
#

Vi starter med å sette av plass i minnet, det heter å deklarere, eller opprette variabelen. Typen skal være `int`. Vi må gi et navn til variabelen, vi har valgt `posisjonY`, men du kan velge hvilket navn du ønsker. Hele kodelinja ser slik ut og skal stå over `setup` metoden:

```processing
    int posisjonY;
```

Så skal vi bestemme hva `posisjonY` skal være når vi starter programmet, det skriver vi inni `setup` metoden. Kodelinja skal se slik ut (husk at dersom du må bruke samme navn som på forrige kodelinje):

```processing
    posisjonY = 20;
```

Så putter vi variabelen inn i firkanten vår. Det er argument nummer to som må byttes ut, og kodelinja hvor vi skriver firkanten ser slik ut:

```processing
    rect(275, posisjonY, 50, 50);
```

Kjør koden og sjekk at dette fungerer før du tester ut oppgavene under.

## Prøv selv {.check}
- [ ] Bytt ut `20` med for eksempen `200` i `setup` metoden der du skriver hva `posisjonY` skal være, hva skjer?
- [ ] Sett `posisjonY` til å være noe som får firkanten til å bli plassert helt på bunn av vinduet.
- [ ] Plasser firkanten så langt opp at du bare ser bunnen av firkanten, du kan bruke negative tall.

Her er koden så langt.

![](steg4.png)

# Steg 5: Beveg firkanten {.activity}

Nå må vi få firkanten til å bevege seg. Som vi skrev helt til å begynne med, så fungerer `draw` metoden slik at den repeteres, all koden inni `draw` bli lest gjennom fra toppen og til bunn og når programmet er kommet til bunn av `draw`, da bare hopper det opp til starten og leser gjennom koden en gang til. Dette skjer helt til vi avslutter programmet. 

For å få firkanten til å endre seg, så må vi oppdatere `posisjonY`, det gjør vi ved å skrive dette inni `draw metoden`:

```processing
    posisjonY = posisjonY + 1;
```

For hver gang programmet leser denne linja, så endrer den pososjon til å bli det samme som det den allerede er pluss en. Det betyr at dersom posisjonen er 20, så vil den bli til 20 + 1 neste gang, og så 21 + 1 gangen etter og slik fortsetter det. Når man bruker ett `=` tegn i koding, så betyr det at man gir noe en verdi, ikke at tallene på begge sider av `=` tenget er det samme.

Kjør programmet og sjekk at firkanten faller.

## Prøv selv {.check}
- [ ] Hva skjer om du setter `+ 10` i stede for `+ 1` når du endrer posisjonY?
- [ ] Gjør endringen i posisjonY til å være større en høyden på firkanten.
- [ ] Hvorfor tror du det blir tegna en stripe over skjermen?
- [ ] Finn en fart firkanten kan falle i som du synes er passelig.

Her er hele koden så langt:

![](steg5.png)

# Steg 6: Fjern stripa som firkanten lager {.activity}

Grunnen til at det blir tegna en stripe over skjermen er fordi bakgrunnsfargen i vinduet bare blir tegna en gang i `setup` metoden. For å få det til å se ut som firkanten faller må metodekallet `background` bli flytta inn i `draw` metoden. Det er vanlig å kalle på `background` helt først i `draw` metoden.

## Prøv selv {.check}
- [ ] Flytt kallet på `background` frem og tilbake fra `draw` til `setup` noen ganger og vær sikker på at du forstår hva som skjer.
- [ ] Kall på `background` øverst i `draw metoden`.

Her er hele koden:

![](steg6.png)
