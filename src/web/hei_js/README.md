---
title: Lærerveiledning - Bruk data: Jente- og guttenavn
language: nb
---

# Om oppgaven {.activity}
I denne oppgaven skal elevene hente data fra SSB og lage en enkel søkefunksjon for å sjekke om navn er jente- eller guttenavn.

## Oppgaven passer til: {.check}
 __Fag__: Matematikk, Norsk

__Trinn__: 2.-7. trinn

__Tema__: Statistikk, Databehandling

__Nivå__: Nybegynner

__Tidsbruk__: Dobbelttime eller mer.

##

## Kompetansemål {.challenge}

+ __Matematikk, 2. årstrinn__: samle, sortere, notere og illustrere data med tellestreker, tabeller og søylediagrammer, og samtale om prosessen og hva illustrasjonene forteller om datamaterialet

+ __Matematikk, 4. årstrinn__: samle, sortere, notere og illustrere data på hensiktsmessige måter med tellestreker, tabeller og søylediagrammer, med og uten digitale verktøy, og samtale om prosess og framstilling

+ __Matematikk, 7. årstrinn__: representere data i tabeller og diagrammer som er framstilt med og uten digitale verktøy, lese og tolke framstillingene og vurdere hvor nyttige de er

+ __Norsk, 4. årstrinn__: søke etter informasjon, skape, lagre og gjenfinne tekster ved hjelp av digitale verktøy

+ __Norsk, 7. årstrinn__: velge ut og vurdere informasjon fra bibliotek og digitale informasjonskanaler


##
## Forslag til læringsmål {.challenge}

+ Elevene kan forklare hva statistikk er.

+ Elevene skal kunne beskrive noen situasjoner hvor det er viktig å bruke statistikk.

+ Elevene skal kunne bruke og formatere ulike filformater.

##
## Forslag til vurderingskriterier {.challenge}

+ Eleven klarer å fullføre oppgaven og finne statistikk på eget navn.

+ Eleven viser høy måloppnåelse ved å finne og bruke annen statistikk.
##


## Forutsetninger og utstyr {.challenge}

+ __Utstyr__: Datamaskiner med tilgang internett og excel installert (ikke nettbrett). Elevene kan fint jobbe to og to.

+ __Forutsetninger__: Elevene burde ha en grunnleggende forståelse for statistikk og litt erfaring med Scratch.
##

## Fremgangsmåte {.teacher}
Her kommer fremgangsmåten til den faktiske oppgaven, med noen tips og vanlige utfordringer ved hvert steg.

# _Steg 1: Statistisk Sentralbyrås navnelister_ {.activity}

*La oss se litt på navnelistene til Statistisk Sentralbyrå. Disse viser hvor
mange i Norge som får hvilke navn, både i dag og tidligere.*

## Sjekkliste {.check}

