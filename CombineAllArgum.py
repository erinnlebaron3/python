# How to work with all function arguments at one time.

#  print out a greeting to the screen for the user and then iterate through the key-value pair of arguments

# use a formatted string
# inside of this going to use a string literal and pass in a joint statement
#  args which is going to take in the full set of arguments and this is going to be the user's name
# if there are any keyword arguments then I want to print out a task list.
#  going to implement a loop
#  talked about looping over dictionaries because remember a keyword argument does return a dictionary 
# key and the value and I'm just going to say key and val in our keyword arguments
# organizing these function calls is I'm passing in first the positional argument because that one does need to be placed 
# at the very start of our function call and then I'm passing in the args. 

# took a positional argument a unpacked set of items and then also our keyword arguments and we were
#  able to combine all of those into a single Python function.
def greeting(time_of_day, *args, **kwargs):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}.")

  if kwargs:
    print('Your tasks for the day are:')
    for key, val in kwargs.items():
      print(f'{key} -> {val}')


greeting('Morning',
         'Kristine', 'Hudgens',
         first = 'Empty dishwasher',
         second = 'Take pupper out',
         third = 'math homework')

answered =
Hi Kristine Hudgens, I hope that you're having a good Morning.
Your tasks for the day are:
first -> Empty dishwasher
second -> Take pupper out
third -> math homework