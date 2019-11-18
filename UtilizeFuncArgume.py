#  passed in argument values to our functions we have used what are called positional arguments and what that means is that the mapping 
# between the value and how that value is used in the function is completely determined by the position and the order that we passed the values in.

def full_name(first, last):
  print(f'{first} {last}')

full_name('Kristine', 'Hudgens')

answered = Kristine Hudgens

# calling them in and the position determines the mapping then it can lead to a number of bugs 
#  in python named arguments give you the ability to be much more explicit with this mapping.

# instead of simply passing a string in I can pass in whatever the name is.
# in whatever order you prefer
def full_name(first, last):
  print(f'{first} {last}')

full_name(first = 'Kristine', last = 'Hudgens')
full_name(last = 'Hudgens', first = 'Kristine')

# Python is much more flexible in that manner where all functions can use either named or pure positional arguments and it's completely up to you
#  that if there are more than 2 arguments I will use named arguments simply because it prevents any issues with me placing the values in in the
#  wrong order or calling the wrong name or anything related to that
