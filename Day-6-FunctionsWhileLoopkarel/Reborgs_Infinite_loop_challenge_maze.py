# Lecture No 50 , time after 9 minutes.
# Here in the reborgs maze game it was a edge case where robot was stuck in the infinite loop. so to clear that used logic of additional if statement to avoid repeatative loop. divert from the infinite loop
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world.json&url=user_world%3Aproblem_world.json


# def right():
#   turn_left()
#   turn_left()
#   turn_left()

# n =4
# while not at_goal():
#   if right_is_clear():
#       right()
#       move()
#       n -=1
#       if n <= 0:
#           right()
#           n += 4
#   elif front_is_clear():
#       move()
#   else:
#       turn_left()