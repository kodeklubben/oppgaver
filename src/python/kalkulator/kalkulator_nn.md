---
title: Kalkulator
author: Ole Kristian Pedersen, Kodeklubben Trondheim
translator: Stein Olav Romslo
language: nn
---


# Kalkulator {.intro}

I denne oppgåva skal du lage ein kalkulator heilt på eiga hand Det er meininga
at du skal skrive all koden sjølv, men du får nokre hint for å hjelpe deg på
veg.

Me vil at kalkulatoren skal kunne addere (`+`), subtrahere (`-`), multiplisere
(`*`) og dividere (`/`). Me kallar `+`, `-`, `*` og `/` for *operatorar*, og i
denne oppgåva skal du lage ein funksjon for kvar operator (du kan til dømes
kalle dei `add`, `subtract`, `multiply` og `divide`, som er dei engelske namna
på operasjonane operatorane gjer). Kvar funksjon skal ha to tal som parametrar,
og skal både utføre rekneoperasjonen og skrive ut svaret.

Brukaren skal sjølv skrive inn kva rekneoperasjon som skal utførast.

Døme på bruk av programmet:

![Illustrasjon av ein ferdig kalkulator](python_calculator.png)


# Klar, ferdig, programmer! {.activity}

Då er det berre å setje i gang!

Her er nokre ting å tenke på:

- Korleis avgjer du kva operasjon som skal utførast?

- Har rekkefølgja på tala noko å seie? Er `4-2` lik `2-4`?

- Viss du står fast kan det vere lurt å lese tipsa i dei gule boksane.

## int() {.protip}

Når du får input frå brukaren får du ein *tekststreng*, sjølv om brukaren skreiv
inn eit tal. Då er det greitt å kunne konvertere teksten til eit tal, ved å
bruke `int()`.

Kva er skilnaden på desse kodesnuttane? Du kan køyre koden og teste sjølv.

```python
tal = input("Skriv eit tal: ")
svar = 3 + tal
print(svar)
```

```python
tal = int(input("Skriv eit tal: "))
svar = 3 + tal
print(svar)
```

## Funksjonar med parametrar {.protip}

Ein funksjon blir deklarert, altså definert, ved hjelp av `def`-nøkkelordet. Den
kan brukast ved å skrive funksjonsnamnet med parentesar bak.

**Døme:**

```python
def hello_word():
    print("Hello World!")

hello_world()
```

Ein funksjon som har *parametrar* blir deklarert med parametrar på innsida av
parentesane i definisjonen av funksjonen.

**Døme:**

```python
def greet(firstName, lastName):
    print("Hello, " + firstName + " " + lastName)
```

Når me kallar funksjonen seinare, så gir me den *argument*.

**Døme:**

```python
greet("Ola", "Nordmann")
```

Du la kanskje merke til skiljet mellom *parametrar* og *argument*. Ein parameter
er namnet me gir variabelen i funksjonsdefinisjonen, slik som `firstName` og
`lastName`. Argument er dei verdiane me gir til funksjonen når me kallar den,
slik som `"Ola"` og `"Nordmann"`.


# Test programmet {.activity}

- [ ] Fungerer programmet som det skal? Viss ikkje må du rette på det.

## Delt på null {.challenge}

- [ ] Kva skjer når du deler på null? Prøv til dømes `4 / 0`.

Viss programmet ditt feilar no, så har du truleg ein delt-på-null-feil. Ein kan
nemleg ikkje dele på null! Fiks programmet ditt slik at programmet skriv ut `"Du
kan ikkje dele på null!"` viss brukaren prøver å dele på null. Slik:

![Bilete av å prøve å dele på null i programmet](python_calculator_zero_division.png)

## Fleire utrekningar {.challenge}

- [ ] Endre programmet ditt slik at brukaren kan skrive inn kor mange
  utrekningar kalkulatoren skal utføre. Då vil programmet fungere slik:

![Bilete av korleis programmet virkar når brukaren kan velje antal
utrekningar](python_calculator_multiple_calculations.png)

## Fleire operasjonar {.challenge}

- [ ] Prøv å leggje til fleire operatorar. Du kan til dømes leggje til
  `**`-operatoren. Den opphøger eit tal i eit anna. Til dømes er `2**3` lik `8`
  fordi `2*2*2` er lik `8`.

- [ ] Kjem du på andre operatorar som kan leggjast til i kalkulatoren din?
