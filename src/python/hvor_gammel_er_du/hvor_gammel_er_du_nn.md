---
title: Kor gamal er du?
author: Sindre O. Rasmussen, Kodeklubben Trondheim
translator: Stein Olav Romslo
language: nn
---


# Kor gamal er du? {.intro}

I denne oppgåva lærer du om nokre av dei grunnleggjande byggjeklossane i Python
i kvart steg. Oppgåva gir deg ikkje noko kode, men fortel kva du skal lage og
korleis du skal gjere det. Difor er det viktig at du les oppgåva for å vite kva
du skal gjere. Når du har gjort alle stega vil du sitje att med eit program som
spør kva år du er fødd og reiknar ut alderen din. For kvart steg du er ferdig
med bør du spørje ein rettleiar om dei kan sjekke at det du har gjort ser riktig
ut. Start ved å åpne ei ny blank Python-fil.


# Del 1: Skrive ut til skjerm {.activity}

**Kva:** Me kan be datamaskina om å skrive kva som helst av tekst eller tal.

**Korleis:** Funksjonen `print()` skriv ut det som er mellom `()`. Tekst må
starte og slutte med `'` slik som `'denne teksten'`.

**Døme:** Prøv dei ut og sjå kva som skjer.

```python
print('Hei')
print(2)
print(2+2)
print('2+2')
```

- [ ] Kan du forklare det som skjer?

- [ ] Hugs å ta bort døma når du fortset med oppgåva.

## Gjere sjølv {.check}

**Skriv ut teksten under. Den skal dekke 3 linjer.**

```
Hei, eg er ei datamaskin.
Difor er eg kjempeflink i matematikk.
Skal eg vise deg?
```


# Del 2: Variablar {.activity}

**Kva:** Variablar gjer at me kan lagre tekst eller tal i datamaskina. Tenk på
det som ei eske me puttar tal eller bokstavar inni. Utanpå skriv me kva som er
inne i eska. Dette er variablenamnet.

**Korleis:** For å lage ein variabel skriv du namnet på variabelen som du vel
sjølv, så `=` og det du vil lagre i variabelen.

**Døme:** Prøv dei ut og sjå kva som skjer.

```python
variabel = 4
petter = 'Ein gut'
frida = 'Ei jente'
eit_tal = 3
eit_nytt_tal = variabel + eit_tal

print(frida)
print(frida)
print(petter)
print(variabel - eit_tal)
print(eit_nytt_tal)
```

Hugs å ta bort døma når du fortset med oppgåva.

## Gjere sjølv {.check}

**Fortset med koden du har frå steg 1.**

- [ ] Lag to variablar som du sjølv gir namnet på. Den eine variabelen skal vere
  dette året, altså <span id="aar">2018</span>. Den andre variabelen skal vere
  året du vart fødd. <script>document.getElementById('aar').innerHTML = new
  Date().getFullYear()</script>

- [ ] Lag ein tredje variabel som skal innehalde alderen din. Korleis kan du
  rekne ut alderen din med variablane i steget over?

- [ ] Skriv ut teksten: `Eg rekna ut at alderen din er:`

- [ ] Skriv ut variabelen som inneheldt alderen din.


# Del 3: Input {.activity}

**Kva:** Input er ein måte me kan hente tekst som blir skrive inn på tastaturet.

**Korleis:** Tekst blir henta ved at du skriv: `input('Tekst som fortel kva ein
skal skrive')`

Skal ein hente inn eit tal: `int(input('Tekst som fortel kva ein skal skrive'))`

**Døme:** Prøv dei ut og sjå kva som skjer.

```python
navn = input('Skriv namnet ditt ')
print(navn)
tal = int(input('Skriv eit tal '))
print(2+tal)
```

## Gjere sjølv {.check}

**No skal du endre på koden som du skreiv i steg 2.**

- [ ] Bruk `input()` slik at variabelen for året du er fødd blir lagra ved hjelp
  av input når programmet køyrer.

- [ ] Test at det fungerer. Hugs at året du skriv må vere eit tal, ikkje tekst.


# Del 4: If-setningar {.activity}

**Kva:** Ei *if-setning* er ein måte å bestemme kva datamaskina skal gjere ved å
*sjekke om noko er sant (*if* tyder *viss* på engelsk). Viss *if-setninga* ikkje
*er sann kan me be datamaskine gjere noko anna, og då brukar me *else* - engelsk
*for *eller*.

**Korleis:**

```python
if dette_er_sant:
    gjer_dette()
elif noe_annet_er_sant:
    gjer_noko_anna()
else:
    ingen_av_if_setningane_er_sanne()
```

Her nokre døme på kva som kan stå bak `if` og `elif`.

`tal < 4`: Sant viss `tal` er mindre enn 4.

`tal > 4`: Sant viss `tal` er større enn 4.

`tal == 4`: Sant viss `tal` er lik 4.

`tekst == 'Hei'`: Sant viss `tekst` er lik `'Hei'`.

`'nei' in tekst`: Sant viss ordet *nei* er inni `tekst`.

**Døme:** Prøv det ut og sjå kva som skjer.

```python
tekst = 'Heisann'
if tekst == 'Hei':
    print('Teksten er lik Hei')
elif tekst == 'Hoho':
    print('Teksten er lik Hoho')
elif 'Hei' in tekst:
    print('Hei er inni teksten')
else:
    print('Teksten er ikkje Hei eller Hoho, og Hei er ikkje inni teksten')
```

## Gjere sjølv {.check}

**Fortset med koden frå steg 3.**

- [ ] Lag ein ny variabel som tek inn tekst som input. Teksten som kjem opp når
  programmet spør om input skal vere `Stemmer det at du er så gamal?`

- [ ] Skriv ei *if-setning* som sjekkar om teksten i variabelen er `ja`.

- [ ] Viss teksten er `ja`, skriv ut teksten: `Der ser du, eg er kjempeflink i
  matematikk!`

- [ ] Viss teksten ikkje er `ja`, trekk frå 1 frå aldervariabelen, og skriv ut
  den riktige alderen med ein forklarande tekst.
