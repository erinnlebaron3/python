# integrate the concept of unpacking into a function argument collection.
#  can't simply place a hard-coded list of items the way we placed here inside of our full name function.
# a scenario where you need more than two

# * means everything else in the rest of the code all the rest of the arguments

#  unpacked our list of arguments it got returned as a tuple. 

# leveraging unpacking we're able to create a much more flexible interface for our function

#  we could take in any number of names and then we can wrap that inside of this argument list unpack it inside of the function 
# body itself and then we can use it and actually have something that works for our program.

# syntax for using unpacking is that you're going to start off with a star *
# common convention is to name the argument list args 
# common to simply use the name args which is short for arguments and then you need to have an asterisk in front of that args name.
def greeting(*args):
  print('Hi ' + ' '.join(args))

# *arges is best practice

def greeting(*args):
  print('Hi ' + ' '.join(args))

greeting('Tiffany', 'Hudgens')
answered = Hi Tiffany Hudgens


# 3 arguments
def greeting(*args):
  print('Hi ' + ' '.join(args))


greeting('Kristine', 'M', 'Hudgens')
answered = Hi Kristine M Hudgens


# Can use * with names but not best practice args is the most used key word
def greeting(*names):
  print('Hi ' + ' '.join(names))


greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')


# working with args you are not limited when you're passing in this unpacking kind of argument you're not limited to only passing in a collection of data. 
#  working with a traditional positional argument here and what that means is anytime you call greeting 
# the first argument needs to be the time of day and then after that we're passing in the args
# working with a traditional type of argument and args
# you still need to use your join = turns it into a string, and then it combines anything that we start off with. 
# if we start off with an empty string then it takes that tuple and it simply puts an empty space in between each one of the values
def greeting(time_of_day, *args):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")


greeting('Afternoon', 'Kristine', 'M', 'Hudgens')
greeting('Morning', 'Tiffany', 'Hudgens')