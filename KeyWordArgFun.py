# can combine named arguments with the same concept. 
#  instead of saying args I'm going to give a double asterisk. So it's going to be two stars followed by kw.
def greeting(**kwargs):

#  kw is not a reserved word. but it common convention in Python. will becode that you are going to see the most

# returned back is a dictionary.
#  one of the biggest keys between working with keyword arguments versus just traditional unpacking
def greeting(**kwargs):
  print(kwargs)

greeting()
answered = {}

# unpacking a list gets a touple
# unpacking keyword arguments it gets returned as a dictionary.
# keyword argument needs to have a set of keys and associated values which as you know is the very definition 
# of a dictionary and so that is one of the key elements to remember.

# Basic way to work keyword
def greeting(**kwargs):
  print(kwargs)

greeting(first = 'Kristine', last = 'Hudgens')
answered = {'first': 'Kristine', 'last': 'Hudgens'}


# conditionl and cynamic basis
def greeting(**kwargs):
  if kwargs:
    print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")
  else:
    print('Hi Guest!')


greeting(first = 'Kristine', last = 'Hudgens')
answered = Hi Kristine Hudgens, have a greatday!