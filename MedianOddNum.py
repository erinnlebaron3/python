#  the tools that you're going to need in order to implement this properly.
# the best one is to use a python statistical library 


# to build this and this is going to be a very specific type of statistical median. 
# It will only work if you have an odd number of elements inside of your list

# The median value is the value that is exactly in the middle of the list.




# my try
"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""


sale_prices =[
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]


sale_prices.sort()
tag_range = sale_prices[3:-4]


print(sale_prices(tag_range))

# his solution
import math
"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""


sale_prices =[
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]


sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sale_items = sorted_list[:]
last_sales_items = sorted_list[-(math.floor(num_of_sales/2)):]
median = sorted_list[math.floor(num_of_sales/2):(math.floor(num_of_sales/2)+ 1)]

print(sorted_list)
print(num_of_sales)
print(first_sale_items)
print(last_sales_items)
print(median)
answer =
[1, 3, 10, 40, 83, 100, 100, 220, 400]
9
[1, 3, 10, 40, 83, 100, 100, 220, 400]
[100, 100, 220, 400]
[83]
