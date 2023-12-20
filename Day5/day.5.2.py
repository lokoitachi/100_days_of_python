import random
from asqr import letters, numbers, symbols

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_letters = ""
password_symbols = ""
password_numbers = ""

for l in range(1, nr_letters + 1):
    password_letters += random.choice(letters)
    
for s in range(1, nr_symbols + 1):
    password_symbols += random.choice(symbols)

for n in range(1, nr_numbers + 1):
    password_numbers += random.choice(numbers)

new_password = [password_letters, password_symbols , password_numbers]
print (new_password)
random.shuffle(new_password)

final_password = ""
for i in new_password:  
    final_password += i
print(f"Your new password is {final_password}")