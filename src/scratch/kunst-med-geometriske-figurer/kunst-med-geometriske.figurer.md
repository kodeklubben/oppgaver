---
title: Kunst med geometriske figurer
author: Carl Andreas Myrland
language: nb
---

# Introduksjon {.intro}

I denne oppgaven skal vi lære oss å lage stilige kunstverk ved hjelp av geometriske figurer, tilfeldighet og funksjoner.

![Bildebeskrivelse](./scratchopplegg.png)

# Steg 1: Vi gjør klar blyanten {.activity}

Først setter vi opp de "kjedelige" tingene for å få programmet til å fungere som det skal senere.

## Sjekkliste {.check}

- [ ] Slett kattefiguren

- [ ] Sett inn figuren `Pencil`

- [ ] Bytt til "Drakter"-fanen, og flytt blyanten slik at blyantspissen peker på senterpunktet.

- [ ] Bytt tilbake til "Kode"-fanen.

- [ ] Legg til Penn-biblioteket ved å trykke på det blå "+"-ikonet nederst i vesntre hjørne på skjermen og velg "Penn"

- [ ] Hent blokken `når grønt flagg klikkes`{.blockevents} og `send melding [melding1]`{.blockevents} og sett disse sammen.

- [ ] Trykk på den lille hvite pilen ved siden av "melding1", velg "ny melding" og gi den navnet "klar":

```blocks
Når grønt flagg klikkes
send melding [klar v]
```

- [ ] Nå skal vi lage en ny sekvens som gjør figuren vår klar til å tegne:

```blocks
Når jeg mottar [klar v]
begrens rotasjon [ikke roter v]
skjul
penn av
slett alt
vis
send melding [ferdig v]
```

- [ ] Til slutt i dette steget lager vi en liten sekvens som sier at figuren skal følge musepekeren eller fingeren vår når vi flytter den over skjermen:

```blocks
Når jeg mottar [ferdig v]
gjenta for alltid
gå til [musepeker v]
```

## Test prosjektet {.flag}

**Klikk på det grønne flagget.**

- [ ] Nå skal du se at figuren vår følger etter musepekeren eller fingeren din når du flytter den over scena.

- [ ] Forstår du hvorfor dette skjer?

# Steg 2: Lag kunst! (PC){.activity}

#

## PC eller nettbrett?{.protip}

I dette steget finner du instruksjoner for både enheter med ekstern mus og enheter med berøringsskjerm. Pass på at du velger riktig instruksjon til enheten du skal bruke, feks iPad eller PC

#

Nå skal vi sette sammen koden som lar oss tegne geometriske figurer! Vi begynner med en enkel variant, og så gjør vi koden mer avansert i steg 3.

## Instruksjoner for PC: {.check}

- [ ] Hopp over dette steget om du bruker en enhet med berøringsskjerm, som iPad eller lignende.

- [ ] Vi vil at figuren skal begynne å tegne når vi trykker med venstre musetast. Derfor setter vi opp denne sekvensen:

```blocks
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

## Test prosjektet - for PC{.flag}

**Klikk på det grønne flagget.**

- [ ] Trykk et tilfeldig sted på scena. Ser du et kvadrat? Forsøk å trykke flere steder etter hverandre. Hva skjer?

- [ ] Nå får vi riktignok bare tegnet én type figur. Forstår du hvorfor? I neste avsnitt skal vi lære å lage flere figurer!

#

# Steg 2: Lag kunst! (nettbrett){.activity}

#

## Instruksjoner for nettbrett {.check}

Siden berøringsenheter som iPad ikke har musepeker, må vi lage en litt annen løsning.

- [ ] Dersom du har en PC/Mac med mus, kan du gå videre til Steg 3.

- [ ] Først må vi lage oss en knapp vi kan trykke på. Sett inn en ny figur fra galleriet, for eksempel `Button1`, og skriv denne koden:

```blocks
Når grønt flagg klikkes
gå til x: (180) y: (-150)

Når denne figuren klikkes
send melding [start v]
```

- [ ] Bytt tilbake til Blyant-figuren og skriv denne koden:

```blocks
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

## Test prosjektet - for nettbrett {.flag}

**Klikk på det grønne flagget.**

- [ ] trykk et tilfeldig sted på scena

- [ ] trykk på knappen vi satte inn

- [ ] Dukker det opp en figur der du trykket?

- [ ] Trykk flere steder på skjermen, etterfulgt av et trykk på knappen. Hva skjer?

- [ ] Nå får vi riktignok bare tegnet én type figur. Forstår du hvorfor? I neste avsnitt skal vi lære å lage flere figurer!

#

#

# Steg 3: Flere geometriske figurer {.activity}

I dette steget skal vi lære hvordan vi kan lage både trekanter, firkanter og femkanter til kunstverket vårt.

**OBS! I dette steget trenger du ikke legge til nye kodeblokker. Vi skal kun endre på verdiene til noen av blokkene vi allerede har!**

