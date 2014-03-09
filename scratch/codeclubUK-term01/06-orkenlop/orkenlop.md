---
title: Ørkenløp
level: 1.6
language: nb-NO
embeds: ["*.png", "../../bilder/*.png"]
...

#Ørkenløp

# Introduction { .intro}
Dette er et spill for to, der en papegøye og en løve kjemper om å komme først gjennom ørkenen. Hver spiller må trykke en tast så fort og ofte som mulig for å flytte figuren sin, og den som kommer først til kanten av skjermen vinner.


![screenshot](ørkenløp.png)

# Steg 1: Lage en scene og legg til figurer { .activity}

## Sjekkliste { .check}

+ Klikk på Scene og hent en ny bakgrunn fra biblioteket. Velg __Natur/desert__.
+ Fjern Sprite1 ved å høyreklikke på figuren og velg Slett.
+ Legg til en ny figur ved å trykke på ![Velg figur fra biblioteket](figur-fra-bibliotek.png). Velg __Dyr/Lionness__.
+ Legg så til enda en ny figur: velg Dyr/Parrot. Krymp figuren slik at den er omtrendt like stor som løvinnen ved å bruke ![Krymp](krymp.png).


# Steg 2: La løven og papegøyen bevege seg { .activity}

Vi vil at figurene skal bevege seg når du trykker på en knapp.

## Sjekkliste { .check}

+ Velg først løvefiguren og få den til å `gå (4) steg`{.blockblue} når du trykker __‘L’__ tasten.
    ```blocks
    når [l v] trykkes
    gå (4) steg
    ```

+ Velg så papegøyefiguren og la den `gå (4) steg`{.blockblue} når du trykker __‘A’__ tasten.

    ```blocks
    når [a v] trykkes
    gå (4) steg
    ```

## Test prosjektet { .flag}

__Trykk på det grønne flagget.__ 
Beveger løven og papegøyen seg over skjermen når du trykker på ‘A’ og ‘L’ tastene?

## Lagre prosjektet { .save}

# Steg 3: Start kappløpet { .activity}

__Nå må vi kjøre i gang kappløpet og kåre en vinner. Vi begynner med å lage startknapp.__

## Sjekkliste { .check}

+ Legg til en ny figur. Velg __Ting/Button3__. Flytt den til midten av scenen. 
+ Klikk på Drakter-fanen og symbolet T for å legge til tekst. Trykk på venstre kant av knappen for å legge til et tekstfelt og skriv inn teksten ‘start’. Du kan flytte på teksten ved å trykke en gang på den, og endre innhold ved å dobbeltklikke.
+ Legg nå til et skript som viser figuren når spillet starter:

    ```blocks
        når grønt flagg klikkes
        vis
    ```
+ I tillegg vil vi ha en knapp som teller ned fra 3, sier ‘LØP’ og deretter blir skjult når den klikkes. Dette ordner du med følgende skript:

    ```blocks
    når denne figuren klikkes
        si [3] i (1) sekunder
        si [2] i (1) sekunder
        si [2] i (1) sekunder
        si [LØP!] i (1) sekunder
        skjul
    ```

## Test prosjektet { .flag}

__Klikk på det grønne flagget__ og __trykk på startknappen__.
Teller knappen ned? Sier den ‘LØP’? Blir den borte?

## Lagre prosjektet { .save}

Vi ønsker at figurene bare beveger seg etter at kappløpet er startet og vi ønsker å vite når kappløpet er over.

+ For å vite når kappløpet har startet og sluttet lager vi en variabel med navnet `kappløp`{.blockorange}. Fjern avhukingen til venstre for variabelen, slik at den ikke vises på scenen.
+ Sett __kappløp__ til __[0]__ når spillet startes. Forandre `når flagget klikkes`{.blockyellow} skriptet slik:

    ```blocks
    når grønt flagg klikkes
        vis
        sett [kappløp v] til (0)
    ```
+ Når nedtellingen er ferdig og løpet begynner, forandrer vi __kappløp__verdien til 1.
+ Now we need to stop the lion and the parrot from moving unless the racing variable is set to be 1. Click on the parrot sprite. __Add a control block to the script__ that only allows the parrot to move if __racing = 1__.

    ```blocks
    
        when [a v] key pressed
        if <(racing) = [1]>
            move (4) steps
    ```
+ Now do the same for the lion sprite.

## Test prosjektet { .flag}
__Klikk på det grønne flagget.__

Does the lioness or the parrot move only after the countdown has finished?

We want to know who wins the race and reset it when it has finished so you can
race again.

## Lagre prosjektet { .save}

# Steg 4: Finishing the race { .activity}

## Sjekkliste { .check}

+ Add a block to the parrot’s script that sets the **racing** variable to be 0 when the sprite touches the edge of the screen.

    ```blocks
    when [a v] key pressed
    if <(racing) = [1]>
        move (4) steps
        if <touching [edge v]?>
        set (racing) to [0]
    ```
