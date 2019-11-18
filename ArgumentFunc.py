# function called name and if we were to try to call this function without some kind of value.

def greeting(name = 'Guest'):
  print(f'Hi {name}!')

greeting()
greeting('Kristine')

answered = 
Hi Guest!
Hi Kristine!

# whenever we do pass in a string like we have right here then that overrides the default argument. 
# And so that is a very nice and clean way of being able to have your system be dynamic enough so that you can call the function 
# and you can pass it arguments or you can leave those arguments blank and this is the proper way of implementing default arguments.


#  wrong way to do this 
#  do not want to make a mutable data type such as a list a default argument 
# entire issue of mutability our collection is staying in memory. 
# calling some function from some other part of the program it is going to go back and it's going to see the very first time 
# where collection was created and it's going to go reference that original collection.
# Two different collections that's what it looks like but it's actually referencing the same spot in memory.
# considered a very bad practice to ever set a default argument as a list.
# Nope
def some_function(collection = []):
  collection.append(1)
  print(id(collection))
  return collection


print(some_function())
print(some_function())