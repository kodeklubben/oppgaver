---
title: Flaksefugl
level: Level 2
language: en-GB
stylesheet: scratch
embeds: "*.png"
materials: "*.sb2"
...

# Introduksjon { .intro}
__I denne oppgaven skal vi lage vår egen versjon av spillet Flappy Bird.__
Trykk på mellomromstasten for å flakse og prøv å styre mellom rørene!

![screenshot](flappy_screenshot.png)

#**Steg 1:** Få Flakse til å falle {.activity}

## Sjekkliste { .check}

+ Start et nytt Scratch-prosjekt. Slett katten ved å høyreklikke den og velge "Slett".
+ Bytt ut bakgrunnen med et utendørslandskap. **desert** er et bra valg.
+ Legg til Flapppy-figuren. Du trenger en figur med drakter for vinger opp og vinger ned. **parrot** er et bra forslag.
+ Bytt navn på figuren til __Flakse__.
+ Gi Flappy dette scriptet:

```blocks
når Grønt flagg klikkes
	gå til x: (-50) y: (0)
	for alltid
		endre y med (-3)
```

## Test prosjektet ditt { .flag}

__klikk det grønne flagget__: starter Flakse midt på skjermen og faller mot bunnen?

## Lagre prosjektet ditt hvis du kan { .save}

#**Steg 2:** Få Flakse til å fly {.activity}

*Nå vil vi at Flakse skal fly oppover når du trykker mellomrom.*

##Sjekkliste { .check}

+ Klikk på __Drakter__ og gi de to draktene navnene **Vinger opp** og **Vinger ned**.
+ Gå tilbake til __Skript__ og legg til dette skriptet:

```blocks
Når [mellomrom] trykkes
	bytt drakt til [Vinger ned]
	gjenta (10) ganger
		endre y med (6)
	end
	bytt drakt til [Vinger opp]
	gjenta (10) ganger
		endre y med (6)
	end
```

## Test prosjektet ditt { .flag}

__Klikk det grønne flagget__: klarer du å kontrollere Flakse med mellomromstasten? La du merke til at noen ganger så flytter ikke Flakse seg når du trykker mellomrom? Det er det neste vi skal fikse.

## Lagre prosjektet ditt { .save}

#**Steg 3:** Gjør kontrollen bedre {.activity}

*Vi vil at Flakse skal reagere hver gang vi trykker mellomrom. Men når vi trykker mellomrom så starter to løkker etterhverandre. Hvis vi trykker mellomrom før disse to løkkene er ferdig så skjer det ikke noe. For å løse dette problemet skal vi bruke en variabel til å telle hvor mange flaks vi trenger å gjøre.*

##Sjekkliste { .check}

+ Ta fra hverandre skriptet som starter med `når mellomrom trykkes` {.blockbrown} og legg de til siden. Vi skal bruke klossene straks.
+ Lag en ny variabel `For denne figuren` {.blockgrey} og kall den `flaks` {.blockorange}.
+ Legg til dette skriptet ved å bruke blokkene du la til siden:

```blocks
når grønt flagg klikkes
	sett [flaks] til [0]
	bytt drakt til [Vinger opp]
	for alltid
		gjenta til <(flaks) = [0]>
			endre [flaks] med (-1)
			bytt drakt til [Vinger ned]
			gjenta (10) ganger
				endre y med (6)
			slutt
			bytt drakt til [Vinger opp]
			gjenta (10) ganger
				endre y med (6)
			slutt

```

+ Til slutt, legg til dette skriptet på `når mellomrom trykkes` {.blockbrown} blokken:

```blocks
når [mellomrom] trykkes
	endre [flaks] med (1)
```

## Test prosjektet{ .flag}

__Klikk det grønne flagget__: Flakser Flakse en gang for hver gang du trykker mellomrom??

## Lagre prosjektet ditt om det trengs { .save}

#**Steg 4:** Legg til rørene {.activity}

*Vi vil legge til noen hindringer som Flakse kan fly igjennom.*

##Sjekkliste { .check}

+ Klikk på `tegn ny figur` {.blockgrey} knappen.
+ Gi den nye figuren navnet **rør**.
+ Hvis drakten er i `Punktgrafikk` {.blockgrey} klikk på `Bytt til vektorgrafikk` {.blockgrey} knappen.
+ Klikk på `Zoom -` {.blockgrey} så du kan se hele tegneområdet.
+ Klikk på `Rektangel` {.blockgrey}, velg en farge og klikk på `Fylt rektangel` {.blockgrey} knappen nederst til venstre.
+ Klikk og dra to bokser, en fra toppen og en fr bunn i midten av tegneflaten. Det skal se sånn ut:

![screenshot](pipe_design.png)
 
+ Du kan skyggelegge røra ved å klikke på `Fyll farge` {.blockgrey} og klikke på en av skyggemetodene i firkantene nede til venstre. Velg to varianter av samme farge: en for forgrunnen og en for bakgrunnen. Når du klikker på en firkant med fylleverktøyet får du en fin effekt.
+ Gi figuren navnet **Rør**.

## Lagre prosjektet ditt { .save}

#**Steg 5:** Få røra til å bevege seg{.activity}

*Nå skal vi få røra til å flytte seg og gjøre plasseringen tilfeldig slik at vi får en hinderløype til Flakse.*

##Sjekkliste { .check}

+ Klikk på **rør**-figuren og velg `Skript` {.blockgrey}.
+ Legg til dette skriptet:

