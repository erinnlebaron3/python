# to only grab a few of these items then a list range gives us the ability to do that
# as a reminder if this part kind of went past you when we were working on strings the second argument here in the range is not included in the results. 
# look at this list you can see that we have Python which has an index of zero development which is one and then tutorials which has an index of two.
# this syntax also allows us to grab ranges that go from end to end.[:]

# Grab one tag with range
tags = ['python', 'development', 'tutorials', 'code']

tag_range = tags[1:2]

print(tag_range)
answer = ['development']


# Grab two tags with range
tags = ['python', 'development', 'tutorials', 'code']

tag_range = tags[1:3]

print(tag_range)
answer = ['development', 'tutorials']

# Grab from one tag to the end
tags = ['python', 'development', 'tutorials', 'code']

tag_range = tags[1:]

print(tag_range)
answer = ['development', 'tutorials', 'code']

# Start at the begining and go to a certain index
tags = ['python', 'development', 'tutorials', 'code']

tag_range = tags[:2]

print(tag_range)
answer = ['python', 'development']

# NEGATIVE IN RANGE
# if you ever want everything from the beginning you never have to pass in a zero.
# if I want all of the elements except the last one what I can do is just pass in a negative index because 
# remember that negative one will go to the very back of the list and it will add this one as the delimiters so this is going to be the one where our range stops

tags = ['python', 'development', 'tutorials', 'code']

tag_range = tags[:-1]

print(tag_range)
answer = ['python', 'development', 'tutorials']

# Pass in all elements leave range blank

tags = ['python', 'development', 'tutorials', 'code']

tag_range = tags[:]

print(tag_range)
answer = ['python', 'development', 'tutorials', 'code']