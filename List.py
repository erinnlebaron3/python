# like an array. It is a collection of values and that collection can be added to. You can remove items. You can query elements inside of it.
# Every time that you want a new database query what it's going to do is it's going to look at its set of data structures and it's going to go and it's going to put them in that.
#  in the case of a list you're going to have to know how to loop through 


#  this is now no longer just a set of strings what we have here is actually a true data structure we have a list of these string names which would be 
# like what we'd get if we queried a database with users.
"""
User Database Query
Kristine
Tiffany
Jordan
"""
users = ['Kristine', 'Tiffany', 'Jordan']
  
print(users)
answer = ['Kristine', 'Tiffany', 'Jordan']


# add to this list
# to add the string Anthony and I want to make this a new element at the list it goes at the very front I pass in the index.
"""
User Database Query
Kristine
Tiffany
Jordan
"""
users = ['Kristine', 'Tiffany', 'Jordan']
  
print(users)
    
users.insert(0, 'Anthony')

print(users)
answer =
['Kristine', 'Tiffany', 'Jordan']
['Anthony', 'Kristine', 'Tiffany', 'Jordan']


#  add element to list
# replace and assign elements
"""
User Database Query
Kristine
Tiffany
Jordan
"""
users = ['Kristine', 'Tiffany', 'Jordan']
  
print(users)
    
users.insert(1, 'Anthony')

print(users)

users.append('Ian')

print(users)
answer = 
['Kristine', 'Tiffany', 'Jordan']
['Kristine', 'Anthony', 'Tiffany', 'Jordan']
['Kristine', 'Anthony', 'Tiffany', 'Jordan', 'Ian']


# square brackets and hit return you can see this last element is what gets returned. Now, this is a very key thing to understand here. 
# Each one of these other times were printed this out. Notice how it had the brackets around the entire collection of data. What that means is that these are still lists.
#  So each one of these is a list object which means that as Python looks at it that you can only call the types of functions that are available to the list data type.
"""
User Database Query
Kristine
Tiffany
Jordan
"""
users = ['Kristine', 'Tiffany', 'Jordan']
  
print(users)
    
users.insert(1, 'Anthony')

print(users)

users.append('Ian')

print(users)

print(users[2])
answer = Tiffany


# change name
"""
User Database Query
Kristine
Tiffany
Jordan
"""
users = ['Kristine', 'Tiffany', 'Jordan']
  
print(users)
    
users.insert(1, 'Anthony')

print(users)

users.append('Ian')

print(users)

print(users[2])

users[4] = 'Braden'

print(users)
answer =
['Kristine', 'Anthony', 'Tiffany', 'Jordan', 'Braden']