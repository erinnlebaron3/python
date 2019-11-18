#  say init and then this is going to receive self and it's also going to receive the title of the website inside of here. 
# I'm going to set this attributes value or I should say this instance attributes value to self.title and set this equal 
# to whatever title that gets passed in.
# instance attribute and what that means is it's an attribute that belongs to this specific instance


#  INSTANCE ATTRIBUTE

class Website:
  def __init__(self, title):
    self.title = title


ws = Website('My Website Title')
print(ws.__dict__)


# data values specific to this instance
class Website:
  def __init__(self, title):
    self.title = title


ws = Website('My Website Title')
print(ws.__dict__)

ws_two = Website('My Second Title')
print(ws_two.__dict__)



# Class Attribute
class DifferentWebsite:
  title = 'My Class Title'

dw = DifferentWebsite()
print(dw.title)
# printed{}


# would think that we set our title we hardcoded it inside of our Website class or a different website class and 
# you'd think that we would have access to it in the same way that we had access to our values up here. 
# one of the key differences between having what is called a class attribute versus an instance attribute.

# have access to values but not treated the same way.

class DifferentWebsite:
    title = 'My Class Title'


dw = DifferentWebsite()
print(dw.title)
# printed My Class Title

# title is similar to function or methond in the class just hardcoded in

class DifferentWebsite:
    title = 'My Class Title'


dw = DifferentWebsite()
print(dw.title)

dw_two = DifferentWebsite()
print(dw_two.title)
# prints My Class Title twices

#  the difference between a class attribute and an instance attribute really comes down to the name
# a class attribute is an attribute that belongs to the class definition. So it's hardcoded directly into the class

#  instance attribute belongs to the instance,
# needed to pass that value in directly into the instance 
# for every other instance of the class we had to pass in a different value and then we were able to have access to it.