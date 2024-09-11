# Question
# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6

# Format the result to 2 decimal places = 33.60

# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.


print(" Restaurant Bill Invoice.")
total_bill = float(input("How much is your total bill ?\n"))
tipInPercent = int(input("How much is your tip percentage 10%, 12% or 15% ?\n"))

if tipInPercent not in [10,12,15]:
  print("You can only choose above tip options ")
  exit()
people = int(input("How many people want to split the bill?\n"))

# calculating  multiply factor from percentage
tip = (1+(tipInPercent/100))
print(tip)

result = (total_bill * tip)/people
result = round(result,2) # It will take only 2 decimal places ex:- 3.33 not 3.333
print(f"Each person should pay {result} rupees ")