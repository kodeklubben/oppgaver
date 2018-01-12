Scratch
=======

Scratch er et programmeringsspråk utviklet ved MIT, med spesiell fokus
på å lære barn og unge å være kreative, tenke systematisk og
samarbeide med andre. Scratch er tilgjengelig på <http://scratch.mit.edu/>.

## Guide til oppgaveskrivere og oversettere

Scratchoppgavene ligger i denne katalogen. Se
[hoved README.md](/README.md#filstruktur-og-formatering) for mer info om den
generelle katalogstrukturen.

## Kodeblokker

Scratchkode kan skrives rett inn i Markdown-teksten. Denne blir oversatt til
figurer av et verktøy som heter [Scratchblocks].

Nyttige ressurser:
- [scratchblocks generator] henter ut kode direkte fra prosjekter på scratch.mit.edu.
- [scratchblocks translator] oversetter kode mellom for eksempel engelsk og norsk.
- På hjemmesidene til Scratch finnes en [dokumentasjon over syntaksen].

[Scratchblocks]: https://github.com/tjvr/scratchblocks
[dokumentasjon over syntaksen]: http://wiki.scratch.mit.edu/wiki/Block_Plugin/Syntax
[scratchblocks generator]: http://scratchblocks.github.io/generator/
[scratchblocks translator]: http://scratchblocks.github.io/translator/

Hele kodesnutter skrives som et eget avsnitt på følgende måte:

<pre>
```blocks
når grønt flagg trykkes
for alltid
pek mot [musepekeren v]
slutt
```
</pre>

Hvis du vil referere til enkeltblokker i teksten kan det gjøres slik:
`` `for alltid`{.b}``. I tillegg er fargene for kategoriene tilgjengenlig:

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
