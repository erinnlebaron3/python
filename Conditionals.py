# the syntax for being able to build a conditional here is to say if and that is a reserved keyword in Python 
# if age is less than 25 and then I follow this up with a colon and then when I come to a new line I need to 
# have indentation and we've already talked about this for our for in loops and are while loops and it's a good rule of thumb in Python.
#  see a colon the next line you're going to have to have indented and so now that we've implemented our basic conditional.

age = 15

if age <25:
  print(f"I'm sorry, you need to be at least 25 years old"

answer = I'm sorry, you need to be at least 25 years old

# when it comes to understanding conditional logic you just have to think of setting up your conditions and assuming 
# they're going to be either true or false. 


# adding a second condition
# if else statement
age = 1500

if age <25:
  print(f"I'm sorry, you need to be at least 25 years old")
else:
  print(f"Your good to go, {age} fits in the range to rent a car.")

answer = Your good to go, 1500 fits in therange to rent a car.

# The else if or elif

# False
age = 1500

if age <25:
  print(f"I'm sorry, you need to be at least 25 years old")
elif age > 100:
  print(f"I'm sorry, {age} is to old to rent a car")
else:
  print(f"Your good to go, {age} fits in the range to rent a car.")

answer = I'm sorry, 1500 is to old to renta car

# True
age = 50

if age <25:
  print(f"I'm sorry, you need to be at least 25 years old")
elif age > 100:
  print(f"I'm sorry, {age} is to old to rent a car")
else:
  print(f"Your good to go, {age} fits in the range to rent a car.")

answer = Your good to go, 50 fits in the range to rent a car.
