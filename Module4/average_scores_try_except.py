"""
Program: average_scores_try_except.py
Author: Brandon Treu
Last date modified: 09/21/2022

I have added the input validation for module 4 to this assignment.
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
try:
    as_int = int(users_age)
    if(as_int >= 0):
        print('input is good for age')
    else:
        print('this is not a valid age input')
except:
    print('you did not enter a valid age')
finally:
    print("let's move on to user scores input")
    #prompt user for the scores
score_one = float(input('Please enter the first score: '))
try:
    score_as_int = int(score_one)
    if(score_as_int >= 0):
        print('input is good for the first score')
        if(score_as_int <= 100):
            pass
        else:
            print("The score you entered is too high!")#this is to catch the inputs over 100
    else:
        print('this is not a valid score input')
except:
    print('you did not enter a valid score')
finally:
    print("let's move on to the next score input")
score_two = float(input('Please enter the second score: '))
try:
    score_as_int_2 = int(score_one)
    if(score_as_int_2 >= 0):
        print('input is good for the first score')
        if(score_as_int_2 <= 100):
            pass
        else:
            print("The score you entered is too high!")#this is to catch the inputs over 100
    else:
        print('this is not a valid score input')
except:
    print('you did not enter a valid score')
finally:
    print("let's move on to the next score input")
score_three = float(input('Please enter the third score: '))
try:
    score_as_int_3 = int(score_one)
    if(score_as_int_3 >= 0):#i just changed the score variable so that i don't reuse
        print('input is good for the first score')
        if(score_as_int_3 <= 100):
            pass
        else:
            print("The score you entered is too high!")#this is to catch the inputs over 100
    else:
        print('this is not a valid score input')
except:
    print('you did not enter a valid score')
finally:
    print("let's move on to the next score input")
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