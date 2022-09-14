"""
Program: elifStatements.py
Author: Brandon Treu
Last date modified: 09/13/2022

The purpose of this program is to accept the input for package the user wants, then give them the price of the package.
"""

#list packages to user
print("Hello! Please sign up for the Programmer's Toolkit Monthly Subscription Box")
print("The options are Platinum, Gold, Silver, Bronze, or Free Trial. Type the option name to see he price.")
#variables
userPackage = input('What package would you like?')
#elif statements
if(userPackage == "Platinum"):
    print("The Platinum Package is $60.00")
elif(userPackage == "Gold"):
    print("The Gold Package is $50.00")
elif(userPackage == "Silver"):
    print("The Silver Package is $40.00")
elif(userPackage == "Bronze"):
    print("The Bronze Package is $30.00")
elif(userPackage == "Free Trial"):
    print("The Free Trial is free!")
else:
    print("Sorry that's not an option")#to make sure the user is typing on of the package options