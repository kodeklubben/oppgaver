---
title: Den gode oppgaven
author: Stein Olav Romslo
---

# Den gode oppgaven

Når du skriver en oppgave som skal legges ut på oppgavesidene må du følge denne
malen. Slik blir utformingen på oppgavene mest mulig lik. På [denne
siden](conventions.md) ser du hvordan vi ønsker at markdown-koden skal skrives.

Rammen for oppgaven er en YAML-header, altså informasjon _om_ oppgaven,
oppgaveteksten med figurer, og en lærerveiledning som forklarer _hvordan_ en
klasse kan jobbe med oppgaven.

Når du har skrevet ferdig en oppgave med riktig formatering kan du sende den inn
til oppgaverepoet på Github. Se oppskrift på det [her](guide_bruk_git.md).

## YAML-header

For å markere YAML-headeren bruker vi `---` før og etter. I YAML-headeren skal
følgende være med:

- [ ] Tittel på oppgavene.

- [ ] Navn på den som har skrevet oppgaven, eventuelt hvem som skrev den originalt.

- [ ] Anbefalt nivå (introduksjon-begynner-erfaren-ekspert).

- [ ] Språk ([ISO 639-1](https://no.wikipedia.org/wiki/Liste_over_ISO_639-1-koder)).

Et eksempel på YAML-header blir da

```
---
title: Astrokatt
level: 1
author: 'Geir Arne Hjelle'
language: nb
---
```

Hvis du ønsker å dele oppgaven med en annen lisens enn det som er standard (CC
BY-SA 4.0), så må du skrive `lisens: 'lisenstype'`, der _lisenstype_ er den
lisensen du ønsker å dele med, i YAML-headeren.

## Oppgaveteksten

Det er vanlig med en introduksjon som forklarer hva formålet med oppgaven er. I
denne passer det å skrive hva som skal programmeres og litt historie dersom
målet er å reprodusere et kjent spill. Ta gjerne med et bilde som viser hvordan
det vil se ut til slutt. Husk å skrive en bildetekst for brukere som ikke ser
bildet.

```
# Introduksjon {.intro}

Katten vår har så lyst å være en astronaut, la oss se om vi kan hjelpe ham?
Underveis vil vi lære hvordan vi flytter figurer rundt på skjermen, og hvordan
katter blir påvirket av gravitasjonskreftene fra jorden.

![Bilde av en katt i verdensrommet](astrokatt.png)
```

Merk at bildet `astrokatt.png` ligger i samme mappe som oppgaveteksten.

### Stegene

En god oppgave bygges i steg, slik at vi gjør en del om gangen. Det gjør det
enklere å holde styr på hvor langt brukeren har kommet i progammeringen, og gir
en mulighet for å sjekke om alt så langt er forstått.

Hvert steg skal inneholde en sjekkliste med ting som skal gjøres i rekkefølge.
De kan gjerne ha følge av forklarende tekst, spørsmål og lignende.

```
# Steg 1: Dette er starten på noe stort {.activity}

Her legger vi grunnlaget for det vi skal programmere.

- [ ] Start et nytt prosjekt i Scratch.

- [ ] Legg inn en ny figur.

Du kan prøve å flytte den nye figuren rundt på skjermen.
```

I tillegg til selve oppgaveteksten kan du legge til utfordringer `{.challenge}`,
tips `{.protip}` eller ting å prøve ut `{.try}`. Til slutt i hvert steg bør du
ha med en test av det som er gjort så langt, merket med `{.flag}`.

### Oppmuntringer og tips

Det er mange plasser det går an å kjøre seg fast når man programmerer. Selv om
du kan det du holder på med vil en nybegynner ha behov for mange vink i riktig
retning. Tenk gjennom hvilket nivå oppgaven skal være for! Er det en
ekspertoppgave kan du kanskje droppe noen av tipsene og kodeeksemplene, mens i
en nybegynneroppgave må du skrive nesten all koden slik at brukeren kan
sammenligne sin egen kode med noe som helt sikkert fungerer.

## lærerveiledning

I tillegg til oppgavene ønsker vi å ha lærerveiledninger til hver enkelt. Denne
kan inneholde mer informasjon om hva som må gjøres på forhånd, anbefalt
aldersnivå og så videre. Dersom du har gjort deg erfaringer med hvor brukerne
møter motstand i oppgaven, så kan du skrive hvordan du løste det.

Dessuten ønsker vi å informere om eventuelle kompetansemål i læreplanene som kan
oppfylles ved hjelp av hver enkelt oppgave. Det skrives i lærerveiledningen. Se
[her](guide_lage_lærerveiledning.md) for informasjon om hvordan du skriver en
lærerveiledning.
