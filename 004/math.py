import math

house_price = 1000000
good_credit = False

if good_credit:
    credit_type = "Good"
    down_payment = house_price * .10
else:
    credit_type = "Poor"
    down_payment = house_price * .20

print(f"You have {credit_type} credit. Your down payment is: ${down_payment}")