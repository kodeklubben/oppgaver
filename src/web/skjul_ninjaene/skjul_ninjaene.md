---
title: Skjul ninjaene
level:  3
language: nb-NO
---

## Introduksjon  { .intro}
Dette prosjektet vil utvide din kunnskapen din om CSS-kungfu.

Fem ninjaer kom til byen, og du må skjule dem før noen legger merke til dem. Ved å bruke dine egne ninja-liknende CSS-kunnskaper må du hjelpe dem å finne et sikkert gjemmested. Du kan flytte ninjaene selv, og noen objekter i gaten også. Fort – det er ingen tid å miste!

![screenshot](ninjas.png)

# Steg 1: Møt ninjaene { .activity}

+ Åpne filen kalt ninjaer.html i teksteditoren. Åpne det opp i nettleseren også.
+ Les gjennom koden. Kan du gjette hvilken del av koden som hører til delene i gatene? Legg merke til av vi bruker to språk her: HTML for å legge til elementene på siden, og CSS plassert mellom `style` taggene.
+ Elementene vi skal leke med er bildene (`<img>` taggen). Vi kan ta kontroll over deres plassering ved å bruke CSS.

**Kom igjen – La oss flytte en ninja! **

+ Alle ninjaene har fått eget navn ved bruk av `id` attributtet. La oss flytte Alex The Ninja først. Finn Alex sin CSS-stil.
+ • Endre verdien på `left`(venstre) til `100px` og `top` til `320px`.
Når position egenskapene er satt til `absolute` menes det at vi vil beskrive posisjonen i relasjon til foreldreelementet til ninjaen – I dette eksempelet `<div>` med `id` `gatehjoerne`.
`px` betyr `pixel`(punkter). `left` beskriver hvor langt fra venstrekanten ninjaen skal plasseres (antall pixler) og `top` forteller nettleseren hvor langt ninjaen skal flyttes ned fra toppen.
+ Endre `left` til `right` og `top` til `bottom`. Nå vil koden fortelle nettleseren at den skal plassere ninjaen `100px` fra den høyre kanten og `320px` fra bunnen.

Pixel beskriver det minste fysiske punktet som kan vises på skjermen din. Det brukes ofte til å beskrive størrelsen på skjermen din.

# Steg 2: Las prøve å beskrive dette litt annerledes. { .activity}

Nå vet du hvordan vi bruker pixel-posisjonering. Dette er ikke den eneste måten man kan beskrive plasseringer på skjermen, så la oss se på hva slags andre muligheter vi har.

+ Finn `soppelkasse` elementet i CSSen.

100% beskriver hele bredden som er tilgjengelig på skjermen. Når vi plasserer ninjaer og andre objekter i forhold til `gatehjornet`, som er 600 pixler bred, så vil 100% være lik `600px` i vårt eksempel. Hvis vi hadde laget et større gatehjørne, f.eks. 800 pixler bredt, ville 100% bety en bredde på `800px`. Avhengig av sammenhengen så kan størrelsen beskrevet i prosenter har forskjellige betydninger.

# Steg 3:  En størrelsetype til { .activity}

Som om vi ikke har nok størrelse-typer nå, skal vi likevel prøve en til! Du vet nå hvordan man skal bruke pixler (px) og prosent(%). La oss nå prøve `em`.

`Em` er en måleenhet som vi låner fra typografi, som er handler om utsende på bokstaver og tekst. Én em er det samme som den gjeldende skriftstørrelsen. Legg merke til at på toppen av CSS, definerte vi font-size i body taggen som 20px, så én em vil være 20 pixler.

+ Vi skrev tidligere at størrelsen på én `em` er basert på fontstørrelsen. For å teste dette, finn `body` i CSSen. Endre `font-size` verdien til 30px. Hva skjedde?
Som dere ser når vi endre `em` til 30 pixler så endrer bredden og høyden seg til 30 pixels bred og 30 pixels høy på alle elementer som bruker denne verdien. Og som dere ser alle disse elementene har endret posisjon!

# Steg 4: Fort deg, skjul ninjaene!  { .activity}

Nå når du vet hvordan du skal flytte på elementene på skjermen, er det på tide å hjelpe ninjaene. Bruk de forskjellige måtene som er beskrevet over. Husk, du kan også flytte noen av objektene. Hvilken måte synes du er den beste å flytte de på? Finn den beste måten å skjule dem på. Lykke til!


## Ting du kan prøve: { .try}

+ Kan du finne ut hvordan du kan få ninjaene til å komme foran noen av gateobjektene? Hva skjer om du kopierer `<img>` taggen for ninjaen etter `<img>` taggen som viser objektet?
+ Klarer du å legge til flere objekter på scenen? Du kan legge til bilder fra datamaskinen din, eller finne noen på internett.
