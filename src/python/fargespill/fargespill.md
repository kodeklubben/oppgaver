---
title: Fargespill
level: 2
author: Steffen Granberg
---

#Introduksjon
Denne oppgaven er (med tillatelse) basert på kode fra http://usingpython.com/programs/. Ta en titt der for flere spennende kodesnutter! 

Hjernen vår lar seg lett lure, og det kan av og til være vanskelig for den å tolke forskjellig inntrykk samtidig. I det spillet vi nå skal lage  vil du både få testet hjernen og skrivehastigheten. Vi skal lage et fargespill! 

![](fargespill.png)

#Steg 1: Klargjøre og importerer bilioteker{.activity}
I dette spillet skal vi lage et grafisk brukergrensesnitt (et GUI). Til dette bruker vi et bibliotek som heter ```tkinter```. Vi trenger også hjelp for å generere tilfeldige tall. 

## Sjekkliste {.check}

+ Åpne IDLE, og lag en ny fil.
+ La oss importere bibliotekene. Skriv inn følgende kode:
	```python 
	import tkinter
	import random
	```
+ Vi vil etterhvert bruke bokstaver som *æøå*. For å gjøre dette må vi legge til noe øverst i koden vår. Gjør om koden din slik at den ser slik ut: 

	```python 
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	import tkinter
	import random 
	```

## Kommentering av kode {.protip}
For å gjøre koden  lettere å forstå kan vi legge inn kommentarer som ikke påvirker programmet. Dette gjør vi ved å skrive inn tegnet ```#```. All tekst som kommer på samme linje etter dette tegnet vil bli ignorert av datamaskinen, men er veldig fint for å hjelpe oss mennesker. Heretter bruker jeg dette for å forklare hva som skjer, du trenger ikke å skrive inn kommentarene hvis du ikke vil!

#Steg 2: Lage grafisk brukergrensesnitt {.activity}

Nå skal vi begynne på GUI. Les kommentarene for å forstå hva som skjer.

## Sjekkliste {.check}

+ Vi skal begynne med å lage hovedvinduet. Dette kaller vi ```root``` Vi tilkaller funksjoner fra ```tkinter``` biblioteket for å hjelpe oss med dette. Legg til dette nederst i koden:
	```python  
	root = tkinter.Tk() 

	root.title("Fargespill")
	root.geometry("675x500")

	root.mainloop()
	```
+ Nå har vi laget hovedvinduet. La oss legge til noen felter med tekst. Vi kommer tilbake til hva disse skal fylles med etterhvert, nå skal vi bare definere områdene. Gjør om koden din slik at den ser ut som dette: 

	```python 
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	import tkinter
	import random

	root = tkinter.Tk()

	root.title("Fargespill")
	root.geometry("675x500")
										#Lager en label kalt instrukser med tekst:
	instrukser = tkinter.Label(root, text="Skriv inn fargen PÅ ordet, ikke selve ordet!", font=('Helvetica', 30))		

	poengLabel = tkinter.Label(root, text="Trykk enter for å starte.", font=('Helvetica', 30))
	poengLabel.pack() 					

	label = tkinter.Label(root, font=('Helvetica', 100))
	label.pack() 

	boks = tkinter.Entry(root) 

	root.mainloop()
	```			

## I koden over skjer det mye, la oss se på noen deler {.protip}

```tkinter.Label```lager et felt i vinduet vårt. I disse feltene kan vi putte blant annet tekst eller tall. ```.pack``` forteller programmet vårt at den skal "tegne" disse feltene slik at de synes for oss, og hvor den skal tegne de. ```tkinter.Entry(root)``` lager et tekstfelt som spilleren kan skrive i. 

## Test prosjektet {.flag}
+ Kjør koden
+ Viser den et vindu? 
+ Det er fortsatt ganske lite som skjer, la oss gå videre. 

#Steg 3: Vi lager tidskontroll {.activity}
## Sjekkliste {.check}

+ Vi skal nå få programmet vårt til å telle 30 sekunder. Vi lager en funksjon ```nedtelling()``` som tar seg av dette. Legg til dette i programmet ditt: 

	```python 
	def nedtelling(): 
	    global tidIgjen

	    if tidIgjen > 0:
	        tidIgjen = tidIgjen - 1 			# Tell ned ett sekund 
	        tidLabel.config(text= "Tid igjen: " + str(tidIgjen))
	        tidLabel.after(1000, nedtelling)	# Denne kjører automatisk nedtelling() igjen etter 1 sekund
	    if tidIgjen == 0:
	        tidLabel.pack_forget()
	        label.pack_forget()
	        boks.pack_forget()
    ```
