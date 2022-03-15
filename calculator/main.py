# Calculator

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

num1 = int(input("What's the first number?: "))

for operation in operations:
    print(operation)

operation_symbol = input("Pick an operation from the line above: ")

num2 = int(input("What's the second number?: "))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

continue_calculator = True

while continue_calculator:

    decision = input(f"Would you like to continue operations on the number: {answer} ? Type 'yes' to continue or 'no' to exit.\t").lower()
    if decision == "no":
        continue_calculator = False
    else:

        for operation in operations:
            print(operation)

        operation_symbol = input("Pick an operation from the line above: ")
        num_next = int(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        new_answer = calculation_function(answer, num_next)

        print(f"{answer} {operation_symbol} {num_next} = {new_answer}")
        answer = new_answer
