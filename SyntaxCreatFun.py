# Functions are one of the most foundational building blocks when it comes to building programs 

# syntax that you utilize whenever you are creating variables should be the same way that you name your functions. 

# build a function
def full_name():


def full_name():
    print('hi')


full_name()
# prints out hi now


# dynamic function
def full_name(first, last):
    print(f'{first} {last}')


full_name('Erinn', 'LeBaron')
# prints Erinn LeBaron

#  now you can simply pass in values and have this full name function that does all of the work for you.
#  first true function

def full_name(first, last):
    print(f'{first} {last}')


full_name('Erinn', 'LeBaron')
full_name('Elvis', 'LeBaron')
# prints Erinn LeBaron and Elvis LeBaron

# Authinication system
# built in a full condition right into this auth function and now we can call this from anywhere else in the program
def auth(email, password):
    if email == 'kritine@hudgens.com' and password == 'secret':
        print('Authorized')
    else:
        print('Not Authorized')

auth('kristine@hudgens.com', 'secret')
# prints Authorized


#  function that takes no arguments 
def hundred():
    for num in range(1, 101):
        print(num) 

hunderd()
# prints 1-100

 def hundred():
    for num in range(1, max_range):
        print(num) 

hunderd(501)     
print()

#  basic example where we simply hardcoded the value in and then you saw how with a few very small 
# changes such as passing in an argument here we were able to make our loop dynamic.