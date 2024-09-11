# Calculate the average height. with use of for loop only.
# Do not use sum() or len() functions.
# Average should be rounded of

# QUESTION
# You are going to write a program that calculates the average student height from a List of heights.

# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

# The average height can be calculated by adding all the heights together and dividing by the total number of heights.


###################### My Answer == Given Solution ################

student_heights = input("Enter heights of all students and give space between two heights:- \n ").split()  # Using split so input will be in list

print(len(student_heights))

for i in range(len(student_heights)):
  student_heights[i] = int(student_heights[i])  # Converting list values from string to int


total_height = 0
no_of_Students = 0
for s in student_heights:
  total_height += s
  no_of_Students += 1

print(f"total height = {total_height}")
print(f"number of students = {no_of_Students}")
print(f"average height = {round(total_height/no_of_Students)}")


