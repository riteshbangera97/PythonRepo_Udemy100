# Random module is used to generate any random module
# first we need to import random module
import random

num1 = random.randint(1, 100) # randint is to generate random integer number 1 to 100 is a range, it will print 1 and 100 as well, its optional

num2 = random.random() # this function is for the floating random value.

print(f"Random integer number is :- {num1}")

print(f"Random float number is :- {num2}")

