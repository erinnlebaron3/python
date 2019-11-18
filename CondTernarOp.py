# `ternary operator` which allows you to create a if else statement.
# ternary operators can be slightly more challenging to read if they're not implemented correctly

#  Zen of Python is that simple is better than complex.

# need to be careful and you need to make sure that when you implement these that they are better than simply going with a standard if else statement

# create a variable here called role
# create another variable here called auth and then this is where we're going to store the output of our ternary operator and so I'm going to 
# add a space and equals because we're performing an assignment 


# so this is a pretty standard approach and this is in my opinion a good way of being able to build out a ternary operator because my rule of thumb 
# is that whenever I'm building out a conditional if it can read as close to normal language as possible then that can be a good scenario where a 
# ternary operator can be used because then it is clear.

# access this if the role is set to admin. If not then you cannot access it.

# essentially what a Ternary operator does is it just reorganizes what a typical conditional does for us

# can access site
role = 'admin'

auth = 'can access' if role == 'admin' else 'cannot access'

print(auth)
answer = can access

# cant access site
role = 'guest'

auth = 'can access' if role == 'admin' else 'cannot access'

print(auth)
answer = cannot access


# assigning here whatever the result of the ternary operator is so you can see that if that condition is true you place that first. 

# just going to return the value or I'm going to set it equal to auth so I can say auth is equal to this or it's equal to this value.
#  if role is equal to admin then to perform this task.
# foremost is what you're going to place in a ternary operator is exactly what you want to happen if the condition is true. 
# And then next you place your condition.
role = 'admin'

# auth = 'can access' if role == 'admin' else 'cannot access'

# print(auth)
auth = 'can access' if role == 'admin' else 'cannot access'

if role == 'admin':
  auth = 'can access'
else:
  auth = 'cannot access'

print(auth)
answer = can access

# could be guest, it could be student, it could be jibberish, it doesn't matter if it's anything besides admin it's going to say cannot access. 
role = 'guest'

# auth = 'can access' if role == 'admin' else 'cannot access'

# print(auth)
auth = 'can access' if role == 'admin' else 'cannot access'

if role == 'admin':
  auth = 'can access'
else:
  auth = 'cannot access'

print(auth)
answer = cannot access

# nice benefits on using a ternary operator and that is that you only need to have this assignment placed here one time. 
#  with the ternary operator all we had to do was say I want to assign whatever the value is whether it's true like we have here or if it's 
# false it is going to store whatever that value is.

#  good example of when to use the ternary operator 
# in this scenario we have a clear mapping for what happens when a rule is set to an admin versus what happens when it's not. 
