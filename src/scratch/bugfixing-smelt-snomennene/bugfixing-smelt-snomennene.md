---
title: "Bugfixing: Smelt snømennene!"
author: "[c4creativity](https://scratch.mit.edu/users/c4creativity)"
translator: "Carl A. Myrland"
language: "nb"
---


# Introduksjon {.intro}

I denne oppgaven skal du forsøke å reparere og forbedre koden som allerede er laget i et program i Scratch. Målet er å få de tre snømennene til å snakke i tur og orden, for så å smelte bort samtidig!

![Bildebeskrivelse](bugfix1.jpg)


# Steg 1: Remiks {.activity}

Først må vi åpne et eksisterende prosjekt og lage en remiks av det. Les gjennom hele sjekklisten før du trykker på lenken!

## Sjekkliste {.check}

- [ ] Åpne prosjektet: [Bugfixing: Smelt snømennene!](https://scratch.mit.edu/projects/445564165/ ){target=_blank}
- [ ] Trykk på "Remix"-knappen
- [ ] Gi gjerne prosjektet et nytt navn som gjør det lett å kjenne igjen

## Test prosjektet {.flag}

**Start prosjektet for å teste koden så langt.**

Besvar gjerne disse spørsmålene i en notatblokk, diskuter dem med en medelev eller to, og forsøk å svare så presist som du kan.

- [ ] Hva skjer når du trykker på det grønne flagget?

- [ ] Målet er at snømennene skal si "Klar, ferdig, smelt!" i tur og orden, der hver snømann kun sier ett ord. Hvordan kan du få til det?

- [ ] Les koden til de tre ulike figurene. Finner du noen spor eller hint i koden som gir deg en idé til hvilke endringer som må gjøres?

## Sjekkliste {.check}

Noen tips du kan bruke:

- [ ] Alle figurene har klossen

```blocks
si [klar] i (2) sekunder
```
- [ ] Figuren "Snømann 1" har i tillegg klossen

```blocks
vent (1) sekunder
```

hektet på under `si`{.blocklooks}-klossen.
- [ ] Hva skjer om du flytter `vent`{.blockcontrol}-klossen over `si`{.blocklooks}-klossen og endrer ventetiden til for eksempel 3 sekunder i stedet for 1?

## Test prosjektet {.flag}

**Klikk på det grønne flagget.**

- [ ] Test den nye koden din. Hva skjer nå? Noter ned det du observerer, eller diskuter med en medelev.
- [ ] Snakker de tre snømennene samtidig nå?


# Steg 2: Klar, ferdig, smelt! {.activity}

Basert på det vi oppdaget på steg 1, er vi nå klare for å løse den første bug-en i koden vår: Snømennene skal si "Klar", "Ferdig", "Smelt!" i tur og orden.

## Sjekkliste {.check}

- [ ] Snømann 1 skal si "Klar" i det du trykker på grønt flagg.

- [ ] Snømann 2 skal si "Ferdig" etter at snømann 1 har sagt "Klar"

- [ ] Snømann 3 skal si "Smelt!" etter at snømann 2 har sagt "Ferdig"

Du trenger å sette inn klossen `vent`{.blockcontrol} hos Snømann 2 og 3, og legge den inn over `si`{.blocklooks}-klossen, slik:

```blocks
vent (1) sekunder
si [Ferdig] i (2) sekunder
```
- [ ] Fjern `vent`{.blockcontrol}-klossen hos Snømann 1

- [ ] Hvor lenge må Snømann 2 og Snømann 3 vente før de får si ordet sitt?

## Test prosjektet {.flag}

**Klikk på det grønne flagget for å teste koden så langt.**

Besvar spørsmålene i en notatblokk eller diskuter dem med en medelev.

- [ ] Sier de tre snømennene "Klar, ferdig, smelt!" i tur og orden nå?

- [ ] Forsvinner de etter at sistemann har sagt "smelt!"?

- [ ] Finner du spor i koden som gir et hint om hva du må gjøre videre?

## {.tip}
Det kan være tungvint å lage lignende algoritmer til hver enkelt figur i Scratch. Derfor er det smart å gjøre koden mer eller mindre ferdig i én figur først, og så kopiere koden over til de andre figurene. Bare dra den algoritmen du vil kopiere bort til figuroversikten under scena, og slipp den over den figuren du vil kopiere til. Da trenger du bare å gjøre noen små justeringer på koden, i stedet for å skrive den på nytt for hver figur.
#

# Steg 3: Smelt! {.activity}

Nå som vi har fått snømennene til å snakke i tur og orden, er det på tide å fikse smelte-koden.

Snømann 1 har et viktig hint til oss:

```blocks
gjenta (2) ganger
endre [ghost v] effekt med (25)
vent (1) sekunder
endre størrelse med (-10)
```

`ghost`{.blocklooks}-effekten bidrar til å gjøre en figur mer og mer usynlig, på en skala fra 0 (helt synlig) til 100 (helt usynlig). I tillegg vil vi at snømannen skal bli litt mindre for hver gang, for å vise at den "smelter" bort. Derfor bruker vi `endre størrelse`{.blocklooks} også.

## Sjekkliste {.check}
- [ ] Endre koden slik at `ghost`{.blocklooks}-effekten til slutt blir 100 når løkka er ferdig med å kjøre. Ghost-verdien starter på 0 når grønt flagg klikkes. Hvor mange ganger må løkka gjentas dersom vi lar ghost-effekten endres med 25 for hver gang?
- [ ] Kan du justere på forholdet mellom antall `gjentakelser`{.blockevents}, `ghost`{.blocklooks}-effekten og `vent`{.blockcontrol}-tiden for å få en smidigere animasjon av smeltingen?

## Test prosjektet {.flag}
Noter svarene i en notatblokk eller diskuter med en medelev.

- [ ] Smelter Snømann 1 helt bort?

- [ ] Ser smelteanimasjonen grei ut? Går den passe fort, og med jevnt tempo helt til snømannen er borte?

- [ ] Hva er det som ikke fungerer som det skal hittil?
#

# Steg 4: Siste justeringer {.activity}
Når du har kommet så langt i oppgaven, skal de tre snømennene si "Klar, ferdig, smelt!" i tur og orden, og snømann 1 smelter helt bort. Men vi er ikke helt i mål enda. Oppgaven er at de tre snømennene skal smelte samtidig *etter* at de har sagt "Klar, ferdig, smelt!" - og der er vi ikke helt i mål enda.

## Sjekkliste {.check}
- [ ] Kopier `gjenta`{.blockcontrol}-løkka over til Snømann 2 og 3.
- [ ] Du ser at Snømann 2 har en algoritme som skal starte `Når denne figuren klikkes`{.blockevents}. Du kan slette hele den algoritmen nå.
- [ ] For å sørge for at alle snømennene smelter samtidig, må du legge til en `vent`{.blockcontrol}-kloss over `gjenta`{.blockcontrol}-løkka til hver enkelt snømann. Snømann 1 må vente lengre enn de to andre før han starter på `gjenta`{.blockcontrol}-løkka, men hvor lenge må han vente?
- [ ] Et hint er at han må vente helt til Snømann 3 har sagt "Smelt!"
- [ ] Til slutt rydder vi opp ved å legge `Sett størrelse`{.blocklooks}-klossen øverst i `Når grønt flagg klikkes`{.blockevents}-algoritmen på alle figurene, sletter eventuelt ubrukte klosser og ser over en siste gang for å sjekke at koden er i orden på alle de tre snømennene.

## Test prosjektet {.flag}
- [ ] Sier de tre snømennene hvert sitt ord i tur og orden?

- [ ] Smelter de bort samtidig og blir helt borte?

- [ ] Blir alle tre snømennene like store og synlige igjen hver gang du trykker på grønt flagg?


Hvis svaret på hvert av de tre spørsmålene er "Ja": Gratulerer, du har klart å fikse alle bugs-ene i koden!

Her er et forslag til hvordan koden til Snømann 1 kan se ut når du er ferdig:

```blocks
Når grønt flagg klikkes
sett størrelse til [100]%
si [Klar] i (2) sekunder
vent (4) sekunder
gjenta (4) ganger
endre [ghost v] effekt med (25)
vent (1) sekunder
endre størrelse med (-10)
```

## Utfordring {.challenge}

Animasjonene og funksjonaliteten i dette lille programmet er jo ganske enkle.

Her er noen tips til ting du kan prøve for å gi programmet litt mer kompleksitet:
- [ ] Lag en algoritme som får snømennene til å gå frem og tilbake på skjermen mens de snakker.

- [ ] Bytt ut "klar, ferdig, smelt!" med en dialog der snømennene for eksempel snakker sammen om hvor varmt det begynner å bli

- [ ] Få snømennene til å si "Hjelp, jeg smelter!" når ghost-effekten begynner.

Lykke til!
#

Når du er ferdig kan du klikke på "Legg ut"-knappen. Da vil det bli lagt ut på Scratch-hjemmesiden din slik at du enkelt
kan dele det med familien og vennene dine.
