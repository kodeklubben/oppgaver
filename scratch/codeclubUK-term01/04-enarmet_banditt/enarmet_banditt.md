---
title: Enarmet Banditt
level: 1.4
language: nb-NO
stylesheet: scratch
embeds: ["*.png", "../../bilder/*.png"]
...

# Introduksjon {.intro}
Dette er et spill med tre figurer som endrer utseende. Spillerens oppgave er å stoppe figurene én etter én, slik at alle blir like. 

![](skjermbilde.png)

# Steg 1: Lag en figur som bytter drakt {.activity}

*La oss importere de bildene vi trenger for spillet*

## Sjekkliste { .check}

+ __Start et nytt Scratch-prosjekt__. __Slett katten__ ved å høyreklikke og velge `slett`.
+ Importer __en ny figur__, ![Velg figur fra biblioteket](figur-fra-bibliotek.png). Velg den figuren du vil.
+ Gå til `Drakter`{.blocklightgrey}, og importer to ekstra drakter fra biblioteket, så figuren til sammen har tre drakter.

# Steg 2: Få figuren til å rullere {.activity}

*Nå som figuren har noen drakter, ønsker vi at den skal veksle mellom dem.*

## Sjekkliste { .check}

+ Klikk på `Skript`{.blocklightgrey}-fanen,
+ Velg `Hendelser`{.blockgrey} og hent en `Når grønt flagg klikkes`{.blockgrey}-blokk. Denne vil kjøre hver gang du klikker på det grønne flagget over scenen.
+ Hent en `for alltid`{.blockyellow}-blokk fra `Styring`{.blockyellow}-kategorien og legg den under den andre blokken slik at den fester seg til den.
+ __Klikk på det grønne flagget__. Du ser at du får en hvit linje rundt skriptet. Det betyr at skriptet kjører.
+ Velg nå `Utseende`{.blockpurple} og dra en `neste drakt`{.blockpurple}-blokk inn i `for alltid`{.blockyellow}-blokken.
+ __Hvordan kan vi få draktbyttet til å gå saktere?__ Velg `Styring`{.blockyellow} og dra inn en `vent (1) sekunder`{.blockyellow}-blokk. 
+ Tilpass tiden til figuren endrer drakt i et hurtigere tempo (0.5 sekunder ser bra ut). Hva tror du ville skjedd om vi ikke hadde med `vent`{.blockyellow}-blokken?

    ```blocks
        Når grønt flagg klikkes
        for alltid
            neste drakt
            vent (0.5) sekunder
    ```

## Test Prosjektet { .test}
__Klikk det grønne flagget.__

+ Endrer figuren drakt i et fornuftig tempo? 

## Ting å prøve { .try}
Tilpass tiden i `vent`{.blockyellow}-blokken. Hvilke tall gjør spillet for vanskelig eller for lett?

# Steg 3: Frys ruletten! {.activity}




