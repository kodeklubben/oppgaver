---
title: "HTML: Publiser nettsiden din"
level: 3
language: nb-NO
---
# Publiser nettsiden din på Internett{ .activity }

Nå har du laget ditt eget nettsted. Du ønsker vel å vise det frem, gjør du ikke?

Husker du servere fra den første økten? Servere er datamaskiner som alltid er på og koblet til Internett, og de er satt opp slik at folk kan besøke nettsteder som lever på disse datamaskinene.

For å legge nettsiden vår på internett skal vi nå bruke `Github Pages`. Dette er det samme som __Kodeklubben__ bruker: `kodeklubben.github.io`. For at du skal kunne gjøre dette må du ha en epost-adresse. Du kan enten lage din egen, bruk den du har på skolen eller spørre om å låne foreldrene dine sin. Det er viktig her at du husker hvilken epost du har bruk, du må også ha tilgang til eposten sånn at du kan få godkjent brukeren din på `Github`. 

# Github {.activity}
Github er en samarbeidsplatform for oss som driver med programmering. Her kan vi legge ut prosjekter som andre kan hjelpe til med, eller vi kan finne et prosjekt vi kan hjelpe til med. På denne måten kan vi enkelt hjelpe, samarbeide og dele med alle som driver med programmering i verden. Vi skal nå lage en bruker.

1. Gå inn på [http://github.com](github.com)
2. Skriv inn `Username`(brukernavn), `epost` og `password`(passord) før du trykker `Sign up for Github` (se bilde under)
<img src="ressurser/sign-in-1.png" width="100%">
3. Følg instruksjonene videre for å godkjenne og lage ferdig brukeren din

# Brukernavn.github.io {.activity}
Nå som vi har en `Github-bruker` kan vi registrere en `github.io`-side. 

1. Trykk på `New repository` (Grønn knapp til venstre eller `+` øverst i høyre hjørne)
2. Under `Repository name` så skriver du `ditt-brukernavn.github.io`. Under ser du et eksempel med `kodeklubben.github.io`. 
<img src="ressurser/1.png" width="100%">
3. Du kan gjerne skrive en beskrivelse av nettsiden under `Description`
4. Velg enten `Public`(alle kan se koden din)  eller `Private`(koden til nettsiden blir privat). Vi har valgt `Public`.
5. Trykk `Create repository`(oppbevaringssted).

Nå skal vi laste ned `repository`-et eller `repo`-et vårt, altså oppbevaringsstedet for koden til nettsiden vår. Denne koden legges i en mappe lokalt på datamaskinen vår. I denne mappen legger vi inn alle filene som skal brukes til nettsiden og bruker programmet eller kommandolinjen til `Github` for å laste opp kode til `ditt-brukernavn.github.io`-siden vår.

Nå som du er her, kan vi trykke på `Set up in Desktop`:
<img src="ressurser/2.png" width="100%">

Hvis du er vant til å bruke `kommandolinjen` til `Linux` eller `Mac OS X`, så kan du gjøre det som står under `Set up in Desktop`.

Du vil få spørsmål om å laste ned Github-programmet, takk ja til det. 

1. Trykk `Tillat` på eventuelle ting som dukker opp når programmet åpner seg:
<img src="ressurser/tillat.png">

2. Hvis du får spørsmål om å logge inn så må du logge inn med `brukernavn` og `passordet` du valgte til `Github`

3. Du får nå spørsmål om å legge mappen `ditt-brukernavn.github.io` et sted, legg det et passende sted hvor du finner det igjen. For eksempel på skrivebordet eller i `Mine dokumenter`.

Da er det påtide å lage sin første fil!

1. I mappen `ditt-brukernavn.github.io`, lag en fil som heter `index.html`. Dette skal være startsiden til nettsiden vår.
2. Skriv hva du vil i denne, du kan gjerne kopiere en av oppgavene du allerede har laget. Hvis du ikke vet hva du skal skrive kan du for eksempel skrive noe sånt:

```html
<DOCTYPE html>
<html>
    <body>
        <h1>Min første hjemmeside!</h1>
        <p>Denne hjemmesiden er laget med Git Pages.<p>
    </body>
</html>
```

Nå skal vi laste opp denne filen til `ditt-brukernavn.github.io`. For å ikke ødelegge det vi har på `kodeklubben.github.io` skal jeg nå vise med brukeren `larsfk.github.io`. 

1. Åpne `Github`-programmet
2. Trykk på `ditt-brukernavn.github.io` i kolonnen til venstre
3. Trykk på `Compare`. Da vil den filen du akkurat la til dukke opp:
<img src="ressurser/commit.png" width="100%">
4. Må du `committe` endringene du har gjort før du får lagt opp filen til `Github`-en din. For å gjøre dette skriver du en kort forklaring i `Summary` nederst, og litt mer detaljert beskrivelse av hva som er gjort i `Description`, som vist på bildet over. 
5. Nå kan du trykke på `Publish` øverst til høyre
<img src="ressurser/pushed.png" width="100%">
6. Hvis du får spørsmål om å `Tillate` en oprasjon, så gjør det. 
7. Nå ser vi (se bildet over) at en `commit` er lagt til og `pushet`(lastet opp) til siden vår. Gå inn på `ditt-brukernavn.github.io` (`larsfk.github.io` for meg) for å se hjemmesiden din! 

<img src="ressurser/hjemmeside.png" width="100%">

__Gratulerer med ny hjemmeside!__ Denne kan du dele med hvem du vil ved å sende lenken `ditt-brukernavn.github.io`.


