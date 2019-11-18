# syntax for doing is by performing something like this where I say teams and then put in the name of the key and then that is going to perform the query.


# want to have a featured team so I can say featured team store this in a variable. 
teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox" : ['Price', 'Bets']
}

featured_team = teams['astros']

print(featured_team)
answer = ['Altuve', 'Correa', 'Bregman']


# fallback -  that's what we can do with the get function inside of Python dictionaries
# make sure that you are catching any kind of scenarios that have a situation like this where we're looking up a key that may or may not exist
#  and you want to have some type of fallback and so this is going to give you instant feedback to let you know that what you tried to look up 
# doesn't actually exist inside of the team's dictionary.

# GET
# get takes two arguments
# The first is a key we're looking for. 
# gives us the abitlity to have multiple checks when using look ups in Python automaticaly
teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox" : ['Price', 'Bets']
}

featured_team = teams.get('mets', 'No featured team')

print(featured_team)
answer = No featured team

