---
title: Gongemeisteren
level: 2
author: 'Geir Arne Hjelle'
translator: 'Gro Anette Vestre'
language: nn
---

# Introduksjon {.intro}

I dag skal me laga eit nyttig spel, nemleg eit spel som vil hjelpa oss å læra andre ting. Me skal få hjelp til å læra gongetabellen!

![](gangemesteren.png)

# Steg 1: Læremeisteren {.activity}

Me skal etterkvart laga eit spel der me får tilfeldige spørsmål frå gongetabellen. Etter at me svarar får me vita om me klarte å svara rett, og me vil også få litt hjelp frå teikningar på skjermen. Men først introduserer me `Læremeister` som skal hjelpa oss med gongetabellen.

## Sjekkliste {.check}

- [ ] Start eit nytt prosjekt og slett kattefiguren.

- [ ] Legg til ein ny figur ved å klikke på ![Velg figur frå biblioteket](../bilder/hent-fra-bibliotek.png). Velg ein av _Wizard_-figurane mest heilt nederst i `Menneske`-kategorien. Kall figuren `Læreimester`.

- [ ] Me skal nå bruka `tilfeldig tal`{.blockoperators}-klossar slik at `Læremeister` kan spørje oss om tilfeldige gongestykker. Skriv dette skriptet:

    ```blocks
    når grønt flagg klikkes
    si (tilfeldig tall fra (2) til (10)) i (2) sekunder
    si [gonger] i (2) sekunder
    si (tilfeldig tall fra (2) til (10)) i (2) sekunder
    ```

## Test prosjektet {.flag}

__Klikk på det grøne flaget.__

- [ ] Spør `Læreimester` deg om eit gongestykke?

- [ ] Me skal etterkvart sjå korleis me kan få `Læreimesteren` til å sei heile teksten, i staden for berre eit ord om gongen.

- [ ] Foreløpig kan du ikkje svara `Læremeister` (iallfall ikkje med datamaskinen, prøv gjerne å rekna ut svaret og sei det til dei som set ved sida av deg).

# Steg 2: Datamaskinen er ein kalkulator {.activity}

Du har kanskje ikkje tenkt på det, men datamaskinen er ein veldig flink kalkulator. Det engelske ordet _computer_ betyr til og med
_reknemaskin_. Me skal nå sjå på korleis me får Scratch til å gonge saman tal.

## Sjekkliste {.check}

- [ ] For å få Scratch til å rekne brukar me `Operatorer`{.blockoperators}-klossar. Prøv for eksempel å dra gongeklossen - med `*`{.blockoperators}-teiknet - til skriptområdet på høyresida. Skriv inn to tal og klikk på klossen. Scratch reknar då ut svaret på gongestykket.

    ![](gangeoperator.png)

- [ ] Me vil nå kombinera gongeklossen med `tilfeldig tal`{.blockoperators}-klossen, men for å få dette til treng me ein  måte å hugse dei tilfeldige tala: **Variabler**.  Gå til `Data`{.blockdata}-kategorien og lag tre nye variabler: `tal1`{.blockdata}, `tal2`{.blockdata}, og `riktig svar`{.blockdata}. La dei gjelde for alle figurar.

- [ ] Skriv nå eit **heilt nytt skript** (la det ligge ved sida av det skriptet du skreiv i forrige steg).

    ```blocks
    når jeg mottar [Nytt spørsmål v]
    sett [tal1 v] til (tilfeldig tall fra (2) til (10))
    sett [tal2 v] til (tilfeldig tall fra (2) til (10))
    sett [rett svar v] til ((tal1) * (tal2))
    ```

- [ ] Prøv å klikka på skriptet for å testa det (sidan det ikkje startar med eit grønt flag kan me ikkje testa det på den vanlige måten). Om du ser på variablane på scenen skal dei endre seg kvar gong du klikkar på skriptet. Er `rett svar`{.blockdata} rett?

    ![](variabler.png)

# Steg 3: Eit skikkeleg spørsmål {.activity}

La oss sjå om me kan setje saman desse tala til eit skikkeleg spørsmål.

## Sjekkliste {.check}

- [ ] Lag ein ny variabel, `spørsmål`{.blockdata}. Også denne skal gjelde for alle figurar.

