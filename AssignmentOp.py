# assignment operator. And so the syntax for that is going to get rid of everything here in the middle and say plus equals and then whatever value. 
total = 100

total = total + 10
print(total)
answer = 110


# assignment operator is +=
total = 100

total += 10 
print(total)
answer = 110

# subtration
total = 100
total -= 10
print(total)
answer = 90

# multiply
total = 100
total *= 2
print(total)
answer = 200

# divide
total = 100
total /= 10
print(total)
answer = 10.0

# floor division
#  remember that our floor division returns an integer it doesn't return a floating point number.
total = 100
total //= 10
print(total)
answer = 10


# modulos
# So here remember it is the percent equals 2. And this is going to return zero because 100 is even if we changed 100 to be 101. 
#  This is going to return one because remember the typical purpose of the modulus operator is to let you know if you're working with an event or an odd value.
total = 100
total **= 2
print(total)
answer = 0

# exponits
total = 100
total %= 2
print(total)
answer = 1






total = 100

total = total + 10
total += 10
total -= 10
total *= 2
total /= 10
total //= 10
total **= 2
total %= 2

product_two = 120
product_three = 10

total += product_two
total += product_three

print(total)