## Vi lager flere geometriske figurer {.check}

- [ ] Hemmeligheten bak å lage ulike geometriske figurer ligger i denne lille sekvensen fra Steg 2:

```blocks
gjenta (4) ganger
gå (100) steg
vend høyre (90) grader
end
```

- [ ] Nøkkelen er _forholdet_ mellom antall ganger `gjenta`{.blockcontrol}-løkken kjøres, og hvor mange grader figuren skal snu.

#

## Vinkelsummer{.protip}

Du vet kanskje at ulike figurer har ulike vinkelsummer. I matematikken lærer vi at en trekant har vinkelsum 180 grader, firkanter 360 grader, femkanter 540 grader, osv.

Dette er riktig dersom man måler innvendige vinkler i figuren. Men for at dette skal bli riktig på en datamaskin, må vi forholde oss til utsiden av vinklene, altså nabovinkelen til de vi vanligvis måler i matematikken.

Du vet kanskje at summen av to nabovinkler alltid er 180 grader. Det betyr at når vi sier at alle vinklene i en likesidet trekant er 60 grader, må vi bruke nabovinkelen 120 grader når vi skal be datamaskinen tegne en likesidet trekant. For en rettvinklet firkant blir nabovinkelen uansett 90 grader. For en femkant er nabovinkelen 72 grader, osv.

Når vi beregner utvendige vinkler på regulære geometriske figurer, blir vinkelsummen alltid 360 grader! Forstår du hvorfor?

#

- [ ] Målet er at produktet av antall repetisjoner multiplisert med antall grader, skal bli 360 grader. Da kan vi tenke oss at antall repetisjoner (`gjenta (3) ganger`{.blockcontrol}) forteller oss hvor mange kanter figuren vår får, mens antall `grader`{.blockmotion} må justeres slik at produktet blir 360 grader. `gå () steg`{.blockmotion} angir kun hvor lange sidene i figuren blir:

```blocks
gjenta (3) ganger
gå (100) steg
vend høyre (120) grader
end
```

## Hvordan finne utvendig vinkel raskt{.protip}

Trenger du å finne ut hvor stor den utvendige vinkelen må være for en gitt mangekant, finner du det ved å dele 360 på antall sider i figuren:

360 : 3 = 120
360 : 4 = 90
360 : 5 = 72

osv.

#

## Test prosjektet {.flag}

**Klikk på det grønne flagget.**

- [ ] Endre verdiene i koden din, slik at du kan tegne trekanter og femkanter.

- [ ] Kjør koden, og se hva som skjer nå!

- [ ] Forstår du hvorfor dette skjer?

# Steg 4: Funksjoner og variabler {.activity}

Nå som vi har fungerende kode som lar oss tegne ulike figurer, kan vi se på hvordan vi kan rydde litt i koden for å gjøre den enda litt bedre, og spare oss for jobb senere! Dette gjør vi ved å først lage en `funksjon`{.blockmoreblocks} som automatiserer en del av jobben for oss. I Scratch kalles `funksjoner`{.blockmoreblocks} "`Mine klosser`{.blockmoreblocks}", så vi finner den første klossen vi trenger der.

## Lag en funksjon {.check}

#

- [ ] Gå til kategorien `Mine klosser`{.blockmoreblocks}, og trykk "Lag en kloss".

- [ ] Her får du opp en meny som lar deg bestemme hva funksjonen skal hete, og hvilke _parametre_ den skal ha.
- [ ] Vi kaller klossen "mangekant" og legger til to felt for "tall eller tekst".
- [ ] Det første feltet kaller vi "kanter", det andre kaller vi "sidelengde".
- [ ] Når du er ferdig, får du en ny kloss på arbeidsflaten din, og en ny kloss under `Mine klosser`{.blockmoreblocks}:

```blocks
definer mangekant (kanter) (sidelengde)

mangekant (kanter) (sidelengde)

```

## Vi endrer koden vår {.check}

**Dette steget kan være litt vanskelig. Sørg for å ha tunga rett i munnen, og les instruksjonene nøye.**
Vi skal nå bygge om koden vår, slik at vi enkelt kan bytte mellom tre-, fire- og femkanter, hele veien opp til sirkler, uten å måtte regne ut vinkler på egenhånd!

- [ ] Først skal vi definere funksjonen vår. De rosa variablene (kanter) og (sidelengde) hentes rett ut fra defineringsblokken øverst, og settes inn i koden som vanlige variabler:

```blocks
definer mangekant (kanter) (sidelengde)
gjenta (kanter) ganger
gå (sidelengde) steg
vend høyre ((180) -  ((((kanter) - (2)) * (180)) / (kanter))) grader
end

mangekant (kanter) (sidelengde)

```

- [ ] Nå skal vi endre på sekvensen som starter `Når denne figuren klikkes`{.blockevents} om man bruker mus, eller `Når jeg mottar start`{.blockevents} om man bruker berøringsskjerm, slik at vi bruker `mangekant`{.blockmoreblocks}-funksjonen i stedet.

