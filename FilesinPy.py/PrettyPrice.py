# pretty price is I mean something that has a normalized price for say an e-commerce shop.

#  to check to see if that second argument if the extension is a decimal or if it's an integer.
# if isinstance this is the function, this is something provided by python.

# if isinstance(extension, int) then I want to perform some other task. 


def pretty_price(gross_price, extension):
    if isinstance(extension, int):
        extension = extension * 0.01
    return int(gross_price) + extension

print(pretty_price(3.50, 0.95))
print(pretty_price(3.50, 95))

# see that our API is much more flexible with our function now
#  working with a program that has decimals that are coming in for that extension you can pass in 
# the decimal if you have whole numbers coming in then you can pass in a whole number and it will work nicely.