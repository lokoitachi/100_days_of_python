from asqr import rock, paper, scissors
import random
from clear import clear

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors "))
computer_option = [rock, paper ,scissors]
computer_option = random.choice(computer_option)


if user_input == 1:
    print(rock)
    print("Computer chose:")
    print(computer_option)

    if computer_option == rock:
        print("It's a draw")
        
    elif computer_option == paper:
        print("You lose")
        print("It's a draw")
    elif computer_option == scissors:
            print("You win")
elif user_input == 2:
    print(paper)
    print("Computer chose:")
    print(computer_option)
    if computer_option == rock:
        print("You win")
    elif computer_option == paper:
        print("It's a draw")
    elif computer_option == scissors:
        print("You lose")
elif user_input == 3:
    print(scissors)
    print("Computer chose:")
    print(computer_option)
    if computer_option == rock:
        print("You lose")
    elif computer_option == paper:
        print("You win")
    elif computer_option == scissors:
        print("It's a draw")
