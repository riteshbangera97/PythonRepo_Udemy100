# ODD EVEN Check
# Which number do you want to check?

number = int(input("Enter a number:- \n"))

result = number%2

if result == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")