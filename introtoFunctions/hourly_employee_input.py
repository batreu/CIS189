"""
Program: hourly_employee_input.py
Author: Brandon Treu
Last date modified: 09/21/2022

"""

def hourly_employee_input():
    """Prompts the user for name as a string, hours worked as an int, and pay rate as a float"""
    FEDERAL_MINIMUM_WAGE = 7.25
    user_name_input = str(input("Please enter your name "))
    try:
        user_name_input_validation = (user_name_input)
        if len(user_name_input_validation) > 12 or len(user_name_input_validation) < 1 :
            raise ValueError
    except ValueError:
        print("The name entered is less than 1 Character or greater than 12, please re-run the program and enter again")
        return
    user_hours_input = int(input("Please enter your hours worked "))
    try:
        user_hours_input_validation = (user_hours_input)
        if user_hours_input_validation < 0 or user_hours_input_validation > 80 :
            raise ValueError
    except ValueError:
        print("The hours worked is not a valid entry, please enter a value above 0, and below 80 hours worked.")
        print("Please re-run the program to try again")
        return
    user_pay_input = float(input("Please enter your pay rate "))
    try:
        user_pay_input_validation = (user_pay_input)
        if user_pay_input_validation < FEDERAL_MINIMUM_WAGE or user_pay_input_validation > 40.00:
            raise ValueError
    except ValueError:
        print("The wage entered is either above $40.00 or below minimum wage.")
        print("Please re-run the program to try again")
        return
    print(f'{user_name_input} worked for{user_hours_input: 2.0f} hours at a rate of {user_pay_input: 4.2f} ')

#here is my driver code
if __name__ == "__main__":
    hourly_employee_input()