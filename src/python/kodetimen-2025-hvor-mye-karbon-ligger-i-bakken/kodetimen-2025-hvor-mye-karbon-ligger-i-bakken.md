---
title: Kodetimen 2025; Hvor mye karbon ligger i bakken!
author: Nora Jeanett Tønnessen
language: nb
---
# Python-oppgave: Karbon i bakken

**Tallene i denne oppgaven kommer fra Klimaetaten i Oslo, og er basert på gjennomsnittsverdier for karbonlagring i skog, myr og i parker: [lenke til kilder](https://www.klimaoslo.no/rapport/kunnskap-om-karbonlagring-i-jord-i-bergen-stavanger-trondheim-oslo/)**
  
# Introduksjon {.intro}
  
Jorda vår lagrer store mengder karbon under bakken. Hvor mye karbon som lagres, avhenger av hva slags område det er - for eksempel en skog, en park eller en myr. I denne oppgaven skal du lage et program i python som regner ut hvor.

I denne oppgaven skal du bruke Python til å beregne hvor mye karbon som er lagret i bakken på et gitt areal (f.eks. skog). Du vil ta utgangspunkt i et gjennomsnittsnivå basert på m2. 

### Hva lærer du i denne oppgaven?
 - Å bruke ordbøker ***(dict)*** i Python


- Å hente ***input*** fra brukeren


- Å bruke en ***while-løkke*** for å kontrollere gyldig inndata


- Å gjøre enkle ***beregninger***


- Å formatere og vise informasjon med ***print()***


## Bakgrunn:
Trær lagrer CO₂ fra lufta som karbon (det er C-en i CO₂). 
Karbonet lagres i stammen, greinene og røttene, men faktisk blir mesteparten, rundt 80 prosent, lagret i jorda! 
Jorda fungerer altså som et stort karbonlager. Det er viktig at dette karbonet blir værende der, og ikke slippes ut igjen som CO₂,  for da øker mengden klimagasser i atmosfæren og bidrar til global oppvarming.

### Ulike typer vegetasjon lagrer forskjellig mengde karbon i jorden. Her er noen eksempler:

**Skog**

Skog på fast mark har et karbonlager i jorda på omkring 6 kg karbon per kvadratmeter. Mens skog på våtmark har 25 kg per m2. 

**Myr**

Myrer er store karbonlagre. De kan lagre hele 52 kg karbon per kvadratmeter. 

**Karbonlagre i byer**

Parker med gress kan lagre 8 kg karbon per m2, mens parker med mye trær kan lagre hele 21 kg/m2.  Hager kan lagre 12 kg/m2. 

# Oppgave{.activity}
### **1. Definer de ulike verdiene nevnt ovenfor og lag en ordbok (dictionary)**
Lag en ordbok som heter ***karbon***, der **nøkkelen** er navnet på arealtypen (f.eks. "***skog***") og **verdien** er hvor mye karbon som lagres per kvadratmeter (f.eks. 6).

***Lag en ordbok med alle verdiene  nevnt i bakgrunnsinformasjonen om de ulike typene vegetasjon! (Hint: 6 typer)***

Eksempel: 
```
karbon = {
    "skog": 6,
    "hage": 12,
}
```




### **2. Lag en meny med input()**
Programmet skal spørre brukeren hva slags areal de har. Brukeren kan velge én av arealtypene i ordboken.

Bruk en løkke (while) som fortsetter å spørre til brukeren har skrevet inn en gyldig arealtype.


Tips:

```
arealtype = ""
while arealtype not in karbon:
    arealtype = input("Hva slags areal har du? ")
```


### 3. Spør om størrelse på arealet
Når brukeren har valgt arealtype, skal programmet spørre hvor stort området er (i kvadratmeter).

Tips:
```python
areal = int(input("Hvor mange kvadratmeter? "))
```

### 4. Regn ut karbonlageret
Ganger du arealet med karbonverdien for den valgte arealtypen, får du det totale karbonlageret i kilogram.

Eksempel:
```python
total_karbon = areal * karbon[arealtype]
```


### 5. Skriv ut resultatet med en forklarende tekst

Til slutt skriver du ut resultatet, for eksempel:

200 kvadratmeter skog har et karbonlager på 1200 kg



## PRØV SELV! {.flag}




# Fasit:
```python

# Oppgave 1
karbon = {
    "skog": 6,
    "våtmarkskog": 25,
    "myr": 52,
    "gresspark": 8,
    "trepark": 21,
    "hage": 12,
}


# Oppgave 2
arealtyper = ", ".join(karbon)

# Oppgave 3
arealtype = ""
while arealtype not in karbon:
    arealtype = input(f"Hva slags areal har du? ({arealtyper}) ")


# Oppgave 4 
areal = int(input("Hvor mange kvadratmeter? "))


# Oppgave 5
total_karbon = areal * karbon[arealtype]
print(f"{areal} kvadratmeter {arealtype} har et karbonlager på {total_karbon} kg")
```






