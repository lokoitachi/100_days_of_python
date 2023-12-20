##### scope ######

# Modifying Global Scope.
enemies = 1

def increase_enemies(): 
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

#Local Scope.

# def drink_potion():
#     potion_strenght = 2
#     print(potion_strenght)

# drink_potion()

# Global Scope.
# player_health = 10

# def drink_potion():
#     potion_strengh = 2
#     print(player_health)

# drink_potion()

# There is no block scope

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]

# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy)


#Global constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"

