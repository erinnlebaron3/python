# partition function works in Python is it's going to look inside the string for whatever you pass in as the argument. 
#   once it finds that it then partitions the entire string and separates it into three elements and so it is going to take python and it is going to be the first element.
#  whenever you call partition and you perform assignment like we're doing here. It actually returns what's called a tuple collection.
#  essentially what it's allowing us to do is it means that it's going to break what used to be a string which was one object into three objects. 
#  It's going to break it into the first the second and the third.
#  very popular Python convention for whenever you have values that you do not want to use the best way to represent those is with an underscore. 
#  So this is not a required syntax it is simply a best practice in the Python community 

heading = "Python: An Introduction"

header, _, subheader = heading.partition(': ')

print(header)
print(subheader)
answer = Python      
An Introduction



#  Python is whenever you have some type of situation where it looks like this where we have some elements that we want. 
#  But then we may have some elements that we don't care about such as what we're trying to pull out so we don't want to care about this colon 
#  we don't want to worry about getting rid of it.
#  We simply want to say that that existed in the string but we don't need it for everything we're going to do after that.
#  ability to clean it up and pull out the contents that you want and leave the things you don't want partitions are a great way of doing it
#  and other developers when they come in they look at your code or when you go back and
#  you look at your program months or years later when you see this underscore you'll understand that it means that whatever gets piped into that value is a throwaway value. 

heading = "Python: An Introduction"

header, _, subheader = heading.partition(': ')

print(header)
print(_)
print(subheader)
answer = Python:
An Introduction


#  Now once again this is simply a python convention. It is not a syntactic rule


heading = "Python: An Introduction"

first, second, third = heading.partition(': ')

print (first)
print(second)
print(third)
answer = Python:
An Introduction

#  important component to remember whenever you're working with partition is that it breaks whatever you pass
#  the colon is considered best practice



# EXAMPLE
fullname = "Erinn Ragan LeBaron"
firstname, _, lastname = fullname.partition('Ragan ')

print(firstname)

print(lastname)
answer = Erinn LeBaron