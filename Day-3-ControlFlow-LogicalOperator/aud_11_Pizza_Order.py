# Question
# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small pizza (S): $15

# Medium pizza (M): $20

# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2

# Add pepperoni for medium or large pizza (Y or N): +$3

# Add extra cheese for any size pizza (Y or N): +$1

# Example Input
# L
# Y
# N
# Example Output
# Thank you for choosing Python Pizza Deliveries!
# Your final bill is: $28.


##################### My Answer ########################

# print("Thank you for choosing Python Pizza Deliveries!")
# size = input("Enter the size of pizza you want (S, M, L)\n") # What size pizza do you want? S, M, or L
# add_pepperoni = input("Do you want pepperoni? (Y, N)\n") # Do you want pepperoni? Y or N
# extra_cheese = input("Do you want extra cheese? Y or N \n") # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

# # Small
# small_pizza = 15
# medium_pizza = 20
# large_pizza = 25


# if size == "S":
#   if add_pepperoni == "Y":
#     if extra_cheese == "Y":
#       print(f"Your final bill is: ${small_pizza + 2 + 1}.")
#     else:
#       print(f"Your final bill is: ${small_pizza + 2 }.")
#   else:
#     if extra_cheese == "Y":
#       print(f"Your final bill is: ${small_pizza + 1}.")
#     else:
#       print(f"Your final bill is: ${small_pizza}.")

# # Medium
# elif size == "M":
#   if add_pepperoni == "Y":
#     if extra_cheese == "Y":
#       print(f"Your final bill is: ${medium_pizza + 3 + 1}.")
#     else:
#       print(f"Your final bill is: ${medium_pizza + 3 }.")
#   else:
#     if extra_cheese == "Y":
#       print(f"Your final bill is: ${medium_pizza + 1}.")
#     else:
#       print(f"Your final bill is: ${medium_pizza}.")

# # Large

# else:
#     if add_pepperoni == "Y":
#       if extra_cheese == "Y":
#         print(f"Your final bill is: ${large_pizza + 3 + 1}.")
#       else:
#         print(f"Your final bill is: ${large_pizza + 3 }.")

#     else:
#       if extra_cheese == "Y":
#         print(f"Your final bill is: ${large_pizza + 1}.")
#       else:
#         print(f"Your final bill is: ${large_pizza}.")




#####################################
# given solution

print("Thank you for choosing Python Pizza Deliveries!")
size = input("Enter the size of pizza you want (S, M, L)\n") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? (Y, N)\n") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N \n") # Do you want extra cheese? Y or N

bill = 0
# Sizes

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

# Pepperoni
if add_pepperoni == "Y":
  if size == "S":
    bill +=2
  else:
    bill +=3
else:
  bill = bill

# Extra cheese
if extra_cheese == "Y":
  bill += 1
else:
  bill = bill

print(f"Your final bill is: ${bill}.")
