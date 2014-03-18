---
title: Labyrint
level: 1.2
language: nb-NO
stylesheet: scratch
embeds: ["*.png", "../../bilder/*.png"]
...

# Introduksjon {.intro}

I dette spillet vil vi kontrollere utforskeren __Guttorm__ mens han
leter etter skatten gjemt inne i labyrinten. Dessverre er skatten
beskyttet av den skumle froskekongen.

![](skjermbilde.png)

# Steg 1: Hvordan styre figurer med piltastene {.activity}

*Vi begynner med å se på hvordan vi kan styre figurer med
piltastene. For å få til dette vil vi bruke
`Hendelser`{.blockgrey}-blokker som merker når man trykker på
tastaturet.*

## Sjekkliste {.check}

+ Start et nytt prosjekt.
+ Slett kattefiguren ved å høyreklikke på den og velge `slett`.
+ Legg til en ny figur. Klikk på ![Velg figur fra biblioteket](hent-fra-bibliotek.png)-knappen og velg en figur du har lyst til å styre rundt. Vi har brukt `Dyr/Beetle`-figuren.
+ Gi den nye figuren navnet `Utforsker` ved å klikke på `i`{.blockblue}.

Vi begynner med å la figuren bevege seg oppover skjermen når vi
trykker på `pil opp`-tasten.

+ Legg til følgende skript på `Utforsker`-figuren din.

    ```blocks
        når [pil opp v] trykkes
        pek i retning (0 v)
        gå (5) steg
    ```

Prøv å trykk på `pil opp`-tasten. Beveger utforskeren din seg oppover skjermen? Nå må vi lage lignende skript for de andre tastene.

+ Legg også til disse skriptene, slik at `Utforsker` har totalt fire
skript, ett for hver tast.

    ```blocks
        når [pil ned v] trykkes
        pek i retning (180 v)
        gå (5) steg

        når [pil høyre v] trykkes
        pek i retning (90 v)
        gå (5) steg

        når [pil venstre v] trykkes
        pek i retning (-90 v)
        gå (5) steg
    ```

## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

+ Beveger utforskeren din seg rundt slik du hadde forventet?
+ Kan du forandre hvor raskt utforskeren flytter seg?

Tallet `5` i `gå 5 steg`{.blockblue}-blokkene bestemmer hvor raskt
utforskeren flytter seg rundt. Vi vil gjerne eksperimentere litt for å
se hvilken fart som passer best i spillet vårt, men for å endre farten
må vi bytte tallet i fire forskjellige skript. Det blir for mye jobb!

## Sjekkliste {.check}

Vi vil i stedet bruke en __variabel__ som kan styre farten til
`Utforsker`-figuren.

+ Lag en ny variabel ved å gå til `Data`{.blockorange}-kategorien og
klikk `Lag en Variabel`{.blocklightgrey}.
+ Kall variabelen `hastighet`, og velg at den bare skal gjelde `For
denne figuren`.
+ Til slutt, fjern avhukingen ved siden av den nye
`hastighet`{.blockorange}-blokken for at variabelen ikke skal vises på
scenen.

Nå må vi endre i skriptene våre slik at bruker `hastighet`-variabelen.

+ Lag først et nytt skript som setter verdien av `hastighet` til `10`.

    ```blocks
        når grønt flagg klikkes
        sett [hastighet v] til (10)
    ```

+ Deretter endrer vi de fire skriptene vi allerede har laget til å
bruke `hastighet`.

    ```blocks
        når [pil opp v] trykkes
        pek i retning (0 v)
        gå (hastighet) steg

        når [pil ned v] trykkes
        pek i retning (180 v)
        gå (hastighet) steg

        når [pil høyre v] trykkes
        pek i retning (90 v)
        gå (hastighet) steg

        når [pil venstre v] trykkes
        pek i retning (-90 v)
        gå (hastighet) steg
    ```

## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

+ Beveger utforskeren din seg fortsatt rundt slik den gjorde tidligere?
+ Forandrer hastigheten til utforskeren seg hvis du endrer verdien av
`hastighet` og klikker på det grønne flagget igjen?
+ Velg en hastighet du synes passer.

# Steg 2: Vi tegner vår egen labyrint {.activity}

*Nå som vi kan bevege utforskeren vår rundt omkring på skjermen, skal
vi gi ham en utfordring! Vi vil tegne en labyrint som han kan bevege
seg rundt inni.*

## Sjekkliste {.check}

+ Velg ![Tegn ny bakgrunn](tegn-ny.png) nederst til venstre på
skjermen for å tegne en ny bakgrunn.
+ Gi den nye bakgrunnen navnet `Labyrint`.
+ Velg en farge du liker og tegn en liten labyrint. Det er viktig at
alle veggene i labyrinten har samme farge (vi oppdager hvorfor
snart). Du kan velge selv hvordan labyrinten skal se ut, den trenger
ikke en gang å ha rette vegger!

![](liten-labyrint.png)

## Tips {.protip}

Dersom du vil tegne rette vegger er det enklest å bruke
linjeverktøyet, ![Linjeverktøy](tegn-linje.png). Du kan i tillegg
holde inne `shift`-knappen for at linjene skal bli helt rette.

## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

+ Kan du bevege utforskerfiguren din rundt inne i labyrinten?
+ Dersom figuren din er for stor kan du gjøre den mindre ved å trykke
på ![krymp](krymp.png)-knappen på toppen av skjermen.
+ Hva skjer dersom figuren din går på veggen i labyrinten?

# Steg 3: Utforskeren kan ikke gå gjennom veggen {.activity}


# Steg 4: På leting etter skatten {.activity}


# Steg 5: Froskekongen vokter i gangene {.activity}


# Ekstra: Andre måter å styre på {.activity}

