# going to build out a HTML class so you can think of this as a tool that can render HTML on the page
# build multiple subclasses that allow you to render custom versions of that HTML.

# going to be a common convention that you see whenever you're using very complex system
#  going to create what is called a abstract class and then this abstract class has the sole purpose of holding and 
# storing shared behavior and then only the inherited classes so only the child classes are going to be the ones 
# that ever called this class.


#  polymorphism does is it's when you have a child class that inherits these methods from a parent class and then it overrides the behavior.

# right here we have access to content we have access to content in all child classes but in this case, 
# we decided to wrap that content in an H1 tag. Here we decided to wrap it in a div tag and so we have different 
# behavior with these child classes and because of it we have some pretty powerful behavior in a very short amount of code. 
# You can see we only have a few different classes here but we were actually able to create our own custom HTML generator
#  just by doing that and we leverage Object-oriented programming we leveraged inheritance and polymorphism.

class Html:
    def __init__(self, content):
        self.content = content

    def render(self):
        raise NotImplementedError("Subclass must implement render method")


class Heading(Html):
    def render(self):
        return f'<h1>{self.content}</h1>'


class Div(Html):
    def render(self):
        return f'<div>{self.content}</div>'

tags = [
    Div('Some content'), 
    Heading('My Amazing Heading'), 
    Div('Another Div')
    ]

for tag in tags:
    print(tag.render())


# do not have any reference at all to the HTML parent class we're only calling those child classes

#  polymorphism it's a very big word that represents something that's actually kind of straightforward which is 
# and it's all in the name poly means many and morphism comes from the word meaning to change. 
# Which means it can have many changes or one item can have many forms.

