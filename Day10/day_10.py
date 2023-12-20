from art import logo
from clear import clear

print(logo)

#Calculator

def add(n1, n2):
    """This function will return the sum of the 2 parameters given."""
    return n1 + n2

def substract(n1, n2):
    """This function will return the substraction of the 2 parameters given."""
    return n1 - n2

def multiply(n1, n2):
    """This function will return the multiplication of the 2 parameters given."""
    return n1 * n2

def divide(n1, n2):
    """This function will return the division of the 2 parameters given."""
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

def calculator():
    """This function will proceed to calculate the basic math operations"""
    num1 = float(input("What is the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit to start a new calculation: ") == "y":
            
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()




