# Tressue Island
"""
Text Snippets of project
'You're at a crossroad. Where do you want to go? Type "left" or "right"' >> right == game over

'You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.' >> swim == game over

"You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?" >> yellow == game win

"It's a room full of fire. Game Over."
"You found the treasure! You Win!"
"You enter a room of beasts. Game Over."
"You chose a door that doesn't exist. Game Over."
"You get attacked by an angry trout. Game Over."
"You fell into a hole. Game Over."

"""

#### Given Solution ####

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")





#### My Answer ###

# print("Welcome to the tresure island, Your mission is to find the tresure ")

# ans1 = input(
#     'You are at a crossroad. Where do you want to go? Type "left" or "right"\n'
# )
# ans1 = ans1.lower()

# if ans1 == "right":
#     print("Game Over")
#     exit()
# elif ans1 == "left":
#     print(
#         'You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n'
#     )

# else:
#     print("cloose correct option")
#     exit()

# ans2 = input(":- ")
# ans2 = ans2.lower()

# if ans2 == "swim":
#     print("Game Over")
#     exit()

# elif ans2 == "wait":
#     print(
#         "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n"
#     )

# else:
#     print("cloose correct option")
#     exit()

# ans3 = input()
# ans3 = ans3.lower()

# if ans3 == "red":
#     print("It's a room full of fire. Game Over.")
#     exit()

# elif ans3 == "blue":
#     print("You enter a room of beasts. Game Over.")
#     exit()

# elif ans3 == "yellow":
#     print("You found the TRESURE! You Win!")

# else:
#     print("You chose a door that doesn't exist. Game Over.")
#     exit()
