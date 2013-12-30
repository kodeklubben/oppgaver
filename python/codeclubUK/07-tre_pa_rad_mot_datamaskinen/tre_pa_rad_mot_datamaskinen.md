---
lesson_title: Spille mot datamaskinen
level: 07
language: no
stylesheet: python
...

# Introduksjon {.intro}

I dag skal vi prøve å skrive kode slik at datamaskinen kan spille tre på rad mot oss. Datamaskinen vil ikke spille så bra i begynnelsen, men etterhvert som den lærer noen triks vil den kanskje klare å vinne mot deg!

# Steg 1: Vi fortsetter fra forrige gang { .activity}

I leksjon 6 skrev vi et tre-på-rad spill for to spillere. Vi brukte "Tk lerretet" fra `tkinter`-biblioteket for å tegne på skjermen. La oss se på hva vi allerede har før vi begynner å skrive ny kode.

1. Åpne IDLE. Åpne filen fra forrige leksjon og lagre den med et nytt navn. Eller om du ikke kan finne den filen kan du kopiere inn følgende:

    ```python
    from tkinter import *

    main = Tk()

    c = Canvas(main, width=600, height=600)
    c.pack()

    c.create_line(200, 0, 200, 600)
    c.create_line(400, 0, 400, 600)

    c.create_line(0, 200, 600, 200)
    c.create_line(0, 400, 600, 400)

    grid = [
        "0", "1", "2", 
        "3", "4", "5",
        "6", "7", "8", 
    ]

    def click(event):
        shape = choose_shape()
        across = int(c.canvasx(event.x) / 200)
        down = int(c.canvasy(event.y) / 200)
        square = across + (down * 3)

        if grid[square] == "X" or grid[square] == "O":
            return

        if winner():
            return

        if shape == "O":
            c.create_oval(across * 200, down * 200,
                (across+1) * 200, (down+1) * 200)
            grid[square] = "O"
        else:
            c.create_line(across * 200, down * 200,
                (across+1) * 200, (down+1) * 200)
            c.create_line(across * 200, (down+1) * 200,
                (across+1) * 200, down * 200)
            grid[square] = "X"

    def choose_shape():
        if grid.count("O") > grid.count("X"):
            return "X"
        else:
            return "O"

    def winner():
        for across in range(3):
            row = across * 3
            line = grid[row] + grid[row+1] + grid[row+2]
            if line == "XXX" or line == "OOO":
                return True
            
        for down in range(3):
            line = grid[down] + grid[down+3] + grid[down+6]
            if line == "XXX" or line == "OOO":
                return True

        line = grid[0] + grid[4] + grid[8]
        if line == "XXX" or line == "OOO":
                return True

        line = grid[2] + grid[4] + grid[6]
        if line == "XXX" or line == "OOO":
                return True
            
    c.bind("<Button-1>", click)

    mainloop()
    ```

2. Lagre, og kjør programmet, så du er sikker på at det virker!

    Du skal kunne klikke i rutene for å plassere sirkler og kryss inntil noen får tre på rad.

3. Før vi begynner med dagens kode vil vi gjøre en liten opprydning i koden for at vi enklere skal kunne lese hva som skjer i prosedyren `click`. Vi flytter koden som tegner sirkler og kryss til en egen prosedyre. Bytt prosedyren `click` ut med disse to prosedyrene:

    ```python
    def click(event):
        shape = choose_shape()
        across = int(c.canvasx(event.x) / 200)
        down = int(c.canvasy(event.y) / 200)
        square = across + (down * 3)

        if grid[square] == "X" or grid[square] == "O":
            return

        if winner():
            return

        grid[square] = shape
        draw_shape(shape, across, down)

    def draw_shape(shape, across, down):
        if shape == "O":
            c.create_oval(across * 200, down * 200,
                (across+1) * 200, (down+1) * 200)
        else:
            c.create_line(across * 200, down * 200,
                (across+1) * 200, (down+1) * 200)
            c.create_line(across * 200, (down+1) * 200,
                (across+1) * 200, down * 200)
    ```
    Kjør koden og test at den fortsatt fungerer på samme måte som tidligere. Dette er et eksempel på noe som kalles refaktorering. Vi har endret på selve koden, men ikke endret hvordan programmet fungerer.

# Steg 2: Spill tilfeldig { .activity}

Før vi kan lære datamaskinen hvordan den gjør gode trekk vil vi lære den hvordan den gjør trekk i det hele tatt. Vi begynner med å la datamaskinen finne en tilfeldig ledig rute, og deretter spille der.

