Scratch
========

Scratch er et programmeringsspråk utviklet ved MIT, med spesiell fokus
på å lære barn og unge å være kreative, tenke systematisk og
samarbeide med andre. Scratch er tilgjengelig på http://scratch.mit.edu/.

# Guide til oppgaveskrivere og oversettere

Scratch-oppgavene ligger under denne scratch-katalogen. Se
https://github.com/kodeklubben/oppgaver for mer info om den generelle
katalogstrukturen.

## Formattering av tekst



## Bilder

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

- Referanse til en fane (drakter, lyder, skript) legges inn slik:
  `![drakter](fane-drakter.png)`. Dette blir da seende slik ut:
  ![drakter](bilder/fane-drakter.png)


## Kodeblokker

