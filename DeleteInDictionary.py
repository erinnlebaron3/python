# remove elements from a dictionary.
# he most basic way and that is simply by deleting the item with the del short for delete keyword and the syntax for this is you're going to 
# pass the name of the dictionary and then use the dictionary lookup syntax here.
# del gives you the nice benefit it's a very fast and as long as you know with 100% certainty that that key exists. It's perfectly fine to use 
# whereas pop gives you a number of extra added features.

# Delete key value pair
# works perfectly fine and for many circumstances such as when you know with 100% certainty that that key exists in the dictionary.
teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

del teams['astros']


print(teams)
answer = 
{'angels': ['Trout', 'Pujols'], 'yankees': ['Judge', 'Stanton'], 'red sox': ['Price', 'Betts']}

# Get Function
 teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

print(teams.get('mets', 'No team found by that name'))
answer = No team found by that name

# Pop
# Pop has a very cool little secret with it and that is that it returns a value. 
# It returns either the value of the Look-Up or it returns the value of this default element here(our default element is 'No team found by that name').
# similar to the get function with the key difference simply being that it also has the side effect of removing that element from the dictionary 
teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

teams.pop('astros', 'No team found by that name')


print(teams)
answer = {'angels': ['Trout', 'Pujols'], 'yankees': ['Judge', 'Stanton'], 'red sox': ['Price', 'Betts']}

# Pop with team that doesn't exist
teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

removed_team = teams.pop('rays', 'No team found by that name')


print(teams)
print(removed_team)
answer = No team found by that name
