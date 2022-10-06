"""
Program: coupon_calculations.py
Author: Brandon Treu
Last date modified: 09/14/2022

The purpose of this program is take the input of the user for the original price, then apply a cash value coupon,
then apply a % coupon, after that calculate the tax rate, then add the shipping cost. The cost for shipping needs to
change based on the cost of the item, then give the total price
"""




#percent_coupons_table = [10, 15, 30]
#constants
TAX = 0.07
SHIPPING = 5.95

#get price from user
amount_of_purchase = int(input("What is the original amount of the purchase?"))
#if cash coupon then
is_there_a_cash_coupon = input("Are you using a cash coupon?(yes/no)")
if(is_there_a_cash_coupon == 'yes'):
    cash_coupon = int(input("Which one? (5 or 10)"))
    if(cash_coupon == 5 or 10):
        post_cash_coupon = amount_of_purchase - cash_coupon
        is_there_a_percent_coupon = input("Are you using a percent coupon?(yes/no)")
    else:
        print("Not a valid Cash Coupon")
        is_there_a_percent_coupon = input("Are you using a percent coupon?(yes/no)")
    if(is_there_a_percent_coupon == 'yes'):
        percent_coupon = int(input("Which one? (10, 15, or 30)"))
        post_percent_coupon = post_cash_coupon - (post_cash_coupon * (percent_coupon * 0.01))
        post_tax_cost = (post_percent_coupon * TAX) + post_percent_coupon
        if(post_tax_cost < 10):
            post_shipping_cost = post_tax_cost + SHIPPING
        elif(post_tax_cost < 30 and post_tax_cost >= 10):
            post_shipping_cost = post_tax_cost + (SHIPPING + 2.00)
        elif (post_tax_cost < 50 and post_tax_cost >= 30):
            post_shipping_cost = post_tax_cost + (SHIPPING + 6.00)
    print("The total cost is: " + str(post_shipping_cost))
else:
    print("no coupon")


