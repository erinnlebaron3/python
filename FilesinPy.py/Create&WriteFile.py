#  very common use case for working with the files system is to log values
# gonna see how we can create a file, and then add it to it.


#  create a variable here where I'm going to open up a file. 
# I'm going to show you here in the console that if I type ls, you can see we do not have a file called logger.
# function open  is going to allow us to open or create a file.
# Python works is if you call open, if it finds a file then it will open up that file.
# you can perform whatever you need to inside of it. If it does not find a file with that name, 
# then it will automatically create it. 

#  regular text file, and it takes another argument which is the way that we want to open it up. 
#  set of permissions that we want our program to follow. It takes in a string 

# write is a function inside of the file library in Python a
# to close the file off. So I'm going to say file_builder.close() and then we're going to call the close function.

# string literal interpolation I'll say {i + 1}.
# right after the curly braces pass in \n, 

# syntax where you are opening a file and then you're just calling right on it, it is not going to care whatsoever about 
# the contents of the file previously.

# This is what you would do if you want to have almost like a temp type of logger

#  truly remember from this guide is that if you use this syntax, where you're opening a file and you're simply
#  calling right you will overwrite all of the content in that file. 

file_builder = open("logger.txt", "w+")

for i in range(100):
    file_builder.write(f"I'm on line {i + 1}\n")

# file_builder.write("Hey, I'm in a file!")

file_builder.close()