Husk at vi har en variabel som heter `grid` som kan fortelle oss hvordan brettet ser ut. Det er en liste som starter som `["0", "1", "2", ... ]`, hvor vi putter inn `"X"` og `"O"` etterhvert som vi spiller. Vi begynner med å finne ledige ruter i denne listen for deretter å spille en slik rute.

1. På toppen av filen vil vi importere `random`-biblioteket, som vi vil bruke til å tilfeldig velge et trekk

    ```python
    from tkinter import *
    import random
    ```
    
    Du husker kanskje at vi brukte `random.choice` i en tidligere leksjon om Hangman.

2. Vi vil nå lage en ny prosedyre, `free_squares`, som kan finne ledige ruter. Legg til denn koden nedenfor prosedyren `winner`, men over linjen `c.bind(...)`:

    ```python
    def free_squares():
        output = []
        for position, square in enumerate(grid):
            if square != "X" and square != "O":
                output.append(position)
        return output
    ```
    
    Denne prosedyren lager en tom liste. Deretter går den gjennom hele rutenettet og sjekker hver rute om den er tom.

    Prosedyren `enumerate` kan fortelle oss posisjonen til hvert element i `grid`-listen. For eksempel vil `enumerate` gjøre om en liste `['A','B','C']` til par `(0, 'A'), (1,'B'), (2, 'C')` slik at vi ikke trenger å telle elementene selv. 

3. Nå skriver vi en prosedyre `play_move()` som kan spille i en tilfeldig tom rute. Legg til denne prosedyren etter `free_squares` men før linjnen `c.bind(...)`

    ```python
    def play_move():
        moves = free_squares()
        square = random.choice(moves)
            
        down = square // 3
        across = square % 3
        
        grid[square] = "X"
        draw_shape("X", across, down)
    ```

    First we get the list of empty squares, pick one, and convert the square number into across and down, using the `%` and `//` operators. Let's look at the numbered grid to see how this works:
    
    ``` 
         0 1 2
         -----
     0 | 0 1 2
     1 | 3 4 5
     2 | 6 7 8
    ```

    The 5 square is 1 down, and 2 across. If we divide 5 by 3, we get 1 with remainder 2

    `5 // 3` is 1, `6 // 3` is 2, and so on. The `//` operator gives us how many times 3 divides it, but ignores the remainder, which tells us how far down we must go.
    
    `5 % 3` is 2, `6 % 3` is 0. The `%` operator gives us the remainder, which is how far along we must go. 
    

4. Til slutt endrer vi `click`-prosedyren slik at den kaller `play_move`. På denne måten vil først spilleren gjøre sitt trekk, og deretter gjør datamaskinen sitt trekk.

    ```python
    def click(event):
        shape = choose_shape()
        across = int(c.canvasx(event.x) / 200)
        down = int(c.canvasy(event.y) / 200)
        square = across + (down * 3)

        if grid[square] == "X" or grid[square] == "O":
            return

        if winner():
            return

        grid[square] = "O"
        draw_shape("O", across, down)

        if winner():
            return
    
        play_move()
    ```

    Vi sjekker først om spilleren har vunnet, og hvis ikke lar vi datamaskinen gjøre sitt trekk.

5. Lagre programmet og kjør det. Datamaskinen vil nå trekke etter deg. Den vil ikke spille spesielt bra siden den bare gjør tilfeldige trekk.
    
# Steg 3: Velg et trekk som vinner { .activity}

The computer can play noughts and crosses, but badly. Let's help it a little. Instead of picking a random move, let's make it pick a move that wins, if it sees one.  The idea is that we can try each move in turn and see if it wins, and then play it.

1. Edit the `winner` function to take an argument `grid`:

    ```python
    def winner(grid):
        for across in range(3):
            row = across*3
            line = grid[row] + grid[row+1] + grid[row+2]
            if line == "XXX" or line == "OOO":
                return True
            
        for down in range(3):
            line = grid[down] + grid[down+3] + grid[down+6]
            if line == "XXX" or line == "OOO":
                return True

        line = grid[0]+grid[4]+grid[8]

        if line == "XXX" or line == "OOO":
                return True

        line = grid[2]+grid[4]+grid[6]
            
        if line == "XXX" or line == "OOO":
                return True
    ```

    You should only have to change the first line of the function. This means `winner` will use a grid passed to it, instead of the grid of the current game

2. Now we change `click` to pass in this grid.

    ```python
    def click(event):
        global shape, grid
        across = int(c.canvasx(event.x)/200)
        down = int(c.canvasy(event.y)/200)

        square = across + (down*3)

        if grid[square] == "X" or grid[square] == "O":
            return

        if winner(grid):
            return

        c.create_oval(
            across*200,down*200,
            (across+1)*200,(down+1)*200
        )
        grid[square] = "O"

        if winner(grid):
            return
    
        play_move()
    ```
    Every time you see `winner()`, you replace it with `winner(grid)`.


