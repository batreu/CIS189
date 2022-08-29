"""
Program: variablesAssignment.py
Author: Brandon Treu, batreu@dmacc.edu
Last date modified: 08/28/2022

The purpose of this program is to show my understanding of variables
The inputs are an integer, a string, a float, and a constant representing the quantity, item, size, and price.
The output a string stating the quantity, followed by the item name, and size. The next line output is the item name
followed by the price constant. I also output the variable types to confirm their type.
"""

#variable declarations
quantity = 7
item = 'shoes'
size = 10.5
output_quantity = str(quantity)
output_item = str(item)
output_size = str(size)

#testing variable types
print(str(type(quantity)))
print(str(type(item)))
print(str(type(size)))

#constants
PRICE = 14.99
OUTPUT_PRICE = str(PRICE)

#testing constant type
print(str(type(PRICE)))

print(output_quantity + ' ' + output_item + ' size: ' + output_size)
print(output_item + ' cost: ' + OUTPUT_PRICE)