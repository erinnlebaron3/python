# one of the most common ones that you're going to be using is the length function and it's actually called the L E N which is short for length and this is going to give you 
# the count for the full number of elements in a list and you will discover as you start building programs out that you are constantly 
# checking to see how many elements are going to be in one of these.

#  when your database query comes back it gets returned to you in a list and you can simply run the len function and get back the number of tags so I can say number of tags and that's going to be equal to len. 
# w one very important item I want you to keep a note of is there is a big difference between length and the index. So if you think that you have a length of four which we have right here and you go and you try 
# to access the last element remember the counter starts and the index starts at 0.
# what that means is you perform some type of task like looping over a list and you thought that you captured all of the values because you use something like Len and then you run into an error because you told 
# the Loop to go through the entire thing and then grab the element with an index of four. 
# But that doesn't exist here and that is called an off by one error and we need to be careful with those and so what happens if this gives us our total count.
tags = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

number_of_tags = len(tags)

print(number_of_tags)
answer = 4


# last item
tags = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

number_of_tags = len(tags)
last_item = tags[-1]

print(number_of_tags)
print(last_item)
answer = Leann

# last index
tags = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

number_of_tags = len(tags)
last_item = tags[-1]
index_of_last_item = tags.index(last_item)

print(number_of_tags)
print(last_item)
print(index_of_last_item)
answer = 3