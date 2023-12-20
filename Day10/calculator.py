from art import logo

print(logo)

def add(n1, n2):
    """Takes 2 inputs and returns their sum"""
    return n1 + n2

def substract(n1, n2):
    """Takes 2 inputs and returns their substraction"""
    return n1 - n2

def multiply(n1, n2):
    """Takes 2 inputs and returns their multiplication"""
    return n1 * n2

def divide(n1, n2):
    """Takes 2 inputs and returns their division as a float number"""
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num_1 = float(input("What is the first number?: "))
    for operation in operations:
        print(operation)
    
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num_2 = float(input("What is the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num_1, num_2)

        print(f"{num_1} {operation_symbol} {num_2} = {answer}")
        
        next_question = input("Do you want to make another operation with the result you have? Type 'y' in order to proceed. Otherwise type 'n' to start the calculator again: ")
        if next_question.lower() == "y":
            num_1 = answer
        else:
            should_continue = False
            calculator()
        


calculator()
