# kalkulator.py


def add(a, b):
    """Adds a and b and prints the answer."""
    print(str(a) + " + " + str(b) + " = " + str(a + b))

def subtract(a, b):
    """Subtracts b from a and prints the answer."""
    print(str(a) + " - " + str(b) + " = " + str(a - b))

def multiply(a, b):
    """Multiplies a and b and prints the answer."""
    print(str(a) + " * " + str(b) + " = " + str(a * b))

def divide(a, b):
    """Divides a by b and prints the answer, if b is not zero."""
    if (b == 0):
        print("Division by zero is not allowed!")
    else:
        print(str(a) + " / " + str(b) + " = " + str(a / b))

numCalculations = int(input("How many calculations? "))
for i in range(numCalculations):

    operator = input("Operator: ")
    a = int(input("First number: "))
    b = int(input("Second number: "))

    if (operator == "+"):
        add(a, b)
    elif (operator == "-"):
        subtract(a, b)
    elif (operator == "*"):
        multiply(a, b)
    else:
        divide(a, b)

    print() # divider between calculations
