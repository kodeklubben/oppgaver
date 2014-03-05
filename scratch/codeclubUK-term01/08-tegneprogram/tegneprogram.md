---
title: Tegneprogram
level: Level 3
language: bn-NO
stylesheet: scratch
embeds: "*.png"
...

__Introduksjon:__
Dette prosjektet lager tegneprogram slik at du kan lage din egen kunst. Du kan tegne med forskjellige farger, bruke viskelær, lage stempler og mye mer!

![screenshot](paintbox_screenshot.png)

##FORBEREDELSER: Last ned ustyr

Denne første delen kan du godt få hjelp fra en voksen til å gjøre!

1. Lag en ny tab i nettleseren din
2. skriv inn denne nettadressen: http://bit.ly/Tegneutstyr
3. Last ned zip-fila "Ressurser_Tegneprogram.zip" og legg det på skrivebordet på datamaskinen din eller en annen plass du husker.
4. Pakk ut zip-filen ved å høyreklikke på den og velge "Extract All".

##STEG 1: Dra og tegn!

Vi starter med en penn som tegner når du drar den rundt på scenen.

1. Start et nytt Scratch-prosjekt. Slett katten ved å høyreklikke og velge slett.
2. Klikk på __Scene__ og så på __Bakgrunner__-fliken. Last opp bakgrunnen som heter frame.bmp fra folderen du hentet i forberedelsene. 
3. Lag en figur som heter __penn__ av bildet __green-pencil__ som ligger i den nedlastede mappen.
4. Bytt til __drakter__-fliken og velge hele figuren med velgeverktøyet. Flytt blyanten slik at spissen peker på det lille grå korset i midten. Da vil spissen tegne og ikke midten av blyanten.
5. Få pennen til å følge musa rundt på scenen ved å bruke __for alltid__-blokka og __gå til musepeker__-blokka.

```blocks
Når grønt flagg klikkes
for alltid
	gå til musepeker
slutt
```

__Nå vil vi bruke denne pennefiguren som en ordentlig penn.__ Om du ser under penn-kategorien kan du se alle slags tegefunksjoner. De vi er interessert i nå er __penn på__ og __penn av__

6. Vi vil bruke museknappen til å kontrollere pennen - når museknappen er nede går pennen ned og når museknappen er oppe er pennen oppe. Vi kan gjøre dette ved å bruke enn hvis ... ellers ... og en mus nede-blokk

```scratch
når grønt flagg klikkes
for alltid
	gå til musepeker
	hvis museknappen er nede?
	penn på
	ellers
	pen av
	(slutt hvis)
(slutt for alltid)
```
##Test prosjektet ditt
__Klikk på det grønne flagget.__
Følger pennen musa rundt? Hva skjer om du holder museknappen nede og flytter på musa? Ikke bry deg om pennefargen enda.


7. Etterhvert vil skjermen bli ganske full av rabbel. Vi kan bruke slett-blokka til å fjerne dette.

```blocks
når grønt flagg klikkes
slett
for alltid
	gå til musepeker
	hvis museknappen er nede?
	penn på
	ellers
	penn av
	(slutt hvis)
(slutt for alltid)
```

##Test prosjektet ditt
__Klikk på det grønne flagget.__

Forsvinner tegningene dine når du klikker på det grønne flagget?

LAGRE PROSJEKTET DITT

##STEG 2: Rydde opp

I stedet for å måtte starte og stoppe prosjektet for å slette tavla kan vi lage en knapp som sletter alt i stedet. Vi kan bruke slett-blokka.

1. Lag en ny figur fra ressursmappa du lasta ned i begynnelsen av prosjektet-. Velg __cancel button__ drakten.
2. Bytt navn på figuren til __slett__.
3. Flytt figuren til nederste høyre hjørne av scenen.
4. Gi slette-figuren dette skriptet:

```blocks
når denne figuren klikkes
slett
```

##Test prosjektet ditt
__Klikk på det grønne flagget.__

Sletter sletteknappen alle tegningene dine?

LAGRE PROSJEKTET DITT

##STEG 3: Bytte farge

Toil nå har vi bare kunnet tegne blå streker. Vi kan bruke andre farger også! Vi legge rtil noen figurer i bunn av rammen. Figurene vil se ut som fargede knapper. Når vi klikker på en knapp endres pennefagen til den fargen knappen har. For å vite at vi har byttet farge skal vi gjøre det slik at blyanten skifter farge til den fargen vi bruker.

1. Add a new sprite, called __red__, using the __resources/red-selector costume__. 
2. Place it somewhere along the bottom of the frame, near the __clear button__.
3. When the red sprite is clicked, it should broadcast the message __red__.

