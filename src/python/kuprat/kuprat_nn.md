---
title: test
author: 

language: nn
---



# Introduksjon {.intro}

I denne kurset skal me introdusere programmeringsspråket Python. Dette er eit
veldig populært programmeringsspråk som kan brukast til det meste. Python
brukast av mange av dei største og mest kjente selskapa i verda, til dømes
Google, NASA og CERN.

Me startar ganske enkelt med å sjå på korleis me kan lage små program i Python
som kan lese og vise tekst. Spesielt skal me lage vår eigen versjon av eit
historisk program som heiter [Cowsay](http://www.cowsays.com/)) der ei smart ku
spreier visdommen sin.

![Bilete av ei ASCII-ku som pratar!](kuprat.png )


# Steg 1: Hei, Verda {.activity}

For å sjekke at Python fungerer som det skal lagar me eit kjempeenkelt program.
Me vil berre skrive ei enkel helsing på skjermen.

## Sjekkliste {.check}

- [ ] Åpne IDLE, editoren som følgjer med Python. Me vil bruke denne til både å
  skrive og køyre programma me skriv.

  **Windows**: Åpne IDLE frå startmenyen.

  **Mac**: Åpne terminal.app, skriv `idle` og trykk enter.

  **Linux**: Åpne ein terminal, skriv `idle` og trykk enter.

  Dette vil åpne eit vindauge som heiter `Python Shell`. Viss du ikkje finn
  IDLE, eller vindauget ikkje åpnar seg, så kan det vere at Python ikkje er
  installert. I så fall kan du laste ned siste versjon frå
  [http://www.python.org/](http://www.python.org/). Spør gjerne om hjelp til
  dette om det er nødvendig.

- [ ] Vindauget `Python Shell` som åpna seg er der du vil sjå resultatet av
  programmet ditt. For å skrive eit nytt program må me åpne eit
  programmeringsvindauge i tillegg. I menyen, vel `File > New File`. Pass på at
  begge vindauga er synlege.

- [ ] I dette nye vindauget skal me skrive vårt fyrste Python-program. Skriv
  følgjande:

  ![Bilete av print('hei på deg')](hei_program.png )

- [ ] No skal me lagre og køyre dette programmet. Vel `File > Save`, og gi
  programmet ditt namnet `hei.py`. Så kan du køyre programmet ved å klikke `Run
  > Run Module`. No skal du sjå at Python skriv ei lita helsing i det fyrste
  vindauget.

  ![Bilete av at Python skriv ut "hei på deg"](hei_kjor.png )

  Gratulerer! No har du skrive og køyrt det fyrste Python-programmet ditt!

### Feilmeldingar {.protip}

Python krever at du er veldig nøyaktig når du programmerer, og viss du skriv
noko Python ikkje forstår vil den skrive ei feilmelding til deg når du vel `Run
> Run Module`. Du har kanskje allereie opplevd dette! Viss ikkje kan du prøve å
byte ut `print` med `pint` i koden din, og prøve å køyre programmet ein gong
til.

Når du får ei feilmelding må du gå attende til koden, og sjekke ekstra nøye at
du har skrive alt riktig. Dette vil bli enklare etter kvart som du får meir
trening i å programmere.

## Sjekkliste {.check}

- [ ] Det fyrste programmet vårt besto berre av ein kommando, nemleg funksjonen
  `print` som brukast for å fortelje Python at me vil skrive ut noko på
  skjermen. Det me vil skrive til skjermen set me inn i parentesar. I det
  tilfellet ville me at Python skulle skrive teksten `Hei på deg!`. For å
  fortelje Python at `Hei på deg!` skal tolkast som rein tekst og ikkje som ein
  Python-kommando må me skrive teksten i fnuttar `'`.

- [ ] Me kan enkelt endre på det Python skriv til skjermen. Prøv å endre
  programmet ditt til dette:

  ```python
  print('Hei, alle saman!')
  ```

  Lagre fila på nytt og køyr programmet.

- [ ] Prøv å endre teksten til noko du finn på sjølv, og køyr programmet att!

### Python-filer {.protip}

Me har akkurat laga eit Python-program som heiter `hei` og som me har lagra i ei
vanleg tekstvil med namnet `hei.py`. Python kallar ei slik tekstfil for ein
`module`. Du kan sjølv bestemme kva du vil kalle Python-programma dine, men
filene med programmet må ha endinga `.py` for at Python skal kjenne dei att.

Det er òg ein god idé å unngå å bruke norske teikn som `æ`, `ø` og `å`, samt
mellomrom i programnamnet. I staden for mellomrom kan du bruke understrek, `_`,
til dømes `mitt_program.py`.


# Steg 2: Kva heiter du? {.activity}

Me skal sjå korleis me kan få Python til å stille oss spørsmål. For å gjere
dette brukar me ein ny funksjon som heiter `input`.

Når du brukar funksjonen `input` ventar datamaskina di med å køyre reisten av
programmet til du har skrive noko og trykka enter-tasten på tastaturet.

## Sjekkliste {.check}

- [ ] Endre programmet ditt så det ser slik ut:

  ```python
  namn = input('Kva heiter du? ')
  print('Hei, ' + namn)
  ```

  Lagre og køyr programmet. Skriv inn namnet ditt når du blir spurt om det, og
  trykk enter-tasten. Helsar Python deg med namn?

- [ ] For at teksten skal sjå bra ut må du passe på at du brukar mellomrom. Det
  ser best ut med eit mellomrom mellom `?` og `'` i input-funksjonen, og eit
  mellomrom mellom `Hei,` og `'` i print-funksjonen.

- [ ] Legg merke til at i programmet brukar me ein variabel `namn` som hugsar
  namnet du skriv inn. Slike variablar brukar me heile tida når me programmerer.
  Variablar blir laga automatisk når me brukar `=`. Du kan bestemme kva
  variablane skal heite sjølv, og det er lurt å velje namn som beskriv det
  variabelen skal hugse for deg.

- [ ] Prøv å leggje inn fleire linjer i programmet ditt. Kanskje Python kan
  spørje deg om kor du bur, kven som er bestevenen din eller kanskje kva som er
  favorittfarga di? Bruk variablar for å hugse desse tinga slik at Python kan
  skrive dei tilbake på skjermen etterpå.

### Hurtigtastar {.protip}

Når me programmerer kan det vere greitt å sleppe å leite inne i menyen for å
lagre og køyre programma. I staden kan me bruke hurtigtastar. Viss du ser etter
i menyen vil du sjå at til høgre for kommandoane står hurtigtastane lista opp.
Til dømes kan du trykke `ctrl + S` for å lagre (`cmd + S` på Mac) eller `F5` for
å køyre programmet (`fn + F5` på Mac).


# Steg 3: Kuprat {.activity}

No skal me lage ein enkel versjon av det klassiske programmet
[Cowsay](http://www.cowsays.com), som vart laga av Tony Monroe. Med dette
programmet kan du få ei stilig ku til å seie omtrent kva som helst.

## Sjekkliste {.check}

- [ ] Me startar med å teikne kua. Start eit nytt IDLE-vindauge ved å velje
  `File > New File`. Skriv inn følgjande program:

  ```python
  print('^__^')
  print('(oo)\_______')
  print('(__)\       )')
  print('    ||----W |')
  print('    ||     ||')
  ```

  Lagre programmet som `kuprat.py` og køyr det. Ei ganske stilig ku!

- [ ] Men no må me få kua til å seie noko. Legg til og endre kodelinjene dine
  slik at dette ser bra ut:

  ```python
  print(' _____________________')
  print('< Python er morosamt! >')
  print(' ---------------------')
  print('     \   ^__^')
  print('      \  (oo)\_______')
  print('         (__)\       )')
  print('             ||----W |')
  print('             ||     ||')
  ```

- [ ] No kan me bruke det me har lært tidlegare for å enkelt endre på meldingane
  kua seier. Ved hjelp av `input` kan me spørje om kva kua skal seie. Endre
  programmet så det ser slik ut:

  ```python
  melding = input('Kva skal kua seie? ')

  print(' ____________________')
  print('< ' + melding + ' >')
  print(' --------------------')
  print('     \   ^__^')
  print('      \  (oo)\_______')
  print('         (__)\       )')
  print('             ||----W |')
  print('             ||     ||')
  ```

- [ ] Korleis verkar programmet når du køyrer det no? Prøv med ulike tekstar.
  Ser du eit problem?

- [ ] Snakkebobla til kua er ikkje tilpassa lengda av meldinga, så av og til
  blir snakkebobla for stor, av og til for liten. For å fikse det skal me bruke
  ein ny funksjon, `len` (`len` er ei forkorting for *length* som tyder lengde).
  Denne kan finne lengda til ein tekst. For å teste funksjonen, prøv å leggje
  inn denne linja rett etter `input`-linja i programmet ditt:

  ```python
  print(len(melding))
  ```

  Dette vil skrive ut lengda av meldinga før kua blir skrive ut.

- [ ] Me kan bruke lengda av meldinga for å rekne ut kor lang snakkebobla må
  vere. Sidan me har mellomrom på begge sider av meldinga bør snakkebobla vere
  to teikn lengre enn meldinga.

  ```python
  boblelengde = len(melding) + 2
  ```

- [ ] For å teikne snakkebobla kan me bruke eit Python-triks som kan repetere
  tekst. Me har allereie sett at me kan setje saman tekst ved å bruke `+`, til
  dømes `'Hei, ' + namn`. For å repetere tekst kan vi gange den med eit tal. Til
  dømes vil `'hei' * 3` bli til `'heiheihei'`. Difor kan me gange `'-'` med
  snakkeboblelengda for å teikne snakkebobla i riktig storleik.

- [ ] Endre programmet ditt så det ser slik ut:

  ```python
  melding = input('Kva skal kua seie? ')
  boblelengde = len(melding) + 2

  print(' ' + '_' * boblelengde)
  print('< ' + melding + ' >')
  print(' ' + '-' * boblelengde)
  print('     \   ^__^')
  print('      \  (oo)\_______')
  print('         (__)\       )')
  print('             ||----W |')
  print('             ||     ||')
  ```

  Lagre og køyr programmet. Får snakkebobla riktig storleik?

### Prøv sjølv {.challenge}

Kan du teikne andre dyr eller figurar som òg kan snakke? Prøv eventuelt å gjere
små endringar på utsjånaden til kua, til dømes kan du forandre augene (med `--`
ser ho ut som ho søv) eller kanskje leggje til ei tunge?

Du kan òg leggje til fleire ulike figurar i same program, slik at det virkar som
dei snakkar saman. Prøv deg fram!