#  going to have to have this concept of key-value pairs, but within that key-value structure, 
# you're going to see that many times that value is not a single value but it's actually a collection of values. 

# syntax for implementing a nested collection is exactly the same as building a standard dictionary. 
# {}

# can only have a single key value one to one type of relationship but the value can contain any other type of data structure 
# it could contain a list, or a tuple, or it could contain another dictionary, or a string, or a number, or anything like that. 

teams = {
  "astros": ["Altuve", "Correa", "Bregman"]
}

print(teams['astros'])
answer = ['Altuve', 'Correa', 'Bregman']

# this is a very important topic when it comes to understanding programming and computer science is that when you break elements
# down in their lowest form possible 

# variable is teams
# assignment is =
# dictionary is {}
# key for dictionary is "astros"
# list is players names in []

# grabbing a slice
teams = {
  "astros": ["Altuve", "Correa", "Bregman"]
}

print(teams['astros'][:2])
answer = ['Altuve', 'Correa']


# Multiple keys with values
teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
}



print(teams['yankees'])
print(teams['astros'])
print(teams['angels'])
answer =
['Judge', 'Stanton']
['Altuve', 'Correa', 'Bregman']
['Trout', 'Pujols']