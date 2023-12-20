print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')
print("Welcome to Tresure Island. !")
print("Your mission is to find the treasure.")

first_choice = input('You are at a crossroad. Where do you want to go? Type "left" or "right". \n')

if first_choice.lower() == "left":
    second_choice = input('You have found yourself a lake. What do you want to do? Write "Swim" or "go around" as the only 2 options available. \n')
    if second_choice.lower() == "go around":
        third_option = input("You have found yourself a house with 3 doors. Which one you would like to open up? Choose 'red', 'yellow', or 'blue' to choose a door. \n ")
        if third_option.lower() == "yellow":
            print("You have found the treasure! You have won the game!")
        elif third_option.lower() == "red":
            print("The door was a room ignited. You entered and died burned.")
            print("Game Over.")
        elif third_option.lower() == "blue":
            print("You are teleported to another dimension where everything is black. You died out of loneliness.")
            print("Game Over.")
        else:
            print("That is not a valid option. Check again the possibilities.")
    elif second_choice.lower() == "swim":
        print("While you were swimming, you found a random whale and it ate you. You died.")
        print("Game Over.")
    else:
         print("That is not a valid option. Check again the possibilities.")
elif first_choice.lower() == "right":
    print("You have fallen down into a hole and died out of fall damage.")
    print("Game Over.")
else:
     print("That is not a valid option. Check again the possibilities.")