---
title: Trigonometri, regulære mangekanter og stjerner
level: 2
author: Sigmund Hansen
---

# Introduksjon {intro}

Nå som du kan tegne [mangekanter](../mangekanter/mangekanter.html)
(hvis du ikke har gjort leksjonen om mangekanter, bør du gjøre dem
først), skal vi se på en litt spesiell type mangekanter: de regulære
mangekantene. Det vil si de mangekantene hvor lengden av hver kant er
lik og vinkelen i hvert hjørne er lik. Vi skal også tegne deres nære
slektninger, de regulære stjernene.

Det er en stor fordel å kunne litt trigonometri før man slår seg løs
på disse oppgavene, men vi skal prøve å gi korte forklaringer av de
konseptene som brukes i leksjonen.

## Sinus og cosinus {.protip}

Før vi begynner å tegne regulære mangekanter, skal vi bare ta en liten
titt på to trigonometriske funksjoner som vi kommer til å bruke mye:
sinus og cosinus. Vi skal se på dem spesifikt i forbindelse med
sirkler.

+ Ethvert punkt langs omrisset av sirkelen befinner seg like langt fra
  midten av sirkelen. Denne avstanden er radius i sirkelen, som regel
  skriver vi bare `r` i figurer og formler.

!()[SirkelRadius.png "En sirkel med linjer med lengde `r` fra sentrum av sirkelen til punkter i omrisset"]

+ Vi kan tegne en rettvinklet trekant som ligger vannrett og strekker
  seg fra midten til dette punktet.

!()[RettvinkletTrekantSirkel.png "En rettvinklet trekant mellom et punkt i sirkelens omriss og sentrum."]

+ Hvis vi sier at sentrum av sirkelen ligger i punktet (0, 0), altså X
  og Y er null i midten av sirkelen, kan vi se på X og Y hver for seg
  når vi finner punktet i omrisset. To av sidene i trekanten ovenfor
  viser da X og Y. Den siste siden er linjen fra sentrum med lengde
  `r`. Her har vi kalt sidene `a`, `b` og `c`; navnet kan brukes for
  lengdene til sidene også. I dette tilfellet har vi `c = r` når vi
  snakker om lengden. For vinkler er det vanlig å bruke greske
  bokstaver, og vi har her brukt `α`.

+ Lengden på de to andre sidene, `a` og `b`, er gitt av funksjonene
  sinus og cosinus, vinkelen `α` og radien til sirkelen. De korte
  sidene som sammen lager det rettvinklede hjørnet, kalles kateter og
  den lange siden med lengde `r` kalles hypotenus. Lengden på katetet
  som er med på hjørnet med vinkelen `α`, har lengden `cos(α) *
  r`. Lengden på det andre katetet er `sin(α) * r`.

!()[TrekantSiderSirkel "Den samme rettvinklede trekanten med formler for lengdene til sidene."]

# Regulære mangekanter {.activity}

La oss tegne opp noen regulære mangekanter. Det vil si mangekanter der
avstanden mellom hvert hjørne er lik, altså de er likesidede, og
vinkelen i hvert hjørne er lik, altså de er likevinklede. Da lurer du
kanskje på hvordan du skal få til dette. Hjørnene i en regulær
mangekant fordeler seg jevnt langs omrisset av en sirkel. Derfor kan
vi bruke formlene for katetene for å regne ut hvor hjørnene skal
være. Opptegningen ellers er som for vanlige
[mangekanter](../mangekanter/mangekanter.html).

+ Vi begynner med å tegne opp en regulær pentagon (femkant).
  
  ```processing
  int KANTER = 5;
  float vinkel = 360.0 / KANTER;
  
  void setup() {
    size(600, 600);
  }
  
  void draw() {
    background(0);
    
    beginShape();
    for (int i = 0; i < KANTER; i++) {
      vertex(300 + cos(radians(vinkel * i)) * 200, 300 + sin(radians(vinkel * i)) * 200);
    }
    endShape(CLOSE);
  }
  ```

  Her har vi noen nye utregninger inne i kallet på `vertex`. Her
  bruker vi tre nye funksjoner `cos` og `sin` som har blitt forklart
  litt lenger opp, og `radians` som regner om grader til radianer, en
  annen måleenhet for vinkler. Sinus og cosinus i dataprogrammer
  bruker vanligvis radianer, så om vi vil jobbe med vinkler i grader,
  må vi gjør denne konverteringen. Du ser at vi har med en variabel
  for vinkelen mellom hvert punkt og denne har vi beregnet i grader ut
  fra at en sirkel er 360°.

![](Femkant.png "Vinkelen mellom to nabohjørner og sentrum i en femkant er 360° / 5 = 72°.")

+ Hva er tallet `200` her? Hva skjer om du endrer det til noe annet?

+ Hva med tallet `300`?

+ Kan du få snudd på femkanten sånn at hjørnet som nå peker rett til
  høyre, peker opp som i figuren ovenfor?

+ Kan du tegne en regulær pentagon, en femkant der alle kantene er
  like lange, og alle hjørnene har samme vinkel? Hjørnene i en regulær
  mangekant ligger på omrisset av en sirkel.

+ Hva med en regulær hexagon, sekskant? Eller heptagon, syvkant?
  Klarer du å gjøre det slik at du bruker variabelen `KANTER` til å
  styre hvor mange kanter den skal ha?

+ Stjerner med et oddetall antall spisser, kan tegnes som en regulær
  mangekant der man hopper over en spiss hver gang. Kan du finne
  spissene og tegne en 5-kantet stjerne?

    Spissene fordeler seg med like stor avstand fra hverandre
    (vinkelen mellom et hjørne, sentrum og det neste hjørnet er lik
    for hver spiss). Når man tegner en femkantet stjerne, tegner man
    en strek fra en spiss til den etter den neste.

![](Pentagram.png "Vinkelen mellom en spiss, sentrum og spissen etter nabospissen i en femkantet stjerne er 2 · 360° / 5 = 144°.")

+ Kan du tegne en syvkantet stjerne? Eller en nikantet stjerne?

+ Stjerner med et partall antall spisser, kan tegnes som to regulære
  mangekanter. Spissene vil da være de samme som hjørnene i
  mangekanten med det antallet kanter. Dette er lettest å løse ved å
  kopiere opptegningen av formene (fra og med `beginShape()` til og
  med `endShape(CLOSE)`), og endre `int i = 0` og `i++` til noe
  passende i løkken.

![](Oktagram.png "Vinkelen mellom en spiss, sentrum og spissen etter nabospissen i en åttekantet stjerne er 2 · 360° / 8 = 90°.")

Hvis du vil ha med alle strekene som vist i bildet ovenfor, må du ty
til tre løkker der den siste kun tegner omrisset av den første formen
(se dokumentasjonen til `noFill()`, `noStroke()` og `stroke()` ved å
velge **Help → Reference** og bruke søkefunksjonaliteten i
nettleseren).
  

