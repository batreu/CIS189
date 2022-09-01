"""
Program: cast_to_integer.py
Author: Brandon Treu
Last date modified: 08/31/2022

The purpose of this program is to accept any input,
convert to a integer type and output the integer.
"""

#get users input and cast it to integer
user_input = input('Please enter the number of ducks you own : ')

#cast the input into an integer
user_input_as_iteger = int(float(user_input))

#test that my casting worked
print(type(user_input_as_iteger))

#outputs the user input as integer
print('The amount of ducks you own is: ' + str(user_input_as_iteger))




# Input /Expected Output /Actual Output
#    2  /        2       /      2
#  2.5  /        3       /      2
# 'I don't own any ducks'/NULL/ValueError