+ Now we want the parrot to let us know if it wins the race. Record a new sound for the Parrot sprite that will be played when the parrot wins. Click `sounds`{.blocklightgrey} and then record the sound of the parrot winning the race!
+ Now add blocks that `play`{.blockpurple} the sound you recorded and makes the parrot say it has won:

    ```blocks
        when [a v] key pressed
        if <(racing) = [1]>
            move (4) steps
            if <touching [edge v]?>
                set (racing) to [0]
                play sound [recording1 v]
                say [The Parrot Wins! v] for (3) secs   
    ```
+ Now repeat these steps for the lioness.

## Test prosjektet { .flag}
__Klikk på det grønne flagget.__

Can you press the start button and race by pressing the ‘A’ and ‘L’ keys?
Do the sprites make their winning sound and say they’ve won when they reach the end of the race?

## Lagre prosjektet { .save}

# Steg 5: Resetting the game { .activity}

After the race is finished we need to tell the other sprites we have won and reset the game so we can play again.

__We need the winning sprite to broadcast that it has won.__

## Sjekkliste { .check}

+ Click on the Parrot sprite.
Add a block that broadcasts a **"finished”** message after the sprite says it has won.

    ```blocks
    when [a v] key pressed
    if <(racing) = [1]>
        move (4) steps
        if <touching [edge v]?>
            set (racing) to [0]
            play sound [recording1 v]
            say [The Parrot Wins! v] for (3) secs
            broadcast [finished v]
    ```

+ Now we need to add a new script that listens for the finished broadcast and moves the parrot back to the start. What happens if you change the value that **x** is set to?

    ```blocks
    when I receive [finished v]
        set x to (-170)
    ```
+ Now add the same script for the lioness. Test different **x** values to make sure the lion and the parrot line up at the start.
+ We also want to put the lion and the parrot in the same position when the project is run, so add another script to each that moves them to the start when we click the flag.

    ```blocks
    when FLAG clicked
        set x to (-170)
    ```
+ Now click on the button sprite and add a script that shows it when it receives the finished message.

## Test prosjektet { .flag}

__Klikk på det grønne flagget.__

Can you race against a friend, one of you moving the parrot by pressing ‘A’ and the other moving the Lion by pressing ‘L’?

## Lagre prosjektet { .save}

##Challenge 1: Add a booster { .challenge}

* __Try to add a booster__ that you can use once each race that moves the parrot or the lion __30 steps in 1 go.__
* __Add a new costume__ with fire coming out behind for each sprite and make it appear when the boost is pressed.
* __Create another sound__ that the sprite will make when the boost is pressed.

    ```blocks
    when [p v] key pressed
    if <<(racing) = [1]> and <(boosted) = [0]>>
        switch to costume [parrot-boost v]
        set [boosted v] to [1]     
        move (4) steps
        if <touching [edge v]?>
             set (racing) to [0]
            play sound [recording1 v]
            say [The Parrot Wins! v] for (3) secs
            broadcast [finished v]
    ```
    
## Test prosjektet { .flag}

## Lagre prosjektet { .save}

##Challenge 2: Use custom blocks to simplify your script { .challenge}

The code to check if the race has finished is now used in two places for each sprite: when the sprite is moving normally and when it's moving with the booster. We can simplify our script using a custom block which is a chunk of code that gets used in more than one place. It's a bit like making up our own Scratch code block!

+  Choose the Parrot's script.
+ Select the `More Blocks`{.blocklightgrey} palette and then click the `Make a Block`{.blocklightgrey} button. 
+ Give the custom block a name by typing **"finished"** into the pink box. Then click OK.
+ You'll now see a `define finished`{.blockpurple} block appear in the scripts window. Drag it to a clear area.
+ Detach the `if`{.blockyellow}`touching edge?`{.blocklightblue}`then`{.blockyellow} block and drag it to the `define finished`{.blockpurple} block.


    ```blocks
    define finished
     if <touching [edge v]?>
         set (racing) to [0]
         play sound [recording1 v]
         say [The Parrot Wins! v] for (3) secs
         broadcast [finished v]
    
    when [q v] key pressed 
    if <<(racing) = [1]> and <(boosted) = [0]>>
        switch to costume [parrot-boost v]
        set [boosted v] to [1]     
        move (4) steps
    finished
    ```
Can you drag the `finished`{.blockpurple} block from the palette and use it like any other code item?

Delete the other `if`{.blockyellow}`touching edge?`{.blocklightblue} block from your script and replace it with another `finished`{.blockpurple} custom block.

Does this make your code easier to read? Can you create a similar custom block for the lioness sprite?

## Test prosjektet { .flag}

## Lagre prosjektet { .save}

__Well done you’ve finished, now you can enjoy the game!__
