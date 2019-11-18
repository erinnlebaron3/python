# FOR IN  clear start and end
# WHILE LOOP  will not stop when it goes through the whole list needs to be told to stop
# be careful and infinante loop can crash computer
# have to set a setninal value to tell While loop to stop

# one of the most common ways that you're going to be using a while loop in Python. 
# It's when you don't really have a clear end of value.


#  while loop is going to be one of the best tools you can have for looping whenever you 
# want a program to go on and on and only breaks out of it when it's given that sentinel value.

nums = list(range(1,100))

# for num in nums
#     print(num)
#     answer = printed 1-99

while len(nums) > 0:
    print(nums.pop())
    answer = reverse 99-1

# printing nums from last value


# Build guessing game
# build function
# return False is the sentinal value which stops the loop
def guessing_game():
    while True: 
        print('What is your guess?')
        guess = input()

        if guess is == '42':
            print('You correctly guessed it!')
            return False
        else:
            print(f'No, {guess} is not the answer, please try again\n')

guessing_game()

answer = can continue to guess until you guess answer
What is your guess?
10 
No, 10 is not the answerm please try again
What is your guess?
55
No, 55 is not the answerm please try again
What is your guess?
45
You correctly guessed it!

# input pauses until input added then returns true or false to go again or stop
# \n = runs it like a sentance not a string
