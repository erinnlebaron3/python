# FLOW OPERATORS
# continue
# break

# for in loop the loop has gone from the beginning of the collection all the way to the end and in many cases that is 
# exactly the behavior that you would want.

#  two different types of control flow logic operators. One is called Continue and then the other is called Break. 
# And so these are the two different flow operators that we are going to work through in this guide.


usernames = [
    'jon',
    'tyrion',
    'theon',
    'cersei',
    'sansa'
]


#  continue the program simply keeps going even though it found what it was looking for. 
# It still goes through the entire collection which is many times exactly what you want it to do.

# Continue
# goes through whole collection
for username in usernames:
    if username == 'cersei':
        print(f'Sorry, {username}, you are not allowed')
        continue
    else:
        print(f'{username} is allowed')

        answer =
        jon is allowed
        tyrion is allowed
        theon is allowed
        Sorry, cersei, you are not allowed
        sansa is allowed



# Break not only breaks you out of this conditional it looks all the way up top so it traverses down this chain 
# and it looks and it notices that it is in a for in loop and it tells Python OK we found what we want and we now 
# want to break out of the loop and python stops and that's a reason why any other elements after cersei right here 
# will not get run.

# Break
# goes until finds what you want
for username in usernames:
    if username == 'cersei':
        print(f'{username} was found at index {usernames.index(username)}')
        break
    print(username)
    answer = 
    jon 
    tyrion
    theon
    cersei was found at index 3

