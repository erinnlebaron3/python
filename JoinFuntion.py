#  how to build a practical feature that you could use in some type of application.
#  uri and url can be used in many senses interchangeably especially for what we're discussing now
#  it's very similar to your route which is just a web page.
# NEED  TO HAVE A DELIMITER AND A LIST OUTPUT MAKES A SINGLE STRING.
# STORED IN ANY VARIABLE

# JOIN
# leverage the join function and the way join works is it is actually a string-based function. 
# join each of these elements together turn them into a string. 
# so we need to tell it what we want to use as the delimiting character in this case we want a little plus sign. 
# the plus sign is called a delimiter

# https://www.google.com/search?q=python+development+tutorial

uri = 'https://www.google.com/search?q='

tags = ['python', 'development', 'tutorial']

formatted_tags = '+'.join(tags)

print(formatted_tags)
answer = python+development+tutorial


# entire uri
# uri combined with our tags which are then separated with the plus
# can use anything as the delimiter

# https://www.google.com/search?q=python+development+tutorial
 
uri = 'https://www.google.com/search?q='

tags = ['python', 'development', 'tutorial']

formatted_tags = '+'.join(tags)
query_uri = f'{uri}{formatted_tags}'
print(query_uri)
answer = https://www.google.com/search?q=python+development+tutorial
