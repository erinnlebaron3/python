# to call math library
import math
# dont need to call import math for ABS math library is not needed for absolute value that is in the core Python library.



# ABS = absolute value of
# absolute value that's going to do is it's going to take just the pure value and it's going to remove this negative sign right 
import math

loss = -20.25 
product_cost = 89.99

print(abs(loss))
answer = 20.25


# MATH FLOOR
# technically you also could just call int on this
# one reason why you may not want to do that is because math.floor very clearly shows your intention
# When you say math floor when you're reading this later on or if someone else is reading it they're 
# going to understand that you wanted the lower value the rounded down lower value of product cost
# int isn't as clear as of what you want
# side effect of also giving you the floor value of that int because it takes away any floating point numbers. 

import math

loss = -20.25
product_cost = 89.99

print(math.floor(product_cost))
answer = 89


# Math cealing
# gives answer that is rounded up not down
# returns and integer
import math

loss = -20.25
product_cost = 89.99

print(math.ceil(product_cost))
answer = 90


# combinging
# math floor being called before absolut value
# The way it works is math floor on loss is what would be called first then the absolute value would be called on that. 
# That's the reason why if you run that you get 21 that's something that's important to know whenever you are nesting functions like that.
import math

loss = -20.25
product_cost = 89.99

print(abs(math.floor(loss)))
answer = 21


# ROUND
# this is when you simply want to round to the nearest whole 
import math

loss = -20.25
product_cost = 89.99

print(round(product_cost))
answer = 90


# SQUARE ROOT
# sqrt how to call square root
# gives floating point number
import math

loss = -20.25
product_cost = 89.99

print(math.sqrt(product_cost)
answer = 9.48


#  POW
# then it takes two arguments.
# print(math.pow(5, 2))   #25.0
# if you go through the math library and you look at the pow function you're going to see that it is much more complex and much more scientifically accurate.
# So if you're using exponents in large scientific calculations then you're going to want to use math POW versus if you just want a simple exponent you can 
# use the basic exponent operator just like we have right here.
import math

loss = -20.25
product_cost = 89.99

print(math.pow(5, 2))
answer = 25.0
print(5 ** 2)
answer = 25


import math

loss = -20.25
product_cost = 89.99

print(abs(loss))
print(math.floor(product_cost))
print(math.ceil(product_cost))
print(abs(math.floor(loss)))
print(round(product_cost))
print(math.sqrt(product_cost))
print(math.pow(5, 2))
print(5 ** 2)