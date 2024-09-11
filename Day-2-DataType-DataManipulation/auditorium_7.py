# Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x weeks left.


# Answer (My Answer) (maam's solution is also same)
age = input("Enter Your age\n")
remaining_age = 90 - int(age)
lifeInWeeks = remaining_age * 52

print(f"You have {lifeInWeeks} weeks left.")