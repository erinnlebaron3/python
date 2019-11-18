# to be a common way that you implement inheritance and polymorphism.
# leverage functions in order to make it possible.

# get rid of this abstract class at the top 
#  copy this init function into both of our classes.
# going to have a heading class and a div class and these are going to be standalone classes.
# not going to have them inherit from anything and they're simply going to be their own classes.
# going to create a function and this is going to be where the polymorphism occurs

#  As you see we were actually able to cut out a decent amount of boilerplate code and were still 
# able to replicate the exact same behavior.

class Heading:
    def __init__(self, content):
      self.content = content

    def render(self):
      return f'<h1>{self.content}</h1>'

class Div:
  def __init__(self, content):
    self.content = content

  def render(self):
    return f'<div>{self.content}</div>'

div_one = Div('Some content')
heading = Heading('My Amazing Heading')
div_two = Div('Another div')

def html_render(tag_object):
  print(tag_object.render())

html_render(div_one)
html_render(div_two)
html_render(heading)

#  have quite a bit of shared behavior so if you're HTML class had say a half dozen functions inside of it, 
# that each one of the inherited classes like a div or heading would need then that would be one time where 
# you'd want to use inheritance.

# on the other hand you don't really have a lot of shared behavior but you simply want to be able to call the same 
# function just like we have right here where you want to make sure that each one of these classes has a render function
#  that you can call it then being able to use polymorphism with a function based approach 