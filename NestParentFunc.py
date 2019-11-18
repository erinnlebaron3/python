# Python is different than many other programming languages where it allows you to place one function inside of another function 

# Nested
def greeting(first, last):
  def full_name():
    return f'{first} {last}'

  print(f'Hi {full_name()}!')


greeting('Kristine', 'Hudgens')


# if some other part of the program does need access to the full name function then you may want to keep it separate and call 
# them independent of each other. 
# nested function is when should you choose to nest versus keep them separate. And one of my rules of thumb for it is whenever 
# I have a function that does not need to exist outside of a parent function then that is a good time to perform nesting.