"""
Brandon Treu
basic_list.py

this program will take a users input up to 3 times and append it to a list, then print the list
"""
list=[]

def make_list():
    for x in range(3):
        x = int(get_input())
        list.append(x)
    print(list)
    return list


def get_input():
    userInput = input("What is your input?")
    try:
        userInput = int(input(""))
    except:
        print("Please enter a number.")
    return userInput



if __name__ == '__main__':
    make_list()