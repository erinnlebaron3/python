# will work with on daily basis
# always have to close off curly bracket {}

#  nested dictionary. 
# So once again we have teams which is a list. 
# This list contains multiple dictionaries and each one of these dictionaries contains a single key-value pair 
# where the key is the name and then inside of that contains all of these various elements.
teams = [
  {
    'astros': {
      '2B': 'Altuve',
      'SS': 'Correa',
      '3B': 'Bregman',
    }
  },
  {},
]

# Level 1
teams = [
  {
    'astros': {
      '2B': 'Altuve',
      'SS': 'Correa',
      '3B': 'Bregman',
    }
  },
  {
    'angles': {
      'OF': 'Trout',
      'DH': 'Pojols',
    }
  }
]

print(teams)
answer = [{'astros': {'2B': 'Altuve', 'SS': 'Correa', '3B': 'Bregman'}}, {'angles': {'OF': 'Trout', 'DH': 'Pojols'}}]

# level 2
# treat it like a traditional list
teams = [
  {
    'astros': {
      '2B': 'Altuve',
      'SS': 'Correa',
      '3B': 'Bregman',
    }
  },
  {
    'angles': {
      'OF': 'Trout',
      'DH': 'Pojols',
    }
  }
]

print(teams[0])
answer = {'astros': {'2B': 'Altuve', 'SS':'Correa', '3B': 'Bregman'}}

# level 3
teams = [
  {
    'astros': {
      '2B': 'Altuve',
      'SS': 'Correa',
      '3B': 'Bregman',
    }
  },
  {
    'angles': {
      'OF': 'Trout',
      'DH': 'Pojols',
    }
  }
]

print(teams[0])

angels = teams[1].get('angels', 'Team not found')
print(angels)
answer = {'OF': 'Trout', 'DH': 'Pujols'}


# treats like list on 4 levels
teams = [
  {
    'astros': {
      '2B': 'Altuve',
      'SS': 'Correa',
      '3B': 'Bregman',
    }
  },
  {
    'angels': {
      'OF': 'Trout',
      'DH': 'Pujols',
    }
  }
]

# print(teams[0])

angels = teams[1].get('angels', 'Team not found')

print(list(angels.values())[1])
answer = Pujols

