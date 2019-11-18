# classes are object mappers so classes essentially give you the ability to create a blueprint for objects
#  classes can have data inside of them and they can also have functions and they can add behavior.

# by itself a class does nothing
# need to perform a process called instantiation.
#  nothing that's going to happen in this class unless we go and we create an object with that class and the process of creating the object is called instantiation.

#  one uppercase letter so this is going to be capital and that is the common convention 
class Invoice:

    def greeting():
        return 'Hi there'


# Instantiation

# stands for invoice one
inv_one = Invoice()
print(inv_one)



class Invoice:

# need to pass a default argument in to any function here that you have in a class and what you need to pass in is the word self.
#  self references the instance so in this case self is going to be referencing inv_one In this case, it's referencing inv_2 
    def greeting(self):
        return 'Hi there'


inv_one = Invoice()
print(inv_one.greeting())

inv_two = Invoice()
print(inv_two.greeting())