+ Gå til navnesidene hos Statistisk Sentralbyrå:
  [ssb.no/navn](http://www.ssb.no/navn). Klikk litt rundt på dem for å bli kjent
  med hvilke data som er tilgjengelige. Prøv å søke på ditt eget navn og se på
  **Historisk utvikling (graf)**.

    Prøv også andre navn: Her er en liten utfordring; Se på grafen over
    historisk utvikling for navnet **Sonja**. Det har to veldig tydelige topper,
    en på 1920-tallet og en til på 1960-tallet. Kan du forklare dette?

+ Vi vil hente ut lister med alle jente- og guttenavnene. Disse finner vi ved å
  klikke på fanen **Tabeller**. På denne siden finner du blant annet to tabeller
  som heter **Jentenavn, alfabetisk** og **Guttenavn, alfabetisk** (med
  årstall). Last ned disse to tabellene enten i **Excel** eller **CSV**-format.

+ Åpne filene du nettopp lastet ned i Excel eller et tilsvarende
  regnearkprogram.

    Vi er her bare interessert i selve navnelistene, ikke alle tallene som sier
    noe om hvor mange som fikk hvert navn. Du kan derfor slette alle kolonnene
    som inneholder tall.

+ Legg begge listene inn i det samme regnearket, og gi dem beskrivende
  overskrifter. Dette vil se ut omtrent som dette:

    ![](navnelister_regneark.png)

+ Dette er viktig! Lagre regnearket som CSV. Du gjør dette ved å velge **Lagre
  som** eller **Eksporter** fra menyen og deretter velge formatet **CSV**. Gi
  filen din et navn du vil kjenne igjen, for eksempel `navnelister.csv`.

+ Gå til verktøyet for å [lese data inn i Scratch](../data/data.html). Trykk på
  knappen **Last opp datafil**, og velg CSV-filen du nettopp laget. Dette vil
  laste ned et Scratchprosjekt på datamaskinen din, sannsynligvis en fil som
  heter `data.sb2` i `Nedlastinger`-katalogen din.

## Tips til læreren {.protip}
+ Her er det et vanlig problem at elevene glemmer å legge inn tittel på Jentenavn og Guttenavn-kolonnene. Da vil ikke programmet fungere.

+
##

# Steg 2: Hent navnelistene inn i Scratch {.activity}

*Vi kan nå lese navnelistene inn i Scratch.*

## Sjekkliste {.check}

+ Start et nytt Scratchprosjekt.

+ Velg **Fil** i menyen og klikk på **Last opp fra maskinen**. Velg filen som
  ble lastet ned i forrige steg, sannsynligvis heter den `data.sb2` og ligger i
  katalogen `Nedlastinger`.

+ Klikk **OK**. Navnelistene vil nå lastes inn. Det skal se omtrent slik ut:

    ![](navnelister_scratch.png)

+ Navnelistene er eksempler på noe som rett og slett kalles **lister** i
  Scratch. De programmeres ved hjelp av klosser som ligger i
  `Data`{.blockdata}-kategorien. Som for variabler kan du ta listene vekk fra
  Scenen ved å fjerne avhukingen, høyreklikke på den eller bruke klossen `skjul
  liste [ v]`{.b}.

## Data i Scratch {.tip}

Vanligvis må man skrive inn alle dataene i lister selv, om man vil bruke dem i
Scratch. Ved hjelp av [dataverktøyet](../data/data.html) kan du lese inn
kjempemasse data som du eller noen andre allerede har laget.

Har du noen ideer til andre data du vil lese inn på samme måte?

## Tips til læreren {.tip}
+ Her er det et vanlig problem at elevene glemmer å legge inn tittel på Jentenavn og Guttenavn-kolonnene. Da vil ikke programmet fungere.


# Steg 3: Bruk navnelistene {.activity}

*Vi skal nå skrive et lite program som bruker navnelistene. Kanskje vi kan få
katten vår til å se forskjellen på jente- og guttenavn?*

## Sjekkliste {.check}

+ Vi begynner med å la katten spørre om et navn. Til dette kan vi bruke `spør
  [Skriv et navn] og vent`{.b}-klossen.

+ For at katten skal kunne huske navnet vi forteller den vil vi bruke en
  variabel. Klikk på `Data`{.blockdata} og deretter `Lag en variabel`. Kall
  variabelen `(Navn)`{.b}.

+ Vi kan nå ta vare på svaret i `(Navn)`{.b}-variabelen.

  ```blocks
  spør [skriv et navn] og vent
  sett [Navn v] til (svar)
  ```

+ Om du ser på klossene som nå finnes i `Data`{.blockdata}-kategorien er det en
  som sier `<[Guttenavn v] inneholder [thing]?>`{.b}. Denne klossen kan vi bruke
  for å finne ut om et navn finnes i jentenavnlisten eller guttenavnlisten
  (eller begge eller ingen av dem).

+ Lag en sjekk for om `(Navn)`{.b} er et jentenavn:

  ```blocks
  spør [skriv et navn] og vent
  sett [Navn v] til (svar)
  hvis <[Jentenavn v] inneholder (Navn)?>
      si (sett sammen (Navn) [ er et jentenavn]) i (2) sekunder
  slutt
  ```

## Test prosjektet {.flag}

__Klikk på koden din.__

+ Spør katten deg om å skrive inn et navn?

+ Skriv inn et jentenavn, for eksempel `Emma`. Sier katten at `Emma er et
  jentenavn`?

+ Hva skjer om du skriver inn et guttenavn? Eller et ord som ikke er et navn?

## Sjekkliste {.check}

+ Lag en sjekk for om `(Navn)`{.b} er et guttenavn. Prøv å lag denne selv. Du
  kan gjøre det på akkurat samme måte som for jentenavn. Legg den nye
  hvis-testen under den du allerede har.

+ Legg til en `for alltid`{.b}-løkke rundt hele koden din. På den måten vil
  katten stadig spørre deg om nye navn.

+ Legg også en `når grønt flagg klikkes`{.b}-kloss på toppen av koden din, slik
  at du kan starte programmet ved å klikke på det grønne flagget.

## Prøv selv {.try}

+ Dette er et veldig enkelt eksempel på hva man kan gjøre med navnelistene (og
  det har noen problemer: for eksempel finner ikke katten dobbeltnavn
  som `Geir Arne`). Har du noen ideer til hvordan du kan bruke navnelistene på
  en enda mer spennende måte?

+ Kjenner du til andre datasett som du har lyst til å jobbe med i Scratch? Bruk
  [dataverktøyet](../data/data.html) for å lese inn dataene.

## Tips til læreren {.protip}
+ Her er det et vanlig problem at elevene glemmer å legge inn tittel på Jentenavn og Guttenavn-kolonnene. Da vil ikke programmet fungere.

+
##

## Variasjoner {.challenge}
+ Elevene skal finne andre datasett. Her kan det være en ide å ha noe
##

## Kommentarer {.challenge}
[Bruk gjerne forumet vårt til å diskutere oppgavene.](https://forum.kidsakoder.no/c/oppgaver)
##
