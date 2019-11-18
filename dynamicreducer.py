import operator
from functools import reduce

"""
dynamic_reducer([1, 2, 3], '+') # 6
dynamic_reducer([1, 2, 3], '-') # -
dynamic_reducer([1, 2, 3], '*') # 6
dynamic_reducer([1, 2, 3], '/') # -
"""

def dynamic_reducer(collection, op):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    return reduce((lambda total, element: operators[op](total, element)), collection)

print(dynamic_reducer([1, 2, 3], '+')) 
print(dynamic_reducer([1, 2, 3], '-')) 
print(dynamic_reducer([1, 2, 3], '*')) 
print(dynamic_reducer([1, 2, 3], '/')) 


# from collections import Counter
# from itertools import chain

# lst = [(1,2,3), (3,4,5), (4,7,8,9), (5,3,9)]

# duh = [k for k, v in Counter(chain.from_iterable(lst)).items() if v==1]
# print(duh)