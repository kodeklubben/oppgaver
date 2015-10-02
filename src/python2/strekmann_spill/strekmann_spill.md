---
title: Strekmann spill
level: 3
Author: Ole Andreas Ramsdal, Kodeklubben Trondheim
---

# Introduksjon {.intro}

I denne oppgaven skal du lage et spill der du styrer en strekmann som skal hoppe over hindringer.

![](skjermdump.png "Slik ser spillet ut")

# Steg 1: Ny fil {.activity}

Lag en ny fil.

Vi starter med å bestemme hvor stort vindu hvis skal bruke:

```python
WIDTH = 550
HEIGHT = 250
```
+ Lagre og kjør programmet, se at du får opp et vindu.

# Steg 2: Hindringer {.activity}

+ Du skal nå lage boksene som strekmannen løper mot. Dette skal du gjøre ved hjelp av en klasse.

Klassen skal hete Box og skal ha egenskapene:
height, width, color, x, y og en funkson som heter draw()

```python
class Box:
    # Skriv egenskaper her

    def draw(self):
    	# Skriv koden som tegner boksen her
```
**Tips:**
Denne koden tegner en boks som har det øverste venstre hjørnet i origo, er 50 piksler høy og bred, og har fargen rød:
```python
screen.draw.filled_rect( Rect((0, 0), (50, 50)) , (255, 0, 0))
```
og denne koden tegner en boks som har det øverste venstre hjørnet i punktet (25, 25) , er 100 piksler høy og bred, og har fargen blå:
```python
screen.draw.filled_rect( Rect((25, 25), (100, 100)) , (0, 0, 255))
```

+ Opprett en boks ved å legge til denne linjen i koden:
```python
box = Box()
```

+ Lagre og kjør programmet og se at du ikke får noen feilmeldinger. 

+ Hvis du vil se boksen i vinduet må du først tegne den. Dette gjør du med draw() funksjonen.

# Steg 3: Strekmann {.activity}

+ Du må nå gjøre at strekmannen blir med: 

Til dette skal vi bruke en klasse som heter Actor som allerede finnes i Pygame Zero. 

```python
stick_man = Actor('running_man')
stick_man.bottomleft = 50, HEIGHT
```

Første linje i koden sier at variabelen som heter stick_man er en 'Actor' som er bildet som heter 'running_man'. 

Andre linje setter posisjonen til nedre høyre hjørne av strekmannen til å være punktet (50, HEIGHT)

 + For at denne koden skal kjøre må du lagre bildet under som 'running_man.png' i en mappe som heter 'images' der du har lagret kodefilen.

![](running_man.png "Strekmann")

Slik:

![](mappestruktur.png "Mappestruktur")

# Steg 4: De globale funksjonene draw() og update()  {.activity}

Alle spill i Pygame Zero må ha to globale funksjoner som heter draw() og update().

Det som står i draw-funksjon skal sørge for at som skal vises i spillviduet blir tegnet.

Det som står i update-funksjonen gjør alle endringer i spillet mellom hver gang tingene tegnes.

+ Vi trenger følgende kode i den globale draw(), pass på at du forstår hva koden gjør.

```python
def draw():
	screen.clear()
	screen.fill((255, 255, 255))
	stick_man.draw()
	box.draw()
```

+ Du må nå skrive koden i update().
Du trenger følgende:
	- Få boksen til å flytte seg mot venstre.
	- Sjekke om boksen er ute av bildet på venstre side av vinduet. Hvis det, flytt den til høyre side av vinduet.
	- Sjekke om strekmannen blir truffet av boksen. (Du skal lage funksjonen som gjør at han kan hoppe etterpå)

```python
def update():
	
	if 'Sjekk om boksen treffer strekmannen':
		print("Du ble truffet")

	elif 'Sjekk om boksen er ute av bildet':
		#Flytt boksen til høyre side av bildet

	#Gjør at boksen flytter seg mot venstre
```

###Tips
Her er tips om hvordan du kan sjekke om strekmannen blir truffet av boksen. Legg merke til at y-aksen er positiv nedover, noe som er motsatt av slik det er i matematikken. Boksen sin x og y posisjon (x, y) er hvor boksens øverste venstre hjørne er plassert. Den røde firkaneten rundt strekmannen viser omrisset at strekmann-bildet.
I tilfelle 1 ser du at boksens øverste venstre hjørne er inni den røde firkanten rundt strekmannen. Dette må du sjekke i if-setningen.
I tilfelle 2 er boksens øvre høyre hjørne inne den røde firkanten, dette må du også sjekke i if-setningen.
![](koord_data2.png "Koordinatsystem med figurer")


# Steg 5: Animasjoner {.activity}

Du skal nå lage funksjoner for å gjøre strekmannen i stand til å hoppe.

+ Vi trenger funksjonen on_key_up() som blir utført hvis man trykker på 'pilopp' på tastaturet.

```python
def on_key_up():
	#TO DO
```

+ Vi vil at det kun skal være lov til å hoppe hvis man står på bakken. Lag en if-setning som sjekker dette i funksjonen.

animate(...) er en funksjon som tar inn ulike parametere. I koden under animerer vi stick_man til å 'decelerate' som betyr å miste fart i en tidsperiode på 0.4 sekunder fra sin nåværende posisjon til posisjonen der bunnen av stick_man har x-verdi = (HEIGHT - box.height*1.5), det vil si han kan hoppe 1,5 ganger så høyt som så hvor høy boksen er.

```python
animate(stick_man, 'decelerate', duration = 0.4, bottom = (HEIGHT - box.height*1.5))
``` 
+ Du kan bruke koden over for å få strekmannen til å hoppe. 

Vi trenger nå en animasjon som gjør at strekmannen kommer ned til bakken igjen. Sammenlign med koden over og se om du skjønner hva som skjer.

```python
def back_down():
	animate(stick_man, 'accelerate', duration = 0.4, bottom = HEIGHT)
``` 
+ Legg til denne koden nederst i filen din.

+ Legg til koden under for å gjøre slik at når strekmannen når toppen av hoppet sitt settes animasjonen som gjør at han beveger seg ned i gang.

```python
clock.schedule_unique(back_down, 0.4)
```

Dette er en skisse på hvordan koden din skal se ut:
```python
def on_key_up():
	if "strekmann på bakken"

		#Animasjon oppover

		#Sett i gang animasjon ned
	
def back_down():
	#Animasjon ned
```

## Test programmet ditt {.flag}