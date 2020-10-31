---
title: "Smitte:Bit"
author: "Sigurd Schaathun" 
language: "nb"
---


# Om oppgaven {.activity}

I denne oppgaven skal vi lære om radioblokkene og bruke det for å simulere smitte. Oppgaven er laget i forbindelse med COVID-19 for å vise hvor fort smitte kan bre seg og hvordan vi kan simulere dette ved programmering. Første steg er pararbeid, mens det siste er for alle i klassen samtidig.

## Oppgaven passer til: {.check}

 **Fag**: Matematikk, naturfag, samfunnsfag og KRLE

**Anbefalte trinn**: 5. - 10. + videregående

**Tema**: Smittsomme sykdommer, simulering, programmering

**Tidsbruk**: 45- 90 minutter

## Kompetansemål {.challenge}

- [ ] **Naturfag, 7. trinn**: bruke og vurdere modeller som representerer fenomener man ikke kan observere direkte, og gjøre rede for hvorfor det brukes modeller i naturfag

- [ ] **Naturfag, 7. trinn**: utforske, lage og programmere teknologiske systemer som består av deler som virker sammen

- [ ] **Naturfag, 10. trinn**: bruke og lage modeller for å forutsi eller beskrive naturfaglige prosesser og systemer og gjøre rede for modellenes styrker og begrensinger

- [ ] **Naturfag, 10. trinn**: utforske, forstå og lage teknologiske systemer som består av en sender og en mottaker
bruke programmering til å utforske naturfaglige fenomener


- [ ] **Matematikk, 5. trinn**: lage og programmere algoritmar med bruk av variablar, vilkår og lykkjer

- [ ] **KRLE, 7. trinn**: utforske og beskrive egne og andres perspektiver i etiske dilemmaer knyttet til hverdags- og samfunnsutfordringer

- [ ] **KRLE, 7. trinn**: reflektere over eksistensielle spørsmål knyttet til menneskets levesett og levekår og klodens framtid

- [ ] **KRLE, 10. trinn**: reflektere over eksistensielle spørsmål knyttet til det å vokse opp og leve i et mangfoldig og globalt samfunn

- [ ] **KRLE, 10. trinn**: identifisere og drøfte etiske problemstillinger knyttet til ulike former for kommunikasjon

- [ ] **KRLE, 10. trinn**: identifisere og drøfte aktuelle etiske problemstillinger knyttet til menneskerettigheter, urfolks rettigheter, bærekraft og fattigdom



## Forslag til læringsmål {.challenge}

- [ ] Elevene kan forklare hva simulering er og simulerer hvordan smitte kan bre seg ved programmering på Micro:bit.

## Forslag til vurderingskriterier {.challenge}

Det er mange ulike måter man kan vurdere et programmeringsprosjekt, og her må en
selv vurdere hva som er den beste måten ut ifra hvilket fag man jobber i,
hvilken aldergruppe og hviklet nivå elevene er på, hva man ønsker å teste og
hvor mye tid man har til rådighet til å jobbe med prosjektet. I vårt
[lærerdokument](https://github.com/kodeklubben/oppgaver/wiki/Hvordan-undervise-i-og-vurdere-programmering){target=_blank} har vi blant
annet beskrevet ulike måter dette kan gjøres på, tillegg til en del andre
nyttige tips til hvordan man underviser i programmering.

## Forutsetninger og utstyr {.challenge}

- [ ] **Forutsetninger**: Elevene bør ha programmert noe på micro:bit før.

- [ ] **Utstyr**: En micro:bit per elev, datamaskiner til å programmere

## Fremgangsmåte

Her kommer tips, erfaring og utfordringer til de ulike stegene i den faktiske
oppgaven. 

# Steg 1: Radiokommunikasjon {.activity}

- [ ] Her jobber elevene i par.

- [ ] Her må lærer/instruktør tildele radiogrupper til hvert par. Radiogrupper bestemmer hvilke micro:bit som skal kommunisere med hverandre. Det er 256 grupper, nummerert fra 0 til 255. 

- [ ] Hvis man vil redusere rekkevidden av smitte ytterligere, kan man bruke `mottok pakke signalstyrke`{.microbitradio} i en `hvis`{.microbitlogic}-løkke. Et svakt signal gir verdien -128, og et sterkt gir -42. Dette krever litt ekstra forskning for de sterkeste elevene.

# Steg 2: Smittespredning{.activity}

- [ ] Her er mesteparten av programmeringen. Pass på rekkefølgen i `hvis - eller`{.microbitlogic}-løkken. Med vilje står vilkårene i "feil" rekkefølge i teksten, med en forklaring i tipsruten. Hvis løkken først tester på >25, vil den gjøre det, selv om verdien er større enn 50 og vilkåret dermed er oppfyllt. Derfor må den teste med det største først. 

- [ ] Det er bare en micro:bit som vil vise X, siden den slutter å sende smitte når den gjør det.

# Steg 3: Prøve med hele gruppen {.activity}

- [ ] Her må du tildele ny radiogruppe til alle.

- [ ] Du trenger en micro:bit som kan starte smitten. Den letteste måten er å ha programmert en ferdig der `smitte`{.microbitvariables} er satt til 30.

- [ ] Det er lurt å starte forsøket på likt: Alle trykker på reset.

- [ ] Når forsøket er ferdig er det viktig å snakke om resultatene og hvorfor. Husk at dette er en simulering som er sterkt forenklet og egentlig bare måler luftsmitte.

- [ ] Aluminiumsfolie rundt micro:biten vil fungere som et __Faradays bur__ og blokkere radiosignaler.

## Variasjoner {.challenge}

- [ ]  Elevene kan legge inn ulike smittetiltak og ekstra smitting som er nevnt i slutten av elevdokumentet. 

- [ ] Radiokommunikasjonen kan også brukes hvis man skal få en micro:bit til å gjøre noe når andre er i nærheten.
 

## Eksterne ressurser {.challenge}

- [ ] Ferdig program på makecode.microbit.org: [https://makecode.microbit.org/_TxkHFz8D2MwE](https://makecode.microbit.org/_TxkHFz8D2MwE){target=_blank}