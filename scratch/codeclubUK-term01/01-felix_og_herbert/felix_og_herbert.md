# Felix og Herbert

## Introduksjon

Vi skal lage et spill hvor katten Felix skal fange musa Herbert. Du styrer Herbert med musepekeren og skal prøve å unngå å bli tatt av Felix. Jo lenger du unngår ham jo flere poeng får du, men blir du tatt, går poengsummen din ned.

![skjearmbilde](Screengrab.PNG)


|Sjekkliste| Følg instruksjonene på lista. Huk av etter hvert.|
|Test| Klikk på det grønne flagget for å teste koden.|
|Lagre| Husk å lagre koden når du har lagt til noe nytt.|

## Steg 1: Felix følger musepekeren

Vi ønsker at katten Felix skal følge etter musepekeren.

### Sjekkliste

* Start et nytt prosjekt.
* Trykk på 'i' i hjørnet av ![Sprite1](sprite1.png) og bytt navn på figuren til 'Felix'.
* Sørg for at Felix kun ser til høyre og venstre ved å sette rotasjonsmåte til ![Høyre/Venstre](rotasjonsmate-hv.png).
* Klikk på scenen ved siden av 'Felix' i vinduet for figurer. Velg fanen 'Bakgrunner' og trykk på ![Velg en ferdig bakgrunn](velg-bakgrunn.png) for å importere en ferdig bakgrunn. Velg bakgrunnen 'Utendørs/Brick wall2'.
* Velg ![skript](ROOT/images/fane-skript.png)-fanen og lag dette skriptet:
![skript](skript1.png)

### Test prosjektet

Klikk på det grønne flagget.

* Følger Felix musepekeren?
* Ser det ut som han går når han beveger seg?
* Beveger han seg med riktig hastighet?

### Lagre prosjektet

## Steg 2: Felix jager Herbert

Nå ønsker vi at Felix skal jage musa Herbert i stedet for musepekeren.

### Sjekkliste

* Lag en ny figur ved å trykke på ![Velg figur fra biblioteket](figur-fra-bibliotek.png) og velg figuren 'Dyr/Mouse1'.
* Bytt navn på figuren til Herbert og sørg for at også Herbert kun kan se til høyre og venstre ![Høyre/Venstre](rotasjonsmate-hv.png).
* Gjør Herbert mindre enn Felix ved å trykke på ![krymp](krymp.png) (øverst mot midten av vinduet). Prøv seks klikk.
* Gi Herbert dette skriptet:
![skript2](skript2.png)

### Test prosjektet

Klikk på det grønne flagget.

* Flytter Herbert seg med musepekeren?
* Jager Felix Herbert?

### Lagre prosjektet

## Steg 3: Felix sier når han har fanget Herbert

Vi vil at Felix skal vite når han har fanget Herbert og fortelle det til oss.

### Sjekkliste

* Endre skriptet til Felix til dette:
![skript3](skript3.png)

### Test prosjektet

Klikk på det grønne flagget.

* Sier Felix fra når han har fanget Herbert?

### Lagre prosjektet

## Steg 4: Herbert blir et spøkelse når han fanges

I stedet for at Felix sier noe, vil vi at Herbert blir forvandlet til et spøkelse når han fanges.

### Sjekkliste

* Endre skriptet til Felix slik at det sender en melding og lager en lyd når han fanger Herbert:
![skript4](skript4.png)
* Velg Herbert og gå til ![drakter](ROOT/images/fane-drakter.png)-fanen.
* Hent en ny drakt ved å trykke på ![Velg drakt fra biblioteket](figur-fra-bibliotek.png) og velg 'Fantasi/ghost2-a'
* Gjør drakten mindre ved å velge ![Krymp](krymp.png) og trykke seks ganger på spøkelsesdrakten.
* Endre navnene på Herbers drakter slik at kattedrakten heter 'levende' og spøkelsesdrakten heter 'død'.
* Lag et nytt skript for Herbert for å gjøre ham om til et spøkelse. Ikke slett det gamle skriptet:
![skript5](skript5.png)

### Test prosjektet

Klikk på det grønne flagget.

* Forvandles Herbert til et spøkelse når han fanges?
* Spiller Felix de riktige lydene til riktig tid?
* Står Felix stille lenge nok til at Herbert kommer seg unna?

### Lagre prosjektet

## Steg 5: Telle poeng

La oss legge til en poengsum slik at vi kan se hvor flink man er til å holde Herbert i live. Vi begynner med poengsummen null og øker den med en for hvert sekund. Hvis Felix fanger Herbert, minker vi poengsummen med hundre.

### Sjekkliste

* På ![skript](ROOT/images/fane-skript.png)-fanen under kategorien ![Data](ROOT/images/kategori-data.png), lag en ny variabel. La den gjelde for alle figurer og kall den poengsum.
![poengsum](ny-variabel-poengsum.png)
* Lag disse to skriptene på scenen:
![skript](skript6.png)

### Test prosjektet

Klikk på det grønne flagget.

* Øker poengsummen med en hvert sekund?
* Går poengsummen ned med hundre når Herbert blir fanget?
* Hva skjer når Herbert fanges før du har hundre poeng?
* Går poengsummen tilbake til null når du starter spillet på nytt?

### Lagre prosjektet

Du er ferdig. Godt gjort. Nå kan du spille spillet!
Husk at du kan dele spillet med familie og venner ved å trykke 'Legg ut' på menylinjen.

