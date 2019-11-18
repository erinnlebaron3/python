# Flask Sequel Alchemy. Now sequel alchemy is it's what's called an ORM which stands for Object Relational Mapper
# ORM does is it gives you the ability to communicate with the database and to do it without having to write pure 
# sequel code so something such as being able to run a basic query in the database.
# many times simply being able to have some helpful methods to run those queries can make your life as a developer
# much easier and it can also make your code easier to read and to maintain. And so that's what sequel alchemy allows you to do

# Flask-Marshmallow
#allows us to do is it allows us to render JSON API and to have some very helpful tools for being able to wrap the code,
#   what marshmallow allows you to do is to with a few helpful libraries and modules.


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hey Flask"


if __name__ == '__main__':
    app.run(debug=True)
    