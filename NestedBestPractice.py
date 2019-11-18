# Mixed_list
users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

ids = [1, 2, 3, 4]

mixed_list = [42, 10.3, 'Altuve', users]

print(mixed_list)
answer = [42, 10.3, 'Altuve', ['Kristine', 'Tiffany', 'Jordan', 'Leann']]


# mixed_with pop
users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

ids = [1, 2, 3, 4]

mixed_list = [42, 10.3, 'Altuve', users]

print(mixed_list)

user_list = mixed_list.pop()

print(user_list)
print(mixed_list)
answer =
['Kristine', 'Tiffany', 'Jordan', 'Leann']
[42, 10.3, 'Altuve']


# nested lists
# there are some rare times where you'd want to do that. Maybe if you're keeping track of a collection that you don't actually want to iterate over you simply want to have 
# all of the elements in nested inside of one object so you can pass it around and just
#  grab the one-off Elements as you need them and you don't have to really worry about their data types because you know everything that's inside of them.
users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

ids = [1, 2, 3, 4]

mixed_list = [42, 10.3, 'Altuve', users]

print(mixed_list)

user_list = mixed_list.pop()

print(user_list)
print(mixed_list)

nested_lists = [[123], [234], [345]]