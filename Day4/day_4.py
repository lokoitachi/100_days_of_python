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
import random

select_your_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_option = random.randint(0, 2)

if select_your_option == 0 and computer_option == 0:
    print("You choose: ")
    print(rock)
    print("Computer chooses:")
    print(rock)
    print('It is a draw')
elif select_your_option == 0 and computer_option == 1:
    print("You choose: ")
    print(rock)
    print("Computer chooses:")
    print(paper)
    print('You lose')
elif select_your_option == 0 and computer_option == 2:
    print("You choose: ")
    print(rock)
    print("Computer chooses:")
    print(scissors)
    print('You win')
elif select_your_option == 1 and computer_option == 0:
    print("You choose: ")
    print(paper)
    print("Computer chooses:")
    print(rock)
    print('You win')
elif select_your_option == 1 and computer_option == 1:
    print("You choose: ")
    print(paper)
    print("Computer chooses:")
    print(paper)
    print('It is a draw')
elif select_your_option == 1 and computer_option == 2:
    print("You choose: ")
    print(paper)
    print("Computer chooses:")
    print(scissors)
    print('You lose')
elif select_your_option == 2 and computer_option == 0:
    print("You choose: ")
    print(scissors)
    print("Computer chooses:")
    print(rock)
    print('You lose')
elif select_your_option == 2 and computer_option == 1:
    print("You choose: ")
    print(scissors)
    print("Computer chooses:")
    print(paper)
    print('You win')
elif select_your_option == 2 and computer_option == 2:
    print("You choose: ")
    print(scissors)
    print("Computer chooses:")
    print(scissors)
    print('It is a draw')
else:
    print("You typed an invalid number, you lose. ")

