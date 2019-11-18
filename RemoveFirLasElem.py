# the cleanest syntaxes for it because of destructuring and because you're able to glob up these elements it's a really nice and easy way to read 
# the way that this works. And also within one line, you can see how quickly you're able to grab those elements and then you can use that content 
# however you want.



"""
remove_first_and_last(list_to_clean)

html = ['<h1>', 'My content', </h1>]

remove_first_and_last(html)
=> ['some content']

html_2 = ['<h1>', 'Some content', 'more', '</h1>']

remove_first_and_last(html_2)
=> ['some content', 'more']
"""

def remove_first_and_last(list_to_clean):
    _, *content, _ = list_to_clean
    return content

html_2 = ['<h1>', 'Some content', 'more', '</h1>']

print(remove_first_and_last(html_2))
# answer = ['Some content', 'more']


