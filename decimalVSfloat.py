# in python all decimals are floating numbers unless decimal is called
# you can create a decimal is to copy decimal it has to be all like this with it titled with the capital D and decimal spelled out and then because it's a 
# function we're going to call decimal.
# when it comes to anything that is finance related or scientific or where the level of precision is incredibly important then it's a good idea to bring in the decimal class
# is a very important caveat when working with decimals and that is if you want to perform advanced calculations that need to be very precise than using the 
# floating point number is not going to be your best option.

#  to import decimal we say import the decimal library and then say from decimal
    from decimal import Decimal


#  Float
product_cost = 88.40
comission_rate = 0.08
qty = 450

product_cost += (comission_rate * product_cost)
print(product_cost * qty)
answer = 42962.4




from decimal import Decimal

product_cost = 88.40
commission_rate = 0.08
qty = 450

product_cost += (commission_rate * product_cost)
print(product_cost * qty) # 42962.4

product_cost = Decimal(88.40)
commission_rate = Decimal(0.08)
qty = 450

product_cost += (commission_rate * product_cost)
print(product_cost * qty) # 42962.40000000000282883716451



# CONVERTING BETWEEN INTEGER, FLOAT, DECIMAL, AND COMPLEX NUMBER DATA




# Float
#   keyword is float and I can say quantity
product_cost = 88.80
commission_rate = 0.08
qty = 450
print(float(qty))
anwer = 450.0

# INTEGER
#  gives us similar behavior to how the floor division computation works where even though 88.8 is closer to 89 all that 
#  essentially it's doing is it's just taking the floating point variable and just throwing it away.
# if you are converting these values it doesn't round it to the Close's hole number. It simply takes whatever integer value is there and it just keeps that and ignores the rest. 
product_cost = 88.80
commission_rate = 0.08
qty = 450

print(int(product_cost))
answer = 88

# DECIMAL
# remember to import decimal we say  from decimal import this decimal
   from decimal import Decimal 

from decimal import Decimal

product_cost = 88.80
commission_rate = 0.08
qty = 450

print(Decimal(product_cost))
answer = 88.790232012122200




# COMMISION RATE
#  say complex and this is going to give us the scientific notation for commission rate
#  scientific notation in parentheses and this actually because it returns in parens this is giving you a complex object that you can work with.
product_cost = 88.80
commission_rate = 0.08
qty = 450
print(complex(commission_rate))





from decimal import Decimal

product_cost = 88.80
commission_rate = 0.08
qty = 450

print(int(product_cost))
print(float(qty))
print(Decimal(product_cost))
print(complex(commission_rate))