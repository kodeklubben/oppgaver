---
title: "CSS: Skjul ninjaane"
author: "Omsett frå [Code Club UK](//codeclub.org.uk)"
translator: Stein Olav Romslo
language: nn
---


# Introduksjon {.intro}

Denne oppgåva skal utvide talenta dine i __CSS-kungfu__.

I denne oppgåva skal du lære korleis du kan flytte rundt på element og gøyme
elementa bak andre element ved hjelp av CSS.

Fem ninjaar kom til byen, og du må skjule dei før nokon legg merke til dei. Ved
å bruke dine eigne ninja-linande CSS-kunnskapar må du hjelpe dei å finne ein
sikker gøymestad. Du kan flytte ninjaane sjølv, i tillegg til nokre objekt på
gata. Fort - det er inga tid å miste!

![Bilete av dei fem ninjaane](ninjas.png)


# Steg 1: Møt ninjaane {.activity}

- [ ] Last ned [ninja.zip](ninja.zip) og pakk ut filene på datamaskina di.

- [ ] Åpne fila kalt `ninjaer.html` i ein teksteditor.

- [ ] Åpne `ninjaer.html` i nettlesaren for å sjå korleis den ser ut.

- [ ] Les gjennom koden. Kan du gjette kva del av koden som høyrer til delane i
  gatene? Legg merke til at me brukar to språk: `HTML` for å leggje til elementa
  på sida, og `CSS` plassert mellom `<style>`-taggane.

- [ ] Elementa me skal leike med er bileta, `<img>`-taggen. Me kan ta kontroll
  over plasseringen deira ved å bruke CSS.

**Kom igjen – la oss flytte ein ninja!**

Alle ninjaane har fått sitt eige namn ved bruk av `id`-attributten. La oss
flytte "Alex The Ninja" fyrst

- [ ] Finn Alex sin CSS-stil.

- [ ] Endre verdien på `left` (venstre) til `100px` og `top` til `320px`.

Når `position`-eigenskapane er sett til `absolute` meiner me at det beskriv
posisjonen samanlikna med foreldreelementet til ninjaen - her er det `<div>` med
`id` `gatehjoerne`.

`px` betyr `pixel` (punkter). `left` beskriv kor langt frå venstrekanten ninjaen
skal plasserast (antal pikslar) og `top` forteller nettleseren hvor langt
ninjaan skal flyttes ned fra toppen.

- [ ] Endre `left` til `right` og `top` til `bottom`. Nå vil koden fortelle
  nettleseren at den skal plassere ninjaan `100px` fra den høyre kanten og
  `320px` fra bunnen.

Pixel er en måleenhet som vi bruker til å forklare hvor stort et element skal
være eller hvor det skal plasseres på siden. Hvis du endrar `right` frå `100px`
til `101px`, så ser me at den ikkje blir flytta veldig langt. Difor gjer pikslar
det enklare for oss å designe nettsida så detaljert me vil.


# Steg 2: Ein annan måte å flytte på {.activity}

No veit du korleis du brukar piksel-posisjonering. Det er ikkje den einaste
måten å beskrive plassering på skjermen, så la oss sjekke nokre andre
moglegheiter. Me skal sjå på korleis me kan bruke `%`, det ser slik ut:

```css
  #id{
    left: 100%;
    top: 100%;
  }
```

`100%` tyder heile breidda som er tilgjengeleg på skjermen. Når me plasserar
ninjaar og andre objekt i forhold til `gatehjornet`, som er 600 pikslar brei, så
vil 100 % være lik `600px` i dømet vårt. Viss me hadde laga eit større
gatehjørne, til dømes 800 pikslar breitt, så ville `100%` vere ei breidde på
`800px`. Avhengig av samanhengen så kan storleiken beskrive i prosent (`%`) ha
ulike tydingar.

- [ ] Finn `soppelkasse`-elementet i CSS-en.

- [ ] Bytt ut verdiane `190px` og `460px` i `soppelkasse`-elementet med
  prosentar slik at søppelkassa står på omlag same stad som no. Det treng ikkje
  vere heilt nøyaktig.


# Steg 3: Endå ein storleikstype {.activity}

Som om me ikkje har nok storleikstypar skal me prøve endå ein! Du veit korleis
du kan bruke pikslar (`px`) og prosent (`%`). La oss prøve `em`.

`Em` er ei måleeining som me låner frå typografi, som handlar om utsjånad på
bokstavar og tekst. Ein `em` er det same som den gjeldande skriftstorleiken.
Legg merke til at på toppen av CSS-en definerte me `font-size` i `body`-taggen
som `20px`, så ein `em` er `20px` i fila vår.

- [ ] La oss teste det ut. Finn `body` i CSS-en. Endre `font-size` verdien til
  `30px`. Kva skjedde?

- [ ] Studér koden for å finne elementa som skal flytte på seg når `font-size`
  endrast.

- [ ] Flyttar dei riktige elementa på seg?

Som du ser endrar høgda og breidda seg på alle element som brukar `em`-verdiar
når me endrar `em` til 30 pikslar.


# Steg 4: Flytt figurar framover {.activity}

Før me skal begynne å gøyme ninjaane skal me studere ein ting til: `z-index`.

- [ ] Leit gjennom CSS-en og sjå om du finn `z-index` nokon stad.

