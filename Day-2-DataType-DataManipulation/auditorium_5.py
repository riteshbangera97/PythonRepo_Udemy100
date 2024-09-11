# Practice Auditorium 5
# Question:- Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input()

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
addition_of_two_digit = int(first_digit) + int(second_digit)

print(addition_of_two_digit)