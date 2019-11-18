# weighted lottery function is Kind of a, not a predetermined amount because the system has to be random, but it wins a majority of the time. 
# in game senario

# input is: is a dictionary. 

#  output is: should be a string that should return in this case winning, break_even, or losing, and it should do it in the right proportion.

# weights = {
#         'winning': 1,
#         'losing': 1000
#         }

# weighted_lottery(weights)
# answer =  it should return winning 1 of those times and then losing 1000 times.


# Do not limit your function to only being able to work with two sets of key-value pairs. It should work with 1, 2, or even 1000

# other_weights = {
#         'winning': 1,
#         'break_even': 2,
#         'losing': 3
#         }

# weighted_lottery(other_weights)

# There's nothing special about underscore, but what it does is it'll tell myself or anyone else who's reading the code: whenever 
# you use underscore as a variable name it usually is a sign that this is a variable that is not going to be used. 

# returns a list
import numpy as np 

def weighted_lottery(weights):
    container_list = []

    for (name, weight) in weight.items():
        #loop 1 time for win
        #loop 1000 for lose
        for _ in range(weight):
            container_list.append(name)

    return container_list
other_weights = {
        'winning': 1,
        'break_even': 2,
        'losing': 3
    }

print(weighted_lottery(other_weights))
answer = win 1, break_even 2, 3 lose


# Grab random tag
import numpy as np 

def weighted_lottery(weights):
    container_list = []

    for (name, weight) in weight.items():
        #loop 1 time for win
        #loop 1000 for lose
        for _ in range(weight):
            container_list.append(name)

    return np.random.choice(container_list) 
other_weights = {
        'winning': 1,
        'break_even': 2,
        'losing': 3
    }

print(weighted_lottery(other_weights))
answer = 
win
lose
break_even
lose
break_even
lose

# look into numpy np