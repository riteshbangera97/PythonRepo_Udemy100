# List contains different values in single variable

states_of_India = ["maharashtra", "karnataka", "goa", "gujrat", "haryana", "telangana"]

print("First value of list is:- ", states_of_India[0])

print("Second value of list is:- ", states_of_India[1])

# printing last value
print("last value of list is:- ", states_of_India[-1])

# Adding new value in list 
states_of_India.append("kerala")

# Removing any existing value
states_of_India.remove("telangana")


print("Updated list is", states_of_India)