from clear import clear
from art import logo
from random import randint

print(logo)

print("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100")

possible_numbers = randint(1, 100)

def guessing_number():
    """Function that will work the guessing number game"""
    user_difficulty = input("Choose a dificulty. Type 'easy' or 'hard': ")
    play_again = False
    counter = 10
    while counter > 0:
        if user_difficulty.lower() == "easy":
            print(f"You have {counter} attempts remaining to guess the number.")
            user_guess = int(input("Make a guess: "))

            if user_guess == possible_numbers:
                print(f"You got it!, the answer was {possible_numbers}")
                start_the_game_again_or_not = input("Do you desire to play again? Type 'y' or 'n': ")
                if start_the_game_again_or_not.lower() == 'y':
                    pass
            elif user_guess > possible_numbers:
                print("Too high! Try again.")
                counter -= 1
                clear()
            elif user_guess < possible_numbers:
                print("Too low! Try again. ")
                counter -= 1
                clear()
        elif user_difficulty.lower() == "hard":
            counter = 5
            print(f"You have {counter} attempts remaining to guess the number.")
            user_guess = int(input("Make a guess: "))

            if user_guess == possible_numbers:
                print(f"You got it!, the answer was {possible_numbers}")
                start_the_game_again_or_not = input("Do you desire to play again? Type 'y' or 'n': ")
                if start_the_game_again_or_not.lower() == 'y':
                    pass
            elif user_guess > possible_numbers:
                print("Too high! Try again.")
                counter -= 1
                clear()
            elif user_guess < possible_numbers:
                print("Too low! Try again. ")
                counter -= 1
                clear()

guessing_number()


        









