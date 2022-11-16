
"""
Brandon Treu
my_definitions.py

"""


def greeting():  # this prints my greeting
    print('Stay a while and listen....')


def author(code_author):  # this function prints the author
    print('The author is :  ',code_author)


def print_dict(dict_name):
    for key, value in dict_name.items():
        print(key, 'are', value)


def print_set(set_name):
    for x in set_name:
        print(x)