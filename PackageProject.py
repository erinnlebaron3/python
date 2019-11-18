# will help you on the entire course capstone project 
# Technically you have learned everything that you need to know in order to build out this project. 
# helps to be familiar with some of the libraries that can make your life a little bit easier and 
# make your code more straightforward to implement

#  web scraper 
#  what it is going to do is go out to a Web site and it is going to go and extract components from 
# that site so that you can use them, you can bring them into your own program.
# so you need to bypass the entire concept of an API 

# http://www.dailysmarty.com/topics/python

#  to be able to build is a program that comes to this url and then scrapes the code from this.
#  leverage the requests library you're going to be able to call the url directly and then get access to all content. 

'http://www.dailysmarty.com/posts/how-to-implement-fizzbuzz-in-python'
"How to Implement FizzBuzz in Python"

"""
Libraries:

-requests
-inflection
-beautifulsoup

pip install requests
pip install inflection
pip install beautifulsoup4
"""


# go to pure web page daily smarty
# program goes to url and scrapes the code from this
# leverage requests to get url directly
# select all links that go to posts
# copy link address
# right-click on this and click copy link address right here let me open up in a text editor say vim project.py 
# and so I'm going to paste in right here what that url looks, and so you are going to get access to this.
# only pull out the links that are related to posts. 
# only the ones that go right to a post
# take link and convert link into page title
# build function takes title text in url and make a string with caps and spaces
# final output should look like different lists of titles with "" around with caps and spacing

import requests
from bs4 import BeautifulSoup
from inflection import titleize

def title_generator(links):
    titles = []

    def post_formatter(url):
        if 'posts' in url:
            url = url.split('/')[-1]
            url = url.replace('-', ' ')
            url = titleize(url)
            titles.append(url)


    for link in links:
        post_formatter(link["href"])


    return titles

r = requests.get('http://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('a')
titles = title_generator(links)


for title in titles:
    print(title)