# how to make changes to old list and additional elements to end of list

# Make changes in place like sort function

# just an overide
# just replaced code
tags = ['python', 'development', 'tutorials', 'code']

# Nope

tags[-1] = 'programing'

print(tags)
answer = ['python', 'development', 'tutorials', 'programing']


# EXTEND
# it actually spreads out each one of the elements that are given to it. 
tags = ['python', 'development',
'tutorials', 'code']

# Nope
# tags[-1] = 'programing'

tags.extend('programing')

print(tags)
answer = ['python', 'development', 'tutorials', 'code', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'n', 'g']

# typicaly add new element
# wrap as a list then extend treats it like an element
tags = ['python', 'development',
'tutorials', 'code']

# Nope
# tags[-1] = 'programing'

tags.extend(['programing'])

print(tags)
answer = ['python', 'development', 'tutorials', 'code', 'programing']

# most common process to add to a list
# make sure to wrap in []
tags.extend(['programing'])


# ADD AND CREATE NEW LIST
# So you simply have to wrap that inside of that list square bracket syntax and then you can add it onto tags 
tags = ['python', 'development',
'tutorials', 'code']

# Nope
# tags[-1] = 'programing'

# tags.extend(['programing'])

new_tags = tags + ['programing']

print(new_tags)
answer = ['python', 'development', 'tutorials', 'code', 'programing']


# Typically whenever you're following this kind of process it's because you do not want to change the original values 
# so you want to keep this list intact. 
# from a best practice perspective usually, you're going to want to go with the second approach. 
tags = ['python', 'development',
'tutorials', 'code']

# Nope
# tags[-1] = 'programing'

# tags.extend(['programing'])

new_tags = tags + ['programing']

print(new_tags)

print(tags)
answer = 
['python', 'development', 'tutorials', 'code', 'programing']
['python', 'development', 'tutorials', 'code']