```blocks
når grønt flagg klikkes
	skjul
	sett størrelse til (200)%
	for alltid
		lag klon av [meg]
		vent (2) sekunder

når jeg starter som klon
	gå til x: (240) y: (tilfeldig tall fra(-80) til (80))
	vis
	gjenta (120) ganger
		endre x med (-4)
	slutt
	slett denne klonen
```

## Test prosjektet { .flag}

__Klikk det grønne flagget__: Kommer det mange rør flygende mot Flakse? Har rørene åpninger til å fly gjennom? Om du synes det er vanskelig å fly Flakse gjennom åpningene kan du endre på åpningen mellom rørene med tegneverktøyet, eller du kan lage Flakse mindre.

## Lagre prosjektet { .save}

#**Steg 6:** Finn ut om Flakse kræsjer med rørene {.activity}

*For at spillet skal bli vanskelig må spilleren styre Flakse gjennom åpningene mellom rørene uten å komme borti hverken rør eller kanten av skjermen. Vi skal legge til noen blokker for å merke om Flakse kræsjer.*

##Sjekkliste { .check}

+ Vi legger til en lyd som vi kan spille når Flakse kræsjer. Kliukk på **Flakse** og så på `Lyder` {.blockgrey}.
+ Klikk på `Velg lyd fra biblioteket` {.blockgrey}.
+ Velg en kræsjelyd for **Flakse**.  **screech** er en kul lyd.
+ Klikk deg tilbake til `Skript` {.blockgrey} fliken.
+ Legg til dette skriptet:

```blocks
når grønt flagg klikkes
	vent til ((berører [kant]?) eller (berører [Rør]?))
	spill lyden [screech v]
	si [Du tapte!]
	send melding [Tap]
	stopp [andre skript i figuren]
```

+ Klikk på **Rør** og legg til dette skriptet:

```blocks
når jeg mottar [Tap]
	stopp [andre skript i figuren]
```

## Test Your Project { .flag}

__Click the green flag__, does the game end when Flappy touches a pipe or the edge of the screen?

## Save your project { .save}

#**Step 7:** Add scoring {.activity}

*The player should score a point every time Flappy makes it though a pipe. Let's add that next.*

##Activity Checklist { .check}

+ Let's add a sound to play when Flappy scores a point. Click on the **Pipe** sprite add a score sound. **bird** is a good choice.
+ Now click back on the `Scripts` {.blockgrey} tab.
+ Make a new variable `For all sprites` {.blockgrey} and call it `score` {.blockorange}.
+ Add a block to set the score to 0 when the flag is clicked.
+ Add the following block:

```blocks
when I start as a clone
	wait until <(x position) < ([x position v] of [Flappy v])>
	change [score v] by (1)
	play sound [bird v]
```

## Test Your Project { .flag}

__Click the green flag__, does the player score points for flying Flappy through the pipes?

## Save your project { .save}

##Things to try { .try}
1. __How many ways can you make this game easier or harder?__
2. __Well done you’ve finished the basic game. There are more things you can do to your game though. Have a go at these challenges!__

##Challenge 1: add a high score { .challenge}

+ Make a new variable and tick the `Cloud variable (stored on server)` {.blockgrey} box. Call the variable `hi-score` {.blockorange}
+ when the game is over check if you need to set a new high score:

```blocks
when I receive [GameOver v]
	if <(score) > (hi-score)> then
		set [hi-score v] to (score)
	end
	stop [other scripts in sprite v]
```

##Test Your Project { .flag}
__Click the green flag__, does your score update the hi score?

##Save your project { .save}

##Challenge 2: add gravity { .challenge}

When something falls under gravity it doesn't usually fall at a fixed rate. For this challenge we will make Flappy fall as if under gravity.

+ Add a new variable `For this sprite only` {.blockgrey} to **Flappy** and call it `rise` {.blockorange}.
+ Change Flappy's falling script:

```blocks
when FLAG clicked
	set [rise v] to [0]
	go to x: (-50) y: (0)
	forever
		change y by (rise)
		change [rise v] by (-0.4)
```

+ And change Flappy's flapping script:

```blocks
when FLAG clicked
	set [flaps v] to [0]
	switch costume to [wings up v]
	forever
		repeat until <(flaps) = [0]>
			change [flaps v] by (-1)
			switch costume to [wings down v]
			change [rise v] by (8)
			wait (0.2) secs
			switch costume to [wings up v]
			wait (0.2) secs
```

##Test Your Project { .flag}
__Click the green flag__, does Flappy now accelerate when falling and flapping?

##Save your project { .save}

##Challenge 3: fall off screen { .challenge}

When the player loses make Flappy fall off the bottom of the screen before ending the game.

+ Replace the `broadcast GameOver` {.blockbrown}  block with `broadcast Fall` {.blockbrown}
+ Now add the following scripts:

```blocks
when I receive [Fall v]
	repeat (10)
		turn ccw (5) degrees

when I receive [Fall v]
	repeat until <(y position) < [-180]>
		change y by (rise)
		change [rise v] by (-0.4)
	end
	hide
	broadcast [GameOver v]
```

+ Don't forget to add a `show` {.blockpurple} block and reset Flappy's direction when the game restarts.

##Test Your Project { .flag}
__Click the green flag__, does Flappy now fall off the screen after hitting a pipe? Does Flappy reappear in the correct orientation when restarting the game.

##Save your project { .save}

__Well done you’ve finished, now you can enjoy the game!__
Don’t forget you can share your game with all your friends and family by clicking on __Share__ on the menu bar!


