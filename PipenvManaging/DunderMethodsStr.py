#  Dunder methods are the methods that start with double underscores have some method names such as init 
# and then they end with two more double underscores (_init_)
# syntax with these double underscores in front of the name how python works with private and 
# protected methods inside of their classes


# Dunder string 

# class Invoice:
#     def __str__(self):
#         return 'This is the invoice class!'

# inv = Invoice() 
# print(str(inv))

# python looks for str to be defined and then what needs to be returned
# not most helpful way to do things

# Dunder init string method
class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total
    
     def __str__(self):
    return f"Invoice from {self.client} for {self.total}"


inv = Invoice('Google', 500)
print(str(inv))

