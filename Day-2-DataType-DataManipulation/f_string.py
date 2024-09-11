score = int(input("Enter your marks\n"))
global result
if score > 39:
  result = True
else:
  result = False

# f strings are yoused here
# here using the f string we can pass any variable in the string
print(f"You got score {score} in exam, Have You cleared the examination? :- {result}")
