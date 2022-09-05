"""
Program: average_scores.py
Author: Brandon Treu
Last date modified: 09/05/2022

The purpose of this program is to accept the input for the first name, last name, and age, then three test scores.
Calculate the average of the three test scores, and the output the average to the user.
"""
#contstant of the number of scores: 3
TOTAL_NUMBER_OF_SCORES = 3
#prompt user for inputs and store input in variables

    #store first name
first_name = input('What is your first name?')
    #store last name
last_name = input('What is your last name?')
    #prompt users age
users_age = int(input('What is your age'))
    #prompt user for the scores
score_one = float(input('Please enter the first score: '))
score_two = float(input('Please enter the second score: '))
score_three = float(input('Please enter the third score: '))
#calculate an average
average_score = (score_one + score_two +score_three) / TOTAL_NUMBER_OF_SCORES

#print output
print(f'Thank you {last_name}, {first_name} Age: {users_age: 3.0f} average grade is: {average_score: 5.2f}')


#testing
"""
Test1
What is your first name?Brandon
What is your last name?Treu
What is your age31
Please enter the first score: 77.5
Please enter the second score: 78.9
Please enter the third score: 89.99
Thank you Treu, Brandon Age:  31 average grade is:  82.13
Test2
What is your first name?Linda
What is your last name?Rodriguez
What is your age43
Please enter the first score: 72.99
Please enter the second score: 89.99
Please enter the third score: 92.55
Thank you Rodriguez, Linda Age:  43 average grade is:  85.18
"""