# the syntax for performing this action is relatively straightforward and all we have to do is update the list so if we have a 
# dictionary like we have right here with teams we can simply add a new key the same way that we would perform a query but 
# instead of performing that query on an item that exists we're going to add a new one.
# the longer the key is and the harder it is to type out or the harder it is to look up the more that you could potentially
#  be running into bugs where you think that you have the right name for the key. 
#  usually you want to keep your keys as simple and as explicit as possible.
# Anything that you'd put in a string that you can put in a key

# New key
teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
}

teams['red sox'] = ['Price', 'Bets']

print(teams)
answer = 
{'astros': ['Altuve', 'Correa', 'Bregman'],
 'angels': ['Trout', 'Pujols'], 
 'yankees': ['Judge', 'Stanton'], 
 'red sox': ['Price', 'Bets']}

