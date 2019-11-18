#  tuple is immutable which means that you're not able to change it whereas a list is mutable which means that you can add 
# elements take elements away and perform any of those kinds of tasks on the fly
#  in order for python to realize that this is a tuple we need to add a comma 

# Re-Assignment
# dding to a tuple what you need to do is place in whatever value you have 
# how tuples work and how python works when it comes to evaluating expressions what would happen right here is these parens. 
# Whenever you have a single element. 
# This is not going to be treated like a tuple. Instead what that's going to be treated like is like a mathematical parens expression.
# did not add to the first tuple. Instead we leveraged reassignment and we actually created a brand new tuple and we simply overrode the variable name 
# what we can do is create two objects add them together so we're concatenating them and then put them inside of this variable and it's simply going to override it.
post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

post = post + ('published',)

title, sub_heading, content, status = post

print(title)
print(sub_heading)
print(content)
print(status)
answer = 
Python Basics
Intro guide to python
Some cool python content
published

# post += ('published',) is the same as post = post + ('published',)

# ID function
# gives a referance and unique id 
# lets us see whats stored in memory

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

print(id(post))
print(id(post))

post += ('published',)

print(id(post))

title, sub_heading, content, status = post

print(title)
print(sub_heading)
print(content)
print(status)
answer =
139989886486640
139989886486640
139989886789968
Python Basics
Intro guide to python
Some cool python content
published
# first two elements here because it's referencing the exact same post tuple have an identical number. 
# This 14 ending in 256. However, this third one which is for our post after we've created a new tuple a new set of combined tuples. 
# This now ends in 5336 and so this is proof that we are no longer working with this original tuple. 
# This one was created it was used here, here and then we took it added this new publish status to it and when we did that python went 
# and it created a new object in memory and therefore a new reference point.