- [ ] Klossen `sett sammen`{.blockoperators} kan brukast for å setje saman fleire tal og ord. Me skal nå bruka to `sett sammen`{.blockoperators}-klossar på denne måten:

    ```blocks
    sett sammen (sett sammen [] []) []
    ```

    Dette gir oss plass til tre tal eller ord. Her kan me putta inn `tal1`{.blockdata}, teksten ` gonger ` og `tal2`{.blockdata}. Pass på at du har mellomrom før og etter `gonger`, det ser best ut da. Om du klikkar på den første `sett sammen`{.blockoperators}-klossen vil du sjå korleis den ferdige teksten blir.

    ![](sett_sammen.png)

- [ ] Legg denne klossen til nedst i `Nytt spørsmål`-skriptet:

    ```blocks
    når jeg mottar [Nytt spørsmål v]
    sett [tal1 v] til (tilfeldig tall fra (2) til (10))
    sett [tal2 v] til (tilfeldig tall fra (2) til (10)
    sett [rett svar v] til ((tal1) * (tal2))
    sett [spørsmål v] til (sett sammen (sett sammen (tal1) [ gonger ]) (tal2))
    ```

- [ ] Nå skal me få `Læremeisteren` til å stilla oss spørsmålet me har sett saman. **Bytt ut** det første skriptet (med det grøne flaget) du skreiv med dette:

    ```blocks
    når grønt flagg klikkes
    send melding [Nytt spørsmål v] og vent
    spør (spørsmål) og vent
    ```

## Test prosjektet {.flag}

__Klikk på det grøne flaget.__

- [ ] Stiller `Læremeister` deg eit skikkeleg spørsmål, for eksempel `9 gonger 6`?

- [ ] Er spørsmåla forskjellige kvar gong?

- [ ] Om du vil ha ein liten utfordring kan du prøva å bruka fleire `sett sammen`{.blockoperators}-klossar slik at spørsmålet blir for eksempel `Kva er 9 gonger 6?`.

# Steg 4: Er svaret rett då? {.activity}

Nå som me kan svara på spørsmål vil me og vite om me svarar rett.

## Sjekkliste {.check}

- [ ] Du ser kanskje at `rett svar`{.blockdata} vises på scenen? Då blir det jo ikkje særleg vanskeleg! Ta bort alle variablane frå scenen ved å gå til `Data`-kategorien og fjern haka framfor kvar variabel.

- [ ] Nå skal me bruka ein `hvis ellers`{.blockcontrol}-kloss for å gjera forskjellige ting ettersom du svarar rett eller feil på gongestykka. **Utvid** det eine skriptet ditt på denne måten:

    ```blocks
    når grønt flagg klikkes
    send melding [Nytt spørsmål v] og vent
    spør (spørsmål) og vent
    hvis ((svar) = (riktig svar))
        si [Ja, så flink du er!] i (2) sekunder
    ellers
        si [Nei, det ble visst feil.] i (2) sekunder
    slutt
    ```

    Klossen `svar`{.blocksensing} huskar svaret du skriv når `Læremeister` spør om gongestykket.

## Test prosjektet {.flag}

__Klikk på det grøne flaget.__

- [ ] Kva skjer om du svarer rett?

- [ ] Klikk det grøne flaget igjen for å få ei ny oppgåve. Kva skjer om du ikkje svarar rett?

# Steg 5: Fleire gongestykke {.activity}
I staden for å måtte trykke det grøne flaget heile tida, kan me be `Læremeister` om å stille oss fleire spørsmål!

## Sjekkliste {.check}

- [ ] Me brukar først ein `gjenta`{.blockcontrol}-kloss slik at me kan få fleire oppgåver. Legg merke til at me og sender ein `Nytt spørsmål`{.blockevents}-melding dersom svaret er rett. Dersom svaret er feil spør me det same spørsmålet ein gang til.

    ```blocks
    når grønt flagg klikkes
    send melding [Nytt spørsmål v] og vent
    gjenta (10) ganger
        spør (spørsmål) og vent
        hvis ((svar) = (riktig svar))
            si [Ja, så flink du er!] i (2) sekunder
            send melding [Nytt spørsmål v] og vent
        ellers
            si [Nei, det ble visst feil.] i (2) sekunder
        slutt
    slutt
    ```

