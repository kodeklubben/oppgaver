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

![](sirkel2.png "Tre hvite sirkler på svart bakgrunn: en stor øverst
til venstre, en middels stor midt i vinduet og en liten nederst til
høyre")

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

![](sirkel3.png "Tre hvite sirkler på svart bakgrunn med piler som
 viser X- og Y-aksen.")

I bildet ovenfor, vises også området utenfor bilderammen hvor resten
av de to siste sirklene tegnes opp. I tillegg viser to piler hvordan
de to første tallene i kallene på `ellipse` brukes. Det første tallet
angir posisjon langs X-aksen, vist med pilen merket X. Det andre
tallet angir posisjon lans Y-aksen, vist med pilen merket Y. Der disse
to pilene krysser hverandre har de verdien `0`, og de strekker seg til
kanten av vinduet med verdiene `640` for X og `480` for Y, som ble
bestemt av kallet på `size`. Man kan også tegne opp ting utenfor
bildet med negative tall eller tall som er større enn de brukt i
kallet på `size`.

# Steg 3: Variabler {.activity}

Til nå har vi brukt faste tall overalt. Dette fungerer ikke alltid så
bra. Hvis vi endrer størrelsen på vinduet, vil ikke sirkelen i midten
være i midten lenger og sirkelen i nederste høyre hjørne vil heller
ikke være riktig plassert. Hvis vi vil at sirklene skal bevege på seg,
kan vi heller ikke bruke faste verdier.

Dette løser vi ved hjelp av noe som heter variabler. En variabel kan
du tenke på som en navngitt verdi. Vi kan også endre på verdien som er
knyttet til navnet, og det er derfor det heter variabler: verdien kan
variere.

## Sjekkliste {.check}

+ For å løse det første problemet skal vi nå første endre størrelsen
  på vinduet i `setup`:

    ```processing
    void setup() {
      size(800, 600);
    }
    ```

  Legg merke til at sirkelen som var i midten og sirkelen i nederste
  høyre hjørnet, nå er litt til venstre og litt lenger opp
  enn midten og hjørnet:

![](variabler1.png "De tre hvite sirklene er nå vist på en svart
 bilderamme som er større enn før.")

+ Vi skal nå ta i bruk to variabler som heter `width` og `height`,
  altså bredde og høyde på engelsk. Disse får sin verdi når `size` kalles.
  Endre `draw` som følger:

    ```processing
    void draw() {
      background(0);
      ellipse(width / 2, height / 2, 100, 100);
      ellipse(0, 0, 200, 200);
      ellipse(width, height, 50, 50);
    }
    ```

  Her har vi også brukt et regnestykke for å tegne opp den første sirkelen.
  Skråstreken, `/`,  betyr delt på, så `width / 2` gir altså halvparten
  av bredden. `height / 2` gir jo da halvparten av høyden. Vi kunne også
  brukt `width * 0.5` for å oppnå det samme, men det blir da bredden ganget
  med en halv. Noen ganger er det enklere med deling og andre ganger ganging,
  men det kommer an på hvor vi vil plassere ting.

+ Lagre og kjør programmet, om du ikke har gjort det allerede.

+ Nå skal vi lage våre egne variabler. Dette kan vi bruke for å få formene
  til å bevege på seg:

    ```processing
    float x;
    float y;
    
    void setup() {
      size(800, 600);
      x = width / 2;
      y = height / 2;
    }
    ```

  De to linjene som ble lagt til før `setup`, sier at vi skal ha to variabler,
  `x` og `y`, og at disse er av typen `float`. `float` er en type som brukes
  til desimaltall. Inne i `setup` har vi gitt disse variablene verdier,
  som kommer fra det samme regnestykket som vi brukte i forrige punkt.

+ Det er ikke nok å bare ha variabler. Vi må bruke dem også, så vi
  endrer igjen på `draw`:

    ```processing
    void draw() {
      x = x + 1;

      background(0);
      ellipse(x, y, 100, 100);
      ellipse(0, 0, 200, 200);
      ellipse(width, height, 50, 50);
    }
    ```

  Den første sirkelen bruker nå variablene til posisjonen. I tillegg
  la vi til en ny linje som sier at `x` skal settes til én høyere enn
  den gamle verdien. Hva tror du vil skje nå som `x` blir større hver
  gang bildet tegnes opp?

+ Lagre og kjør programmet, om du ikke har gjort det allerede.

### Lagre som {.protip}

Hvis du ikke vil miste de forskjellige stegene som er gjort på veien,
kan du bruke *Save as* (*Lagre som*) istedenfor *Save* (*Lagre*). Du
finner dette under **File -> Save as** ved å trykke **Shift + Ctrl +
S**. Da kan du lagre programmet med et annet navn, og beholde to
forskjellige varianter.

## Utforsking {.try}

Prøv å utforske hvordan du kan endre `x` og `y` for hver gang `draw` kjøres.

+ Kan du få sirkelen til å bevege seg mot venstre istedenfor høyre?
+ Klarer du å få den til å bevege seg opp eller ned istedenfor til en
  av sidene?
+ Hva med å å få den til å bevege seg på skrå?

# Steg 4: Sprette i veggen {.activity}

Det er litt kjedelig når sirkelen forsvinner ut av vinduet hele
tiden. Så nå skal vi lære å få sirkelen til å snu når den treffer
kanten av vinduet, som en ball som spretter tilbake hvis den kastes i
veggen.

## Sjekkliste {.check}

+ Vi trenger et par nye variabler for å styre retningen til
  sirkelen. Legg til følgende før `setup`:

    ```processing
    float xFart = 1.5;
    float yFart = 2;
    ```

  Disse skal vi bruke til å styre farten til sirkelen, som også
  bestemmer retningen. Her kan du også se hvordan desimaltall ser ut i
  Processing: vi bruker punktum istedenfor komma fordi det er det som
  brukes i engelsk. Du har kanskje lagt merke til at vi nå gir
  variablene verdier med en gang, mens vi tidligere ga dem verdier i
  `setup`. Grunnen til dette er at `width` og `height` kan ikke brukes
  før `size` er kjørt, så vi kunne ikke sette `x` og `y` med en gang.

+ Nå skal vi legge til en større bit med kode i `draw` for å få ballen
  til å snu. Merk at vi endrer også setningen hvor vi øker `x` og
  fjerner de to sirklene i hjørnene:

    ```processing
    void draw() {
      x = x + xFart;
      y = y + yFart;
      
      if (x < 50 || x > width - 50) {
        xFart = -xFart;
      }
        
      if (y < 50 || y > height - 50) {
        yFart = -yFart;
      }

      background(0);
      ellipse(x, y, 100, 100);
    }
    ```
    
+ Lagre og kjør programmet.

### Forklaring {.protip}

I `draw` ser vi en del nytt som du ikke har sett før. `if`, *hvis* på
engelsk, lar oss utføre en kodesnutt bare i spesielle tilfeller. Det
som bestemmer om koden skal utføres eller ikke kommer rett bak `if` i
parenteser. I den første`if`-setningen er det `x < 50 || x > width -
50`. Dette er egentlig to tilfeller satt sammen, `x < 50` og `x >
width - 50`, og de er slått sammen med `||` som betyr *eller*. `x <
50` betyr *er x mindre enn 50* og `x > width - 50` betyr *er x større
enn bredden minus 50*. `50` er halvparten av bredden til sirkelen, og
siden `x` er midt i sirkelen, betyr dette er venstre eller høyre side
av sirkelen utenfor sirkelen. Hvis det er det, så skal vi utføre koden
`xFart = -xFart;` Denne setningen gjør at retningen langs X-aksen,
altså venstre og høyre, blir snudd. Hvis `xFart` er positiv, blir den
negativ og motsatt. Så gjør vi akkurat det samme for farten i Y-aksen,
altså opp og ned.

# Steg 5: Andre former {.activity}

Denne leksjonen heter ikke *Sirkler*, men *Former*. Så da må vi nesten
lære hvordan vi kan tegne opp andre former enn sirkler. Derfor skal vi
nå se på hvordan man kan tegne firkanter og trekanter.

## Firkanter {.check}

+ La oss først se på enkle firkanter, vi bytter ut `ellipse` med `rect`:

    ```processing
    void draw() {
      x = x + xFart;
      y = y + yFart;
      
      if (x < 50 || x > width - 50) {
        xFart = -xFart;
      }
        
      if (y < 50 || y > height - 50) {
        yFart = -yFart;
      }

      background(0);
      rect(x, y, 100, 100);
    }
    ```

+ Lagre programmet, her kan det være fint å bruke *Save as* (*Lagre
  som*) med **Shift + Ctrl + S** og gi programmet et nytt navn. Kjør
  programmet. Legg merke til at firkanten beveger seg litt utenfor
  vinduet nederst og til høyre, og ikke helt til kanten øverst og til
  venstre. Dette er fordi firkanter tegnes fra øverste venstre hjørne,
  mens ellipser tegnes fra midten.

+ Vi har nå to valg for hvordan vi kan fikse dette problemet. Vi kan
  endre hvordan vi sjekker om firkanten har truffet kanten, eller vi
  kan endre hvordan vi tegner opp firkanter. Den første løsningen
  gjøres ved å endre `setup` slik:

    ```processing
    void setup() {
      size(800, 600);
      x = width / 2;
      y = height / 2;
      rectMode(CENTER);
    }
    ```

  Hvis man skal løse det på den andre måten, gjør man det ved å endre
  de to `if`-setningene i `draw`:

    ```processing
    void draw() {
      x = x + xFart;
      y = y + yFart;
      
      if (x < 0 || x > width - 100) {
        xFart = -xFart;
      }
        
      if (y < 0 || y > height - 100) {
        yFart = -yFart;
      }

      background(0);
      rect(x, y, 100, 100);
    }
    ```

  Du må ikke bruke begge løsningene samtidig. Da vil ikke firkanten nå
  frem til kantene nederst og til høyre, og heller gå litt utenfor
  vinduet øverst og til venstre.

+ Lagre programmet før vi prøver å lage trekanter.

## Enkle trekanter {.check}

+ Når vi skal lage en trekant, må vi si hvor alle hjørnene i trekanten
  skal være. Dette gir oss mer frihet. Vi kan for eksempel flytte
  hvert hjørne for seg ved å bruke flere variabler, fire for hvert
  hjørne: to til posisjon og to til hastighet. Vi ser først hvordan vi
  kan få en enkel trekant til å sprette rundt som firkanten og
  sirkelen tidligere, så skal vi lage en hvor hvert hjørne beveger seg
  for seg selv:

    ```processing
    void draw() {
      x = x + xFart;
      y = y + yFart;
      
      if (x < 50 || x > width - 50) {
        xFart = -xFart;
      }
        
      if (y < 50 || y > height - 50) {
        yFart = -yFart;
      }

      background(0);
      triangle(x, y - 50, x + 50, y + 50, x - 50, y + 50);
    }
    ```

  Hvis du endret `if`-setningene i punktet ovenfor om firkanten, så er
  dette nå endret tilbake. Her er det også viktig å holde rede på
  pluss og minus for hvert av de tre punktene i trekanten i kallet på
  `triangle`.

+ Lagre programmet igjen, gjerne med nytt navn ved hjelp av *Save as*.

### Forklaring av triangle {.protip}

`triangle` tar seks argumenter. Disse kommer i par, slik at de to
første hører sammen og bestemmer posisjonen til det første av de tre
hjørnene. De neste to bestemmer posisjonen til det andre hjørnet og de
to siste det tredje. Hvis vi sier at `x` og `y` er midten av
trekanten, da har vi det første hjørnet `50` piksler over midten (`y -
50`), og de to neste hjørnene er `50` piksler under (`y + 50`) midten
og `50` piksler til høyre (`x + 50`) og venstre (`x - 50`) for midten.

## Trekanter {.check}

+ Nå skal vi se hvordan vi kan lage trekanter hvor hvert hjørne
  beveger seg for seg selv. Da trenger vi fire variabler for hvert
  hjørne, to for posisjon og to for farten, og dette for tre hjørner
  som blir tolv variabler. Vi kunne kalt dem f.eks. `x1`, `x2`, `x3`
  og tilsvarende for `y` og farten, men vi skal isteden bruke noe som
  kalles *array*. Det er vanlig å bruke det engelske ordet også på
  norsk, men det oversettes noen ganger til vektor, rekke, tabell
  eller matrise, men de kan lett forveksles med andre typer enn
  *arrays*. Vi begynner med å endre variablene.

    ```processing
    float[] x = new float[3];
    float[] y = new float[3];
    float[] xFart = new float[3];
    float[] yFart = new float[3];
    ```

  Nå har vi endret typen av variablene fra `float` til `float[]`. Når
  vi putter firkantklammer etter en type, er det en *array* med
  verdier av typen foran klammene. Bak likhetstegnet ser vi også noe
  nytt `new float[3]` betyr at vi skal lage en ny `float`-*array* med
  tre tall i.

+ Nå må vi endre startverdiene til disse tallene, ellers vil de bare
  være `0` alle sammen:

    ```processing
    void setup() {
      size(800, 600);
      
      x[0] = width / 2;
      x[1] = width / 2;
      x[2] = width / 2;
      
      y[0] = height / 2;
      y[1] = height / 2;
      y[2] = height / 2;
      
      xFart[0] = 1.5;
      xFart[1] = 2.5;
      xFart[2] = 3.5;
      
      yFart[0] = -5;
      yFart[1] = 2.5;
      yFart[2] = -1.5;
    }
    ```

  Her ser vi hvordan vi jobber med verdiene i en *array*. Vi bruker
  firkantklammer med et tall i for å si hvilken verdi vi skal jobbe
  med. Den første verdien finnes på plass `0`, og den siste verdien er
  på plass `2` som er én lavere enn størrelsen. Tallet for
  plasseringen kalles *indeks*. Indeksen er alltid én lavere enn om vi
  skulle telle vanlig fordi vi begynner på `0`. Derfor er den siste
  indeksen én lavere enn størrelsen.

+ Og til slutt må vi flytte rundt på hjørnene og tegne opp trekanten
  vår:

    ```processing
    void draw() {
      for (int i = 0; i < x.length; i++) {
        x[i] = x[i] + xFart[i];
        y[i] = y[i] + yFart[i];
        
        if (x[i] < 0 || x[i] > width) {
          xFart[i] = -xFart[i];
        }
        
        if (y[i] < 0 || y[i] > width) {
          yFart[i] = -yFart[i];
        }
      }

      background(0);
      triangle(x[0], y[0], x[1], y[1], x[2], y[2]);
    }
    ```

  Dette er en ganske stor endring med mye nytt. Vi skal derfor se litt
  nærmere på hver av de nye tingene i forklaringen nedenfor, men først
  kan du lagre og kjøre programmet.

### Forklaring {.protip}

I begynnelsen av `draw` har vi nå lagt inn noe som kalles en løkke,
*loop* på engelsk. En løkke er en del med kode som utføres flere
ganger. Det finnes andre slags løkker, og denne kalles en
*for-løkke*. Inne i parentesene etter `for` har vi tre setninger. Den
første, `int i = 0`, blir utført før løkken. Den neste, `i <
x.length`, bestemmer om koden i løkken skal utføres eller om løkken er
ferdig. Den siste, `i++`, utføres etter koden mellom krøllparentesene,
altså innholdet i løkken. `i` bruker vi inne i løkken som indeks når
vi jobber med arrayene istedenfor å skrive faste tall.

Så om vi går gjennom koden steg for steg, ser vi at først lages en
variabel `i` av typen `int` som starter med verdien `0`. `int` er
typen som brukes for tall uten desimaler, altså *heltall* eller
*integer* på engelsk. Så sjekker vi om `i` er mindre enn størrelsen
til arrayen `x`. Hvis den er det, og det er den, for størrelsen til
`x` er `3` og `i` er bare `0`, kjøres koden mellom
krøllparentesene. Når all koden mellom krøllparentesene er kjørt, så
kjøres `i++` som også er nytt for oss. `i++` gjør det samme som `i =
i + 1`, altså det øker `i` med `1`. Nå sjekker vi igjen om `i` er
mindre enn størrelsen til `x`. Og sånn fortsetter det helt til `i`
blir like stor eller større enn størrelsen til `x`.

Løkker som ser slik ut, med et heltall som økes med én og sjekkes mot
størrelsen på en array, er veldig vanlig og brukes til å jobbe med
arrayer. Du kommer til å se mange slike i fremtidige oppgaver. Løkker
kan kreve litt øving før man blir god på det, men etter hvert blir man
veldig glad for at man slipper å skrive den samme koden mange ganger.

### Utfordringer {.try}

+ Det går også an å lage firkanter hvor man plasserer hvert hjørne for
  seg. Da bruker man funksjonen `quad` istedenfor `rect`. For å tegne
  en firkant trenger man ett hjørne mer enn i en trekant. Prøv å endre
  programmet til å lage en firkant med hjørner som spretter rundt på
  skjermen.

+ Man kan lage mangekanter også, men da må vi bruke flere
  funksjoner. Først må vi begynne med `beginShape();`, så må vi angi
  hvert hjørne med `vertex(x, y);` og til slutt avslutte med
  `endShape();`. Endre programmet til å tegne en femkant med hjørner
  som spretter rundt på skjermen. Husk å bytte ut `x` og `y` i kallet
  på `vertex` med riktige X- og Y-verdier fra arrayene.

+ Hvis du bruker en løkke til å løpe gjennom alle hjørnene, og kaller
  `vertex` som innholdet i løkka, er det lett å lage former med enda
  flere kanter. Prøv å lage en sekskant, syvkant eller åttekant.
