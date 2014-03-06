Scratch
=======

Scratch er et programmeringsspråk utviklet ved MIT, med spesiell fokus
på å lære barn og unge å være kreative, tenke systematisk og
samarbeide med andre. Scratch er tilgjengelig på http://scratch.mit.edu/.

## Guide til oppgaveskrivere og oversettere

Scratch-oppgavene ligger under denne scratch-katalogen. Se
https://github.com/kodeklubben/oppgaver for mer info om den generelle
katalogstrukturen.

### Formattering av tekst

Oppgaveteksten skrives i Markdown. Nettet har flere beskrivelser av
![Markdown-syntaksen](http://daringfireball.net/projects/markdown/syntax). De
viktigste vi bruker er

- *Kursiv skrift* skrives `*Kursiv skrift*`,

- __Fet skrift__ skrives `__Fet skrift__`.

### Bilder

Generelle bilder av grensesnittet som kan brukes på tvers av oppgavene
ligger i `bilder`-katalogen, mens bilder som er spesielle for en gitt
oppgave ligger i den oppgavens katalog.

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
  kode `![](lite-bilde.png)`, men da med koden som en del av
  teksten. For disse bildene blir billedteksten (mellom `[` og `]`)
  ignorert.

- Referanse til en fane (skript, drakter, lyder) legges inn slik:
  `![drakter](fane-drakter.png)`. Dette blir da seende slik ut:
  ![drakter](bilder/fane-drakter.png).

- Referanse til en kategori (bevegelse, utseende, lyd, penn, data,
  hendelser, styring, sansning, operatorer, flere klosser) legges inn
  slik: `![Bevegelse](kategori-bevegelse.png)`. Dette blir da seende
  slik ut: ![Bevegelse](bilder/kategori-bevegelse.png).

### Kodeblokker

