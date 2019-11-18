# going to use to remove elements they're not going to actually be removing elements from the original tuple
# here is we're going to be creating new tuples with elements that have been removed


# Remove from Begining
post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

# Removing elements from beginning
post = post[1:]

print(post)
answer = 
('Intro guide to Python', 'Some cool python content', 'published')




# Removing elements from end

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

# Removing elements from end
post = post[:-1]

print(post)
answer = 
('Python Basics', 'Intro guide toPython', 'Some cool python content')




# Removing specific elements
# not recomended
post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

# Removing specific element (messy/not recommended)
post = list(post)
post.remove('published')
post = tuple(post)

print(post)
answer = ('Python Basics', 'Intro guide toPython', 'Some cool python content')
