# can treat a Touple like a list when comes to Slices
#  slices with tuples it's going to return a tuple 
# Now all of the same rules apply when it comes to working with tuple elements which means that you can pass in 3 different arguments here
# key differences when it comes to a tuple versus a list if you remember whenever you run a slice or arrange in a list it returns a list 
# of the items that you requested.
# working with slices with tuples it's going to return a tuple 

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

print(post[1::2])
answer = ('Intro guide to Python', 'published')