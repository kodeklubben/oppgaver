---
title: Bygg et Hus
level: 1.4
language: nb-NO
embeds: ["*.png", "../../bilder/*.png"]
...

# Introduksjon {.intro}

I denne leksjonen vil vi se litt på hvordan vi kan få en robot til å
bygge et hus for oss. Underveis vil vi lære hvordan vi kan bruke
løkker og funksjoner for å gjenta ting som gjøres flere ganger.

# Steg 1: Grunnmuren {.activity}

Vi har tidligere lært om hvordan roboter behøver fuel for å kjøre og
byggemateriell for å bygge. Pass på at roboten din har nok fuel mens
du gjør oppgavene under.

## Sjekkliste {.check}

+ Lag en robot, gi den fuel og legg en del byggemateriell i robotens
  inventory.

+ Vi husker at kommandoen `turtle.place()` kunne brukes til å bygge
  med. Lag et nytt program, `edit bygghus`, som bare består av en
  linje foreløbig:

	```lua
	turtle.place()
	```

	Kjør programmet. Bygger roboten en kloss foran seg?

+ For å bygge en liten vegg må vi passe på å flytte roboten
  også. Utvid programmet ditt slik at det ser slik ut:

	```lua
	turtle.back()
	turtle.place()
	turtle.back()
	turtle.place()
	turtle.back()
	turtle.place()
	```

	Når du kjører dette vil roboten forsøke å sette ut tre klosser
    etter hverandre.

+ I stedet for at vi gjentar kode kan vi bruke løkker. For å gjøre
  ting et bestemt antall ganger bruker vi `for`-løkker. For eksempel,
  kan koden ovenfor heller skrives som

	```lua
	for kloss = 1, 3 do
		turtle.back()
		turtle.place()
	end
	```

	Endre koden din som over, og kjør programmet for å forsikre deg om
    at det fortsatt virker. En ekstra bonus er at det også har blitt
    enklere å bygge vegger med andre størrelser enn 3. Hvordan vil du
    for eksempel bygge en vegg som er 7 klosser lang?

+ Vi kan nå prøve å bygge flere vegger, for å lage et lite hus. Dette
  kan vi gjøre ved å bygge fire vegger, men hvor vi snur roboten litt
  mellom hver vegg. Endre koden din som følger:

	```lua
	for vegg = 1, 4 do
		for kloss = 1, 3 do
			turtle.back()
			turtle.place()
		end
		turtle.turnRight()
	end
	```

	Når du kjører dette vil du få fire vegger, men du vil se at det er
    noen problemer med siste hjørnet. Skjønner du hva som skjer? Tenk
    på hva roboten gjør dersom den ikke kan flytte seg.

+ Vi har et lite problem med at roboten stadig kommer borti ting mens
  den bygger. For å gjøre dette problemet litt mindre kan vi la
  roboten fly i lufta, og bygge under seg. Endre koden igjen:

	```lua
	turtle.up()

	for vegg = 1, 4 do
		for kloss = 1, 3 do
			turtle.back()
			turtle.placeDown()
		end
		turtle.turnRight()
	end

	turtle.forward()
	turtle.down()
	```

# Steg 2: Et høyere hus {.activity}

### Prøv selv {.try}

Hvordan vil du bygge et hus med høyere vegger? Kanskje en ny
**for**-løkke kan være til hjelp?

Hva med dører og vinduer? Dette er litt vanskeligere, men ved å bruke
**if**-tester kan du la være å sette klosser enkelte steder. Se om du
får dette til!

# Steg 3: Taket {.activity}

### Prøv selv {.try}

Taket kan vi bygge etter at resten av huset er ferdig. Hvordan vil du
lage taket? Se om du kan lage løkker slik at roboten klarer å bygge
hele taket?
