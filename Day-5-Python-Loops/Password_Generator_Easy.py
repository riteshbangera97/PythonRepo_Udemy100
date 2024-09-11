#Password Generator Project (Easy)
# My answer is little difficult, In Given solution random.choice(list_name) is used 
# My answer and given solution is merged together.


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


# creating random letters password
password = ""
for l in range (0, nr_letters):
  # password += letters[random.randint(0, len(letters) -1)] # taking n th index value from list letters and adding to let ## >>> My Answer
  password += random.choice(letters) ## Given Solution
  

for s in range(0, nr_symbols):
  # password += symbols[random.randint(0, len(symbols) - 1)] # taking n th index value from list symbols ## >>> My Answer
  password += random.choice(symbols) ## Given Solution


for n in range(0, nr_numbers):
  # password += numbers[random.randint(0, len(numbers) - 1)] # taking n th index value from list numbers ## >>> My Answer
  password += random.choice(numbers) ## Given Solution


print(f"Your Password is :- {password}")



