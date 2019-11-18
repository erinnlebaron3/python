#  going to walk through and we're going to be using what is called the in operator
#  condition it is going to check to see if one element is inside of or contained in another element. 


sentence = 'The quick brown fox jumped over the lazy Dog'
word = 'quick'

if word in sentence:
  print('The word was found in the sentence')
else:
  print('The word was not in the sentence')
answer = The word was found in the sentence


# the word dog but notice even though we have a dog in this sentence our searching or our in operator is not case insensitive 
# which means that if we look for dog spelled this way with the lower case d. It is not going to find this Dog with an uppercase D.
sentence = 'The quick brown fox jumped over the lazy Dog'
word = 'dog'

if word in sentence:
  print('The word was found in the sentence')
else:
  print('The word was not in the sentence')
  answer = The word was not found

#   Fix lower case letters
sentence = 'The quick brown fox jumped over the lazy Dog'
word = 'dog'

if word.lower() in sentence.lower():
  print('The word was found in the sentence')
else:
  print('The word was not in the sentence')
  answer = The word was found in the sentence


# Works on collections of data
nums = [1, 2, 3, 4]

if 3 in nums:
  print('The number was found')
else:
  print('The number was not found')

  answer = The number was found