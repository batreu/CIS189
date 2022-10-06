"""
Brandon Treu
favorite_class_function.py

"this program takes the input of the users favorite class and prints it as many times as requested"
"""


class_name = input('enter your favorite class name')
number = input('how many times would you like this printed?')


def multiply_string(class_name, number):
    i = 0
    while i != number :
        i = i + 1
        print(class_name)

if __name__ == '__main__':
    multiply_string(class_name, int(number))