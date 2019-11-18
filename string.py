sentence = 'The quick brown fox jumped over the lazy dog'

sentence_two = 'That is my dog\'s bowl'

sentence_three = "That is my dog's bowl"

sentence_four = "Tiffany said, \"That is my dog's bowl\""

#  SINGLE QUOTES
    # can use in Python

# DOUBLE QUOTES
    # used in Ruby
    # can be used in Python
    # when you have an ' (dont's) you need to use double quotes or \'


# FUNCTIONS WITH STRINGS

# sentence = 'The quick brown fox jumped'
# sentence -> variable
# 'The quick brown fox jumped' -> string
# = -> assignment

sentence = 'The quick brown fox jumped'
sentence_two = sentence.upper()

print(sentence)
print(sentence_two)
answer = The quick brown fox jumped and THE QUICK BROWN FOX JUMPED

sentence = 'the quick brown fox jumped'.capitalize()
print(sentence)
answer = The quick brown fox jumped

sentence = 'the quick brown fox jumped'.title()
print(sentence)
answer = The Quick Brown Fox Jumped

sentence = 'the Quick Brown fOx jumped'
print(sentence.lower())
answer = the quick brown fox jumped

str.upper()
Return a copy of the string with all the cased characters [4] converted to uppercase. Note that s.upper().isupper() might be False > if s contains uncased characters or if the Unicode category of the resulting character(s) is not “Lu” (Letter, uppercase), but e.g. > “Lt” (Letter, titlecase).

str.capitalize()
Return a copy of the string with its first character capitalized and the rest lowercased.

str.lower()
Return a copy of the string with all the cased characters [4] converted to lowercase.

can also wait to call in print()

# ACCESS VALUES IN STRINGS AND RANGES

# The quick brown fox jumped
# T => 0
# h => 1
# e => 2
# ' ' => 3

starter_sentence = 'The quick brown fox jumped'
print(starter_sentence[0])
answer = T
print(starter_sentence[12])
answer = o

# Ranges a way of accesing more than one value

starter_sentence = 'The quick brown fox jumped'
first = starter_sentence[0]
second = starter_sentence[1]
third = starter_sentence[2]
new_sentence = first + second +third
print(new_sentence)
answer = The

starter_sentence = 'The quick brown fox jumped'
first = starter_sentence[0:3]
new_sentence = first_word
print(new_sentence)
answer = Th

# you can think of this being almost like the end of a bookend or something like that on a shelf where this two is not going to be captured 
# inside the range. It's going to stop right before it gets there. So inside of our sentence, it's 0 1 and then 2. 
# But because we said this range needs to end at two. It means it's going to end right before it gets to that to index 

starter_sentence = 'The quick brown fox jumped'
new_sentence = 'Thy' + starter_sentence[3:]
print(new_sentence)
answer = Thy quick brown fox jumped
# [3:] three colon empty means go from third spot to end of sentence

# Immutability 
        # is a very very long word that simply means that you can't change an element. 
        # So for a string in Python strings are what are called immutable which means that we can't actually alter this string once it has been created.
        # we can create a new variable and alter them that way by performing some formatting and some different tasks like that



