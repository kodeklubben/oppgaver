Scratch
=======

Scratch er et programmeringsspråk utviklet ved MIT, med spesiell fokus
på å lære barn og unge å være kreative, tenke systematisk og
samarbeide med andre. Scratch er tilgjengelig på <http://scratch.mit.edu/>.

## Guide til oppgaveskrivere og oversettere

Scratch-oppgavene ligger under denne scratch-katalogen. Se
<https://github.com/kodeklubben/oppgaver> for mer info om den generelle
katalogstrukturen.

### Formattering av tekst

Oppgaveteksten skrives i Markdown. Nettet har flere beskrivelser av
[Markdown-syntaksen](http://daringfireball.net/projects/markdown/syntax). De
viktigste vi bruker er

- *Uthevet skrift* skrives `*Uthevet skrift*`,

- __Fet skrift__ skrives `__Fet skrift__`.

Overskrifter lages ved å begynne en linje med en eller flere `#`. En
`#` gir den største overskriften, mens seks `######` gir den minste
tilgjengelige overskriften. I tillegg bruker vi stiler på
overskriftene, som byggevektøyet anvender på de ferdige HTML- og
PDF-dokumentene. Stilene er som følger (antall `#` er viktig her):

- Introduksjon brukes øverst i hver oppgave: `# Introduksjon
  {.intro}`.

- Hver oppgave er delt inn i steg: `# Steg 1: Lag en figur
  {.activity}`.

- Hvert steg har flere aktiviteter i en sjekkliste: `## Sjekkliste
  {.check}`.

I tillegg finnes flere stiler som brukes ved behov:

- Ting å prøve: `## Ting å prøve {.try}`,

- Utfordringer: `## Utfordring: Flere ting {.challenge}`,

- Test prosjektet: `## Test prosjektet {.flag}`,

- Lagre prosjektet: `## Lagre prosjektet {.save}`.

### Bilder

Generelle bilder av grensesnittet som kan brukes på tvers av oppgavene
ligger i `bilder`-katalogen, mens bilder som er spesielle for en gitt
oppgave ligger i den oppgavens katalog. Bruk `bilder`-katalogen så mye
som mulig slik at vi får mest mulig gjenbruk av bildene.

For at bilder skal legges inn riktig av byggeverktøyet, må de
defineres i header-delen av oversettelsen:

```
    embeds: ["*.png", "../../bilder/*.png"]
```

Denne koden sier at alle png-bilder i oppgavekatalogen og i
bilder-katalogen kan brukes i oppgaveteksten.

- Store bilder legges inn ved å skrive `![](stort-bilde.png)` på en
  egen linje, med blanke linjer før og etter. Bildet vil da sentreres
  i et avsnitt for seg selv. Eventuell billedtekst kan legges mellom
  `[` og `]` slik `![Dette er en billedtekst](stort-bilde.png)`.

- Små bilder, som skal være en del av teksten, legges inn med samme
  kode `![bilde](lite-bilde.png)`, men da med koden som en del av
  teksten. For disse bildene blir teksten mellom `[` og `]` brukt som
  alternativ tekst i tilfelle bildet ikke kan vises.

### Kodeblokker

Scratchkode kan skrives rett inn i Markdown-teksten. Denne blir
oversatt til bilder av et verktøy som heter
[Scratchblocks2](https://github.com/blob8108/scratchblocks2). På
hjemmesidene til Scratch finnes
[dokumentasjon](http://wiki.scratch.mit.edu/wiki/Block_Plugin/Syntax).

Hele kodesnutter skrives som et eget avsnitt på følgende måte:
```
    ```blocks
        når grønt flagg trykkes
        for alltid
            pek mot [musepekeren v]
        slutt
    ```
```
Man kan rykke inn koden slik at den ligger i flukt med teksten
rundt. For eksempel vil man typisk ha fire mellomrom innrykk for kode
som er en del av en sjekkliste.

Man kan også referere til enkeltblokker i teksten. Dette gjøres slik:
```for alltid`{.blockorange}-klossen``. Man kan velge mellom fargene
grey, lightgrey, orange, purple, pink, blue, lightblue, yellow, green
og lightgreen.

Den samme funksjonaliteten brukes for å referere til faner og
kategorier:

- Referanse til en fane (Skript, Drakter, Lyder) legges inn slik:
  ```Drakter`{.blocklightgrey}``. For fanene brukes alltid fargen
  lightgrey.

- Referanse til en kategori (Bevegelse, Utseende, Lyd, Penn, Data,
  Hendelser, Styring, Sansning, Operatorer, Flere klosser) legges inn
  slik: ```Bevegelse`{.blockblue}``. Pass på at du bruker de riktige
  fargene (per nå matcher ikke alle helt, vi skal få lagt inn de
  riktige fargene etterhvert). Det vil si
    - ```Bevegelse`{.blockblue}``
    - ```Utseende`{.blockpurple}``
    - ```Lyd`{.blockpink}``
    - ```Penn`{.blockgreen}``
    - ```Data`{.blockorange}``
    - ```Hendelser`{.blockgrey}``
    - ```Styring`{.blockyellow}``
    - ```Sansning`{.blocklightblue}``
    - ```Operatorer`{.blocklightgreen}``
    - ```Flere klosser`{.blockpurple}``