+ Denne funksjonen jobber på en global variabel ```tidIgjen```, vi må lage den. Programmet ditt skal nå se slik ut: 

	```python 
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	import tkinter
	import random

	tidIgjen = 30 

	def nedtelling(): 
	    global tidIgjen

	    if tidIgjen > 0:
	        tidIgjen = tidIgjen - 1
	        tidLabel.config(text= "Tid igjen: " + str(tidIgjen))
	        tidLabel.after(1000, nedtelling)
	    if tidIgjen == 0:
	        tidLabel.pack_forget()
	        label.pack_forget()
	        boks.pack_forget()


	root = tkinter.Tk()

	root.title("Fargespill")
	root.geometry("675x500")
	                                    #Lager en label kalt instrukser med tekst:
	instrukser = tkinter.Label(root, text="Skriv inn fargen PÅ ordet, ikke selve ordet!", font=('Helvetica', 30))     

	poengLabel = tkinter.Label(root, text="Trykk enter for å starte.", font=('Helvetica', 30))
	poengLabel.pack()                   


	label = tkinter.Label(root, font=('Helvetica', 100))
	label.pack() 

	boks = tkinter.Entry(root) 

	root.mainloop()
	```

#Steg 4: Definere farger. {.activity}

Nå må vi definere fargene som programmet skal bruke. 

## Sjekkliste {.check}

+ Fargene legger vi til som en liste. Legg til denne koden under ```import random ```
	```python 
	fargerEng = ['Red','Blue','Green','Pink','Black','Yellow','Orange','Purple','Brown']
	```
+ Siden vi vil at programmet vårt skal skrive ut de norske ordene, lager vi en liste til, med de norske navnene. Legg til dette rett under den andre listen. 
	```python 
	farger  =   ['Rød', 'Blå', 'Grønn', 'Rosa', 'Svart', 'Gul', 'Oransje', 'Lilla', 'Brun']
	```
+ Vi må også lage en variabel for å holde orden på hvor mange poeng spilleren har. Legg til denne over ```tidIgjen```variabelen. 
	```python 
	poeng = 0
	```
+ Nå må vi lage funksjonen som genererer en tilfeldig farge og viser denne til spilleren. Her er det mye som skjer, så vi skal ta det stegvis. Først definerer vi funksjonen og legger til variablene. Legg denne funksjonen til over den forrige ```nedtelling()```funksjonen:

	```python 
	def nesteFarge():
						# Definerer globale variabler: 
    	global poeng
    	global tidIgjen
    	global farger
    	global fargerEng
    ```

+ Vi må nå sette tekstboksen brukeren kan skrive i aktiv hvis det er tid igjen på klokka. Legg til denne inne i ```nesteFarge()```funksjonene: 

	```python
	if tidIgjen > 0: 
    	boks.focus_set() 
    ```

+ Så vil vi sammenligne det brukeren skriver inn i boksen, med den første fargen i den norske fargelisten vår. ```.lower()``` gjør om alt til små bokstaver, slik at man ikke får feil om man skriver "Rød" i steden for "rød". Legg til dette under: 
	
	```python 
	if boks.get().lower() == farger[1].lower():		# Hvis det spilleren skrev er riktig farge.
        poeng = poeng + 1 		# Pluss på ett poeng
    ```
+ Nå vil vi slette det som brukeren skrev inn. Slik at alt er klart for neste runde. Legg til dette under ```poeng = poeng + 1```:
	```python 
	boks.delete(0, tkinter.END)
	```
+ Nå kommer det en litt vanskelig del. Siden tkinter må få de engleske navnene på fargene for å forstå de, er det de vi må stokke om rekkefølgen på. Da får vi en tilfeldig farge i neste runde. Derimot vi vil at de norske fargene skal forsatt stemme overens slik at 'Red' == 'Rød'. Derfor bruker vi en funksjon som heter ```zip``` for å slå sammen de to listene, slik at vi stokker om på begge samtidig. (Det er greit om du ikke forstår alt som skjer her, bare keep going!) Legg dette til nederst i funksjonen: 

	```python 
	#Kobler sammen to lister, siden tkinter bruker engelsk
    sammen = list(zip(fargerEng, farger))   # Slår sammen før omstokking
    random.shuffle(sammen)					# Stokker om rekkefølgen
    fargerEng, farger = zip(*sammen)        # deler listene igjen
    ```
