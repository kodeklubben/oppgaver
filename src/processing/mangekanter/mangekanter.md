---
title: Kanter, kanter, mange mangekanter
level: 2
author: Sigmund Hansen
---

# Introduksjon: {.intro}

Her skal vi se på litt mer avansert opptegning og bevegelse. Vi skal
ta utgangspunkt i oppgaven om
[den sprettende ballen](../sprettende_ball/sprettende_ball.html), men
bytte ut ballen med trekanter, firkanter og mangekanter. Det anbefales
derfor at du har gjort den oppgaven før, eller at du har en forståelse
av `if`-setninger og posisjonssystemet fra før. Altså skal du lære å
tegne former med kanter, mange kanter.

# Steg 1: Enkle firkanter {.activity}

Vi begynner med rektangler: de firkantene som det er enklest å tegne
på datamaskinen.

## Sjekkliste {.check}

+ Start Processing og skriv dette:

    ```processing
    float x;
    float y;
    float xFart = 1.5;
    float yFart = 2;
    
    void setup() {
      size(640, 480);
      x = width / 2;
      y = height / 2;
    }
    
    void draw() {
      x += xFart;
      y += yFart;
      
      if (x < 0) {
        xFart = -xFart;
      }
      
      if (x > width - 100) {
        xFart = -xFart;
      }
      
      if (y < 0) {
        yFart = -yFart;
      }
      
      if (y > height - 100) {
        yFart = -yFart;
      }
    
      background(0);
      rect(x, y, 100, 100);
    }
    ```
    
    Dette programmet er ganske likt det som ble lagd i siste oppgave
    om den sprettende ballen, men det er noen små forskjeller:

    + Vi har endret tallene brukt i `if`-setningene. Hvorfor tror du
      dette er gjort? Hva skjer om du også tegner opp en sirkel rett
      etter at du har tegnet opp firkanten?

    + Vi har også tatt i bruk `+=`. `x += 1;` gjør det samme som `x =
    x + 1;` Dette er bare en forkortelse for det siste. Altså øk `x`
    med det som står på høyresiden av `+=`.

