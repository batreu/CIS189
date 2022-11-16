"""
Brandon Treu
topic_2_dictionaries.py



Write a second function average_scores() that accepts the dictionary as the only parameter and returns the average scores
Use len() to determine your num_scores for calculation
Note a dictionary is a set of key, value pairs.
You can get the keys with .keys() function
You can access the value using a key variable scores_dict.get(k)
What about testing?
Write a main to test your functions
Unit Tests can also help test average_scores()
"""
# Write a function get_test_scores()
def get_test_scores():
    scores_dict = dict()  # Create an empty dictionary scores_dict = dict()
    num_scores = []  # as an example, 6 test scores
    # counter_value = 0  # I was going to use this to loop but decided to create a dynamic range from input
    while True:  # loop...ask for num_scores test scores
        try:
            num_scores = int(input('How many test scores are there? : '))
        except ValueError:  # so if the value is not an int
            print('Please enter an integer')
            continue
        else:  # must be a valid input
            break
    for s in range(num_scores):
        score_key = 'score' + str(s + 1)  # creates key
        while True:
            try:
                score_value = int(input('Enter the integer test score: ')) # asks user for score
            except ValueError:
                print('You must enter an integer. Try again. ')
                continue
            else:
                score = {score_key: score_value}  # creates key and value and adds to dictionary
                scores_dict.update(score)
                break
    return scores_dict

    # store in dictionary, such as {'Score1':98, ...etc}


# calculates value average in score dictionary
def average_scores(scores_dict):
    score_sum = 0
    # this will iterate through the dict by providing the key and then getting the associated value
    for s in range(len(scores_dict)):
        # generate key and pull associated value then average scores
        score_key = 'score' + str(s+1)
        score_value = scores_dict[score_key]
        score_sum = score_sum + score_value  #the value is added to the sum
    average_grade = score_sum/len(scores_dict)  # sum is divided by the number of scores, produces by the len of dictionary
    print(scores_dict)
    print(average_grade)
    return average_grade


if __name__ == '__main__':
    average_scores(get_test_scores())