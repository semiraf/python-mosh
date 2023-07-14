price = 1000000
good_credit = False

if good_credit == True:
    down_payment = 0.1 * price
    
elif good_credit == False:
    house_price = 0.2 * price

print(f"Down payment: {house_price}")