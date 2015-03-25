[![Build Status](https://travis-ci.org/kodeklubben/oppgaver.svg?branch=master)](https://travis-ci.org/kodeklubben/oppgaver)
# Kodeklubbens oppgavesett

Her finnes kilden til kodeklubbens oppgaver. Oppgavene er skrevet i formatet
markdown, og det er en [bygger](/arve0/codeclub_lesson_builder) som konverterer
oppgavene til [websider](http://kodeklubben.github.io/). For å komme i gang,
følg [anvisningene under](#komme-i-gang).


## Kurs/programmeringsspråk
Per nå finnes følgende kurs:
- [ComputerCraft (Minecraft)](src/computercraft)
- [JavaFX](src/javafx)
- [Python](src/python)
- [Scratch](src/scratch)
- [Web](src/web) - denne er ikke ferdig og vi trenger **din** hjelp.

## Fiks og rapporter enkle feil
For enkle feil og fiks kan du gjerne bruke webgrensesnittet til github. Se
[denne videoen](http://youtu.be/v9CS62-MED4) for hvordan dette fungerer uten å
installere noen programvare. Dersom du ønsker å oversette eller lage nye oppgaver
anbefaler vi at leser videre for et oppsett som laster ned oppgavene til din 
egen maskin slik at du kan jobbe lokalt. (Det er ikke noe galt i å kun bruke
githubs websider, kun litt vanskeligere når man ikke ser resultatet.)

## Komme i gang
Enkleste vei for å komme i gang er å se videoen som forklarer hvordan man
setter opp og arbeider med oppgavene: http://youtu.be/GtXxBGsAXOs Videoen er
laget for windows-brukere, men det vil være tilsvarende for Linux og
Mac-brukere. Dersom du er en *tekst-type* og foretrekker terminalen, les videre.

For å bygge oppgavene lokalt trenger du [git](//help.github.com/articles/set-up-git/)
og [node](//nodejs.org). Når du har installert git og node, kan du følge
anvisningene under. Anvisningene er kommandoer som må skrives inn i en konsoll.

#### Ubuntu-brukere merk dette!
For å installere node trenger man å installere både *nodejs* og *npm*, samt lenke
*nodejs* til *node* (ellers vil installasjonen av noen pakker feile).
```sh
sudo apt-get install nodejs npm git
sudo ln -s /usr/bin/nodejs /usr/local/bin/node
```

#### Laste ned oppgavene
```
git clone --recursive https://github.com/kodeklubben/oppgaver
cd oppgaver
```
*Du kan også laste ned oppgavene med [github for windows](//windows.github.com)
eller [github for mac](//mac.github.com).*  

#### Sette opp
```
./setup
```


#### Start
```
./gulp
```
Dette steget vil bygge websider av oppgavene og åpne de i nettleseren din. Hver
gang en oppgave endres bygges websidene om igjen og nettleseren oppdaterer
nettsiden. For brukere av windows, finnes også `gulp.bat` som kan åpnes direkte
fra filbehandleren.

## Problemer og support
[![Chat med oss på gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/kodeklubben/oppgaver)

Dersom du har problemer med å komme i gang, hjelper vi deg gjerne om du kommer
og [chatter med oss på gitter](https://gitter.im/kodeklubben/oppgaver).

## Filstruktur og formatering
Alle oppgavene finnes i katalogen [src](src). Hver mappe i `src`
representerer et programmeringsspråk eller kurs. Filer som heter `README.md`
blir ekskludert, men vises på github (slik som denne teksten du leser nå).
Derfor egner `README.md` seg for merknader til lærere og lignende.

Oppgavene skrives i markdown og har en YAML-header i toppen. Formatet er
beskrevet i [FORMAT.md](//github.com/arve0/codeclub_lesson_builder/blob/docs/FORMAT.md),
men vi tar det viktigste her.

Først et eksempel:
```
---
title: Superhus
level: 1
---

# Introduksjon {.intro}
Dette er introen.
```

YAML-headeren er alt som befinner seg mellom `---` i toppen, som blir
gjort tilgjengelig som variabler i malen. Det er bare `title` og
`level` som er påkrevd, men man kan også definere `author`,
`translator` og `license` (standard lisens er
[CC-BY 4.0](//creativecommons.org/licenses/by/4.0/deed.no)).


#### Bygging

Ved *bygging* blir alle markdown-filer (.md) omgjort til HTML og bilder eller
andre filer blir kopiert. Dersom en oppgave skal inkludere filer eller bilder,
skal oppgaven ligge i en egen mappe med filene. I motsatt tilfelle, dersom en
oppgave ikke inkluderer bilder eller filer, så skal den ligge i roten av sitt
kurs/programmeringsspråk (feks ligger scratch-oppgavene [her](src/scratch)).

Byggeren lager en forside som viser alle oppgavene. Forsiden er sortert
etter nivå (`level` i YAML) og deretter filnavnet til oppgavene. Så dersom en
spesiell rekkefølge er ønsket kan man bruke prefiks i filnavnene, som eksempel
`01-felix_og_herbert`, `02-spokelsesjakten`, osv.

Det er også mulig å lage spillelister, som er nyttig for å kombinere oppgaver i
en spesiell rekkefølge for et kurs eller lignende. Les mer om spillelister
og se eksempler [her](/src/scratch/playlists).

Hvis en oppgave bare skal vises i sin spilleliste, kan `indexed: false` legges
til i YAML-header. Hvis oppgaven ikke finnes i noen spilleliste, vil det ikke
lenkes til oppgaven fra noe sted og den er da gjemt.


#### Markdown

Nettet har flere beskrivelser av [Markdown-syntaksen]. Du kan
også lære endel ved å bruke en [live markdown editor].

[Markdown-syntaksen]: http://daringfireball.net/projects/markdown/syntax "Markdown-syntaks"
[live markdown editor]: http://jbt.github.io/markdown-editor/ "live markdown editor"

Her kommer noen eksempler:
- *Uthevet skrift* skrives `*Uthevet skrift*`,
- **Fet skrift** skrives `**Fet skrift**`.


#### Overskrifter

Overskrifter lages ved å begynne en linje med en eller flere `#`. En `#` gir
den største overskriften, mens seks `######` gir den minste overskriften. I
tillegg kan en stil legges til overskriften slik som dette `# Overskrift {.stil}`.
Stilene som er tilgjengelige er (antall `#` er viktig her):

- Introduksjon brukes øverst i hver oppgave: `# Introduksjon {.intro}`.

- Hver oppgave er delt inn i steg: `# Steg 1: Lag en figur {.activity}`.

- Hvert steg har flere aktiviteter i en sjekkliste: `## Sjekkliste {.check}`.

I tillegg finnes flere stiler som brukes ved behov:

- Ting å prøve: `## Ting å prøve {.try}`,

- Utfordringer: `## Utfordring: Flere ting {.challenge}`,

- Test prosjektet: `## Test prosjektet {.flag}`,

- Lagre prosjektet: `## Lagre prosjektet {.save}`.


#### Bilder

- Store bilder legges inn ved å skrive:

    ```

    ![](bilde-felix.png "katten felix")

    ```

  Legg merke til de tomme linjene over og under bildet. Bildet vil da sentreres
  i et avsnitt for seg selv. Alternativ billedtekst legges mellom
  `"` og `"` slik at bildene også gir mening for synshemmede.

- Små bilder, som skal være en del av teksten, legges inn med samme
  kode `![bilde](lite-bilde.png)`, men da med koden som en del av
  teksten. For disse bildene blir teksten mellom `[` og `]` brukt som
  alternativ tekst i tilfelle bildet ikke kan vises.


#### Kodeblokker

Kodeblokker skrives med tre `-tegn foran og bak koden:

<pre>
```
for i in range(10):
    print(i)
```
</pre>

For å få farger og stil som passer til et spesielt programmeringsspråk, legges
språkets navn etter <code>```</code> slik som dette:

<pre>
```python
for i in range(10):
    print(i)
```
</pre>

Les videre for inkludering av scratchkode.


#### Scratch kodeblokker

Scratchkode kan skrives rett inn i Markdown-teksten. Denne blir oversatt til
figurer av et verktøy som heter [Scratchblocks2][sb2]. På hjemmesidene til
Scratch finnes [dokumentasjon over syntaks][doc sb]. Et nyttig verktøy er
[scratchblocks translator][sbt] som lar deg hente ut og oversette scratchkode.

[sb2]: https://github.com/blob8108/scratchblocks2 "Scratchblocks2"
[doc sb]: http://wiki.scratch.mit.edu/wiki/Block_Plugin/Syntax "Dokumentasjon scratchblocks"
[sbt]: http://scratchblocks.codeclub.org.uk/translator/ "Scratchblocks translator"

Hele kodesnutter skrives som et eget avsnitt på følgende måte:

<pre>
```blocks
når grønt flagg trykkes
for alltid
pek mot [musepekeren v]
slutt
```
</pre>

Rykkes koden ekstra inn i lister, vil den flyte med teksten rundt. For eksempel
vil man typisk ha innrykk på fire mellomrom for kode som er en del av en
sjekkliste:

<pre>
## Sjekkliste {.check}
- En forklarende tekst her. Og kode som hører til:

    ```blocks
    for alltid
    pek mot [musepekeren v]
    ```

- Neste sjekkpunkt.
</pre>

Hvis du vil referere til enkeltblokker i teksten kan det gjøres slik:
`` `for alltid`{.blockcontrol}-klossen``. Kategorier som er tilgjengelig er
*motion*, *looks*, *sound*, *pen*, *data*, *events*, *control*, *sensing*,
*operators* og *moreblocks*.

Her er en liste over alle kategoriene med navn:
- `` `Bevegelse`{.blockmotion}``
- `` `Utseende`{.blocklooks}``
- `` `Lyd`{.blocksound}``
- `` `Penn`{.blockpen}``
- `` `Data`{.blockdata}``
- `` `Hendelser`{.blockevents}``
- `` `Styring`{.blockcontrol}``
- `` `Sansning`{.blocksensing}``
- `` `Operatorer`{.blockoperators}``
- `` `Flere klosser`{.blockmoreblocks}``

For å referere til en fane som skript, drakter eller lyder, brukes `` ` `` slik
som dette: `` `Drakter` ``

## Lisens
Som standard settes lisensen på alle oppgaver til [CC BY-SA 4.0]. Dersom du ønsker
å dele en oppgave med en annen lisens må du legge `license` i YAML-headeren:

```
---
title: Din tittel
license: Din lisens
---
```

Er ikke dette gjort, godtar du at oppgaven din deles med vilkårene i [CC BY-SA 4.0].

[CC BY-SA 4.0]: http://creativecommons.org/licenses/by-sa/4.0/deed.no

## Bidra
Dersom du finner feil eller har lyst å forbedre noe, vent ikke med å sende en
[issue](//github.com/kodeklubben/oppgaver/issues). Vi trenger din hjelp!
