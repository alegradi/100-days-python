# Calculator
from art import logo

def add (n1, n2):
    """Returns n1 + n2
    """
    return n1 + n2

def subtract (n1, n2):
    """Returns n1 - n2
    """
    return n1 - n2

def multiply (n1, n2):
    """Returns n1 * n2
    """
    return n1 * n2

def divide (n1, n2):
    """Returns n1 / n2
    """
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# Recursion with the calculator function
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)

    continue_calculator = True
    while continue_calculator:
        operation_symbol = input("Pick an operation. ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        decision = input(f"Type 'y' to continue calculating with: {answer}, or type 'n' to start a new calculation.\t").lower()

        if decision == "y":
            num1 = answer

        else:
            continue_calculator = False
            calculator()

calculator()