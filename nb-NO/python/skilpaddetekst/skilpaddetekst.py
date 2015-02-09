# Author: Ole Kristian Pedersen

# Behavior:
# This program creates the text in the variable TEXT as turtle graphics.
# The text is drawn character by character, each inside a "box" of 
# size SIZE x SIZE. When drawing a character, the function assumes it is
# in the upper left corner of this box, pointing "east". Likewise, it
# assures that it leaves the box in the upper right corner, pointing 
# east (which will be the upper left corner of the next box). This does
# create some "weird"/inefficient behavior, especially when drawing 
# underlines.


from turtle import *
from time import sleep

# ASCII art text is created by
# http://patorjk.com/software/taag/#p=display&f=Doom&t=Python%0A 
# Font: Doom
# The font contains a lot of straight lines (e.g. /|\_), making it easy to draw.

TEXT = """
______      _   _
| ___ \    | | | |
| |_/ /   _| |_| |__   ___  _ __
|  __/ | | | __| '_ \ / _ \| '_ \\
| |  | |_| | |_| | | | (_) | | | |
\_|   \__, |\__|_| |_|\___/|_| |_|
       __/ |
      |___/
"""

LINES = TEXT.split('\n')

SIZE = 15

def underline(): # _
    # move into position
    penup()
    right(90)
    forward(SIZE)
    left(90)

    # draw line
    pendown()
    forward(SIZE)
    penup()

    # get to exit positon
    left(90)
    forward(SIZE)
    right(90)

def bar(): # |
    penup()
    forward(SIZE/2)
    right(90)

    pendown()
    forward(SIZE)
    penup()

    left(180)
    forward(SIZE)
    right(90)
    forward(SIZE/2)
    
def slash(): # /
    penup()
    right(90)
    forward(SIZE)
    left(135)

    pendown()
    forward((2*SIZE**2)**0.5)
    penup()

    right(45)

def backslash(): # \
    penup()
    right(45)

    pendown()
    forward((2*SIZE**2)**0.5)
    penup()

    left(135)
    forward(SIZE)
    right(90)

def blank():
    penup()
    forward(SIZE)

def newline(lineLength): # move to next line
    penup()
    right(90)
    forward(SIZE)
    right(90)
    forward(SIZE*lineLength)
    right(180)


MOVES = {
    " " : blank,
    "_" : underline,
    "/" : slash,
    "|" : bar,
    "\\": backslash,

    # the following are left as an excercise for the kid
    "(" : bar,
    ")" : bar,
    "'" : blank,
    "," : blank,
}

def create_text():
    # start in upper left corner
    penup()
    setx(-window_width()/2)
    sety(window_height()/2)

    for line in LINES:
        for char in line:
            # alternatively: MOVES.get(char, blank)()
            if char in MOVES:
                move = MOVES[char]
            else:
                move = blank
            move()
        newline(len(line))

def main():
    shape("turtle")

    for i in range(2):
        speed(11)
        width(5)
        create_text()
        sleep(5)
        reset()

main()
