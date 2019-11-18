class Invoice:

    def __init__(self, client, total):
        self._client = client
        self._total = total

    def formatter(self):
        return f'{self._client} owes: ${self._total}'


    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, client):
        self._client = client

    @property
    def total(self):
        return self._total



google = Invoice('Google', 100)

print(google.client)

google.client = 'Yahoo'

print(google.client)

# property decorator
# going to be able to fix the whole issue where everyone has access to all of the data.
#  may have a situation where we want to pick and choose and say okay some of the data should be able to be accessible 

#  any time that you're dealing with data that you want to have either private or protected.
#  want to add underscores in front of it.
# want something protected and what that means is that anything in the class you want to have
#  access to and any child classes

# nothing special about the underscores before the variable name it is a clue to you and developers saying this data should be protected
# for private attribute is 2 underscores before the variable name 

# @ symbol followed by the name property.
#  going to do this is called a decorator and what it essentially does is it decorates it wraps around the property 
# that we're wanting to work with.
# now what we've done is we have given a clear distinction with how we've written our code on how you should treat this invoice.

#  see that there is a property decorator here, tells me that I will most likely want to access what is here at some point

