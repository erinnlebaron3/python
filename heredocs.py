# use """"   """" to do multipel line

# Heredoc

content = """

j;efjcoivj;oajvug;oajsmdovjadvjddajfvfdkvf'a.

oadkijfo;ajfdoijaoijoiaj.

fajnfajf;oja;t.

"""
print(content)
answer prints whats in the """

# strip

    #with the strip function is at the very end of the string I can say .strip and because this is a function call. Remember we always put parens at the end of a function call. 

# Heredoc

content = """
Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
""".strip()

print(content)

str.strip([chars])
Return a copy of the string with the leading and trailing characters removed. 
The chars argument is a string > specifying > the set of characters to be removed. 
If omitted or None, the chars argument defaults to removing >whitespace. 
The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped

# RAW MULTILINE STRING

repr = representation

 is it's actually giving us the way the content and the string and it gives it to us in the same way that the computer is processing. 
 So repr is short for representation. So what it means is it's giving us more of the computer-based representation that's what the computer uses to decide when to put a 
 new line character in and different things like that. So right here we can see this backslash n is a new line character


content = """
Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
"""

print(repr(content))
answer =  gives you what the computer is processing

# LONG STRING

long_string = '\nNullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.\n\nVestibulum id 
ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. 
Cras justo odio, dapibus ac facilisis in.\n\nInteger posuere erat a ante venenatis dapibus posuere velit aliquet.\n'

print(long_string)
answer = 
Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.


repr(object)
Return a string containing a printable representation of an object. For many types, 
this ?>function makes an attempt to return a string that would yield an object with the same value >when passed to eval(), 
otherwise the representation is a string enclosed in angle brackets that >contains the name of the type of the object together with additional information often 
>including the name and address of the object. A class can control what this function returns >for its instances by defining a repr() method.