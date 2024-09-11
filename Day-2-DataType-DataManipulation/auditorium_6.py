# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# BMI = weight / height square

# 1st input: enter height in meters e.g: 1.65
height = input("Enter your height in meters\n")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("Enter your weight in kg\n")


height_square = (float(height))**2
weight = float(weight)

BMI= (weight)/(height_square)
print(int(BMI))