#  going to allow us to do is actually merge our lists or merge multiple lists into a set of tuples.
# many of the algorithms that you build whenever you're working with machine learning algorithms are what are called matrix matrices.
# matirx set of nested colections that can be built with Zip Function
# one important component to understand whenever you're working with the zip function is the sorted order of your list is very important
#  because if it's not sorted right then your list or both of your lists are not going to merge properly and so that could be an issue and 
# it's something you have to watch out for.

# Now if you were to try to do this manually you would need to loop over one of these elements and then you'd have to add each one of the 
# array items or each one the list items, create a new tuple merge them together and that would be a little bit of a messy process.

#  zip does is it allows us to merge those automatically 
# whenever you hear that you have two list and you need to merge them together and you want to have a direct mapping. 

positions = ['2b', '3b', 'ss', 'dh']
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

scoreboard = zip(positions, players)

print(list(scoreboard))
answer = [('2b','Altuve'), ('3b','Bregman'), ('ss', 'Correa'), ('dh','Gattis')]