3. Run your code, it should work like before. It is important to make sure we haven't made any mistakes.


4. Let's change play_move to find a winning move!

    ```python
    def play_move():
        move = -1
        moves = free_squares()
        if not moves:
            return

        # find winning move if exists
        for possible in moves:
            new_grid = list(grid)
            new_grid[possible] = "X"
            if winner(new_grid):
                move = possible
                break
            
        if move <0:
            move = random.choice(moves)
            
        across, down = move%3, move//3
        
        grid[move] = "X"
        c.create_line(
            across*200, down*200,
            (across+1)*200, (down+1)*200
        )
        c.create_line(
            across*200, (down+1)*200,
            (across+1)*200, down*200
        )
        
    ```

    We make a copy of the grid, using `list(grid)`, place an X where we could play, and call `winner` to see if it wins!


5. Run and test your program. If the computer is lucky, it should try and win. 

## Try { .try}

Try playing a few games and seeing what happens.

# Step 4: Pick the move that blocks { .activity}

The other strategy we will use, is to look for a winning move for the player, and play it instead. I.e block any potential three in a row.

1. Edit `play_move` to find the players winning move, and block it!

    ```python
    def play_move():
        move = -1
        moves = free_squares()
        if not moves:
            return

        # find winning move if exists
        for possible in moves:
            new_grid = list(grid)
            new_grid[possible] = "X"
            if winner(new_grid):
                move = possible
                break

        if move < 0:
            for possible in moves:
                new_grid = list(grid)
                new_grid[possible] = "O"
                if winner(new_grid):
                    move = possible
                    break
            
        if move <0:
            move = random.choice(moves)
            
        across, down = move%3, move//3
        
        grid[move] = "X"
        c.create_line(
            across*200, down*200,
            (across+1)*200, (down+1)*200
        )
        c.create_line(
            across*200, (down+1)*200,
            (across+1)*200, down*200
        )
    ```
        
2. Run your code, and try to win. It should be a lot harder to beat the computer.


# The Complete Program { .activity}

Your final program should look something like this!

    ```python
    from tkinter import *
    import random 
    main = Tk()

    c = Canvas(main, width=600, height=600)
    c.pack()

    c.create_line(200, 0, 200, 600)
    c.create_line(400, 0, 400, 600)

    c.create_line(0, 200, 600, 200)
    c.create_line(0, 400, 600, 400)

    grid = [
        "0", "1", "2", 
        "3", "4", "5",
        "6", "7", "8", 
    ]
        

    def click(event):
        global shape, grid
        across = int(c.canvasx(event.x)/200)
        down = int(c.canvasy(event.y)/200)

        square = across + (down*3)

        if grid[square] == "X" or grid[square] == "O":
            return

        if winner(grid):
            return

        c.create_oval(
            across*200,down*200,
            (across+1)*200,(down+1)*200
        )
        grid[square] = "O"

        if winner(grid):
            return

    def winner(grid):
        for across in range(3):
            row = across*3
            line = grid[row] + grid[row+1] + grid[row+2]
            if line == "XXX" or line == "OOO":
                return True
            
        for down in range(3):
            line = grid[down] + grid[down+3] + grid[down+6]
            if line == "XXX" or line == "OOO":
                return True

        line = grid[0]+grid[4]+grid[8]

        if line == "XXX" or line == "OOO":
                return True

        line = grid[2]+grid[4]+grid[6]
            
        if line == "XXX" or line == "OOO":
                return True

    def play_move():
        move = -1
        moves = free_squares()
        if not moves:
            return

        # find winning move if exists
        for possible in moves:
            new_grid = list(grid)
            new_grid[possible] = "X"
            if winner(new_grid):
                move = possible
                break

        if move < 0:
            for possible in moves:
                new_grid = list(grid)
                new_grid[possible] = "O"
                if winner(new_grid):
                    move = possible
                    break
            
        if move <0:
            move = random.choice(moves)
            
        across, down = move%3, move//3
        
        grid[move] = "X"
        c.create_line(
            across*200, down*200,
            (across+1)*200, (down+1)*200
        )
        c.create_line(
            across*200, (down+1)*200,
            (across+1)*200, down*200
        )
        
    def free_squares():
        output = []
        for position, square in enumerate(grid):
        if square != "X" and square != "O":
            output.append(position)
        return output
            
    c.bind("<Button-1>", click)

    mainloop()
    ```

## Challenge { .challenge}

It's still possible to win against the program, but can you make changes to it to make it play perfectly? 
