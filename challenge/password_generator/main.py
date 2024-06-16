#Password Generator Project
import random
import source

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password_easy=[]

for n in range(1,nr_letters+1):
    password_easy.append(random.choice(source.letters))

for n in range(1,nr_symbols+1):
    password_easy.append(random.choice(source.symbols))

for n in range(1,nr_numbers+1):
    password_easy.append(random.choice(source.numbers))

password_easy_string=""
for character in password_easy:
    password_easy_string+=character

print("Easy password:",password_easy_string)

password_hard=password_easy
random.shuffle(password_hard)

password_hard_string=""
for character in password_hard:
    password_hard_string+=character

print("Hard password:",password_hard_string)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P