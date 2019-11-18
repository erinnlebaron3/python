# identical to when we wanted to add a new string element inside of the Touple

# a list here called tags and I'm going to add some strings inside of that list.
# to update this tuple we're going to have to perform reassignment the same way we did with the string  
post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

tags = ['python', 'coding', 'tutorial']

post += (tags,)

print(post)
answer =
('Python Basics', 'Intro guide topython', 'Some cool python content', ['python', 'coding', 'tutorial'])


# Accses Sting
post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

tags = ['python', 'coding', 'tutorial']

post += (tags,)

print(post[-1][1])
answer = coding