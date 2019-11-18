# difference between printing something out from a function and returning something from a function and this is going to be a critical 

#  full name function 
# takes in two arguments 

# return values which means that when you call this full name function here you don't care about it printing 
# this out to the console in a program such as a django or a flask API application.

#  can understand any programming concept as long as you can understand the input and the output of a process. 


# in review that is the key difference between the return and the print statements.

#  full name function here
def full_name(first, last):
    print(f'{first} {last}')


full_name('Erinn', 'LeBaron')

# first and last inputs
# only outputs is print right now


# Return Function
def full_name(first, last):
    return f'{first} {last}'


full_name('Erinn', 'LeBaron')


# SOURCE CODE
def full_name(first, last):
  return f'{first} {last}'


kristine = full_name('Kristine', 'Hudgens')

def greeting(name):
  print(f'Hi {name}!')


greeting(kristine)