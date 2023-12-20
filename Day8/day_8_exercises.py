#Simple function
def greet():
    print("Hi!")
    print("How are you? ")
    print("I hope you are doing alright.")

#Function that allows for input
def greet_with_name(name):
    print(f"Hi {name} !")
    print(f"How are you, {name}? ")

# greet_with_name("David") 

#Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(F"What is it like in {location}?")

greet_with("David", "Colombia")

greet_with(location="Canada", name="Juancho")