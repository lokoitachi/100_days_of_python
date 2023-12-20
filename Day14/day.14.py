# import logo from the art.py module and print it
from art import logo, vs
import random
from data import data
print(logo)
#Choose randomly the name, follower_count, description, and country data from the dictionary and paste it in a variable.

#Show the different options to choose from
def comparison(plain_name, plain_follower_count, plain_description, plain_country):
    compare_option_1 = print(f" Compare A:{plain_name}, a {plain_description}, from {plain_country}")
    print(vs)
    compare_option_2 = print(f"Compare B:{plain_name}, a {plain_description}, from {plain_country} ")



for _ in range(2):
    temp_dictionary = random.choice(data)
    name = temp_dictionary["name"]
    follower_count = temp_dictionary["follower_count"]
    description = temp_dictionary["description"]
    country = temp_dictionary["country"]
    comparison(plain_name=name, plain_follower_count=follower_count, plain_description=description, plain_country=country)

print(comparison(plain_name=name, plain_follower_count=follower_count, plain_description=description, plain_country=country))





#Ask the user to choose for the option they believe it has the most followers.

#If the user answers correctly, the game should continue, otherwise, the game must finish

#Keep a track of the user score depending on how many correct answers the user has given.