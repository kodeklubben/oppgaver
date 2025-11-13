---
title: 'Kodetimen - Utforsk en fremmed planet! '
author: marikisfoss
language: nb
---
![Bildebeskrivelse](./kodar.png)
  
# Introduksjon {.intro}
  
Vel møtt, modige romfarere! Jeg heter Kodar, og velkommen til min planet; Timenor! 

Som gjester på min planet vil jeg at dere skal utforske hvilket liv som finnes her. I dette oppdraget skal dere bruke Micro:bit til å sende signaler til basen, for å loggføre funnene på Timenor!


Denne oppgaven utføres som grupper (eller et rommannskap om du vil). Lærer vil ha rollen som kaptein for romstasjonen, og være ansvarlig for å motta informasjon på hvert rommannskaps romstasjon-Micro:bit. 

Kanskje dere gjør oppdraget til en konkurranse, der det er om å gjøre å finne så mange fremmede vesen og planter som mulig? 


**Det kan være lurt å dele denne oppgaven inn i to deler: En der dere fokuserer på å lage figurer, og klippe de ut, og en del der dere programmerer og gjennomfører den fysiske delen av oppgaven der elevene går rundt i klasserommet og leter etter liv på den fremmede planeten (klasserommet).** 

## Oppgaven passer til: {.check}

 **Fag**: Matematikk, Naturfag, Programmering, Kunst og Håndverk

**Anbefalte trinn**: 8.-10. klasse, 5.-7. klasse

**Tema**: Elektronikk, Programmering

**Tidsbruk**: 1 - 2 timer

## Kompetansemål {.challenge}

Relevante kompetansemål:


**4. trinn:**

Naturfag:
utforske teknologiske systemer som er satt sammen av ulike deler, og beskrive hvordan delene fungerer og virker sammen
K&H:


Matte:
lage algoritmar og uttrykkje dei ved bruk av variablar, vilkår og lykkjer


**7. trinn:**

Naturfag:
utforske, lage og programmere teknologiske systemer som består av deler som virker sammen
skille mellom observasjoner og slutninger, organisere data, bruke årsak-virkning-argumenter, trekke slutninger, vurdere feilkilder og presentere funn


K&H:


Matte:
lage og programmere algoritmar med bruk av variablar, vilkår og lykkjer (5. trinn)


**10. trinn:**

Naturfag:
utforske, forstå og lage teknologiske systemer som består av en sender og en mottaker
bruke programmering til å utforske naturfaglige fenomener


K&H:


Matte:
utforske korleis algoritmar kan skapast, testast og forbetrast ved hjelp av programmering (8. trinn)


## Forslag til læringsmål {.challenge}

Læringsmålene dekker kompetansemål innen naturfag og matematikk:

 Programmere trådløse sendere og mottakere med micro:bit
Lage og utforske algoritmer med blant annet hendelser og variabler


## Forslag til vurderingskriterier {.challenge}

