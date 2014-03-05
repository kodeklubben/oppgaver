---
title: Enarmet Banditt
level: 1.4
language: nb-NO
embeds: ["*.png"]
...

#Enarmet banditt

#Introduksjon { .intro}
Dette er et spill med tre figurer som endrer utseende. Spillerens oppgave er å stoppe figurene én etter én, slik at alle blir like. 

![skjermbilde](skjermbilde.png)



#Steg 1: Lag en figur som bytter drakt

##Sjekkliste { .check}
__La oss importere de bildene vi trenger for spillet::

+ __Start et nytt Scratch-prosjekt__. __Slett katten__ ved å høyreklikke og velge ´slett´.
+ Importer __en ny figur__. Velg den du vil.
+ Gå til Drakter, og importer __to ekstra drakter__, så figuren til sammen har tre drakter.

__Nå som figuren har noen drakter, ønsker vi at den skal veksle mellom dem.__

#Steg 2: Få figuren til å rullere

+ Klikk på ´skript´-fanen,
+ Velg ´hendelser´ og hent en ´´´Når grønt flagg klikkes´´´-blokk. Denne vil kjøre hver gang du klikker på det grønne flagget over scenen.
+ Legg til en ´for alltid´, slik at denne fester seg under den andre blokken.
+ __Klikk på det grønns flagget__. Du ser at du får en hvit linje rundt skriptet. Det betyr at skriptet kjører.
+ Velg nå ´Utseende´ og dra inn en ´Neste drakt´-blokk.
+ __Hvordan kan vi få draktbyttet til å gå saktere?__ Velg ´Styring´og dra inn en ´´´vent (1) sekunder´´´. 
+ Tilpass tiden til figuren endrer drakt i et hurtigere tempo (0.1 sekunder ser bra ut). Hva tror du ville skjedd om vi ikke hadde med vent-blokken?

´´´blocks

    Når grønt flagg klikkes
    for alltid
      neste drakt
      vent (0.1) sekunder
´´´

## Test Prosjektet { .test}
__Klikk det grønne flagget.__
Endrer figuren drakt i et fornufitg tempo? 

##Lagre Prosjektet { .save}

##Ting å prøve { .try}
Tilpass tiden i vent-blokken. Hvilke tall gjør spillet for vanskelig, eller for lett?

#Steg 3: Frys ruletten!



