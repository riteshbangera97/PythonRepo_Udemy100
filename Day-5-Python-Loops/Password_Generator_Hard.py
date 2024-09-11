#Password Generator Project (HARD)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("**** Welcome to the PyPassword Generator! ****")
nr_letters= int(input("\nHow many letters would you like in your password?\n")) 
if 0 >= nr_letters or nr_letters >= 12:
  print("Value of letters should be from 1 to 12 ")
  exit()

nr_symbols = int(input(f"\nHow many symbols would you like to include in your password?\n"))

if 0 >= nr_symbols or nr_symbols >= 12:
  print("Value of symbols should be from 1 to 12 ")
  exit()

nr_numbers = int(input(f"\nHow many numbers/Digits would you like to include in your password?\n"))

if 0 >= nr_numbers or nr_numbers >= 12:
  print("Value of numbers should be from 1 to 12 ")
  exit()

password = []

for l in range(0, nr_letters):
  password += random.choice(letters)

for s in range(0, nr_symbols):
  password += random.choice(symbols)

for n in range(0,nr_numbers):
  password += random.choice(numbers)

random.shuffle(password) # To shuffle the list so we will get random shuffled password.

Strong_password = ""
for p in password:
  Strong_password += p
  

print(f"Your Strong Password is:- {Strong_password}")