`Z-index` skal du finne to stader: i klassa `.ninja` og i ID-en
`#andre_gjenstandar`. `Z-index` bestemmer kva element som ligg fremst på sida,
altså kva element som skal liggje oppå dei andre. Me ser at `#andre_gjenstandar`
har ein verdi på 200 og `.ninja` har ein verdi på 1. Dette tyder at ninjaane vil
leggje seg bak dei andre elementa, sidan dei har høgare `z-index`-verdi.

Her er eit bilete som beskriv `z-index`:

![Illustrasjon av z-index](zindex1.png){width="30%"}

- [ ] Prøv å endre på `z-index`-verdien og sjå kva som skjer.

- [ ] Legg til `z-index` på eit element og sjå om du kan få elementet til å
  leggje seg bak eller framfor eit anna.

__Døme:__

```css
  #andre_objekt{
    z-index: 1;
  }

  .ninja{
    z-index: 2;
  }
```

- [ ] Bytt tilbake og førebu deg på redde ninjaane!


# Steg 5: Fort deg, skjul ninjaane! {.activity}

- [ ] Sjå gjennom koden, finn ut kva element du kan gøyme ninjaane bak.

- [ ] Bruk det du har lært til å gøyme ninjaane.

Her er det ingen fasit, så du må leggje til og endre kode slik at du får gøymt
ninjaane. Viss du står fast bør du lese oppgåva på nytt, eller prøve å finne
hjelp på [w3schools.com](http://www.w3schools.com/css/default.asp). Det ligg eit
døme på løysing nedst i denne oppgåva.

__LYKKE TIL!__

## Ting du kan prøve {.challenge}

- [ ] Legg gjerne til `z-index` eller endre `position` i CSS-en på dei elementa
  du føler treng dei.

- [ ] Kan du finne ut korleis du kan få ninjaane til å kome framfor gateobjekta?
  Kva skjer viss du kopierer `<img>`-taggen for ninjaen etter `<img>`-taggen som
  viser objektet?

- [ ] Klarar du å leggje til fleire objekt på scena? Du kan leggje til bilete
  frå datamaskina di, eller finne nokon på Internett.

## Døme på kode

![resultat](resultat.png)

<toggle>
<strong>Vis forslag til kode</strong>
  <hide>

  ```html
  <!DOCTYPE html>
<html>
<head>
 <meta charset=utf-8 />
 <title>Skjul ninjaane</title>
 <style>

   body {
     font-size: 20px;
   }

   #gatehjorne {
     width: 955px;
     height: 700px;
     margin-left: auto;
     margin-right: auto;
     background: url(gatehjorne.png);
     position: relative;
   }
   #andre_objekt {
     margin-left: auto;
     margin-right: auto;
     top: 0px;
     left: 0px;
     position: absolute;
     z-index: 200;
   }
   #kontainer {
     position: absolute;
     top: 14%;
     left: 73%;
     z-index: 2;
   }
   #soppelkasse {
     position: absolute;
     bottom: 190px;
     left: 460px;
   }
   #sykkel {
     position: relative;
     bottom: -520px;
     right: -20em;
   }
   #kafe_skilt {
     position: fixed;
     bottom: 2em;
     left: 11em;
     z-index: 2;
   }
   #kumlokk {
     position: fixed;
     bottom: 20em;
     left: 520px;
   }

   /* Ninjas */

   #lucy_the_ninja {
     position: fixed;
     top: 0px;
     left: 280px;
   }
   #alex_the_ninja {
     position: absolute;
     top: 90px;
     right: 140px;
   }
   #katy_the_ninja {
     position: relative;
     top: 380px;
     left: 6em;
   }
   #sam_the_ninja {
     position: static;
     top: 100px;
     left: 150px;
   }
   #omar_the_ninja {
     position: fixed;
     bottom: 100px;
     left: 250px;
   }
   .ninja {
     z-index: 1;
   }

   /* Andre objekt (du kan ikkje flytte desse) */

 </style>
<style id="jsbin-css"></style>
</head>
<body>
 <div id="gatehjorne">

   <img id="lucy_the_ninja" alt="lucy_the_ninja" class="ninja" src="lucy.png" />
   <img id="alex_the_ninja" alt="alex_the_ninja" class="ninja" src="alex.png" />
   <img id="katy_the_ninja" alt="katy_the_ninja" class="ninja" src="katy.png" />
   <img id="omar_the_ninja" alt="omar_the_ninja" class="ninja" src="omar.png" />
   <img id="sam_the_ninja" alt="sam_the_ninja" class="ninja" src="sam.png" />


   <img id="kumlokk" alt="kumlokk" class="movable" src="kumlokk.png" />
   <img id="kontainer" alt="kontainer" class="movable" src="kontainer.png" />
   <img id="soppelkasse" alt="soppelkasse" class="movable" src="soppelkasse.png" />
   <img id="sykkel" alt="sykkel" class="movable" src="sykkel.png" />
   <img id="kafe_skilt" alt="kafe_skilt" class="movable" src="kafe_skilt.png" />

   <img id="andre_objekt" alt="andre_objekt" src="andre_objekt.png" />

 </div>

<script>

</script>
</body>
</html>

  ```

  </hide>
</toggle>
