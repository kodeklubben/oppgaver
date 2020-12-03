---
title: "Feilsøking: Smelt snømennene 2"
author: "Carl A. Myrland" 
language: 
---


# Om oppgaven {.activity}

I denne oppgaven skal elevene feilsøke koden til tre snømenn og rette opp alle feilene, slik at spillet funker som det skal. Til slutt må de lage en klokke som teller ned fra 10. Denne oppgaven legger opp til stor grad av samarbeid og problemløsning. Løsningene blir ikke grundig forklart i oppgaveheftet, og elevene oppfordres til å finne løsninger på egenhånd. Løsningsforslag finner du nederst her i lærerveiledningen.

## Oppgaven passer til: {.check}

 **Fag**: Matematikk, Programmering

**Anbefalte trinn**: 5.-7. klasse, 8.-10. klasse, Videregående Skole

**Tema**: Blokkbasert, Spill

**Tidsbruk**: 1 skoletime

## Kompetansemål {.challenge}

**Matematikk, 8. årstrinn**:
- [ ] utforske korleis algoritmar kan skapast, testast og forbetrast ved hjelp av programmering

## Forslag til læringsmål {.challenge}

- [ ] Elevene kan lese, feilsøke og fikse enkle algoritmer ved å bruke enkle problemløsningsstrategier, alene og sammen med andre.
- [ ] Elevene klarer med litt hjelp og samarbeid å lage nye algoritmer som løser et problem.


## Forslag til vurderingskriterier {.challenge}

Det er mange ulike måter man kan vurdere et programmeringsprosjekt, og her må en
selv vurdere hva som er den beste måten ut ifra hvilket fag man jobber i,
hvilken aldergruppe og hviklet nivå elevene er på, hva man ønsker å teste og
hvor mye tid man har til rådighet til å jobbe med prosjektet. I vårt
[lærerdokument](https://github.com/kodeklubben/oppgaver/wiki/Hvordan-undervise-i-og-vurdere-programmering){target=_blank} har vi blant
annet beskrevet ulike måter dette kan gjøres på, tillegg til en del andre
nyttige tips til hvordan man underviser i programmering.

## Forutsetninger og utstyr {.challenge}

**Forutsetninger**:
- [ ] Elevene bør ha en del kjennskap til koding fra før, og være kjent i Scratch.

**Utstyr**:
- [ ] PC/læringsbrett med eksternt tastatur.

## Fremgangsmåte

Her kommer tips, erfaring og utfordringer til de ulike stegene i den faktiske
oppgaven. 

# Steg 1: Remiks {.activity}

- [ ] Her skal elevene helt enkelt trykke på lenken og lage sin egen remiks av prosjektet. Dersom elevene ikke har Scratch-konto, kan de bare trykke "se inni" og begynne å kode. De må da trykke på "Fil - Lagre på datamaskinen" om de vil ta vare på prosjektet sitt.

Dersom du har printet ut oppgaveheftene, kan du be elevene gå til denne adressen for å remikse prosjektet: [scratch.mit.edu/projects/448963560/](scratch.mit.edu/projects/448963560/){target=_blank}

# Steg 2: Fiks koden {.activity}

- [ ] De tre snømennene skal ha eksakt samme kode:

```blocks
Når grønt flagg klikkes
sett størrelse til (100)%
pek i retning [90 v]
begrens rotasjon [vend sideveis v]
vend venstre (15) grader
gjenta for alltid
gå (3) steg
sprett tilbake ved kanten
```
og

```blocks
Når denne figuren klikkes
Gjenta (4) ganger
vent (1) sekunder
endre [ghost v] effekt med (25)
endre størrelse med (-10)

```
# Steg 3: Legg til en nedtelling {.activity}
Her må elevene opprette variabelen `tid`{.blockdata}. Selve koden oppretter de ved å trykke på "Bakgrunn" og lage koden der. Det er ofte en god idé å legge generelle algoritmer som ikke tilhører bestemte spillfigurer til bakgrunnen - sånt som nedtellinger, poengsystemer, skifting av bakgrunner osv.

```blocks
Når grønt flagg klikkes
sett [tid v] til (10)
gjenta (10) ganger
vent (1) sekunder
endre [tid v] med (-1)
end
stopp [alle v]
```

Dette er en ganske enkel og grov nedtellingsalgoritme som kan utvides og forbedres mye av en med litt erfaring!


## Utfordring {.challenge}

- [ ]  Elevene blir utfordret til å forsøke å videreutvikle prosjektet med en rekke forslag. Disse utfordringene lages det ikke løsningsforslag til. Oppfordre elevene til å diskutere og feilsøke hverandres kode. Kan de finne ideer til løsninger i andre oppgaver på [oppgaver.kidsakoder.no](oppgaver.kidsakoder.no){target=_blank}? 

## Eksterne ressurser {.challenge}

- [ ] Foreløpig ingen eksterne ressurser ...