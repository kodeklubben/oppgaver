---
title: Farger
level: 1
author: Sigmund Hansen
---

# Introduksjon {.intro}

På skolen lærer vi om farger og hvordan vi kan blande dem for å få
andre farger. Slik er det med farger i datamaskinen også; vi blander
primærfarger og mengden av hver farge bestemmer hvilken farge vi
får. Det er en liten forskjell mellom fargene vi har lært om når vi
tegner og maler og fargene som vises på skjermen. Det skal vi lære om
i denne leksjonen hvor vi skal se nærmere på farger i Processing.

# Steg 1: Mer enn grått {.activity}

Her skal vi raskt se litt på farger. I det første punktet viser vi
hele programmet, og i resten av punktene ser vi kun på `draw` som er
den delen av koden som skal endres. For hvert steg kan du kjøre
programmet med **Ctrl + R**, og hvis du vil, kan du lagre det med
**Ctrl + S**.

## Sjekkliste {.check}

+ Vi begynner med å fylle bakgrunnen med sort:

    ```processing
    void setup() {
      size(800, 600);
    }
    
    void draw() {
      background(0);
    }
    ```

  Dette har du kanskje sett før. Når vi kaller på `background` med
  bare ett tall får vi en gråtone der `0` er sort og `255` er hvitt.

+ La oss endre på `draw` slik at vi får en rød bakgrunn:

    ```processing
    void draw() {
      background(255, 0, 0);
    }
    ```

  Dette likner på det vi hadde i det første steget, men nå bruker vi
  plutselig tre tall istedenfor ett. La oss utforske dem litt.

+ La oss endre på kallet på `background` igjen:

    ```processing
    void draw() {
      background(0, 255, 0);
    }
    ```

  Hvis du kjører programmet, får du nå en grønn bakgrunn istedenfor en
  rød.

+ La oss endre på kallet på `background` enda en gang:

    ```processing
    void draw() {
      background(0, 0, 255);
    }
    ```

  Og nå får du en blå bakgrunn istedenfor en grønn.

## Forklaring av additive farger {.protip}

Som nevnt har du sikkert lært om farger i skolen og blandet farger med
maling, fargeblyanter eller -stifter. Da lærte du nok om primærfargene
rødt, gult og blått, og at du kunne lage omtrent alle slags farger ved
å blande disse sammen. Jo flere farger du blandet, desto mørkere ble
den ferdige fargen. Dette er fordi du tegnet med fargede pigmenter som
absorberer lys. Jo flere farger i lyset som absorberes, desto færre
farger og mindre lys reflekteres og treffer øyet ditt.

I en datamaskin er det annerledes. Du har nok lagt merke til at
skjermen lyser. Derfor angir vi fargen som hvor mye lys vi skal lage
av hver farge. Siden øyet reagerer på rødt, grønt og blått lys, er
disse valgt som primærfargene i skjermer. Det er derfor de tre
verdiene i kallet på `background` ga oss henholdsvis rødt, grønt og
blått. Fordi primærfargene er rød, grønn og blå kalles dette systemet
som regel RGB. Det er også kjent som et *additivt* system, fordi man
legger sammen fargene, mens i tegning på papir jobber man med et
*subtraktivt* system der farger trekkes fra.

Vi kan også blande farger her, men det oppfører seg litt annerledes
fra du kanskje er vant til fra maling. Hvis vi blander rødt og grønt,
får vi gult. Hvis vi blander grønt og blått, får vi en slags turkis,
kalt cyan. Hvis vi blander rødt og blått, får vi en slags rosa, kalt
magenta. Når alle tre fargene er like sterke, får vi en gråtone. Med
alle tre på fullt, `255`, får vi hvitt.

