class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total

    def formatter(self):
        return f'{self.client} owes: ${self.total}'


google = Invoice('Google', 100)
snapchat = Invoice('Snapchat', 200)

print(google.formatter())
print(snapchat.formatter())


#  constructor function.
# Dunder init __init__
# init work is that this is a function that will be automatically called whenever you instantiate the class.
# whatever got passed in for client and total and we're going to assign that to the newly created object so we're saying that we're creating two new 
# variables here that are related directly to the instance.

# self is saying dunder init
# have to use self when using init