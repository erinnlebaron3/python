#  regular expressions give you the ability to match patterns, 
#  going to group them by their file type

#  leveraged the fnmatch library in Python, and we've seen how we can pass in patterns of data
#  focused on the file name, so this is a very common tool that you'll use whenever you're 
# working with the file system in Python.


# should finde all files related to the name searches


# fnmatch library. This is giving us the ability to pass in a regular expression so that this pattern right here 
# is just saying, "If the text that we're going over, if anything in there includes a .txt,
#  then I want you to say that this condition is true. If not, just skip over it and keep on going."

# this asterisk represents is this says that it doesn't matter, we do not care what kind of content
# only care about is that the string ends in .txt here, and .rb here, and YML, and .py here.

#  combine the operating system library with the fnmatch library 
# could search through it and we could filter down a list of file names
#  ever need to perform a task such as filtering down a list, then you can also use the same library

import fnmatch
from fnmatch import fnmatchcase
import os

def list_files():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.txt'):
            print('Text files:', file, "\b")

        if fnmatch.fnmatch(file, '*.rb'):
            print('Ruby files:', file)

        if fnmatch.fnmatch(file, '*.yml'):
            print('Yaml files:', file)

        if fnmatch.fnmatch(file, '*.py'):
            print('Python files:', file)


list_files()

players = [
    "Jose Altuve 2B",
    "Carlos Correa SS",
    "Alex Bregman 3B",
    "Scooter Gennett 2B"
]

second_base_players = [player for player in players if fnmatchcase(player, "* 2B")]

print(second_base_players)