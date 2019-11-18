# high level inheritance is the ability to create specialized versions of classes.

# the way that you declare that one type a class inherits from another is right here in the top line where you say 
# class you give the name of the class and then you pass in using parentheses the element so whatever class you want 
# it to inherit from. 

#  created a specialized class that has all of the attributes and all the behavior of the parent class

class User:
  def __init__(self, email, first_name, last_name):
    self.email = email
    self.first_name = first_name
    self.last_name = last_name

  def greeting(self):
    return f'Hi {self.first_name} {self.last_name}'

class AdminUser(User):
  def active_users(self):
    return '500'


erinn = AdminUser('erinn@devcamp.com', 'Erinn', 'LeBaron')

chantelle = User('chantelle@devcamp.com', 'Chantelle', 'Leany')

print(erinn.active_users())
print(erinn.greeting())
print(chantelle.greeting())

# greeting here for Tiffany even though Tiffany is an admin user and there is no greeting function inside of this class. 
# If I run this again you'll see that it prints out the full greeting.
# his is possible is because of inheritance
# Whenever we use inheritance the way it works is that the child classes like AdminUser these specialized classes they 
# have access to all of the same attributes and behavior as the parent class. And then you can simply add on any 
# specialized attributes or behavior into that child class the way we did right here with the admin user.