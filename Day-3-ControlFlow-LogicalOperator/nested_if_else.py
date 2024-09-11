# Nested If else

# Example 1
def rollerCoaster():
  height = input("What is your hright in centimeter\n")
  
  if height >= "120":
    print("You are eligible for ticket of rollercoaster")
    age= input("What is your age? \n")
    if age > "18":
      print("As you are an adult, Your ticket price is 300 rupees")
    elif "12" < age < "18" :
      print("As you are teenager, Your ticket price is 200 rupees")
    else:
      print("As you are kid, Your ticket price is 100 rupees")
      
  
  else:
    print("You are not eligible for ticket of rollercoaster")


#############################################################

# Example 2 
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

# rollerCoaster()
bmiCalculator()