Det er mange ulike måter man kan vurdere et programmeringsprosjekt, og her må en
selv vurdere hva som er den beste måten ut ifra hvilket fag man jobber i,
hvilken aldergruppe og hviklet nivå elevene er på, hva man ønsker å teste og
hvor mye tid man har til rådighet til å jobbe med prosjektet. I vårt
[lærerdokument](https://github.com/kodeklubben/oppgaver/wiki/Hvordan-undervise-i-og-vurdere-programmering){target=_blank} har vi blant
annet beskrevet ulike måter dette kan gjøres på, tillegg til en del andre
nyttige tips til hvordan man underviser i programmering.

## Forutsetninger og utstyr {.challenge}

- [ ] **Forutsetninger**:
Elevene har kodet litt micro:bit fra tidligere. 

- [ ] **Utstyr**:
- [ ] 2 micro:bit per rommannskap
- [ ] 2 batteripakker per rommanskap
- [ ] Papir / kartong - kanskje forskjellige farger?
- [ ] Fargeblyanter / tusjer
- [ ] Teip / lim
- [ ] Sakser
- [ ] Klistremerker?
- [ ] Glitter?
- [ ] Lærertyggis for å henge opp kreasjonene


## Fremgangsmåte


# Steg 1: Forberedelser {.activity}

- [ ] Klassen tegner ulike vesen og mystiske planter. Lag så mange dere har lyst, og vær kreativ med hvilke vesen og planter dere lager! 
- [ ] Disse klipper dere ut og leverer de ulike figurene til læreren.
- [ ]  Læreren gjemmer figurene rundt om i klasserommet - **klasserommet har nå blitt forvandlet til Kodars planet Timenor!**
![Bildebeskrivelse](./timenor.png)



# Steg 2: Programmer romstasjon-micro:bit'en {.activity}

I dette steget skal vi programmere vår "romstasjon-Micro:bit".  

- [ ] Gå inn på [https://makecode.microbit.org/](https://makecode.microbit.org/){:target=_blank} og opprett et nytt prosjekt. Kall prosjektet ROMSTASJON MICRO:BIT. 

Dette er Micro:biten som skal motta informasjonen romfarerne sender. 

- [ ]  Definer to variabler: `Planter`{.microbitvariables} og `Vesen`{.microbitvariables}
- [ ] Legg til en `Ved start`{.microbitbasic} -kloss
- [ ]  Sett `radio til gruppe`{.microbitradio} (...)  - **Her er det viktig at hver elev velger seg sin egen unike radiokanal, så man ikke blander seg med de andre romfarernes oppdrag!** 

- [ ] Vi skal også sende en beskjed til romfarerne, der vi spør "HVA FINNER DU?" når vi trykker på A-knappen på Micro:bit'en. 

- [ ] Når romstasjon-Micro:biten `mottar en beskjed`{.microbitradio} fra romfarerne  de sender via `radio`{.microbitradio}.skal vi `vise teksten`{.microbitbasic}  de har sendt. 
- [ ] Romstasjon-Micro:bit'en skal også vise antall `Planter`{.microbitvariables} og `Vesen`{.microbitvariables} romfarerne sender. 

```microbit
radio.onReceivedNumber(function (receivedNumber) {
    basic.showString("" + (receivedNumber))
})
input.onButtonPressed(Button.A, function () {
    radio.sendString("HVA FINNER DU?")
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
let Planter = 0
let Vesen = 0
radio.setGroup(1)

```
# Steg 3: Programmer astronaut-micro:bit'en til å kommunisere med romstasjonen {.activity}
 

Nå skal vi programmere micro:biten astronautene skal bruke for å registrere og kommunisere sine funn på Timenor til romstasjonen. 

- [ ] Opprett et nytt prosjekt og kall dette ASTRONAUT MICRO:BIT. 


- [ ] Legg til en `ved start`{.microbitbasic} - kloss. Denne kobles til to `variabelklosser`{.microbitvariables} der vi setter `Planter`{.microbitvariables} og `Vesen`{.microbitvariables} til `0`{.microbitvariables}. 

- [ ] Legg til en `radiokloss`{.microbitradio} som har lik `gruppe`{.microbitradio} som romstasjonen vår. 

 

- [ ] I forrige steg programmerte vi romstasjonen vår til å sende astronautene en beskjed - sørg for at Micro:bit'en `viser beskjeden`{.microbitbasic} som er sendt over `radio`{.microbitradio}. 

```microbit
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)

```
```microbit
let vesen = 0
let planter = 0

vesen = 0
radio.setGroup(1)
```

# Steg 4: Programmer astronaut-micro:bit'en til å registrere og sende data {.activity}
Nå skal vi programmere micro:bit'ens knapper til å telle funnene våre, og å sende informasjonen når vi er ferdig. For å registrere informasjonen vi samler inn, skal vi bruke knappene på micro:bit’en. 

Nærmere bestemt: A, B og A+B. 
Knappene skal telle antall planter og vesen astronautene finner på den mystiske planeten de utforsker, og sende informasjonen til romstasjonen ved endt oppdrag. 

- [ ] Bruk `inndata`{.microbitinput}-klosser til knapp `A`{.microbitinput} og `B`{.microbitinput} til å telle `Vesen`{.microbitvariables} og `Planter`{.microbitvariables}. Hvert trykk skal `endre antallet`{.microbitvariables} med 1. 

- [ ] For å sende dataen, bruker vi `inndata`{.microbitinput} for `A+B`{.microbitinput}. Vi skal `sende teksten`{.microbitradio} **"VI FANT VESEN"** og **"VI FANT PLANTER"**, og tallet på `antall Planter`{.microbitvariables} og `Vesen`{.microbitvariables}. Vi legger også inn en `pause`{.microbitbasic} på 2000 ms, så all infoen ikke kommer rett etter hverandre. 

```microbit
input.onButtonPressed(Button.A, function () {
    VESEN += 1
})
input.onButtonPressed(Button.B, function () {
    PLANTER += 1
})
input.onButtonPressed(Button.AB, function () {
    radio.sendString("VI FANT VESEN :")
    radio.sendNumber(vesen)
    basic.pause(2000)
    radio.sendString("VI FANT PLANTER : ")
    radio.sendNumber(PLANTER)
```

![Bildebeskrivelse](./microbitss.png)

## Test prosjektet {.flag}

**Last ned prosjektet for å teste koden.**

- [ ] Du skal se at det dukker opp en "HVA FINNER DU?"-beskjed på astronaut-micro:biten når du trykker på A på romstasjon-micro:biten 

- [ ] Nå kan du prøve å trykke på A og B noen ganger før du trykker på A+B samtidig på astronaut-micro:bit'en. Dukker det opp beskjeden "VI FANT VESEN :" "(TALL)" og "VI FANT PLANTER :" "(TALL)" på romstasjon-micro:bit'en? 

# Steg 5: Utforsk Timenor med ditt astronaut-crew!  {.activity}
Nå som dere er ferdige med å programmere begge micro:bitene er det klart for å utforske planeten! Let høyt og lavt etter liv på planeten, og registrer funnene deres med micro:biten før dere sender informasjonen til romstasjonen. 

Husk at A er Vesen og B er Planter! 

Lykke til modige romfarere! 

## Lagre spillet {.save}


Husk å lagre programmet ditt på Makecode.
