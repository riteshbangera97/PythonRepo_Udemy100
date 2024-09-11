## Rock, Paper, Scissor
# Me Vs Computer using random function

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


user_choice = int(input("Enter any choice between rock paper and scissor, 0 for rock, 1 for paper, 2 for scissor:-  \n"))

if user_choice not in (0, 1, 2):
  exit("Its a invalid choice")

computer_choice = random.randint(0,2)
print(f"Computer choice is { computer_choice}")

game =[rock, paper, scissors]

print(f"{game[user_choice]}\n{game[computer_choice]}")

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")




# elif Computer == 1 and user == 2:
#   print("Computer Wins")
# elif Computer == 2 and user == 1:
#   print("Computer Wins")
# elif Computer == 1 and user == 0:
#   print("Computer Wins")

# elif user > Computer:
#   print("You Wins")

# elif Computer > user:
#   print("Computer Wins")
