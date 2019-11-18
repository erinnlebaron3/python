create custome Moduel and import in Repl

import math

math.sqrt(4)


# Place in file helper.py
def greeting(first, last):
  return f'Hi {first} {last}!'

# Call from repl
import helper

helper.greeting('Kristine', 'Hudgens')


Import Moduel into another file
# libs/helper.py file
def greeting(first, last):
    return f'Hi {first} {last}!'

# main.py file
import sys
sys.path.insert(0, './libs')
import helper

def render():
    print(helper.greeting('Kristine', 'Hudgens'))


render()

Import Single Function from Moduel
from math import sqrt

sqrt(4)

import sys
sys.path.insert(0, './libs')
from helper import greeting

def render():
    print(greeting('Tiffany', 'Hudgens'))


render()

Import Moduel Assign Alias
import sys
sys.path.insert(0, './libs')
import helper as h

def render():
    print(h.greeting('Tiffany', 'Hudgens'))


render()


import math as m

m.sqrt(4)


