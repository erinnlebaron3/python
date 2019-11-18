# sort function inside of Python lists and that is that it sorts all of the elements in place and there may be times where you do want to perform 
# that action. However, there may also be times where you simply want to sort a list and not change the original one.

# create some means such as sorted_list I create a variable like this and try to print this out. What's going to happen is it's going to print out 
# none and that is because sort does not return value.

# notice we're actually calling the original list. And so what that means is simply by calling the sort function on sale prices we have changed 
# the entire structure of these items and that may be something that you want to do.

sale_prices = [
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

print(sale_prices)
answer = [1, 3, 10, 40, 83, 100, 100, 220, 400]

# SORTED 
# has the same type of behavior as sort except it allows you to actually store that value. 
# sorted does not change the values in place so the list is going to remain completely intact 
# sorted called from front not back like sort
sale_prices = [
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

print(sorted_list)
answer = [1, 3, 10, 40, 83, 100, 100, 220, 400]

#  the sort function is that you can store items in ascending or descending values and sorted you can perform the exact same task.
#  it is sorting in a top to bottom order where it's taking the greatest values and it's putting them there first

sale_prices = [
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

sorted_list = sorted(sale_prices, reverse=True)

print(sorted_list)
answer = [400, 220, 100, 100, 83, 40, 10, 3, 1]