# 2 types of loops in python
# FOR IN loops
# WHILE loops

# differences are because both of them can be used to iterate over collections over a range of numbers over lists anything like that.

#  going to be using a for in loop most likely about 95 percent of the time

# FOR IN loop can only go through as many times as there are items : specificly for number of items
# WHILE continue as many times as you want it to go : while this is true or whatever do this

# FOR IN LOOP
# how to iterate over a list
# a touple will work the same way
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

for player in players:
    print(player)
    answer = 
    Altuve
    Bregman
    Correa
    Gattis

  
# WORK WITH DITIONARY'S
# add keys and values
players = {
    '2b': 'Altuve',
    '3b': 'Bregman',
    'ss': 'Correa',
    'dh': 'Gattis'
}

for position, player in players.items():
    print('Position', position)
    print('Player Name', position)
    answer = 
    Position 2b
    Player Name Altuve 
    Position 3b
    Player Name Bregman
    Position ss 
    Player Name Correa
    Position dh
    Player Name Gattis

# must indent print
# when there is a colon after a function need to have an indentation
#  whenever you see this colon in Python you will most likely need to have the next set of code so anything inside of this is called a code block.