+ Kjør programmet ved å trykke på **Ctrl + R** eller knappen
  ![](../play.png "Play - En knapp i verktøylinjen merket med pil)
+ Lagre programmet som Firkant ved å trykke på **Ctrl+S** eller
  velg **File --> Save** i menyen.

## Utfordringer {.try}

+ Kan du lage et rektangel som ikke er kvadratisk, altså hvor bredden
  og høyden er forskjellig? Husk at vi ikke vil at den skal bevege seg
  utenfor vinduet.

# Enkle trekanter {.activity}

Å tegne rektangler var omtrent helt likt som å tegne sirkler, men nå
skal du lære å tegne trekanter. Om en trekant ble tegnet opp med en
posisjon og en bredde og høyde, hadde man ikke hatt så veldig god
kontroll over hvordan trekanten så ut. Derfor må vi si for hvert
hjørne befinner seg.

## Sjekkliste {.check}

+ Vi skal nå bytte ut firkanten med en enkel trekant. Endre `draw` som
  vist under:

    ```processing
    void draw() {
      x += xFart;
      y += yFart;
      
      if (x < 0) {
        xFart = -xFart;
      }
      
      if (x > width - 100) {
        xFart = -xFart;
      }
      
      if (y < 0) {
        yFart = -yFart;
      }
      
      if (y > height - 100) {
        yFart = -yFart;
      }
    
      background(0);
      triangle(x, y, x + 100, y, x + 50, y + 100);
    }
    ```
    
    Her har vi tatt i bruk `triangle` istedenfor `rect`. Denne tar
    imot seks argumenter, to for hvert hjørne i trekanten. `x, y` er
    posisjonen til det første hjørnet øverst til venstre, `x + 100, y`
    er posisjonen til det øverste høyre hjørnet og `x + 50, y + 100`
    er det siste hjørnet nederst i midten.

+ Lagre programmet som *Trekant* ved å velge **File -> Save as** eller
  trykke **Shift + Ctrl + S**.

+ Kjør programmet.

### Forbedre leseligheten {.protip}

Noen ganger kan det være vanskelig å lese kall på funksjoner som tar
mange argumenter. I Processing tar de fleste funksjoner bare imot noen
få argumenter, men `triangle` og et par andre tar seks eller flere. Da
kan det være nyttig å dele opp kallet over flere linjer. For eksempel
kunne setningen ovenfor vært skrevet slik at hvert hjørne var på hver
sin linje:

```processing
triangle(x, y,
  x + 100, y,
  x + 50, y + 100);
```

Hvis man fortsatt synes det er vanskelig å lese eller rotete, kan man
legge til noen ekstra mellomrom for å få ting på linje. Merk at om man
bruker automatisk formatering av koden i Processing, vil den fjerne
mellomrom den mener er overflødig.

## Trekanter {.check}

+ Nå skal vi se hvordan vi kan lage trekanter hvor hvert hjørne
  beveger seg for seg selv. Da trenger vi fire variabler for hvert
  hjørne, to for posisjon og to for farten, og dette for tre hjørner
  som blir tolv variabler. Vi kunne kalt dem f.eks. `x1`, `x2`, `x3`
  og tilsvarende for `y`, `xFart` og `yFart`. Isteden skal vi bruke
  noe som kalles *array*. Det er vanlig å bruke det engelske ordet
  også på norsk, men det oversettes noen ganger til vektor, rekke,
  tabell eller matrise, men de kan lett forveksles med andre typer enn
  *arrays*. Vi begynner med å endre variablene:

    ```processing
    float[] x = new float[3];
    float[] y = new float[3];
    float[] xFart = new float[3];
    float[] yFart = new float[3];
    ```
    
    Nå har vi endret typen av variablene fra `float` til
    `float[]`. Når vi putter firkantklammer etter en type, er det en
    *array* som inneholder verdier av typen foran klammene. Bak
    likhetstegnet ser vi også noe nytt `new float[3]` betyr at vi skal
    lage en ny `float`-*array* med tre tall i.

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
    med. Den første verdien finnes på plass `0`, og den siste verdien
    er på plass `2` som er én lavere enn størrelsen. Tallet for
    plasseringen kalles *indeks*. Indeksen er alltid én lavere enn om
    vi skulle telle vanlig fordi vi begynner på `0`. Derfor er den
    siste indeksen én lavere enn størrelsen.

+ Og til slutt må vi flytte rundt på hjørnene og tegne opp trekanten
  vår:

    ```processing
    void draw() {
      for (int i = 0; i < x.length; i++) {
        x[i] += xFart[i];
        y[i] += yFart[i];
        
        if (x[i] < 0) {
          xFart[i] = -xFart[i];
        }
        
        if (x[i] > width) {
          xFart[i] = -xFart[i];
        }
        
        if (y[i] < 0) {
          yFart[i] = -yFart[i];
        }
        
        if (y[i] > width) {
          yFart[i] = -yFart[i];
        }
      }

      background(0);
      triangle(x[0], y[0], x[1], y[1], x[2], y[2]);
    }
    ```
    
    Her ser du en helt ny konstruksjon som vi skal se nærmere på i
    forklaringen nedenfor, men først kan du lagre og kjøre programmet.

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
  `endShape(CLOSE);`. Endre programmet til å tegne en femkant med
  hjørner som spretter rundt på skjermen. Husk å bytte ut `x` og `y` i
  kallet på `vertex` med riktige X- og Y-verdier fra arrayene.

+ Hvis du bruker en løkke til å løpe gjennom alle hjørnene, og kaller
  `vertex` som innholdet i løkka, er det lett å lage former med enda
  flere kanter. Prøv å lage en sekskant, syvkant eller åttekant.
