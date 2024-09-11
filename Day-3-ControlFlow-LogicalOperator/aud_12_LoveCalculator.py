  # LOVE CALCULATOR

# Question 

# """
# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs.

# Then check for the number of times the letters in the word LOVE occurs.

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is *z*."
# e.g.

# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times

# R occurs 1 time

# U occurs 2 times

# E occurs 2 times

# Total = 5

# L occurs 1 time

# O occurs 0 times

# V occurs 0 times

# E occurs 2 times

# Total = 3

# Love Score = 53

# Print: "Your score is 53."

# """

########################## # My Answer ##################################

print("The Love Calculator is calculating your score...")
name1 = input("What is your name?\n") # What is your name?
name2 = input("# What is their name?\n") # What is their name?

name = name1 +" "+name2
count1 = name.count("T") + name.count("t")
count2 = name.count("R")+ name.count("r")
count3 = name.count("U")+ name.count("u")
count4 = name.count("E")+ name.count("e")
count_True = count1 + count2 + count3 + count4

count5 = name.count("L") + name.count("l")
count6 = name.count("O")+ name.count("o")
count7 = name.count("V")+ name.count("v")
count8 = name.count("E")+ name.count("e")
count_Love = count5 + count6 + count7 + count8


love_calculator = str(count_True)+ str(count_Love)
love_calculator =int(love_calculator)

if love_calculator < 10 or love_calculator > 90:
  print(f"Your score is {love_calculator}, you go together like coke and mentos.")
elif 40 < love_calculator < 50:
  print(f"Your score is {love_calculator}, you are alright together.")
else:
  print(f"Your score is {love_calculator}.")


####################### GIVEN SOLUTION ######################
# Same as mine just difference is they have converted all names is lower case

lower_name = name.lower()
