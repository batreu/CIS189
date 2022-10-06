"""
Brandon Treu
input_while_break.py

this program will take a user input as many times as they want, and exit from the loop when the sentinel value is given
it will then print the user list using a for loop

I added a break out to my file, i decided to use the isnumeric() method to see if the user input is a number, if it is
we continue and if it isnt we break out.
"""

#declare a list variable
user_input_list = []
#prompt and get the user input
sentinel_value = 'proceed'

while sentinel_value not in ['quit','stop','exit','q']:#while my sentinel value does not match it will loop asking for scores
    try:
        user_input_value_int = int(input("Please enter your score or type quit to exit"))
        if user_input_value_int not in range(1,101):
            print("That is not a valid input, please enter a number between 1 and 100.")
            if user_input_value_int.isnumeric():#i did some research and found the "isnumeric()" method, it sends backa boolean value
                continue#as long as it is a number we can continue as normal
            else:
                break# if its not a number we break out of the while loop
        else:
            user_input_list.append(user_input_value_int)
    except:
        sentinel_value = input("Are you sure you want to exit? Type 'quit' to exit: ").lower()
print(str(user_input_list))

