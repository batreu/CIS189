#don't forget your docstring
"""
Brandon Treu
validate_input_in_functions.py

This program will take a users input, validate it , and Return the string with test name and score if it passes
validation; otherwise return the test name with invalid_message
"""



#Write a function score_input() that takes parameters test_name, test_score, and invalid_message
def score_input(test_name, test_score=-1, invalid_message='Invalid test score!'):
    try:
        test_score = int(test_score)#TRY to cast test_score to an integer
    except ValueError:
        print(invalid_message)
    if test_score >= 0 and test_score <= 100:#Validate if test_score is between 1 and 100 inclusive
        good_test = test_name, test_score
        return good_test#return string with test_name, and Score #such as 'Test 1: 70'
    elif test_score <0 or test_score > 100:
        bad_test = test_name, invalid_message
        return bad_test#return string with test_name and invalid_message #such as 'Test 2: Invalid Test Score!'


#Write your drive code here
#the one that starts with if __name__ == '__main__':

if __name__ == '__main__':
    print("What is the name of the test? :")
    test_name = input()

    print("What is the test score?(this is optional) :")
    test_score = input()

    print(score_input(test_name, test_score))