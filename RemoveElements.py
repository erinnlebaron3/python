

# Remove Value
users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

print(users)

users.remove('Jordan')

print(users)
['Kristine', 'Tiffany', 'Leann']

# popping
# removes very last element
# doesnt delete returns so you can use it
# want to take off list and use in program
users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

print(users)

users.remove('Jordan')

print(users)

popped_user = users.pop ()

print(popped_user)
print(users)
answer =
['Kristine', 'Tiffany']
Leann


# pure delete
# del
users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

print(users)

users.remove('Jordan')

print(users)

popped_user = users.pop ()

print(popped_user)
print(users)

del users[0]

print(users)
answer =
['Kristine', 'Tiffany']
['Tiffany']