+ Nå gjenstår det bare å vise teksten og fargen i vinduet. Vi oppdaterer feltene.  Funksjonen skal nå se slik ut:

	```python 
	def nesteFarge():
	    global poeng
	    global tidIgjen
	    global farger
	    global fargerEng

	    if tidIgjen > 0: 
	    	boks.focus_set() 

	    if boks.get().lower() == farger[1].lower():
	        poeng = poeng + 1

	    boks.delete(0, tkinter.END)

	    
	    sammen = list(zip(fargerEng, farger))  
	    random.shuffle(sammen)
	    fargerEng, farger = zip(*sammen)        
	        
	    label.config(fg=str(fargerEng[1]), text=str(farger[0]))		# Oppdaterer labels
	    poengLabel.config(text= "Poeng: " + str(poeng))
    ```

## Test prosjektet {.flag}
+ Kjør koden, får du noen feilmeldinger? 
+ Hvis du får feilmeldinger prøv å se etter hvor de er og fiks de. 

#Steg 5: La oss starte programmet! {.activity}
Det skjer fortsatt lite i spillet vårt, men det er fordi vi ikke har startet selve spilldelen. Det skal vi gjøre nå!

## Sjekkliste {.check}

+ Vi lager en funksjon som starter spillet. Legg til denne funksjonen i programmet: 

	```python 
	def startSpill(event):
	    if tidIgjen == 30: 
	        nedtelling()
	    nesteFarge() 
	```
+ Siste steg er å kjøre denne funksjonen når spilleren trykker *enter*. Legg til dette rett over ```root.mainloop```:

	```python 
	root.bind('<Return>', startSpill)	# Kjører funksjonen startSpill() når enter trykkes
	boks.pack()	
	boks.focus_set()
	```
+ Programmet ditt skal nå se slik ut: 

	```python 
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	import tkinter
	import random 


	fargerEng = ['Red','Blue','Green','Pink','Black','Yellow','Orange','Purple','Brown']
	farger    = ['Rød', 'Blå', 'Grønn', 'Rosa', 'Svart', 'Gul', 'Oransje', 'Lilla', 'Brun']

	poeng = 0

	tidIgjen = 30

	def startSpill(event):
	    if tidIgjen == 30: 
	        nedtelling()
	    nesteFarge() 

	def nesteFarge():
	    global poeng
	    global tidIgjen
	    global farger
	    global fargerEng

	    if tidIgjen > 0: 
	    	boks.focus_set() 

	    if boks.get().lower() == farger[1].lower():
	        poeng = poeng + 1

	    boks.delete(0, tkinter.END)

	    sammen = list(zip(fargerEng, farger))   
	    random.shuffle(sammen)
	    fargerEng, farger = zip(*sammen)        
	        
	    label.config(fg=str(fargerEng[1]), text=str(farger[0]))
	    poengLabel.config(text= "Poeng: " + str(poeng))


	def nedtelling(): 
	    global tidIgjen

	    if tidIgjen > 0:
	        tidIgjen = tidIgjen - 1
	        tidLabel.config(text= "Tid igjen: " + str(tidIgjen))
	        tidLabel.after(1000, nedtelling)
	    if tidIgjen == 0:
	        tidLabel.pack_forget()
	        label.pack_forget()
	        boks.pack_forget()
	 

	root = tkinter.Tk() 

	root.title("Fargespill")
	root.geometry("675x500")

	instrukser = tkinter.Label(root, text="Skriv inn fargen PÅ ordet, ikke selve ordet!", font=('Helvetica', 30))

	poengLabel = tkinter.Label(root, text="Trykk enter for å starte.", font=('Helvetica', 30))
	poengLabel.pack() 

	tidLabel = tkinter.Label(root, text="Tid igjen: " + str(tidIgjen), font=('Helvetica', 30))
	tidLabel.pack()

	label = tkinter.Label(root, font=('Helvetica', 100))
	label.pack() 

	boks = tkinter.Entry(root) 

	root.bind('<Return>', startSpill)
	boks.pack()
	boks.focus_set()

	root.mainloop()
	```

## Test prosjektet {.flag}
+ Starter spillet og nedtellingen når du trykker enter? 
+ Får du ny farge etter du har skrevet inn svar? 
+ Får du +1 poeng når du skriver riktig farge på ordet? 
+ Slutter programmet etter 30 sek? 