```scratch
when Red clicked
broadcast red
```
__Yes, that’s all it does. The hard work is done by the pencil.__

In the pencil, import a new costume, __resources/red-pencil__. Set the costume centre to be the tip of the pencil as you did for the original costume.

4. Add a new script to the pencil. When the pencil receives the message __red__, it should change to the red pencil costume and change the pen colour to red (using the set pen color to block).

__Hint:__ if you click on the coloured square
in the __set pen color to__ block, you can
click the eyedropper on the red sprite to make sure it’s the same colour.

```scratch
when I receive red
switch to costume
red-pencil
set pen color to (red)
```

##Test Your Project
__Click on the green flag.__

Start by drawing a line. Then click on the red selector sprite and draw some more. Does the pencil change costume? Does it now draw red? Does it draw from the tip of the red pencil?

SAVE YOUR PROJECT

5. Repeat what you just did for the blue, yellow, and green selector sprites.

##Test Your Project
__Click on the green flag.__

Do all the selector buttons work? Do they all change the pencil’s costume to the right colour? Do they all make the pencil draw in the right colour? Do all the costumes draw with the tip of the pencil?

SAVE YOUR PROJECT

##STEP 4: Only drawing inside the border

You’ve probably noticed that you can draw all over the Stage, even in the border. We don’t want that to happen. We want to keep the drawing in the middle of the Stage. We can do this by making sure the pen isn’t allowed to leave the drawing area - the light grey part on the Stage.


Remember that Scratch defines points using x and y axis. Our drawing area lies between 230 and -230 on the x-axis and 170 and -120 on the y-axis. We can use these values in an __if__ block, making sure the mouse is inside this area before we move the pencil to it.

To do this, wrap a new if block around your existing __go to... if__ block, and inside this new if check for the following:

mouse y is greater than -120 and mouse y is less than 170
and mouse x is greater than -230 and mouse x is less than 230

__Note__ to do this you’ll need to use multiple __and__ operator blocks, one for the two mouse x conditions, one for the two mouse y conditions and a final one to join these all together:

```scratch
clear
forever if mouse y is greater than -120 and mouse y is less than 170 and mouse x is greater than -230 and mouse x is less than 230
go to mouse-pointer
```

Since we can’t draw outside of the drawing area, we could hide the pencil tool whenever we leave it. To do this, replace the __if__ with an __if else__ block. Keep the same condition for the __if__, and __show__ the pencil if it’s true, otherwise hide it.

```scratch
when FLAG clicked
pen up
clear
forever
	if mouse y is greater than -120 and mouse y is less than 170 and mouse x is greater than -230 and mouse x is less than 230
		go to mouse-pointer
		show
		if mouse down?
			pen down
		else
			pen up
		(end if)
	else
		hide
	(end if)
(end forever)
```

##Test Your Project
__Click on the green flag.__

Can you still draw inside the drawing area? Can you draw outside the drawing area? What happens to the pencil when you leave the drawing area and go back in?

SAVE YOUR PROJECT

##STEP 5: Eraser

__Drawing lines is great, but there are times when you’ve made a mistake and you want to rub it out.__ We can do that with a new pencil tool that draws in grey (the same colour as the background).

Add a new button-sprite to the Stage to select the eraser. Use the __resources/eraser__ costume for it, making it smaller to fit at the bottom of the Stage. It should work the same as the other colour-selection buttons, sending an eraser message.

The pencil sprite should respond to the eraser message by switching the pen colour to grey (remember you can use the __picker__ to select the colour of the background). It will also need a new costume to represent the eraser tools: use the same __resources/eraser__ costume. __Remember to reset the costume’s centre.__

##Test Your Project
__Click on the green flag.__

Does the eraser rub out lines? Does it work right up to the edges? Can you switch between eraser and pencil tools?

SAVE YOUR PROJECT

##STEP 6: Stamps

The next thing to add is a stamp tool, to stamp small pictures on the drawing.
Activity Checklist

1. Add a new sprite, using whichever image or costume you want. Shrink the sprite down and place it at the bottom of the screen alongside the other tools. When this sprite is clicked, it should __broadcast stamp__
2. Add a new costume for this pencil sprite, the same as the one you chose for the __stamp__ button.
3. Select the pencil sprite and create a new variable __pencil mode__ for this sprite only. We’ll use this variable to keep track of whether or not we are drawing or stamping.
4. Add a new script to respond to the stamp message. It needs to set the costume to the stamp and set the __pencil mode__ variable to __false__.
5. Change the other scripts that respond to tool-selection messages (red, green, blue, and eraser) so that they each set the __pencil mode__ to __true__.
6. Finally, lets check this variable __when the mouse button is down__ to see if we should be drawing or stamping. If pencil mode = true we should use the existing __pen down__, if not we should stamp instead. 

