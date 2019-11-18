    #  STRING INTERPOLATION

# String interpellation at a very high level simply allows us to process python code inside of strings shown by F

name = 'Kristine'
greeting = f'Hi {name}'
print(greeting)
answer = Hi Kristine

name = 'Kristine'
greeting = f'This is my {{bracket}} blog post'
print(greeting)
answer = This is my {bracket} blog post


name = 'Kristine'
product = 'Python elearning course'

email_content = f"""
Hi {name}

Thank you for purchasing {product}

Regards,

Sales Team
"""

print(email_content)
answer = Hi Kristine 
Thank you for purchasing Python elearning course
Regards,
Sales Team


# FORMAT METHOD

name = 'Kristine'
age = 12
product = 'Python eLearning course'

greeting - "Hi {0}, you are listed as {1} years old and you have purchased: {2}...".format(name, age, product)
print(greeting)
answer = 
product purchase
hi Kristine, you are listed as 12 years old and youu have purchased: Python elearning course... 


# str.format(*args, **kwargs)
# Perform a string formatting operation. The string on which this method is called can contain literal text or >replacement fields delimited by braces {}.
# Each replacement field contains either the numeric index of a positional >argument,
# or the name of a keyword argument. Returns a copy of the string where each replacement field is >replaced with the string value of the corresponding argument.


name = 'Kristine'
age = 12
product = 'Python eLearning course'
from_account = 'Jordan'

greeting = f"Product purchase: {product} - Hi {name}, you are listed as {age} years old. - {from_account}"

print(greeting)
answer =
hi Kristine, you are listed as 12 years old and youu have purchased: Python elearning course...- Jordan

