#  lambda, essentially what it is, is a tool that allows you to wrap up a function. 
#  then easily pass it to other functions
# wrap up some behavior, usually pretty small behavior and then pass it to other functions. 
# very mobile and easy to use
# lambda is a very similar almost to a variable
#  lets you wrap up a process

#  lambda returns of value so you're pretty much always going to be using a lambda where you're returning something. 

#  call lambda 
# followed by a list with a comma
# end list with colon
# function f with a quotation with curly brackets {} 
full_name = lambda first, last: f'{first} {last}'


# greeting function
def greeting(name):
  print(f'Hi there {name}')

greeting(full_name('Kristine', 'Hudgens'))

# Combined
full_name = lambda first, last: f'{first} {last}'

def greeting(name):
  print(f'Hi there {name}')

greeting(full_name('Kristine', 'Hudgens'))

answered = Hi there Kristine Hudgens