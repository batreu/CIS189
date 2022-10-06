"""
Program: forLoopTopic1.py
Author: Brandon Treu
Last date modified: 09/26/2022

This program will create a list of float point numbers and print each.
Then I create a list of odd numbers from 33 to 99 and print each odd number descending from 99 to 33
"""

my_float_list = [10.25, 11.25, 12.25, 13.25, 14.25,15.25]#Declare a list of floating point numbers

for number in my_float_list:#Write a for loop to print each
    print(number)

odd_number_list = []#here i am declaring a list that i want to use inside of my loop

for odd_numbers in range(31,101,2):#im stepping by 2 each time to just catch the odd numbers, and im starting at 31 since it is not inclusive
    odd_number_list.append(odd_numbers)#adding each odd number to my list
odd_number_list.reverse()#reversing the order of the list
print(odd_number_list)#printing