# f = format to read as a variable with curly brackets
# f = lets you use multiple things
# use string interpolater for this
# where it says blank replace with blank

"""
name_maker(title, heading_type)
name_maker('Welcome', '1')
<h1>Welcome</h1>
"""

def name_maker(title, heading_type):
    return f'<h{heading_type}>{title}</h{heading_type}>'


print(name_maker('Welcome', '1'))






 








# def heading_generator(title, heading_type):
#   return f'<h{heading_type}>{title}</h{heading_type}>'
  

# print(heading_generator('Greetings!', '1'))
# print(heading_generator('I am in a title', '3'))