import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

different_posibilities = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

len_list = len(different_posibilities)
computer_choice = random.randint(0,  len_list - 1)


if user_choice == 0:
    print("You choose:")
    print(different_posibilities[user_choice])
    if computer_choice == 0:
        print("Computer chooses: ")
        print(different_posibilities[computer_choice])
        print("It is a draw")
    elif computer_choice == 1:
        print("Computer chooses: ")
        print(different_posibilities[computer_choice])
        print("Paper defeats Rock. You lose")
    elif computer_choice == 2:
        print("Computer chooses: ")
        print(different_posibilities[computer_choice])
        print("Rock defeats Scissors. You win!")


if user_choice == 1:
    print("You choose:")
    print(different_posibilities[user_choice])
    if computer_choice == 0:
        print("Computer chooses: ")
        print(different_posibilities[computer_choice])
        print("Paper defeats Rock. You win!")
    elif computer_choice == 1:
        print("Computer chooses: ")
        print(different_posibilities[computer_choice])
        print("It is a draw")
    elif computer_choice == 2:
        print("Computer chooses: ")
        print(different_posibilities[computer_choice])
        print("Scissors defeat paper. You lose")


if user_choice == 2:
    print("You choose:")
    print(different_posibilities[user_choice])
    if computer_choice == 0:
        print("Computer chooses: ")
        print(different_posibilities[computer_choice])
        print("Rock defeats Scissors. You lose")
    elif computer_choice == 1:
        print("Computer chooses: ")
        print(different_posibilities[computer_choice])
        print("Scissors defeats paper. You win!")
    elif computer_choice == 2:
        print("Computer chooses: ")
        print(different_posibilities[computer_choice])
        print("it's a draw")
