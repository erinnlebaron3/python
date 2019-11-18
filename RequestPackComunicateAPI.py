#  API before it stands for application programming interface
# language for our application to use and to communicate with another third-party application 
# the API going to look like.
# is called json which stands for a javascript object notation.
# json is, is a set of key-value pairs. 

# Source Code
import requests
import pprint

r = requests.get('https://api.dailysmarty.com/posts')
r.json()
pprint.pprint(r.json()['posts'][0])
pprint.pprint(r.json()['posts'][0]['url_for_post'])