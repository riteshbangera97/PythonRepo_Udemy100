# Addition of even numbers

################## My ans ~~ Given Solution ###############

target = int(input("Enter any number:- \n"))

if (target % 2) == 0: 
  target = target + 1 # as we need to take last even number as well
else:
  target = target

total = 0
for i in range(0, target, 2):
  total += i

print(total)