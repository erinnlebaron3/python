#  important topic called the dictionary view object and this is in the newer versions of python 
# dictionary view objects allow us to do is they allow us to peek in and view the values the keys and all of the different items inside of dictionaries.


# dict_keys right before the list and it wraps the entire thing in parentheses. 
# So whenever you see this that means in Python is there is some type of object that is wrapping the values that we want. 
# dictionary view object
# dict_values object does not support indexing can not treat view objects like true lists
#  was we cast this dictionary view object as a list. 

# https://docs.python.org/3.0/library/stdtypes.html#dictionary-view-objects

# Key
players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

print(players.keys())
answer = dict_keys(['ss', '2b', '3b', 'DH', 'OF'])

# Values
players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

print(players.values())
answer = dict_values(['Correa', 'Altuve', 'Bregman', 'Gattis', 'Springer'])

# Items
# gives entire key value pair as a touple
players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

print(players.items())
answer = dict_items([('ss', 'Correa'), ('2b', 'Altuve'), ('3b', 'Bregman'), ('DH', 'Gattis'), ('OF', 'Springer')])

# View/Values
# because whenever we're running processes so say that we have a query engine and we're pulling all of these players every 
# time we run one of those queries it's going to run on what is called a thread and so that thread is going to perform that action.
#  dynamic view. So what this means is that if something changes inside of the dictionary this is actually going to change for us.
# open up a query start running through our dictionary and if some other user at the exact same time change's one of the values the 
# dictionary view is going to keep it open. Because it does not close it off which means that we're going to keep all of those active changes available.
players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

print(list(players.values()))
answer = ['Correa', 'Altuve', 'Bregman', 'Gattis', 'Springer']

# pass in a one
players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

print(list(players.values())[1])
answer = Altuve

# Copy
#  issue of thread safety. So which means that if we have some other user that goes or some process that changes one of these values and we have a 
# long-running query occurring 
#  copy the list and this is a way you can make your entire process what is called thread-safe which means that we can simply make a quick copy of 
# the list then we can perform our actions.
players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

player_names = list(players.copy().values())

print(player_names)
answer = ['Correa', 'Altuve', 'Bregman', 'Gattis', 'Springer']

# Nested items
teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

team_groupings = teams.items()


print(team_groupings)
answer = 
dict_items([('astros', ['Altuve','Correa', 'Bregman']), 
('angels',['Trout', 'Pujols']), 
('yankees',['Judge', 'Stanton']),
('red sox', ['Price', 'Betts'])])

# len function
teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

team_groupings = teams.items()


print(len(team_groupings))
answer = 4

# List 
teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

team_groupings = teams.items()

"""
[
    ('astros', ['Altuve', 'Correa', 'Bregman']),
    ('angels', ['Trout', 'Pujols']),
    ('yankees', ['Judge', 'Stanton']),
    ('red sox', ['Price','Betts'])
]
"""

print(list(team_groupings))
answer = [('astros', ['Altuve', 'Correa', 'Bregman']), ('angels', ['Trout', 'Pujols']), ('yankees', ['Judge', 'Stanton']), ('red sox', ['Price','Betts'])]

# Touple
teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

team_groupings = teams.items()

"""
[
    ('astros', ['Altuve', 'Correa', 'Bregman']),
    ('angels', ['Trout', 'Pujols']),
    ('yankees', ['Judge', 'Stanton']),
    ('red sox', ['Price','Betts'])
]
"""

print(list(team_groupings)[1][1])
answer = ['Trout', 'Pujols']

# chained elements and look ups
#  pass these chained elements in and these chained look ups just right next to each other.
# have a data collection like this where you have a dictionary and you have all of these elements here and you want to grab one of the nested items this is the type of traversal you can perform
# 
teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

team_groupings = teams.items()


print(list(team_groupings)[1][1][0])
answer = Trout













