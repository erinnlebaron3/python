# list comprehension works is by setting up the alternative because what a list comprehension is is essentially a set of for in loops and 
# conditionals that can all be placed inside of a single line of code.


# instead of simply appending to cubed_nums what we're doing is we're dynamically generating this list. 

# num is the iterator variable and can be whatever you want

# perfered syntax
num_list = range(1, 11)
cubed_nums = []

for num in num_list:
  cubed_nums.append(num ** 3)

print(list(num_list))
print(cubed_nums)
answer = 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]



# List comprehention
# short cut for code for FOR IN LOOP
# not perfered syntax
num_list = range(1, 11)
cubed_nums = []

# for num in num_list:
#   cubed_nums.append(num ** 3)

cubed_nums = [num ** 3 for num in num_list]

print(list(num_list))
print(cubed_nums)
answer = 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

#  in addition to having this kind of behavior we also can add a condition.



# get only EVEN numbers
# we're to use the modulus operator(%) here. 
# modulus operator will tell us if there is a remainder or not and it will return whatever that value is. 

num_list = range(1, 11)

even_numbers = []

for num in num_list:
  if num % 2 == 0:
    even_numbers.append(num)

print(list(num_list))
print(even_numbers)
answer = 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[2, 4, 6, 8, 10]


# how we were able to take four lines of code and condense it down into a single line. 
# don't have to call append. And the reason is because we're not starting with an empty list like we did before. 
/Instead, we are generating this on the fly. 
num_list = range(1, 11)

even_numbers = []

# for num in num_list:
#   if num % 2 == 0:
#     even_numbers.append(num)

even_numbers = [num for num in num_list if num % 2 == 0]

print(list(num_list))
print(even_numbers)
answer = 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[2, 4, 6, 8, 10]