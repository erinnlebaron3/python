# def manual_exponent (5, 4):
# take first argument and mutlipy over and over four times
# print(manual_exponent)

# def manual_exponent (num, exp):
#     counter = exp - 1
#     total = num

#     while counter > 0:
#         total *= num
#         counter -= 1
#     return total

# print(manual_exponent(2, 3))
from functools import reduce

def manual_exponent(num, exp):
    computed_list = [num] * exp
    return (reduce(lambda total, element: total * element, computed_list))


print(manual_exponent(2, 3))