"""
Brandon Treu
set_membership.py

this program will declare a set, then test to see if a value is within that set and print results
"""

test_set = {'banana', 'apple', 'cherry', 'mango', 'strawberry'}
test_value = 'mango'

def in_set(test_set, user_input):
    test_value = user_input
    if test_value in test_set:  # this will check the user input against the set
        print(test_value + ' is in the set!')  # if the user input is found in the set return true and give statement
        return True
    else:  # if the user input is not in the set return false and print negative statement
        print(test_value + ' is not in the set!')
        return False

if __name__ == '__main__':
    in_set(test_set, input('Enter a fruit to see if it is in the set : '))
    print(str('You asked if ' + str(test_value) + ' was in the set, the set was :' + str(test_set)))