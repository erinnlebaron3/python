# wont be using set to much
# set is a merging of list and dictionary syntax
# not using key value pairs with no values
# set will always have unique elements 
# set does not support indexing

# SET IS A DICTIONARY WITHOUT VALUSE THATS WHY EVERY VALUE HAS TO BE UNIQUE
# set up a list of tags and instead of using brackets like we use if we are building a
#  list we're actually going to look like we're creating a dictionary but we're not because we're not using key-value pairs.
# using elements and we're listing them out just like we would in a traditional list 

# most important reason why you are going to ever want to use a set and that is that a set requires that all of the elements 
# inside of the set are unique. 

# very important whenever we're using a set, our set is always going to be guaranteed to have unique elements and so that is one of the top reasons.

#  if you have a collection of elements where you want to check if one of those elements exist or if a element exists in that set then this gives a 
# really nice syntax for doing that.



# Query is to ask or search through

# tags = variable
# python... elements
# query_one and query_two  = variable
# in = function doing something in python Key term reserve word
# print = function doing something in python Key term reserve word

tags = {
    'python',
    'coding',
    'tutorials'
}

print(tags)
answer = {'tutorials', 'python', 'coding'}

# Query is a value in this  set IN is the key word
tags = {
    'python',
    'coding',
    'tutorials'
}
# nope
# print(tags[0])
query_one = 'python' in tags


# Query is a value in this  set IN is the key word
print(query_one)
answer = True

tags = {
    'python',
    'coding',
    'tutorials'
}

query_two = 'ruby' in tags
print(query_two)
answer = False