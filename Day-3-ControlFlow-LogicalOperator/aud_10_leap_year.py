# Which year do you want to check?
year = int(input("Enter any year\n"))

if year % 100 == 0:
    if year % 400 == 0: 
      print(f"{year} is a Leap year")
    else:
      print(f"{year} is Not leap year")
elif year % 4 == 0:
    print(f" {year} is a Leap year")
else:
    print(f"{year} is Not leap year")