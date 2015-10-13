---
title: Strekmann spill
level: 3
Author: Ole Andreas Ramsdal, Kodeklubben Trondheim
---

#Introduksjon {.intro}

I denne oppgaven skal du lage et spill der du styrer en strekmann som skal hoppe over hindringer.

![](animasjon_spill.gif "Slik ser spillet ut")

# Steg 1: Ny fil {.activity}

+ Lag en ny fil.

Vi starter med å bestemme hvor stort vindu hvis skal bruke:

```python
WIDTH = 550
HEIGHT = 250
```
+ Lagre og kjør programmet, se til at du får opp et vindu.

# Steg 2: Hindringer {.activity}

Du skal nå lage boksene som strekmannen løper mot. Dette skal du gjøre ved hjelp av en klasse.

+ Klassen skal hete Box og skal ha egenskapene:
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
screen.draw.filled_rect( Rect((0, 0), (50, 50)) , (255, 0, 0) )
```
og denne koden tegner en boks som har det øverste venstre hjørnet i punktet (25, 25), er 100 piksler høy og bred og har fargen blå:
```python
screen.draw.filled_rect( Rect((25, 25), (100, 100)) , (0, 0, 255) )
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
		#(Din kode) Flytt boksen til høyre side av bildet

	#(Din kode) Gjør at boksen flytter seg mot venstre
```
####**Tips 1:**
For å få boksen til å flytte seg mot venstre kan du gjøre x-posisjonen til boksen mindre og mindre.

####**Tips 2:**
Her er tips om hvordan du kan sjekke om strekmannen blir truffet av boksen. Legg merke til at y-aksen er positiv nedover, noe som er motsatt av slik det er i matematikken. Boksen sin x og y posisjon (x, y) er hvor boksens øverste venstre hjørne er plassert. Den røde firkaneten rundt strekmannen viser omrisset at strekmann-bildet.
I tilfelle 1 ser du at boksens øverste venstre hjørne er inni den røde firkanten rundt strekmannen. Dette må du sjekke i if-setningen.
I tilfelle 2 er boksens øvre høyre hjørne inne den røde firkanten, dette må du også sjekke i if-setningen.

####**Tips 3:**
any_actor.bottom gir x-verdi til bunnen av 'any_actor'.

any_actor.left gir x-verdi til venstre side av 'any_actor'.


![](koord_data2.png "Koordinatsystem med figurer")


# Steg 5: Animasjoner {.activity}

Du skal nå lage funksjoner for å gjøre strekmannen i stand til å hoppe.

+ Vi trenger funksjonen on_key_up(key) som blir utført hvis man trykker på 'pilopp' på tastaturet.

```python
def on_key_up(key):
	#(Din kode)
```

+ Vi vil at det kun skal være lov til å hoppe hvis man står på bakken. Lag en if-setning som sjekker dette i funksjonen.

+ I if-setningen må du også sjekke at input-parameteren key er det samme som keys.UP. 

animate(...) er en funksjon som tar inn ulike parametere. I koden under animerer vi stick_man til å 'decelerate' som betyr å miste fart. Dette gjøres i en tidsperiode på 0.4 sekunder fra sin nåværende posisjon til posisjonen der bunnen av stick_man har x-verdi = (HEIGHT - box.height*1.5). Det vil si han kan hoppe 1,5 ganger så høyt som så hvor høy boksen er. Du kan endre disse verdiene for å endre vanskelighetsgrad på spillet.

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
def on_key_up(key):
	if "Strekmann på bakken og key er piltast-opp":

		#Animasjon oppover

		#Sett i gang animasjon ned
	
def back_down():
	#Animasjon ned
```

# Steg 6: Poeng {.activity}

+ Lag en variabel som heter score og gi den verdien 0.

 Du trenger også en variabel som holder styr på om du er blitt truffet. Strekmannen er ikke truffet i begynnelsen så denne skal ha verdien False.

+ Lag variabelen stick_man_hit.

Du trenger nå å bruke disse i update(). For at python skal forstå at der disse variablene du skal bruke må du skrive global foran dem øverst i funksjonen.

+ Slik skal de to øverste linjer i update() se ut:

```python
def update():
	global score
	global stick_man_hit

	...
```

+ Inne i update(), sett score = 0 hvis du blir truffet. Endre stick_man_hit til True.

+ Økt poengsummen med 10 poeng hvis du ikke ble truffet og boksen er ute av bildet på venstre side. Sett stick_man_hit til False.

Du trenger nå en funksjon som printer poengene:

```python
def print_score():
	global score
	screen.draw.text("Poeng: " + str(score), (400, 30), color = (0, 0, 0))
```

+ Legg funksjonen til i programmet.

+ Nå trenger du å kalle på denne funksjonen inne i draw().

## Test programmet ditt {.flag}

## Utfordringer: {.challenge}

- Utvidspillet slik at boksen har forskjellig høyde eller bredde for hver gang.

- Gjør at flere bokser kommer inn på skjermen samtidig.

- Dine egne ideer?