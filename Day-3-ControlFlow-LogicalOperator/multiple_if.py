photo_price = 25

height = input("What is your hright in centimeter\n")

if height >= "120":
  print("You are eligible for ticket of rollercoaster")
  age= input("What is your age? \n")
  if age > "18" and not ("45" <= age <= "55"): # tickets are free for people aged between 45 -55 (OFFER)
    pic = input("Do you want pics during ride? (Give answer in yes or no) \n")
    if pic == "yes":
      print(f"As you are an adult, Your ticket price is {300 + photo_price} rupees")
    else:
      print("As you are an adult, Your ticket price is 300 rupees")
      
  elif "45" <= age <= "55":
    print("As you aged between 45 to 55 your tickects are free")
    # tickets are free for people aged between 45 -55 (OFFER)
  
  elif "12" < age < "18" :
    pic = input("Do you want pics during ride? (Give answer in yes or no) \n")
    if pic == "yes":
      print(f"As you are teenager, Your ticket price is {200 + photo_price} rupees")
    else:
      print("As you are teenager, Your ticket price is 200 rupees")
  else:
    pic = input("Do you want pics during ride? (Give answer in yes or no) \n")
    if pic == "yes":
      print(f"As you are kid, Your ticket price is {100 + photo_price} rupees")
    else:
      print("As you are kid, Your ticket price is 100  rupees")

else:
  print("You are not eligible for ticket of rollercoaster")