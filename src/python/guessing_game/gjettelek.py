# gjettelek.py

from random import randint

number = randint(1, 100)
guess = 0
while guess != number:
    guess = int(input("Please guess a number: "))
    if (guess < number):
        print("Higher!")
    elif (guess > number):
        print("Lower!")

print("Correct!")
