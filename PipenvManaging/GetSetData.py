# going to be some functions that you need in order to add or to query any data from the function
# in Python this entire process is actually done for you so you do not have to create your own getter setter functions.

#  in other languages called the setter process where we were able to go into the object and then set a value
#  if you want to change it or override a value you need to create a setter function 



class Invoice:

    def __init__(self, client, total):
        self.client = client
        self.total = total

    def formatter(self):
        return f'{self.client} owes: ${self.total}'

google = Invoice('Google', 100)

print(google.client)

google.client = 'Yahoo'

print(google.client)