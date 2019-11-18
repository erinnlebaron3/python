#  use split to break our string into as many different elements as we want.
#   most likely going to be using split in your day to day Python development.
#  Three parts of you count the delimiter itself but that's when you should use partition but was split.




heading = "Python: An Introduction, and Python: Advanced"

tags = 'python,coding,programing,deveopment'

list_of_tags = tags.split(',')

print(list_of_tags)
answer = ['python', 'coding', 'programing', 'deveopment']



#  Now split also can be run without any arguments at all. So if I were to take this and call tag split here and pass in no arguments.
#  partition giving different parts If we were to call partition on tags all we would end up getting is the first element
#   we would then get the comma and then we would get all the rest of these as a single string 
#  split allows us to break this entire string into as many elements as the string contains and then we can work with all of those independently.
#   split does is it converts this into a list so that each one of these is now its own element is its own standalone string
#  probably use split about 95 percent of the time partition about 5 percent of the time




heading = "Python: An Introduction, and Python: Advanced"

tags = 'python,coding,programing,deveopment'

list_of_tags = tags.split(', ')

print(list_of_tags)

list_of_tags = tags.split()

print(list_of_tags)
answer = ['python','coding','programing','deveopment']
['python,coding,programing,deveopment']