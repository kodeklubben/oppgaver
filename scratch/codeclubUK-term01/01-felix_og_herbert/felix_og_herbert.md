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
* Trykk på 'i' i hjørnet av !sprite1.png(Sprite1)! og bytt navn på figuren til 'Felix'.
* Sørg for at Felix kun ser til høyre og venstre ved å sette rotasjonsmåte til !rotasjonsmate-hv.png(Høyre/venstre)!.
* Klikk på scenen ved siden av 'Felix' i vinduet for figurer. Velg fanen 'Bakgrunner' og trykk på !velg-bakgrunn.png(Velg en ferdig bakgrunn)! for å importere en ferdig bakgrunn. Velg bakgrunnen 'Utendørs/Brick wall2'.
* Velg !ROOT/images/fane-skript.png(skript)!-fanen og lag dette skriptet:
!(skript)skript1.png!

h3(test). Test prosjektet

Klikk på det grønne flagget.

* Følger Felix musepekeren?
* Ser det ut som han går når han beveger seg?
* Beveger han seg med riktig hastighet?

h3(lagre). Lagre prosjektet

h2(steg). Steg 2: Felix jager Herbert

Nå ønsker vi at Felix skal jage musa Herbert i stedet for musepekeren.

h3(sjekkliste). Sjekkliste

# Lag en ny figur ved å trykke på !figur-fra-bibliotek.png(Velg figur fra biblioteket)! og velg figuren 'Dyr/Mouse1'.
# Bytt navn på figuren til Herbert og sørg for at også Herbert kun kan se til høyre og venstre !rotasjonsmate-hv.png(Høyre/venstre)!.
# Gjør Herbert mindre enn Felix ved å trykke på !krymp.png(Krymp)! (øverst mot midten av vinduet). Prøv seks klikk.
# Gi Herbert dette skriptet:
!(skript)skript2.png!

h3(test). Test prosjektet

Klikk på det grønne flagget.

* Flytter Herbert seg med musepekeren?
* Jager Felix Herbert?

h3(lagre). Lagre prosjektet

h2(steg). Steg 3: Felix sier når han har fanget Herbert

Vi vil at Felix skal vite når han har fanget Herbert og fortelle det til oss.

h3(sjekkliste). Sjekkliste

# Endre skriptet til Felix til dette:
!(skript)skript3.png!

h3(test). Test prosjektet

Klikk på det grønne flagget.

* Sier Felix fra når han har fanget Herbert?

h3(lagre). Lagre prosjektet

h2(steg). Steg 4: Herbert blir et spøkelse når han fanges

I stedet for at Felix sier noe, vil vi at Herbert blir forvandlet til et spøkelse når han fanges.

h3(sjekkliste). Sjekkliste

# Endre skriptet til Felix slik at det sender en melding og lager en lyd når han fanger Herbert:
!(skript)skript4.png!
# Velg Herbert og gå til !ROOT/images/fane-drakter.png(drakter)!-fanen.
# Hent en ny drakt ved å trykke på !figur-fra-bibliotek.png(Velg drakt fra biblioteket)! og velg 'Fantasi/ghost2-a'
# Gjør drakten mindre ved å velge !krymp.png(Krymp)! og trykke seks ganger på spøkelsesdrakten.
# Endre navnene på Herbers drakter slik at kattedrakten heter 'levende' og spøkelsesdrakten heter 'død'.
# Lag et nytt skript for Herbert for å gjøre ham om til et spøkelse. Ikke slett det gamle skriptet:
!(skript)skript5.png!

h3(test). Test prosjektet

Klikk på det grønne flagget.

* Forvandles Herbert til et spøkelse når han fanges?
* Spiller Felix de riktige lydene til riktig tid?
* Står Felix stille lenge nok til at Herbert kommer seg unna?

h3(lagre). Lagre prosjektet

h2(steg). Steg 5: Telle poeng

La oss legge til en poengsum slik at vi kan se hvor flink man er til å holde Herbert i live. Vi begynner med poengsummen null og øker den med en for hvert sekund. Hvis Felix fanger Herbert, minker vi poengsummen med hundre.

h3(sjekkliste). Sjekkliste

# På !ROOT/images/fane-skript.png(skript)!-fanen under kategorien !ROOT/images/kategori-data.png(Data)!, lag en ny variabel. La den gjelde for alle figurer og kall den poengsum.
!ny-variabel-poengsum.png!
# Lag disse to skriptene på scenen:
!(skript)skript6.png!

h3(test). Test prosjektet

Klikk på det grønne flagget.

* Øker poengsummen med en hvert sekund?
* Går poengsummen ned med hundre når Herbert blir fanget?
* Hva skjer når Herbert fanges før du har hundre poeng?
* Går poengsummen tilbake til null når du starter spillet på nytt?

h3(lagre). Lagre prosjektet

Du er ferdig. Godt gjort. Nå kan du spille spillet!
Husk at du kan dele spillet med familie og venner ved å trykke 'Legg ut' på menylinjen.

