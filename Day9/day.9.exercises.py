programing_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
#Retrieving items from a dictionary.
print(programing_dictionary["Bug"])

#Adding items to a dictionary.
programing_dictionary["Loop"] = "Something that happens all over again and again"

print(programing_dictionary)

#Create and empty dictionary.

empty_dictionary = {}

# #Wipe an existing dictionary.

# programing_dictionary = {}

#Edit an item in a dictionary
programing_dictionary["Bug"] = "An insect"

print(programing_dictionary)

#Loop through a dictionary
for key in programing_dictionary:
    print(key)
    print(programing_dictionary[key])

######
#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nest a list in a dictionary.
travel_log = {
    "France": ["Paris", "Dijon", "Lillie"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart",]
}

#Nest a dictionary in a dictionary.

travel_log = {
    "France": {
        "Cities_visited": ["Paris", "Dijon", "Lillie"],
        "Total_visits": 12
    },
    "Germany": ["Berlin", "Hamburg", "Stuttgart",]
}

#Nesting a dictionary in a list.

travel_log = [
    {"Country": "France", 
    "Cities_visited": ["Paris", "Dijon", "Lillie"],
    },
]