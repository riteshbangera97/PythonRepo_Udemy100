def bmiCalculator():
  print(" Welcome To BMI Calculator")
  # Enter your height in meters e.g., 1.55
  height = float(input("Enter your height in meters \n"))
  # Enter your weight in kilograms e.g., 72
  weight = int(input("Enter your weight in KG \n"))

  height_square = height * height

  weight = float(weight)

  BMI = weight/height_square 

  if BMI < 18.5 :
    print(f"Your BMI is {BMI}, you are underweight.")
  elif 18.5 <= BMI < 25 :
    print(f"Your BMI is {BMI}, you have a normal weight.")
  elif  25 <= BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
  elif 30 <= BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
  elif BMI >= 35 :
    print(f"Your BMI is {BMI}, you are clinically obese.")

bmiCalculator()