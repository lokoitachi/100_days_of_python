from art import logo
from random import choice
print(logo)

print("Welcome to the number guessing game! ")
print("I'm thinking of a number between 1 and 100.")

NUMBERS = []
computer_number = 0
is_game_finished = False


def choose_random_number(add_number):
    """This function will automatically add numbers from 1 to 100 to a given list. Will append them all to the list and will return a random number taken from that list."""
    for i in range(1, 101):
        NUMBERS.append(i)
    add_number = choice(NUMBERS)
    return add_number

computer_number = choose_random_number(computer_number)
print(f"Psss. The answer is: {computer_number}")


user_choice_dificulty = input("Choose a dificulty: Type 'easy' or 'hard'")

def hard_dificulty():
    """This function will change the game mode to hard"""
    print("You have only 5 attempts remaining to guess the correct number.")
    counter = 5
    while counter > 0:
        user_guess = int(input("Make a Guess: "))
        if user_guess == computer_number:
            print("You guessed the number. Congratulations!")
            counter = 0
        elif user_guess > computer_number:
            print("Too big")
            counter -= 1
            print(f"Remaining attempts: {counter}")
            if counter == 0:
                print("You don't have any more attempts. You lose.")
        elif user_guess < computer_number:
            print("Too low")
            counter -= 1
            print(f"Remaining attempts: {counter}")
            if counter == 0:
                print("You don't have any more attempts. You lose.")
        else:
            print("That is not a valid option, you lose.")
            break


def game(user_input):
    """This function is the main game. It wil allow you to guess the computer random chosen number. You can type easy or hard in order to choose the dificulty"""
    if user_input.lower() == "easy":
        print("You have 10 attempts remaining to guess the correct number.")
        counter = 10
        while counter > 0:
            user_guest = int(input("Make a guess: "))
            if user_guest == computer_number:
                print("You guessed the number. Congratulations!")
                counter = 0
            elif user_guest > computer_number:
                print("Too big")
                counter -= 1
                print(f"Remaining attempts: {counter}")
                if counter == 0:
                    print("You don't have any more attempts. You lose.")
            elif user_guest < computer_number:
                print("Too low")
                counter -= 1
                print(f"Remaining attempts: {counter}")
                if counter == 0:
                    print("You don't have any more attempts. You lose.")
            else:
                print("That is not a valid option, you lose.")
                break
    elif user_input == "hard":
        hard_dificulty()
    else:
        return "That is now a valid option."

game(user_choice_dificulty)






