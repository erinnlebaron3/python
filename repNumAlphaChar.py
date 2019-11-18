#   one of the most modern ways of using python in development is to build and manage API requests.
#  most API data comes in a string format. 
#  isnumeric is incredibly helpful because there are so many times where you might be getting data from API. 


#  data variable that stores 5
#  greeting variable that simply stores the word Hi.
#  you need to make sure you need to make 100 percent sure that your string does represent a integer and not just a traditional alpha numeric set of characters like we have right

api_data = '5'
greeting = 'Hi'

print(api_data.isalpha())
print(greeting.isalpha())
answer = False
True


#  so what this is doing is it's checking to see is this variable values so is this 5 a set of alphanumeric characters or not. 
#  This one is a 5 inside the string so it is not alpha and therefore it is false. 
#  Now the greeting Hi contains two characters and they are both alphanumeric so yes those are true. So this is a way of checking to see what the value is.

api_data = '5'
greeting = 'Hi'

print(api_data.isnumeric())
print(greeting.isnumeric())
answer = True
False

#  checking to see is the value numeric and in this case 5 is numeric it may be a string but inside that string it is a number 
#  and same thing with hi hi is a set of alphanumeric characters so it is not numeric and so therefore it is false.


#  isalpha letters with no space if there is a space no longer alpha
#  isnumeric is numbers
# trys to find ture or false
