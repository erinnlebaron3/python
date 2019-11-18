#  ranges and the word slices are used many times interchangeably 
# advanced ranges and advanced slices inside of Python lists.

# start with development and then it's going to go and it's going to go all the way up to the very last element. 
# It's not going to include it because remember with ranges and slices it is going to simply end right before this element
tags = [
  'python',
  'development',
  'tutorials', 
  'code',
  'programing',
  'computer science',
]

tag_range = tags[1:-1]

print(tag_range)
answer = ['development', 'tutorials', 'code', 'programing']

# ADDING ANOTHER INTERVAL INTO THE RANGE AKA SLICING
#  adding another colon you can pass in an interval
# this grabs everyother thing in list
#  something that you will come across especially in the machine learning space
# one of those is going to be doing things such as grabbing every other element in a list and this makes this very easy and straightforward.

tags = [
  'python',
  'development',
  'tutorials', 
  'code',
  'programing',
  'computer science',
]

tag_range = tags[:-1:2]

print(tag_range)
answer = ['python', 'tutorials', 'programing']

# FLIP ORDER OF LIST

tags = [
  'python',
  'development',
  'tutorials', 
  'code',
  'programing',
  'computer science',
]

# tag_range = tags[:-1:2]
tag_range = tags[::-1]

print(tag_range)
answer = ['computer science', 'programing','code', 'tutorials', 'development', 'python']

#  All that our method here did was it just cared about the index value and swapping those out sort works very differently.
# the way the sorting function works is it looks at the alphabetical value. 

tags = [
  'python',
  'development',
  'tutorials', 
  'code',
  'programing',
  'computer science',
]

# tag_range = tags[:-1:2]
# tag_range = tags[::-1]

# print(tag_range)

# ['computer science', 'programing','code', 'tutorials', 'development', 'python']

# ['tutorials', 'python', 'programing', 'development', 'computer science', 'code']

tags.sort(reverse=True)

print(tags)
answere = ['tutorials', 'python', 'programing', 'development', 'computer science', 'code']

# performing sorting in both of these options so we sorted our list just like we did here. We also sorted the list right here. However, 
# they were looking at different criteria to generate the new results set.

# SORT FUNCTION
# Python is so careful about immutability that sort doesn't actually return anything.
# So sort will go and it will change the order of the tags so it will go in and it will, in this case, reverse them it'll sort them alphabetically 
# it'll perform its full set of tasks and it will change tags but it will not return that value.
tags = [
  'python',
  'development',
  'tutorials', 
  'code',
  'programing',
  'computer science',
]

# tag_range = tags[:-1:2]
# tag_range = tags[::-1]

# print(tag_range)

# ['computer science', 'programing','code', 'tutorials', 'development', 'python']

# ['tutorials', 'python', 'programing', 'development', 'computer science', 'code']

sorted_tags = tags.sort(reverse=True)

print(sorted_tags)
answer = None

# So sort will go and it will change the order of the tags so it will go in and it will, in this case, reverse them it'll sort them alphabetically 
# it'll perform its full set of tasks and it will change tags but it will not return that value.
#  the key is that the sort function goes in and it changes tags but it doesn't store it as a standard operation inside of a variable.

tags = [
  'python',
  'development',
  'tutorials', 
  'code',
  'programing',
  'computer science',
]

# tag_range = tags[:-1:2]
# tag_range = tags[::-1]

# print(tag_range)

# ['computer science', 'programing','code', 'tutorials', 'development', 'python']

# ['tutorials', 'python', 'programing', 'development', 'computer science', 'code']
tags.sort(reverse=True)
# sorted_tags = tags.sort(reverse=True)

print(tags)
answer = ['tutorials', 'python', 'programing', 'development', 'computer science', 'code']
