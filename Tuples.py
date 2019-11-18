# Lists can change Touples can't
#  if at some point a sort method is called on the post data structure. And remember this is a list. 

# List: []
# Dictionary: {}
# Tuple: ()

# Tuple: immutable 
# List: mutable


# Touple

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')

# title, sub_heading, content = post

title = post[0]
sub_heading = post[1]
content = post[2]

print(title)

print(sub_heading)

print(content)
answer = 
Python Basics
Intro guide to Python
Some cool python content

# Unpacking Techinque
# always going to have title mapped to the first element subheading to the second content to the third. 
post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')

title, sub_heading, content = post

# title = post[0]
# sub_heading = post[1]
# content = post[2]

print(title)

print(sub_heading)

print(content)
answer =
Python Basics
Intro guide to Python
Some cool python content


# the title that should always be mapped to Python basics 
# subheading should be mapped to intro guide to Python 
# content should be mapped right to some cool Python content

# Tuple: ()

# Tuple: immutable 
# List: mutable

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')

# Tuple unpacking
title, sub_heading, content = post

# Equivalent to Tuple unpacking
# title = post[0]
# sub_heading = post[1]
# content = post[2]

print(title)

print(sub_heading)

print(content)
answer = 
Python Basics
Intro guide to Python
Some cool python content

#  list if the order of the elements change then you're unpacking may give you some
#  unexpected behavior may place certain elements in an order that you weren't expecting.
#  cannot sort a tuple
#  always going to have title mapped to the first element subheading to the second content to the third.
#  So that is truly the key difference between a tuple and a list you can work with them in a very similar manner as you can see. 
# You can carry them with their specific index you can pack them you can access them however you need and they allow you to store a set collection of data.