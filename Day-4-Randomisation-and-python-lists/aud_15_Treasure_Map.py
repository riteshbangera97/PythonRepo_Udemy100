# Treasure Map
# Question  
# You are going to write a program that will mark a spot on a map with an "O", 

# ex :- if we given input as B3 then it will print O at B3's position.If we enter input as a C3 then it will print O at C3's position. Below is the example how positions of respective index looks like.


# Example:- print(f"{line1}\n{line2}\n{line3}")
# line1 = ["a1", "b1", "c1"]
# line2 = ["a2", "b2", "c2"]
# line3 = ["a3", "b3", "c3"]

# Example:- (if we print map)
# map = [["a1", "b1", "c1"], ["a2", "b2", "c2"], ["a3", "b3", "c3"]]




################# MY Answer ##################
# Same as given solution but lenghty


p = input("Enter position :- \n").upper()

if "A" in p:
  second_index = 0
elif "B" in p:
  second_index = 1
elif "C" in p:
  second_index = 2
else:
  exit("choose between A1 to A3 or B1 to B3 or C1 to C3")


if "1" in p:
  first_index = 0
elif "2" in p:
  first_index = 1
elif "3" in p:
  first_index = 2
else:
  exit("choose between A1 to A3 or B1 to B3 or C1 to C3")


line1 = ["*", "*", "*"]
line2 = ["*", "*", "*"]
line3 = ["*", "*", "*"]

map = [line1, line2, line3]

map[first_index][int(second_index)] = "O"

print(f"{line1}\n{line2}\n{line3}")




######################## GIVEN SOLUTION ########################

position = input("Enter position :- \n").upper()

line1 = ["*", "*", "*"]
line2 = ["*", "*", "*"]
line3 = ["*", "*", "*"]

map = [line1, line2, line3]


letter = position[0].upper()  # Index of letter
abc = ["A", "B", "C"]

letter = abc.index(letter)

number = int(position[1]) -1  # position of number in input - 1 for index. Ex:- number- 1 = index 

map[number] [letter] = "O"

print(f"{line1}\n{line2}\n{line3}")