![](RGB.png "Tre overlappende sirkler i rødt, grønt og blått. Der de
 overlapper blandes fargene til gul, cyan, magenta og hvitt.")

Du har sikkert også sett et fargehjul før, der primærfargne plasseres
rundt hjulet. Sekundærfargene, fargene man får når man blander to
primærfarger plasseres da mellom disse. Vi kan også lage et slikt for
RGB.

![](FargehjulRGB.png "RGB-fargehjulet med primær- og sekundærfarger.")

# Steg 2: Fyllfarger og omriss {.activity}

Når vi tegner former, er det en stor sjanse for at vi vil bruke andre
farger enn svart og hvit. Foreløpig har vi bare sett at vi kan styre
fargen på bakgrunnen, så la oss se hva vi kan gjøre med fargene til
formene vi tegner opp.

## Sjekkliste {.check}

+ Legg til en sirkel i `draw`:

    ```processing
    void draw() {
      background(0, 0, 255);
      ellipse(width / 2, height / 2, 100, 100);
    }
    ```

    Hvis du kjører programmet, ser du kanskje noe du ikke har lagt
    merke til før: rundt sirkelen er det en tynn sort strek.

+ Endre fargen som sirkelen fargelegges med, med funksjonen `fill`:

    ```processing
    void draw() {
      background(0, 0, 255);
      fill(255, 192, 64);
      ellipse(width / 2, height / 2, 100, 100);
    }
    ```

    Nå får du en mørkegul sirkel midt i vinduet på en blå bakgrunn.

+ Endre fargen på omrisset med funksjonen `stroke`:

    ```processing
    void draw() {
      background(0, 0, 255);
      fill(255, 192, 64);
      stroke(192, 96, 64);
      ellipse(width / 2, height / 2, 100, 100);
    }
    ```

    Nå er streken rundt sirkelen en rødlig brun. Det er kanskje ikke
    så lett å se fargen på streken siden den er så tynn.

+ Gjør omrisset fetere med funksjonen `strokeWeight`:

    ```processing
    void draw() {
      background(0, 0, 255);
      fill(255, 192, 64);
      stroke(192, 96, 64);
      strokeWeight(3);
      ellipse(width / 2, height / 2, 100, 100);
    }
    ```

    Nå er omrisset tre piksler bredt.

## Eksperimenter {.try}

+ Prøv forskjellige bakgrunnsfarger. Hvordan synes du forskjellige
  bakgrunnsfarger passer sammen med fargene på sirkelen?
+ Prøv forskjellige fyllfarger. Hvordan passer disse med fargen på
  omrisset?
+ Prøv forskjellige farger på omrisset. Hvordan passer det med
  bakgrunnen og fyllfargen?
+ Prøv andre tykkelser på omrisset. Hvor synes du at det er passe
  tykt?
+ Kan du tegne to sirkler på skjermen i forskjellige farger?

# Steg 3: Fargevelgeren {.activity}

Noen ganger kan det være tungvint å skulle lage fargene man har lyst
på ved å bare tenke ut tallene. Man blir riktignok flinkere på dette
etter hvert som man har gjort det en del ganger. Inntil man har blitt
komfortabel med dette, kan det være lurt å bruke fargevelgeren som
finnes i Processing.

## Sjekkliste {.check}

+ Åpne fargevelgeren ved å velge **Tools → Color Selector**

    ![](Fargevelger.png "Fargevelgeren slik den er når den først åpnes.")

    Du får da opp et vindu som lar deg velge farger. Her kan du fylle
    inn tallverdiene som vi har sett tidligere, R, G og B. Det er også
    noen andre felter hvor du kan fylle inn verdier. Det ene er for et
    annet fargesystem enn RGB. Det er også noen områder som har farge.

+ Prøv å trykke i fargefeltet til venstre. Her kan du velge hvor sterk
  og hvor lys fargen skal være.

    Hva skjer med verdiene i de forskjellige tekstfeltene? Kan du se
    hvordan de to tekstfeltene S og B henger sammen hvilken farge du
    velger i dette fargefeltet?

+ Prøv å trykke i fargefeltet rett ved siden av. Her kan du velge
  hvilken farge du vil ha.

    ![](Fargevelger.gif "En animasjon som viser at fargen endres i
     fargevelgeren.")

    Du ser kanskje at øverst til høyre er det et fargefelt til. Her
    vises den fargen du har valgt.

    Hva skjer med verdiene i de forskjellige tekstfeltene nå? Hvordan
    oppfører H, S og B seg sammenliknet med forrige gang?

+ Finn en farge du liker til bakgrunnsfarge. Skriv inn verdiene for R,
  G og B inn i kallet på `background` i `draw`.

+ Finn en farge du liker til sirkelen. Trykk på knappen **Copy**. Visk
  ut alle verdiene gitt i kallet på `fill` og lim inn den kopierte
  fargekoden: enten med **Edit → Paste** eller trykk på **Ctrl + V**
  eller **Cmd + V** hvis du bruker Mac.

    Nå ser du kanskje at verdien som ble kopiert, er den koden som sto
    i det siste tekstfeltet. Disse verdiene er forklart i boksen
    under.

## Web-farger - fargekoder i heksadesimaler {.protip}

Mange som har jobbet med nettsider, er vant til å angi farger på en
litt annen måte. De bruker ofte en sekssifret kode med en firkant
foran: `#00ff00`. Du tenker kanskje: «Kan **f** være et siffer?» Ja, i
heksadesimaler, eller sekstentallssystemet, utvides sifrene med
bokstavene A-F. Da får vi sifre fra 0-F, som er tallene fra null til
femten. Det er ingen forskjell på små og store bokstaver her.

Siden vi skal angi tre farger, består koden egentlig bare av tre
tosifrede tall fra 00 til FF (255). De første to angir rødt, de neste
to grønt og de to siste blått. I programmet under er bakgrunnen lilla,
med rødt satt til `8 · 16 = 128`, grønt til `2 · 16 = 32` og blått til
`15 · 16 + 15 = 255`.

```processing
void setup() {
  size(800, 600);
}
    
void draw() {
  background(#8020FF);
}
```

Disse kodene kan være nyttige å bruke hvis man er kjent med det fra
før. De kan bare brukes direkte, og fungerer ikke så bra om man vil at
fargen skal variere. For eksempel om bakgrunnsfargen ikke endrer seg i
løpet av programmets kjøring, kan de brukes med `background`. Man kan
gi variabler av typen `color` verdier med disse kodene.

# Steg 4: HSB {.activity}

Da vi så på fargevelgeren, så vi tre tekstfelter merket H, S og B. Vi
så også hvordan disse oppførte seg når vi endret fargevalget: H ble
styrt av det høye fargefeltet i fargevelgeren, S ble styrt av hvor
langt vi flyttet oss sidelengs i det store kvadratiske feltet og B ble
styrt av hvordan vi flyttet oss opp og ned i dette feltet.

Dette systemet kalles HSB: Hue, Saturation, Brightness. Som på norsk
er fargetone/kulør, fargemetning og lyshet/valør. Det første tallet,
**H**, bestemmer hva slags farge det blir. Det andre, **S**, bestemmer
hvor sterk fargen skal være. Det siste, **B**, bestemmer hvor lys
fargen skal være.

## Sjekkliste {.check}

+ La oss prøve ut HSB:

    ```processing
    void setup() {
      size(800, 600);
      colorMode(HSB, 360, 100, 100);
    }
    
    void draw() {
      background(0, 100, 100);
      fill(120, 100, 100);
      stroke(120, 75, 50);
      strokeWeight(3);
      ellipse(width / 2, height / 2, 100, 100);
    }
    ```

    Her kaller vi på en ny funksjon `colorMode` som tar imot
    fargesystemet som første argument og så maksverdier for de
    forskjelloge *kanalene* (H, S og B). Bare **RGB** og **HSB** kan
    brukes som fargesystem.

    Du lurer kanskje på hvorfor **H** har fått `360` som
    maksverdi. Det er fordi fargetonen baseres på fargehjulet, og det
    gir 360 grader med fargetoner. Metning og lys gis typisk i
    prosent. Du kan selvfølgelig velge helt andre maksverdier om du
    ønsker det.

+ Kjør programmet om du ikke har gjort det allerede.

+ Vi har sett at rød ligger på null grader, og grønn på `120`
  grader. La oss se hvilke farger som befinner seg rundt hjulet ved å
  endre `draw`:

    ```processing
    void draw() {
      background(0);
      
      fill(0, 100, 100);
      ellipse(width / 4, height / 3, 100, 100);
      
      fill(60, 100, 100);
      ellipse(2 * width / 4, height / 3, 100, 100);
      
      fill(120, 100, 100);
      ellipse(3 * width / 4, height / 3, 100, 100);
      
      fill(180, 100, 100);
      ellipse(width / 4, 2 * height / 3, 100, 100);
      
      fill(240, 100, 100);
      ellipse(2 * width / 4, 2 * height / 3, 100, 100);
      
      fill(300, 100, 100);
      ellipse(3 * width / 4, 2 * height / 3, 100, 100);
    }
    ```

    Her går vi gjennom fargetonene `60` grader ad gangen. Hvilke
    farger ligger på de seks vinklene: `0, 60, 120, 180, 240` og
    `300`? Hva tror du befinner seg på `360` grader?
    
    Om du lurer på regnestykkene for plasseringene av sirklene, så
    deler vi bredden på fire fordi det blir fire tomrom med tre
    kolonner. Tilsvarende blir det tre tomrom i høyden når vi har to
    rader. Ved å dele på antall tomrom, får vi bredden på avstanden
    mellom to nabosirkler eller vinduskanten og den nærmeste sirkelen.

+ Kjør programmet om du ikke har gjort det.

+ La oss se på hvordan metningen og lysheten påvirker fargen. Vi
  legger til en variabel for fargetone som skal endres over tid, sånn
  at vi kan se effekten også på forskjellige fargetoner. Legg derfor
  til følgende øverst i programmet:

    ```processing
    int tone;
    ```
    
    Så endrer vi `draw` til å tegne opp 9 sirkler der radene har samme
    metning, og kolonnene har samme lyshet:
    
    ```processing
    void draw() {
      background(0);
      
      int metning = 100;
      int lyshet = 100;
      
      tone = tone + 1;
      if (tone > 360) {
        tone = 0;
      }

      fill(tone, metning, lyshet);
      ellipse(width / 4, height / 4, 100, 100);

      lyshet = lyshet - 40;
      fill(tone, metning, lyshet);
      ellipse(2 * width / 4, height / 4, 100, 100);

      lyshet = lyshet - 40;
      fill(tone, metning, lyshet);
      ellipse(2 * width / 4, height / 4, 100, 100);

      lyshet = 100;
      metning = metning - 40;
      fill(tone, metning, lyshet);
      ellipse(width / 4, 2 * height / 4, 100, 100);

      lyshet = lyshet - 40;
      fill(tone, metning, lyshet);
      ellipse(2 * width / 4, 2 * height / 4, 100, 100);

      lyshet = lyshet - 40;
      fill(tone, metning, lyshet);
      ellipse(2 * width / 4, 2 * height / 4, 100, 100);

      lyshet = 100;
      metning = metning - 40;
      fill(tone, metning, lyshet);
      ellipse(width / 4, 3 * height / 4, 100, 100);

      lyshet = lyshet - 40;
      fill(tone, metning, lyshet);
      ellipse(2 * width / 4, 3 * height / 4, 100, 100);

      lyshet = lyshet - 40;
      fill(tone, metning, lyshet);
      ellipse(2 * width / 4, 3 * height / 4, 100, 100);
    }
    ```
    
    