##Test Your Project
__Click on the green flag.__

Does the stamp tool work correctly?

What happens when you switch back to one of the normal pencil tools?

SAVE YOUR PROJECT

__Well done, you have completed the basic steps for this project.
Try these challenges!__

##Challenge 1: Rainbow pencil

Let’s add a special pencil that paints in rainbow colours. It’s something that you can’t do with ordinary pens and pencils, so it’s nice to show off how drawing on a computer allows you do to different things. The secret to making it work is the change pen colour by block.

First, add the rainbow tool selection sprite and the rainbow tool costume to the pencil sprite:

1. Create a new tool selection sprite and place it at the bottom of the stage, alongside all the other pencil colour sprites. Use the resources/rainbow-selector costume and have it broadcast rainbow when clicked.
2. Add the resources/rainbow-pencil costume to the pencil sprite.

You need to build a script that will change the pen colour many times a second to give the rainbow effect (I found that changing it by 5 every 0.05 seconds works well, but you should try out different values). The timer Scratch card shows how you can make something change every so often. Use a change pen colour by 5 block instead of a change timer by -1 block inside the loop.

You also need to control that loop so that it only changes the pen colour when you’ve selected the rainbow pencil, otherwise all the pencils will have a rainbow effect! You can do this in a very similar way to how the pencil sprite changes between pencil and stamp modes. You need to create a variable called rainbowChange that has the value true when you want the rainbow effect and false otherwise. Every time the pencil responds to a tool-selection message, it should set the value of rainbowChange accordingly.

Use what you learnt from the stamp step above to control the rainbow effect. The scripts that respond to the tool-selection messages will set two variables each: pencilMode and rainbowChange.

##Test Your Project
__Click on the green flag.__

Does the rainbow tool work correctly?

What happens when you switch back to one of the normal pencil tools?

SAVE YOUR PROJECT

##Challenge 2: Keyboard shortcuts

Rather than using the tool-selection sprites at the bottom of the stage, you can use the keyboard to select the different tools.
You can use the when [] key pressed blocks to respond to the keyboard. For each key you want to use, you’ll need another when [] key pressed block, which sends the same message as the respective tool-selection sprite does when its clicked. Add these scripts to the stage.

I used these shortcuts:
* Clear all - a
* Eraser - e
* Red pencil -r 
* Blue pencil - b
* Yellow pencil - y
* Green pencil - g
* Rainbow pencil - w
* Stamp - s

##Test Your Project
__Click on the green flag.__

Do all the tools get selected with the correct keyboard shortcuts? Does each of the tools work correctly when you select it with keyboard? Are the correct tools still selected with the tool-selection sprites on the stage?

SAVE YOUR PROJECT

##Challenge 3: Big and Small
Another feature that most drawing packages have is the ability to change the
size of the pencil. Let’s add that.
There’s one complication, though, which is that sometimes the resizing needs to change the pen size and sometimes it needs to change the pencil sprite’s costume size. It depends on whether you’re using a pencil or a stamp.

Create two new tool-selection sprites, called bigger and smaller. They should have the resources/bigger-selector and resources/smaller-selector costumes and should send the bigger and smaller messages.

The pencil sprite can respond to the messages by changing either the pen size by 1 or the costume size by 10, depending on the value of pencil mode (use an if-else block, similar to how the sprite chooses between putting the pen down or stamping)
Don’t forget the keyboard shortcuts for the bigger and smaller tools. I used the up and down arrows.

SAVE YOUR PROJECT

What you should have noticed is that changing the size of the stamp also changes the size of the pencil on-screen when you change to that tool.
To stop that, you need to set the size to 100% every time you change to a pencil tool. so that the tools look the right size.

To make it even better, have the stamp remember what size it was before you selected the pencil and go back to that size when you select the stamp tool again. The easiest way to do that is to create a new variable called stampSize, that is updated with the current size every time the stamp is resized. When the stamp tool is selected, it can set its size from the contents of this variable.

##Test Your Project
__Click on the green flag.__

Do the size controls work for the pencils?

What happens if you switch to the stamp, change the size and then switch back to a pencil?

SAVE YOUR PROJECT


__Well done you’ve finished, now you can enjoy the game!__


Don’t forget you can share your game with all your friends and family by clicking on __Share__ on the menu bar!
