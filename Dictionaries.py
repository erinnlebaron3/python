# dictionary is what's called a key-value data store
# So what that means is that we can store this in a 
# variable we can create not just elements the way that we did with lists but we can create a key with a corresponding value. 

# {} syntax for calling in dictionary
# the syntax is to start with a string
# ss stands for shortstop 
# from there supply a colon and then a value
# creates a key-value pair

players = {
  "ss": "Correa",
  "2b": "Altuve",
  "3b": "Bregman",
  "dh": "Gattis",
  "of": "springer",
}

print(players)
answer = {'ss': 'Correa', '2b': 'Altuve', '3b': 'Bregman', 'dh': 'Gattis', 'of': 'springer'}

#  different type of structure than a list.
# both have elements inside of them but now instead of working with an index the way we do with the list 
# is how you can query an element by having an index value with a dictionary. 
# with the dictionary we use a key-value structure which means we pass in the key in order to access the value.
# When talking about dictionaries in Python we have some way of referencing this so we actually are working with 
# words instead of indices and so that is a very very important distinction between the two.

# QUERY VALUES
# pass in the string value of that key 

players = {
  "ss": "Correa",
  "2b": "Altuve",
  "3b": "Bregman",
  "DH": "Gattis",
  "OF": "springer",
}

second_base = players['2b']

print(second_base)
answer = Altuve

# make sure that whatever string bass key that you're looking up is an identical match. 
# And whenever you're building this into a program you are most likely going to be passing in these kinds of direct match kind of values. 

players = {
  "ss": "Correa",
  "2b": "Altuve",
  "3b": "Bregman",
  "DH": "Gattis",
  "OF": "springer",
}

second_base = players['2b']
designated_hitter = players['DH']

print(designated_hitter)
answer = Gattis