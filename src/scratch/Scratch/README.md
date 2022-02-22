---
title: Kunst med geometriske figurer
author: ''
language: nb
---
# Om oppgaven {.activity}

I denne oppgaven lærer elevene å skrive et enkelt program som lar deg tegne regulære mangekanter ved å trykke på et tilfeldig sted på scena. I første omgang setter vi opp en enkel algoritme vi kan justere på for å tegne ulike regulære mangekanter. For nybegynnere kan det være nok å kode til og med Steg 2. For elever som har kodet litt fra før, eller skal lære om funksjoner (matematikk, 6. trinn) og forbedring av algoritmer (matematikk, 8. trinn), er stegene 3-5 nyttige.

Vi har forsøkt å skrive oppgaven så enkelt og tydelig som mulig, slik at alt eleven trenger står i oppgaveteksten. Vi har også lagt inn noen infobokser med tilleggsinformasjon til oppgaven. Dette kan det være nyttig at du som lærer eller instruktør i kodeklubb tar opp og diskuterer med elevene, gjerne med litt konkretisering.

Legg også merke til at Steg 2 er skrevet to ganger, én gang for nettbrett, og én gang for PC. Dette pga ulikheter i hvordan brukeren interagerer med Scratch med mus vs touchskjerm.



## Oppgaven passer til: {.check}

 **Fag**: Matematikk, Kunst og Håndverk, Programmering

**Anbefalte trinn**: 5.-7. klasse, 8.-10. klasse

**Tema**: Blokkbasert, Stegbasert

**Tidsbruk**: 90 min for hele opplegget.

## Kompetansemål {.challenge}

- [ ] **Matematikk, 5. årstrinn**: lage og programmere algoritmar med bruk av variablar, vilkår og lykkjer
- [ ] **Matematikk, 6. årstrinn**: bruke variablar, lykkjer, vilkår og funksjonar i programmering til å utforske geometriske figurar og mønster
- [ ] **Matematikk, 8. årstrinn**: utforske korleis algoritmar kan skapast, testast og forbetrast ved hjelp av programmering

## Forslag til læringsmål {.challenge}

- [ ] Elevene kan bruke grunnleggende kunnskap om regulære mangekanter til å endre koden for å tegne ønsket figur
- [ ] Elevene kan bruke funksjoner og variabler til å forbedre måten et program fungerer på.

## Forslag til vurderingskriterier {.challenge}

Det er mange ulike måter man kan vurdere et programmeringsprosjekt, og her må en
selv vurdere hva som er den beste måten ut ifra hvilket fag man jobber i,
hvilken aldergruppe og hviklet nivå elevene er på, hva man ønsker å teste og
hvor mye tid man har til rådighet til å jobbe med prosjektet. I vårt
[lærerdokument](https://github.com/kodeklubben/oppgaver/wiki/Hvordan-undervise-i-og-vurdere-programmering){target=_blank} har vi blant
annet beskrevet ulike måter dette kan gjøres på, tillegg til en del andre
nyttige tips til hvordan man underviser i programmering.

## Forutsetninger og utstyr {.challenge}

- [ ] **Forutsetninger**: Grunnleggende kunnskap om regulære mangekanter er en fordel.

- [ ] **Utstyr**: PC/nettbrett. Scratch-konto er en fordel, men ikke et krav.

## Kodefasit

Her kommer tips, erfaring og utfordringer til de ulike stegene i den faktiske
oppgaven. 

# Steg 1: Komplett kode etter steg 1 {.activity}
For figuren `Pencil`
```blocks
Når grønt flagg klikkes
send melding [klar v]

Når jeg mottar [klar v]
begrens rotasjon [ikke roter v]
skjul
penn av
slett alt
vis
send melding [ferdig v]

Når jeg mottar [ferdig v]
gjenta for alltid
gå til [musepeker v]
```


# Steg 2: Komplett kode etter steg 2 (PC) {.activity}
For figuren `Pencil`

```blocks
Når grønt flagg klikkes
send melding [klar v]

Når jeg mottar [klar v]
begrens rotasjon [ikke roter v]
skjul
penn av
slett alt
vis
send melding [ferdig v]

Når jeg mottar [ferdig v]
gjenta for alltid
gå til [musepeker v]

Når denne figuren klikkes
stopp [andre skript i figuren v]
penn på
pek i retning (90)
gjenta (4) ganger
gå (100) steg
vend høyre (90) grader 
end
penn av
send melding [ferdig v]
```
# Steg 2: Komplett kode etter steg 2 (nettbrett) {.activity}
For figuren `Button1`

```blocks
Når grønt flagg klikkes
gå til x: (180) y: (-150)

Når denne figuren klikkes
send melding [start v]
```

For figuren `Pencil`

```blocks
Når grønt flagg klikkes
send melding [klar v]

Når jeg mottar [klar v]
begrens rotasjon [ikke roter v]
skjul
penn av
slett alt
vis
send melding [ferdig v]

Når jeg mottar [ferdig v]
gjenta for alltid
gå til [musepeker v]

Når jeg mottar [start v]
stopp [andre skript i figuren v]
penn på
pek i retning (90)
gjenta (4) ganger
gå (100) steg
vend høyre (90) grader 
end
penn av
send melding [ferdig v]
```

# Steg 3:  {.activity}
Her skal ikke elevene lage ny kode, kun endre på eksisterende kode.
#

# Steg 4: Komplett kode fra steg 4 {.activity}

Her må elevene bygge om koden fra steg 2 til å bli slik.

Første del gjelder både PC og nettbrett:

```blocks
Når grønt flagg klikkes
send melding [klar v]

Når jeg mottar [klar v]
begrens rotasjon [ikke roter v]
skjul
penn av
slett alt
vis
send melding [ferdig v]

Når jeg mottar [ferdig v]
gjenta for alltid
gå til [musepeker v]

definer mangekant (kanter) (sidelengde)
gjenta (kanter) ganger
gå (sidelengde) steg
vend høyre ((180) -  ((((kanter) - (2)) * (180)) / (kanter))) grader
end
```

**Den neste delen er ulik for PC og nettbrett.**

**PC:**

For figuren `Pencil`
```blocks
Når denne figuren klikkes
stopp [andre skript i figuren v]
penn på
pek i retning (90)
mangekant () () 
penn av
send melding [ferdig v]
```

**For nettbrett:**

For figuren `Button1`

```blocks
Når grønt flagg klikkes
gå til x: (180) y: (-150)

Når denne figuren klikkes
send melding [start v]
```

For figuren `Pencil`

```blocks
Når grønt flagg klikkes
send melding [klar v]

Når jeg mottar [klar v]
begrens rotasjon [ikke roter v]
skjul
penn av
slett alt
vis
send melding [ferdig v]

Når jeg mottar [ferdig v]
gjenta for alltid
gå til [musepeker v]

```

#

# Steg 5: Eksempel på hvordan koden kan utformes {.activity}
Dette steget åpner for kreativitet og utforskning. Her er et forslag til hvordan koden kan settes opp. Merk: Dette er justeringer på eksisterende kode. 

```blocks
Når grønt flagg klikkes
sett pennfarge til ()
send melding [klar v]
```

For figuren `Pencil`
```blocks
Når denne figuren klikkes
stopp [andre skript i figuren v]
endre pennfarge med (15)
sett pennbredde til (tilfeldig tall fra (1) til (10))
penn på
pek i retning (tilfeldig tall fra (-180) til (180))
mangekant (sideAntall) (sideLengde) 
penn av
send melding [ferdig v]
```
#
