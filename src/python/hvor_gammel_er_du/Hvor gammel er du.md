---
title: Hvor gammel er du?
level: 2
author: Sindre O. Rasmussen, Kodeklubben Trondheim
---

# Hvor gammel er du? {.intro}
I dette oppgavesettet skal du i hvert steg lære om noen av de grunnleggende byggeklossene i python. Oppgaven gir ingen kode, men forteller hva du skal lage og hvordan du skal gjøre det. Det er derfor viktig at du leser oppgaven for å vite hva du skal gjøre. Når du har gjort alle stegene vil du sitte igjen med et program som spør hvilket år du er født og regner ut alderen din. For hver oppgave du er ferdig med bør du spørre veilederne om de kan se om du har gjort riktig. Start ved å åpne en ny blank Python-fil.

# Del 1: Skrive ut til skjerm {.activity}
**Hva:** Vi kan be datamaskinen om å skrive hva som helst av tekst eller tall.

**Hvordan:** Funksjonen  `print()`  skriver ut det som er mellom `()` . Tekst må starte og slutte med  `'`  slik som  `'denne teksten'` 

**Eksempler, prøv dem ut og se hva som skjer:**
```python
print('Hei')
print(2)
print(2+2)
print('2+2')
```
Kan du forklare hvorfor det skjer?

Husk å ta bort eksemplene når du forsetter med oppgaven

## Gjøre selv{.check} 
**Skriv ut teksten under. Den skal dekke 3 linjer**

```
Hei, jeg er en datamaskin.
Jeg er derfor kjempeflink i matematikk.
Skal jeg vise deg?
```

# Del 2: Variabler {.activity}
**Hva:** Variabler gjør at vi kan lagre tekst eller tall i datamaskinen. Tenk på det som en eske som vi putter tall eller bokstaver inni. Utenpå skriver vi hva som er inni esken. Dette er variabelnavnet.

**Hvordan:** For å lage en variabel skriver du navnet på variabelen som du velger selv, deretter =, og så det du ønsker å putte i variabelen.

**Eksempler:** Prøv dem ut og se hva som skjer
```python
variabel = 4
petter = 'En gutt'
frida = 'En jente'
etTall = 3
endaEtTall = variabel + etTall

print(frida)
print(frida)
print(petter)
print(variabel-etTall)
print(endaEtTall)
```
Husk å ta bort eksemplene når du forsetter med oppgaven

## Gjøre selv {.check} 
**Fortsett under koden fra del 1**

- Lag to variabler som du selv gir navnet på. Den ene skal være lik året i år, altså 2015. Den andre skal være lik året du ble født i. 

- Lag så en tredje variabel, som du velger navn på selv. Hvordan kan du få denne til å bli lik alderen din ved hjelp av de to andre variablene?

- Skriv ut teksten: `'Jeg regnet ut at alderen din er:'`

- Skriv så ut variabelen som sier alderen din.

# Del 3: Input {.activity}
**Hva:** Input er en måte vi kan hente tekst som skrives på tastaturet

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
**Du skal nå endre på koden som du skrev i del 2**

Du skal nå bruke input slik at variabelen for året du er født settes ved hjelp av input i stedet for slik du gjorde i oppgave 2. Husk at året du skriver er et tall, ikke tekst.

# Del 4: If-setningen{.activity}

**Hva:** En if-setning er en måte vi kan bestemme hva datamaskinen skal gjøre basert på en bestemt betingelse som vi forteller den. (if betyr hvis på engelsk) Hvis betingelsen ikke oppfylles kan vi si noe annet som skal skje ved hjelp av else som er engelsk og betyr eller.

**Hvordan:** 
```python
if (hvis dette skjer):
	Gjør dette
elif(hvis dette skjer i stedet)
	Gjør dette
else:
	Gjør dette hvis ingen av de andre skjedde
```

**Her er noen eksempler på betingelser som står bak if og elif:**

`tall < 4`: Denne sier at tall må være mindre enn 4

`tall > 4`: Denne sier at tall må være større enn 4

`tall ==4`: Denne sier at tall må være lik 4

`tekst == 'Hei'`: Denne sier at tekst må være lik Hei

**Eksempel:** Prøv det ut og se hva som skjer

```python
tekst = 'heisann'
if tekst == 'hei':
	print('Teksten var hei')
elif tekst == 'hoho':
	print('Teksten var hoho')
else:
	print('Teksten var ikke hei eller hoho')
```
## Gjøre selv {.check}
**Du skal fortsette under koden fra del 3**

- Lag en ny variabel som tar inn tekst som input. Teksten som kommer opp når programmet spør om input skal være `'Stemmer det at du er så gammel? '`

- Skriv så en if-setning som sjekker om teksten i denne variabelen er `'ja'`

- Hvis teksten er ja, skal du skrive ut teksten: `'Der ser du, jeg er kjempeflink i matematikk'`

- Hvis teksten ikke var ja, skal du minke aldervariabelen med 1 og skrive den ut. Gjerne sammen med en forklarende tekst.