## Viktig info {.protip}

Koden for mus og berøringsskjerm er lik herfra og ut, den eneste forskjellen er hendelsen som starter skriptet som lager tegningen. For mus er det `Når denne figuren klikkes`{.blockevents}, for berøringsskjerm er det `Når jeg mottar [start]`{.blockevents}

#

- [ ] Først må vi fjerne `gjenta`{.blockcontrol}-løkken fra sekvensen, slik at vi sitter igjen med

```blocks
Når denne figuren klikkes
stopp [andre skript i figuren v]
penn på
pek i retning (90)
penn av
send melding [ferdig v]

```

- [ ] Så setter vi inn `mangekant`{.blockmoreblocks}-blokken der gjenta-løkka var:

```blocks
Når denne figuren klikkes
stopp [andre skript i figuren v]
penn på
pek i retning (90)
mangekant () ()
penn av
send melding [ferdig v]

```

#### Feil farge på klossene? {.protip}

`Mangekant`{.blockmoreblocks}-blokken vises med rød farge i koden over, men det er av tekniske årsaker i verktøyet vi skriver oppgaven med. Du kan se bort fra feil farger på klossene i denne delen av oppgaven.

#

Du kan nå fylle inn hvor mange kanter du vil at figuren skal ha, og hvor lange de skal være i funksjonsblokken

- [ ] Hvis vi vil tegne en sekskant med 40 piksler lange sider, fyller vi inn:

```blocks
mangekant (6) (40)
```

## Test koden din {.flag}

- [ ] Fyll inn hvor mange kanter du vil at figuren din skal ha, og hvor lange sidene skal være

- [ ] Trykk på grønt flagg

- [ ] Hvis du bruker mus, trykk et sted på scena der du vil at figuren skal tegnes.

- [ ] Hva skjer om du endrer på verdiene i `mangekant`{.blockmoreblocks}?

- [ ] Forstår du hva som skjer?

#

## Den magiske formelen {.challenge}

Denne formelen er det "magiske" elementet i koden vår:

```blocks
vend høyre ((180) -  ((((kanter) - (2)) * (180)) / (kanter))) grader
```

Denne utregningen finner nemlig vinkelen i en regulær mangekant, kun ved å vite hvor mange kanter figuren består av. Sett inn hvor mange kanter figuren din skal ha (3 for trekant, 4 for firkant, osv) i `kanter`{.blockdata}-variabelen, og regn ut, så finner du alltid riktig vinkel.

Klarer du å finne ut hvorfor det blir slik?

#

# Steg 5: Litt mer farge og liv! {.activity}

#

Vi har nå laget et program som lar deg lage mange forskjellige kunstverk ved hjelp av geometriske figurer, men figurene har kanskje litt kjedelige farger?

- [ ] Ved å sette inn

```blocks
sett pennbredde til ()
```

og

```blocks
sett pennens (farge v) til ()
```

etter `penn på`{.blockpen}-klossen, kan du endre på både strekens bredde og farge. Prøv deg frem!

- [ ] Du kan også eksperimentere med klossene

```blocks
endre pennens (farge v) med ()
```

og

```blocks
endre pennens bredde med ()
```

og se hva som skjer da!

- [ ] For å gjøre kunsten enda mer variert, kan du også eksperimentere med å sette inn klossen

```blocks
tilfeldig tall fra () til ()
```

fra `operatorer`{.blockoperators}-kategorien. `Tilfeldig tall`{.blockoperators}-klossen kan settes inn i `pek i retning`{.blockmotion}-klossen, i `mangekant`{.blockmoreblocks}-klossen, og i de ulike `penn`{.blockpen}-klossene for å endre farge og bredde.

#

## Gjør programmet enda enklere å bruke! {.protip}

For å gjøre programmet enda mer brukervennlig, kan du lage to variabler. La oss kalle dem `sideAntall`{.blockdata} og `sideLengde`{.blockdata}. Sett inn variablene i `mangekant ( ) ( )`{.blockmoreblocks}-klossen. Variablene vil også vises på scena. Trykk og hold på hver av variabel-boblene, slik at du får opp en meny. I denne menyen velger du "skyveknapp". Da kan du enkelt endre på hva slags type mangekant du vil ha, og hvor lange sidene skal være, ved å dra skyveknappen til høyre eller venstre. I menyen kan du også velge å endre verdiområdet for variabelen, sånn at sideAntall begrenses mellom 3 og 20, og sideLengde begrenses mellom 10 og 100, for eksempel.

## Lagre programmet {.save}

Husk å gi programmet ditt et navn, sånn at du lett finner det igjen senere. Når du er ferdig kan du klikke på "Legg
ut"-knappen. Da vil det bli lagt ut på Scratch-hjemmesiden din slik at du enkelt
kan dele det med familien og vennene dine.
