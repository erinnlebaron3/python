# how to use touple in dictionary key
# two tags for one key
# can add multiple values in each key
# ave a dictionary, we have a tuple which is being used as a key and then the value is the list.
#  And so what this allows us to do is actually to add metadata directly into our key.
# combining all 3 popular python codes dictionary ,  touple as key, value as list
# can use all standard ways to grab items
# can use loop with this to select certain items
# weight is a value
#  tuple as a dictionary key and that may sound a little bit strange up until this 
# point of course whenever we work with dictionaries the keys were always string values.
# now we can actually add multiple values inside of each one of those keys.
# we can actually have multiple items in the key itself


priority_index = {
    (1, 'prmeier'): [1, 34, 12],
    (1, 'mvp'): [84, 22, 24],
    (2, 'standard'): [93, 81, 3],
}

print(list(priority_index.keys()))
answer = [(1, 'prmeier'), (1, 'mvp'), (2, 'standard')]
