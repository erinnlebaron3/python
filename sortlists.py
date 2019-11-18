#  common process you're going to have to implement is the ability to sort your elements. 
# Python has an index here of zero development of one so on and so forth 
# Python lists are mutable which means you can change them. They're not like strings or those types of data type.
# So that means that if we make a change to our list that change is permanent so we don't have to reassign it to a value 
#  sort function is pretty intuitive in being able to check to see which values are inside and which data type is contained 
# inside of each one of these elements and then it adjusts how it performs its sorting process based off of that.

# it's going to print them in the exact order of their index 
tags = ['python', 'development', 'tutorials', 'code']

print(tags)
answer = ['python', 'development', 'tutorials', 'code']

# BASIC SORT

# .sort puts functions in alphabetical order
tags = ['python', 'development', 'tutorials', 'code']

tags.sort()

print(tags)
answer = ['code', 'development', 'python','tutorials']

# tags.sort(reverse=True)
# if you want it backwards
# True has to be capitalized
# taking the value of the alphabetical list and it simply flipping it back. So now it's going from Z to A
# this is with alphanumeric characters like we have right here. If we have the integers the same process pretty much follows. 
tags = ['python', 'development', 'tutorials', 'code']

tags.sort(reverse = True)

print(tags)
answer = ['tutorials', 'python', 'development', 'code']

# Integer
totals = [234, 1, 543, 2345]

print(totals)
answer = [234, 1, 543, 2345]

# integer with .sort()
# sorts them by value
# sorting by the value that the integer represents when it comes to strings. 
totals = [234, 1, 543, 2345]

totals.sort()

print(totals)
answer = [1, 234, 543, 2345]

# Integer with True
# goes from the greatest value all the way down
totals = [234, 1, 543, 2345]

totals.sort(reverse = True)

print(totals)
answer = [2345, 543, 234,1]

# COMPLETE CODE
tags = ['python', 'development', 'tutorials', 'code']

print(tags)

tags.sort()

print(tags)

tags.sort(reverse=True)

print(tags)

totals = [234, 1, 543, 2345]

totals.sort(reverse=True)

print(totals)
answers =
['python', 'development', 'tutorials', 'code']
['code', 'development', 'python','tutorials']
['tutorials', 'python', 'development', 'code']
[1, 234, 543, 2345][2345, 543, 234,1]