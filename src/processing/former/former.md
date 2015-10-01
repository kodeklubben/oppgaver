---
title: Former
level: 1
logo: ../../assets/img/ccuk_logo.png
author: Sigmund Hansen
---

# Introduksjon: {.intro}

I denne modulen skal vi lære et programmeringsspråk og verktøy som
heter Processing. Det ble laget for å gjøre programmering lett for
designere og andre som ikke har programmert før, sånn at de kan lage
multimedieprogrammer, spill og liknende. Mange liker Processing fordi
det går fort å lage programmer som vanligvis krever mye arbeid.

# Steg 1: Vindu {.activity}

Nå skal vi begynne helt enkelt med å lage et vindu og fylle det med en
bakgrunnsfarge. Dette vil bli grunnlaget for nesten alle programmer
som du lager med Processing, så det er et fint sted å starte.

## Sjekkliste {.check}

+ Start Processing og skriv dette:

    ```processing
    void setup() {
      size(640, 480);
    }
    
    void draw() {
      background(0);
    }
    ```
+ Kjør programmet ved å trykke på **Ctrl+R**, knappen med en pil
  eller **Sketch --> Run** i menyen.
+ Lagre programmet som Former ved å trykke på **Ctrl+S** eller
  velg **File --> Save** i menyen.

### Hvordan skrive krøllparenteser og liknende {.protip}

TODO: Fikse bredden på celler i tabellen (det trengs marger for å få
litt horisontal luft). Sjekk at pipe skrives med Shift + 7 på Mac.

Her finner du en oversikt over hvordan man skriver en del tegn som
brukes i Processing og ofte i andre programmeringsspråk. Dette
beskriver hvordan det gjøres med vanlig norsk tastatur. Den dekker
også tegn som ikke blir brukt i denne øvelsen, så den kan være fin å
ta med seg videre.

| Tegn | Windows/Linux          | Mac                    |
|:----:| ---------------------- | ---------------------- |
| ;    | Shift + ,              | Shift + ,              |
| "    | Shift + 2              | Shift + 2              |
| \'   | \' (til høyre for Æ)   | \' (til venstre for 1) |
| \|   | \| (til venstre for 1) | Shift + 7              |
| \&   | Shift + 6              | Shift + 6              |
| \[   | Alt Gr + 8             | Alt + 8                |
| \]   | Alt Gr + 9             | Alt + 9                |
| {    | Alt Gr + 7             | Shift + Alt + 8        |
| }    | Alt Gr + 0             | Shift + Alt + 9        |

## Utforsking {.try}

Det anbefales at man utforsker mulighetene selv. Hva skjer hvis du:

+ Bytter ut det første tallet i `size(640, 480);`?
+ Bytter ut det andre tallet?
+ Hva om du bruker et annet tall i `background(0);`?
+ Hva skjer hvis tallet er høyere enn `255`?
+ Hva skjer hvis tallet er lavere enn `0`?
+ Før du går videre kan det være lurt å fjerne endringene som ble gjort i
  denne utforskingen.

## Forklaring av koden {.protip}

Selv om du har utforsket size og background litt, lurer du sikkert på
hva resten av koden gjør eller er godt for. Før vi går videre, skal vi
derfor ta en liten titt på hva all koden gjør.

`void setup() {` sier at vi skal ha en funksjon som heter setup, og
når denne blir kalt, vil all koden som kommer mellom krøllparentesene,
bli kjørt. Du lurer kanskje nå på hva en funksjon er og hva det vil si
å kalle en funksjon. En funksjon er en navngitt del med kode som kan
kjøres når man trenger det, ved å kalle den. `size(640, 480);` er et
eksempel på hvordan man kaller en funksjon. `size` er en funksjon som
er innebygd i Processing. Noen funksjoner gir en verdi som resultat
når de blir utført, men `setup` gjør ikke det. Siden den ikke har en
verdi som resultat, skriver vi `void` foran navnet. Parentesene etter
navnet har ikke noe innhold her, men her kan man bestemme hva slags
verdier som kan sendes til funksjonen når man kaller den. Hvis du ser
på kallet på `size` på linje to, ser du at denne får to tall
inn. `setup` er en spesiell funksjon som blir kjørt når programmet
starter. Krøllparentesen `}` på linje tre sier at funksjonen `setup`
er ferdig.

På linje 5 ser vi enda en funksjon som heter `draw`. Denne er også
spesiell, og blir kjørt om og om igjen så lenge programmet
kjører. Koden inne i denne: `background(0);` setter bakgrunnsfargen i
vinduet. Faktisk fylles hele vinduet med denne fargen. Tallet `0`
betyr at ikke noe lys skal lages, altså blir bakgrunnen svart. Hvit
har verdien `255`. Tallene imellom gir forskjellige gråtoner. Senere
skal vi se på hvordan vi kan gå fra svart-hvitt til farger.

# Steg 2: Sirkel {.activity}

Siden denne oppgaven skal handle om former, er det på tide at vi
kommer i gang med å tegne noen former. La oss begnne med å tegne en
sirkel midt i vinduet.

## Sjekkliste {.check}

+ Endre `draw` til følgende uten å endre `setup`:
    ```processing
    void draw() {
      background(0);
      ellipse(320, 240, 100, 100);
    }
    ```
+ Lagre med **Ctrl+S** og kjør programmet med **Ctrl+R**. Du skal
  da se en hvit sirkel midt i vinduet som i bildet under.

![](sirkel1.png "En hvit sirkel på svart bakgrunn midt i et vindu")

+ Legg til en sirkel til og kjør programmet igjen:
    ```processing
    void draw() {
      background(0);
      ellipse(320, 240, 100, 100);
      ellipse(0, 0, 200, 200);
    }
    ```

+ La oss legge til en siste sirkel og kjøre programmet enda en gang:
    ```processing
    void draw() {
      background(0);
      ellipse(320, 240, 100, 100);
      ellipse(0, 0, 200, 200);
      ellipse(640, 480, 50, 50);
    }
    ```

![](sirkel2.png "Tre hvite sirkler på svart bakgrunn:
en stor øverst til venstre, en middels stor midt i vinduet og en liten nederst til høyre")

## Forklaring av koden {.protip}

Nå har du kanskje knekt koden for hvordan `ellipse` fungerer og hva de
forskjellige tallene gjør. Det første tallet bestemmer hvor langt til
høyre i vinduet sirkelen skal tegnes opp. Det andre tallet bestemmer
hvor langt ned i vinduet den skal tegnes opp. Det tredje tallet
bestemmer hvor bred sirkelen skal være. Det siste tallet bestemmer
hvor høy sirkelen er. Det siste hørtes kanskje rart ut, for en sirkel
er jo like bred som den er høy. Hvis de to siste tallene ikke er like,
får du nemlig ikke en sirkel, men en ellipse som er bredere enn den er
høy eller høyere enn den er bred. Og det er derfor funksjonen heter
`ellipse` og ikke `circle`.

# Steg 3: Variabler