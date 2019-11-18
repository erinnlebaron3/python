#  a manual way of doing it it is what's called an iterative approach where we are going to simply iterate over the elements and then build up the solution.
#  a functional approach and a functional approach is going to leverage, and this is where one of the hints will be, it is going to leverage the reduce function.
#  import from functools import reduce
#  build out a function called manual_exponent that takes in two arguments and then it uses whatever the first argument is as the base and the next argument is the 
#  exponent and it returns whatever the value of that is. 


# manual_exponent and it's going to take a number and an exponent and arguments. And so the very first thing I'll do is I'm going to create a couple of variables 
# I'm going to create a counter variable which is going to have the exponent minus one.
# asterisk equals so this is going to give us a product so the total is going to be equal to num. And now this is the same exact thing as saying total equals total times num.

from functools import reduce

#  def manual_exponent(num, exp):
#      computed_list = [num] * exp
#      return (reduce(lambda total, element: total * element, computed_list))
#
#
#  print(manual_exponent(2, 3))
#  print(manual_exponent(10, 2))
#  print(manual_exponent(3, 3))
#  print(manual_exponent(10, 5))

def manual_exponent(num, exp):
    counter = exp - 1
    total = num

    while counter > 0:
        total *= num
        counter -= 1

    return total

print(manual_exponent(2, 3)) 8
print(manual_exponent(10, 2)) 100
print(manual_exponent(3, 3)) 
print(manual_exponent(10, 5))

# creating a counter variable and by default, it's going to be set to whatever the exponent value is minus one. And the reason for that is because I'm 
# setting total equal to whatever the value of num is. 
# So the first time the counter is going to for this specific example the counter is going to start at 2 then it's going to iterate it's going to multiply two 
# times two which will be four. Then it will decrement that counter down to 1 which means it only has one more time of going through it and then it's going 
# to multiply by two one more time and that is how you get 8.

def manual_exponent(num, exp):
    computed_list = [num] * exp
    return (reduce(lamda total, element: total * element, computed_list))