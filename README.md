# Kodeklubbens oppgavesett

Her finnes kodeklubbens oppgaver i flere programmeringsspråk. For å komme i gang, følg anvisningene under.

## Komme i gang
Enkleste vei for å komme i gang er å se videoen som forklarer hvordan man setter opp og arbeider med oppgavene: http://youtu.be/GtXxBGsAXOs Videoen er laget for windows-brukere, men det vil være tilsvarende for Linux og Mac-brukere. Dersom du er mer en *tekst-type* og foretrekker terminalen fremfor GUI, les videre.

For å bygge oppgavene lokalt trenger du [git](//help.github.com/articles/set-up-git/) og [node](//nodejs.org). Når du har installert git og node, kan du følge anvisningene under. Anvisningene er kommandoer som må skrives inn i en konsoll.

**Laste ned oppgavene**
```
git clone --recursive https://github.com/arve0/oppgaver
cd oppgaver
```
*Du kan også laste ned oppgavene med [github for windows](//windows.github.com) eller [github for mac](//mac.github.com).*

**Sette opp**
```
./setup
```

**Start**
```
./gulp
```
Dette steget vil bygge websider av oppgavene og åpne de i nettleseren din. Hver gang en oppgave endres bygges websidene om igjen og nettleseren oppdaterer nettsiden. For brukere av windows, finnes også `gulp.bat` som kan åpnes direkte fra filbehandleren.


## Kurs/programmeringsspråk
Per nå finnes følgende kurs:
- [ComputerCraft (Minecraft)](src/computercraft)
- [Python](src/python)
- [Scratch](src/scratch)
- [Web](src/web)


## Filstruktur og formatering
Alle oppgavene finnes i katalogen [src](src). Hver mappe i `src` representerer et programmeringsspråk eller kurs. Filer som heter `README.md` blir ekskludert fra byggingen, men vises på github (slik som denne teksten du leser nå). Derfor egner `README.md` seg for merknader til lærere og lignende.

Ellers blir alle markdown-filer (.md) omgjort til HTML og bilder eller andre filer blir kopiert ved bygging. Dersom en oppgave skal inkludere filer eller bilder, skal oppgaven ligge i en egen mappe med filene. I motsatt tilfelle, dersom en oppgave ikke inkluderer bilder eller filer, så skal den ligge i roten av sitt kurs/programmeringsspråk (feks ligger scratch-oppgavene [her](src/scratch)).

Byggeren lager en førsteside som viser alle oppgavene. Det er to typer oppgaver, vanlige og spillelister. Førstesiden er sortert etter filnanvet til oppgavene, så dersom en spesiell rekkefølge er ønsket kan man bruke prefiks i filnavnene. For eksempel `01-felix_og_herbert`, `02-spokelsejakten`, osv.

Oppgavene skrives i markdown og har en YAML-header i toppen. Formatet er beskrevet i [FORMAT.md](codeclub_lesson_builder/FORMAT.md), men vi tar det viktigste her.

Først et eksempel:
```
---
title: Superhus
level: 1
---

# Introduksjon {.intro}
Dette er introen.
```

YAML-headeren er alt som befinner seg mellom `---` i toppen, som blir gjort tilgjengelig som variabler i malen. Det er bare `title` og `level` som er påkrevd, men man kan også definere `author`, `language` (hvis en ønsker inkludere engelske oppgaver), `license` (standard lisens er [CC-BY 4.0](//creativecommons.org/licenses/by/4.0/deed.no)) og `playlist` (navn på spilleliste dersom oppgaver skal grupperes).

Nettet har flere beskrivelser av
[Markdown-syntaksen](//daringfireball.net/projects/markdown/syntax). Du kan også lære endel ved å bruke en [live markdown editor](//jbt.github.io/markdown-editor/). Her er noen eksempler:

- *Uthevet skrift* skrives `*Uthevet skrift*`,

- **Fet skrift** skrives `**Fet skrift**`.


**Overskrifter**

Overskrifter lages ved å begynne en linje med en eller flere `#`. En
`#` gir den største overskriften, mens seks `######` gir den minste
tilgjengelige overskriften. I tillegg bruker vi stiler på
overskriftene, som byggevektøyet anvender. Stilene er som følger (antall `#` er viktig her):

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


**Bilder**

- Store bilder legges inn ved å skrive `![](stort-bilde.png)` på en
egen linje, med blanke linjer før og etter. Bildet vil da sentreres
i et avsnitt for seg selv. Eventuell billedtekst kan legges mellom
`[` og `]` slik `![Dette er en billedtekst](stort-bilde.png)`.

- Små bilder, som skal være en del av teksten, legges inn med samme
kode `![bilde](lite-bilde.png)`, men da med koden som en del av
teksten. For disse bildene blir teksten mellom `[` og `]` brukt som
alternativ tekst i tilfelle bildet ikke kan vises.


**Kodeblokker**

Kodeblokker skrives med tre `-tegn foran og bak koden:

<pre>
```
for i in range(10):
    print(i)
```
</pre>

For å få farger og stil som passer til et spesielt, legges språkets navn etter
<code>```</code> slik som dette:

<pre>
```python
for i in range(10):
    print(i)
```
</pre>

Les videre for inkludering av scratchkode.

**Scratch kodeblokker**

Scratchkode kan skrives rett inn i Markdown-teksten. Denne blir oversatt til
figurer av et verktøy som heter [Scratchblocks2][sb2]. På
hjemmesidene til Scratch finnes [dokumentasjon over syntaks][doc sb]. Et
nyttig verktøy er [scratchblocks translator][sbt] som lar deg hente ut og
oversette scratchkode.

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

Man kan rykke inn koden slik at den ligger i flukt med teksten
rundt. For eksempel vil man typisk ha fire mellomrom innrykk for kode
som er en del av en sjekkliste.

Man kan også referere til enkeltblokker i teksten. Dette gjøres slik:
`` `for alltid`{.blockorange}-klossen``. Man kan velge mellom fargene
grey, lightgrey, orange, purple, pink, blue, lightblue, yellow, green
og lightgreen.

Den samme funksjonaliteten brukes for å referere til faner og
kategorier:

- Referanse til en fane (Skript, Drakter, Lyder) legges inn slik:
`` `Drakter`{.blocklightgrey}``. For fanene brukes alltid fargen
lightgrey.

- Referanse til en kategori (Bevegelse, Utseende, Lyd, Penn, Data,
  Hendelser, Styring, Sansning, Operatorer, Flere klosser) legges inn
  slik: `` `Bevegelse`{.blockblue}``. Pass på at du bruker de riktige
  fargene (per nå matcher ikke alle helt, vi skal få lagt inn de
    riktige fargene etterhvert). Det vil si
    - `` `Bevegelse`{.blockblue}``
    - `` `Utseende`{.blockpurple}``
    - `` `Lyd`{.blockpink}``
    - `` `Penn`{.blockgreen}``
    - `` `Data`{.blockorange}``
    - `` `Hendelser`{.blockgrey}``
    - `` `Styring`{.blockyellow}``
    - `` `Sansning`{.blocklightblue}``
    - `` `Operatorer`{.blocklightgreen}``
