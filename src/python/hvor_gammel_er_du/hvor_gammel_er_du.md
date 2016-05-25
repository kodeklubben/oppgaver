---
title: Hvor gammel er du?
level: 2
author: Sindre O. Rasmussen, Kodeklubben Trondheim
---

# Hvor gammel er du? {.intro}
I dette oppgavesettet skal du i hvert steg lære om noen av de grunnleggende byggeklossene i python. Oppgaven gir ingen kode, men forteller hva du skal lage og hvordan du skal gjøre det. Det er derfor viktig at du leser oppgaven for å vite hva du skal gjøre. Når du har gjort alle stegene vil du sitte igjen med et program som spør hvilket år du er født og regner ut alderen din. For hver oppgave du er ferdig med bør du spørre veilederne om de kan se om du har gjort riktig. Start ved å åpne en ny blank Python-fil.

# Del 1: Skrive ut til skjerm {.activity}
**Hva:** Vi kan be datamaskinen om å skrive hva som helst av tekst eller tall.

**Hvordan:** Funksjonen  `print()`  skriver ut det som er mellom `()` . Tekst må starte og slutte med  `'`  slik som  `'denne teksten'`.

**Eksempler:** Prøv dem ut og se hva som skjer.
```python
print('Hei')
print(2)
print(2+2)
print('2+2')
```
Kan du forklare det som skjer?

Husk å ta bort eksemplene når du forsetter med oppgaven

## Gjøre selv{.check}
**Skriv ut teksten under. Den skal dekke 3 linjer.**

```
Hei, jeg er en datamaskin.
Jeg er derfor kjempeflink i matematikk.
Skal jeg vise deg?
```

# Del 2: Variabler {.activity}
**Hva:** Variabler gjør at vi kan lagre tekst eller tall i datamaskinen. Tenk på det som en eske som vi putter tall eller bokstaver inni. Utenpå skriver vi hva som er inni esken. Dette er variabelnavnet.

**Hvordan:** For å lage en variabel skriver du navnet på variabelen som du velger selv, deretter `=` og det du ønsker å lagre i variabelen.

**Eksempler:** Prøv dem ut og se hva som skjer
```python
variabel = 4
petter = 'En gutt'
frida = 'En jente'
et_tall = 3
enda_et_tall = variabel + etTall

print(frida)
print(frida)
print(petter)
print(variabel - et_tall)
print(enda_et_tall)
```
Husk å ta bort eksemplene når du forsetter med oppgaven

## Gjøre selv {.check}
**Fortsett med koden du har fra del 1.**

- Lag to variabler som du selv gir navnet på. Den ene variabelen skal være dette året, altså 2015. Den andre variabelen skal være året du ble født i.

- Lag så en tredje variabel som skal inneholde alderen din. Hvordan kan du regne ut alderen ved hjelp av variablene i steget over?

- Skriv ut teksten: `Jeg regnet ut at alderen din er:`

- Skriv ut variabelen som inneholder alderen din.

# Del 3: Innputt {.activity}
**Hva:** Innputt er en måte vi kan hente tekst som skrives på tastaturet.

**Hvordan:**
Tekst hentes ved at du skriver: `input('Tekst som forteller hva en skal skrive')`

Skal man hente inn et tall: `int(input('Tekst som forteller hva en skal skrive'))`

**Eksempler:** Prøv dem ut og se hva som skjer
```python
navn = input('Skriv navnet ditt ')
print(navn)
tall = int(input('Skriv et tall '))
print(2+tall)
```

## Gjøre selv {.check}
**Du skal nå endre på koden som du skrev i del 2**.

- Bruk `input()` slik at variabelen for året du er født lagres ved hjelp av innputt når programmet kjøres.
- Test at det fungerer. Husk at året du skriver må være et tall, ikke tekst.

# Del 4: If-setningen{.activity}

**Hva:** En *if-setning* er en måte for å bestemme hva datamaskinen skal gjøre ved å sjekke om noe er sant (if* betyr *hvis* på engelsk). Dersom *if-setningen* ikke er sann kan vi be datamaskinen gjøre noe annet, og vi bruker da *else* som er engelsk for *eller*.

**Hvordan:**
```python
if dette_er_sant:
    gjor_dette()
elif noe_annet_er_sant:
    gjor_noe_annet()
else:
    ingen_av_if_setningene_er_sann()
```

Her er noen eksempler på hva som kan stå bak `if` og `elif`.

`tall < 4`: Sant hvis `tall` er mindre enn 4.

`tall > 4`: Sant hvis `tall` er større enn 4.

`tall == 4`: Sant hvis `tall` er lik 4.

`tekst == 'Hei'`: Sant hvis `tekst` er lik `'Hei'`.

`'nei' in tekst`: Sant hvis ordet *nei* er inni `tekst`.

**Eksempel:** Prøv det ut og se hva som skjer.

```python
tekst = 'Heisann'
if tekst == 'Hei':
    print('Teksten er lik Hei')
elif tekst == 'Hoho':
    print('Teksten er lik Hoho')
elif 'Hei' in tekst:
    print('Hei er inni teksten')
else:
    print('Teksten er ikke Hei eller Hoho og Hei er ikke inni teksten')
```
## Gjøre selv {.check}
**Fortsett med koden fra del 3.**

- Lag en ny variabel som tar inn tekst som innputt. Teksten som kommer opp når programmet spør om innputt skal være `Stemmer det at du er så gammel?`

- Skriv en *if-setning* som sjekker om teksten i variabelen er `ja`.

- Hvis teksten er `ja`, skriv ut teksten: `Der ser du, jeg er kjempeflink i matematikk!`

- Hvis teksten ikke er `ja`, mink aldervariabelen med 1 og skriv ut den riktige alderen i lag med en forklarende tekst.
