---
title: Tallgjetting
level: 1
author: Steffen Granberg
---

#Introduksjon
I denne oppgaven skal vi lage et spill vi kan spille mot datamaskinen. Datamaskinen genererer et tilfeldig tall mellom 1-20 og man skal prøve å gjette dette på færrest mulig forsøk. Klarer du å finne ut hvilket tall den tenker på?

#Steg 1: Les inn navnet ditt {.activity}
Det første vi skal gjøre er å lese inn spillerens navn.

## Sjekkliste {.check}
+ Åpne IDLE, og åpne en ny fil.
+ Skriv inn følgende kode:

    ```python
    navn = input('Navn: ')

    ```

## Test prosjektet {.flag}

+ Lagre programmet og kjør det ved å trykke f5 (eller ved å velge ```run -> Run Module``.
+ Spør datamaskinen om navnet ditt? 

## Kommentering av kode {.protip}
For å gjøre koden  lettere å forstå kan vi legge inn kommentarer som ikke påvirker programmet. Dette gjør vi ved å skrive inn tegnet ```#```. All tekst som kommer på samme linje etter dette tegnet vil bli ignorert av datamaskinen, men er veldig fint for oss mennesker. Heretter bruker jeg dette for å forklare hva som skjer, du trenger ikke å skrive inn kommentarene hvis du ikke vil!

#Steg 2: Generere tilfeldig tall {.activity}
Nå vil vi at datamskinen skal generere et tilfeldig tall mellom 1-20.

## Sjekkliste {.check}
+ For at datamaskinen skal klare dette trenger den å hente inn et bibliotek som har disse funksjonene. Skriv inn denne koden øverst i filen din:

    ```python
    from random import randint  
    ```
+ Nå vil vi at datamaskinen skal generere et tilfeldig tall. I samme filen, gjør om koden din så den ser ut slik:

    ```python
    from random import randint
    fasit = randint(1, 20)

    navn = input('Navn: ')
    ```
+ For at vi skal kunne bruke æøå i spillet vårt må vi legge til noe i koden vår. Gjør om koden til dette:

    ```python
    #!/usr/bin/python
    # -*- coding: UTF-8 -*-

    from random import randint
    fasit = randint(1, 20)

    navn = input('Navn: ')
    ```
+ La oss skrive ut dette tallet til skjermen. Siden fasit er et **tall** må vi gjøre om dette til en **streng** slik at det kan skrives ut på skjermen. Dette gjør vi ved å bruke ```str(fasit)``` Legg denne til slik du ser her:

    ```python
    #!/usr/bin/python
    # -*- coding: UTF-8 -*-

    from random import randint  # Henter inn bibliotek
    fasit = randint(1,20)       # Generer et tilfeldig tall.
    print(str(fasit))           # Skriver ut tallet.
    navn = input('Navn: ')      # Spør og leser inn navnet til spilleren.
    ```

## Test prosjektet {.flag}

+ Kjør koden.
+ Skrives det ut et tall mellom 1-20?
+ Spør den om navnet ditt?


# Steg 3: Gjett tallet! {.activity}
## Sjekkliste {.check}

+ Nå skal vi prøve å gjette tallet! Gjør om koden din slik at den ser ut som dette:

    ```python
    #!/usr/bin/python
    # -*- coding: UTF-8 -*-

    from random import randint
    fasit = randint(1, 20)
    antallforsøk = 0       # Her lagrer vi hvor mange ganger brukeren har gjettet.

    navn = input("Navn: ")
    print ('Hei ' + navn + ', jeg tenker på ett tall mellom 1 og 20.')
    ```

+ Nå skal vi legge inn selve gjettingen. Vi vil at spilleren maks skal kunne gjette 6 ganger før han taper spillet.
Gjør om koden din slik at den ser ut som dette:

    ```python
    #!/usr/bin/python
    # -*- coding: UTF-8 -*-

    from random import randint
    fasit = randint(1, 20)

    antallforsøk = 0

    navn = input("Navn: ")
    print ('Hei ' + navn + ', jeg tenker på ett tall mellom 1 og 20.')

    while antallforsøk < 6:         # Test for å se om brukeren har brukt opp maks antall forsøk.
        print('Antall mulige forsøk igjen: ' + str(6-antallforsøk))
        tall = input('Gjett et tall: ')
        tall = int(tall)            # Gjør om strengen til tall.

        antallforsøk = antallforsøk + 1  # Plusser på med 1 for hvert forsøk.
    ```

## Test prosjektet {.flag}

+ Kjør koden.
+ Får du spørsmål om å gjette et tall?
+ Slutter programmet etter at du har gjettet 6 ganger?

## While-løkke {.protip}
I programmering har vi ofte behov for å gjøre ting flere ganger. Vi kan selvfølgelig skrive den samme koden mange ganger, men dette er derimot mye ekstra arbeid. Derfor har vi i noe vi kaller løkker. Løkker hjelper oss med å utføre noen deler av koden flere ganger. En while-løkke er en slik løkke. Den gjentar noe inntil en betingelse er møtt. For eksempel i programmet vårt bruker vi ```while antallforsøk < 6```. Dette betyr: så lenge antall gjettinger er mindre en 6, gjør koden inne i løkken. Koden inne i løkken vår er : 
```python 
print('Antall mulige forsøk igjen: ' + str(6-antallforsøk))
tall = input('Gjett et tall: ')
tall = int(tall)          

antallforsøk = antallforsøk + 1
```   
Denne koden kjøres så lenge betilgelsen vår en **sann**. Når antallforsøk blir 6 eller større, vil den slutte å kjøre løkken å fortsette videre i koden. 

# Steg 4 Sjekk om gjettingen er riktig. {.activity}
Nå skal vi sjekke om spilleren gjetter riktig.

## Sjekkliste {.check}

+ Nå vil vi at datamaskinen skal merke om tallet spilleren gjetter er for lite, stort eller riktig. Til dette bruker vi ```if-setninger``` Gjør om koden din, slik at den bli seende slik ut:

    ```python
    #!/usr/bin/python
    # -*- coding: UTF-8 -*-

    from random import randint
    fasit = randint(1, 20)

    antallforsøk = 0;

    navn = input("Navn: ")
    print ('Hei ' + navn + ', jeg tenker på ett tall mellom 1 og 20.')

    while antallforsøk < 6:
        print('Antall mulige forsøk igjen: ' + str(6-antallforsøk))
        tall = input('Gjett et tall: ')
        tall = int(tall)

        if tall < fasit:                    # Kjør denne koden hvis tallet er for lavt
            print('Tallet er for lite')
        elif tall > fasit:                  # Kjør denne koden hvis tallet er for høyt
            print('Tallet er for stort')
        elif tall == fasit:                 # Kjør denne koden hvis tallet er riktig
            break                           # Avslutt while-løkken.

        antallforsøk = antallforsøk + 1
    ```

## if-setninger {.protip}
I programmet vårt vil vi at datamaskinen skal ta noen valg. for å gjøre disse valgene lager vi if-setninger. Den første if-setningen vår ```if tall < fasit``` betyr *hvis* tallet spilleren gjetta, er mindre en fasit, gjør det som står inne i if-setningen. Vi vil også at den skal gjøre noe annet hvis tallet er **større** enn fasit, og enda en ting hvis tallet faktisk er det tallet datamskinen tenker på. Derfor setter vi inn flere if-setninger. Når vi har flere enn en, bruker vi ```elif```. Dermed blir de to neste ```elif tall > fasit``` og ```elif tall == fasit ```. Legg merke til at når vi skal sjekke om noe er likt bruker vi ```== ``` og ikke ```=```. 

## Test prosjektet {.flag}
+ Kjør koden
+ Merker den at tallet du skriver inn er større eller mindre enn datamaskinens hemmelige tall? 
+ Avslutter den programmet hvis du gjetter mer enn 6 ganger? 
+ Avslutter den programmet hvis du gjetter riktig? 

#Steg 5: Skriv seiersmelding. {.activity}
Nå har vi nesten et fullverdig spill, men vi trenger å skrive ut en seiersmelding hvis spilleren gjetter riktig tall. Og en annen melding om den ikke klarer å gjette riktig tall på 6 forsøk. 

## Sjekkliste {.check}
+ Vi må nå legge til noe på slutten av koden. For nå vil vi sjekke om tallet brukeren gjetta er det samme som datamaskinens hemmelige tall etter at ```while antallforsøk < 6```er ferdig. Gjør om koden din slik at den ser ut som dette: 

```python 
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from random import randint
fasit = randint(1, 20)

antallforsøk = 0;

navn = input("Navn: ")
print ('Hei ' + navn + ', jeg tenker på ett tall mellom 1 og 20.')

while antallforsøk < 6:
    print('Antall mulige forsøk igjen: ' + str(6-antallforsøk))
    tall = input('Gjett et tall: ')
    tall = int(tall)

    if tall < fasit:                
        print('Tallet er for lite')
    elif tall > fasit:              
        print('Tallet er for stort')
    elif tall == fasit:             
        break                           

    antallforsøk = antallforsøk + 1

if tall == fasit:                   # Kjør denne koden hvis tallet som er gjetta er riktig. 
    print('Riktig, bra jobbet!')
else:                               # Ellers (ikke riktig), kjør denne koden: 
    print('Beklager, du klarte det ikke. Jeg tenkte på tallet ' + str(fasit)) 
```

## else {.protip}
Nå brukte vi enda en ting som hører til under if-setninger: ```else```. Dette betyr: hvis ingen if-setninger stemmer, så vil vi kjøre denne koden. Vi bruker den slik: 
```python
if tall == fasit:                  
    print('Riktig, bra jobbet!')
else:                               
    print('Beklager, du klarte det ikke. Jeg tenkte på tallet ' + str(fasit)) 
```
Hvs tall er likt fasit gjør man det som står inne i if-setningen. **Ellers** (```else```) så gjør det som står inne i else-setningen. Dette er nyttig når vi har if-setninger. Vi vil ofte at datamaskinen skal gjøre noe hvis den ikke finner noen if-setninger som stemmer.

## Test prosjektet {.flag}

+ Kjør koden
+ Skriver den seiersmelding hvis du gjetter riktig?
+ Skriver den ut en annen melding hvis du ikke gjetter riktig? 

## Oppgave: Utvid spillet, bare fantasien setter grenser {.challenge}
+ Få datamaskinen til å tenke på et tall mellom 1-100? Eller et annet intervall.
+ Gi spilleren 10 forsøk istedet for 6. 
+ Legg til en mulighet for å spille en gang til etter man har spilt en gang. (Denne kan være litt vanskelig hvis du ikke har programmert mye før.)
+ Noen kodelinjer i dette programmet kunne vært unngått ved å skrive flere kommandoer på samme linje. Klarer du å gjøre koden noe kortere? 
+ Andre ting du kan gjøre for å gjøre spillet mer spennende? 
