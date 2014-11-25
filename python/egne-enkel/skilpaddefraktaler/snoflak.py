from turtle import *
import math

shape('turtle')
shapesize(2)
bgcolor('white')
color('black')
speed(11)

def fjell(lengde, dybde):
    if dybde <= 1:
        circle(lengde)
        penup()
        forward(lengde)
        pendown()
    else:
        fjell(lengde / 3, dybde - 1)
        left(60)
        fjell(lengde / 3, dybde - 1)
        right(120)
        fjell(lengde / 3, dybde - 1)
        left(60)
        fjell(lengde / 3, dybde - 1)


def firkantfjell(lengde, dybde):
    if dybde <= 1:
        forward(lengde)

    else:
        firkantfjell(lengde / 3, dybde - 1)
        left(90)
        firkantfjell(lengde / 3, dybde - 1)
        right(90)
        firkantfjell(lengde / 3, dybde - 1)
        right(90)
        firkantfjell(lengde / 3, dybde - 1)
        left(90)
        firkantfjell(lengde / 3, dybde - 1)


def trekant(lengde, dybde):
    if dybde <= 1:
        pendown()
        for i in range(3):
            forward(lengde)
            left(120)
        penup()
        return

    trekant(lengde / 2, dybde - 1)
    forward(lengde / 2)
    trekant(lengde / 2, dybde - 1)
    left(120)
    forward(lengde / 2)
    right(120)
    trekant(lengde / 2, dybde - 1)
    right(120)
    forward(lengde / 2)
    left(120)

def snoflak(lengde, dybde):
    for i in range(3):
        fjell(lengde, dybde)
        right(120)


def drage(lengde, dybde):
    if dybde <= 1:
        forward(lengde)

    else:
        left(60)
        drage(lengde / 2, dybde - 1)
        right(120)
        drage(lengde / 2, dybde - 1)
        drage(lengde / 2, dybde - 1)
        left(120)
        drage(lengde / 2, dybde - 1)
        right(60)

penup()
setpos(0, 150)
pendown()
drage(450, 1)
penup()
setpos(0, -100)
pendown()
drage(450, 2)




penup()
back(600)
input()