- [ ] Me kan også telje poeng kvar gong du svarar rett. For å gjera dette treng me ein ny variabel, `Poeng`{.blockdata}. Denne skal gjelde for alle figurar, og denne lar me vera på scenen slik at me ser den.

- [ ] Legg til ein kloss i skriptet som set `Poeng`{.blockdata} til `0` rett etter at det grøne flaget vert klikka på.

- [ ] Legg og til ein kloss som endrar `Poeng`{.blockdata} med `1` dersom `svar`{.blocksensing} er rett.

## Test prosjektet {.flag}

__Klikk på det grøne flaget.__

- [ ] Får du fleire oppgåver utan at du må trykje på det grøne flaget?

- [ ] Får du eit poeng kvar gong du svarar rett?

- [ ] Klarar du 10 poeng?

# Steg 6: Litt hjelp kanskje ... {.activity}

Til slutt skal me sjå på korleis`Læremeister` kan gje oss litt hjelp med gongestykka. Ein måte å tenkje på gongestykker er at me har mange ting som me plasserar i eit rutenett. For eksempel kan me tenkje på **3 gonger 4** som **3** rader med **4** elefanter i kvar som dette:

![](elefanter.png)

Dersom me ikkje hugsar kor mykje 3 ganger 4 er, kan me telje elefantar og finne ut at svaret er **12**.

## Sjekkliste {.check}

- [ ] Legg til ein ny figur som me kan få litt hjelp frå. Du kan velje kva figur du vil, men me har brukt `Dyr/Elephant`. Gi figuren navnet `Hjelpar`.

- [ ] For å teikne eit rutenett med Hjelpere bruker me to `gjenta`{.blockcontrol}-klossar i tillegg til `stemple avtrykk`{.blockpen} som teiknar Hjelparane på skjermen. Skriv dette  skriptet på `Hjelper`-figuren:

    ```blocks
    når jeg mottar [Tegn hjelper v]
    slett
    sett størrelse til (20)%
    vis
    sett y til (140)
    gjenta (tal1) ganger
        sett x til (-140)
        gjenta (tal2) ganger
            stemple avtrykk
            endre x med (40)
        slutt
        endre y med (-25)
    slutt
    skjul
    ```

    Om du har brukt ein annan figur som `Hjelpar` kan det henda du må bruka nokre andre tal i dette skriptet. Prøv i så fall først å forandra på `sett størrelse til 20%`{.blocklooks}-klossen.

- [ ] Nå skal me teikna dette rutenettet kvar gong me lagar eit nytt spørsmål. Klikk på `Læremeister`, og legg til ein kloss nedst i `Nytt spørsmål`-skriptet:

    ```blocks
    når jeg mottar [Nytt spørsmål v]
    sett [tal1 v] til (tilfeldig tall fra (2) til (10))
    sett [tal2 v] til (tilfeldig tall fra (2) til (10))
    sett [rett svar v] til ((tall1) * (tall2))
    sett [spørsmål v] til (sett sammen (sett sammen (tal1) [ gonger ]) (tal2))
    send melding [Tegn hjelper v]
    ```

## Test prosjektet {.flag}

__Klikk på det grøne flaget.__

- [ ] Vert det teikna eit rutenett av hjelparane til kvar oppgåve?

## Fleire utfordringar {.challenge}

- [ ] Du kan forandra kor vanskelege gongestykka er ved å forandre tala i `tilfeldig tal`{.blockoperators}-klossene.

- [ ] Om du gir `Hjelper` fleire draktar kan du bruke ein `neste drakt`{.blocklooks}-kloss i `Tegn hjelper`-skriptet for å få litt variasjon i hjelperfigurane. Om du gjer dette er det enklast om draktane er omtrent like store.

- [ ] Kanskje `Læremeister` kan gje litt meir hjelp når ein svarar feil? Klarar du å få henne til å sei `Nei, det riktige svaret er større`  eller `Nei, det riktige svaret er mindre`?

- [ ] `Læremeister` kan mykje rart! Kanskje ho kan lera bort andre ting enn gongestykke?
