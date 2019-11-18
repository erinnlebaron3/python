sentence = 'The quick brown fox jumped over the lazy dog.'

query = sentence.find('oops')
query_two = sentence.index('oops')

print(query)
print(query_two)
answer = error

query = 'oops' in sentence

print(query)
answer = false


sentence = 'The quick brown fox jumped over the lazy dog.'

query = sentence.find('quick')
print(query)
answer = 4

sentence = 'The quick brown fox jumped over the lazy dog.'

query = sentence.index('quick')
print(query)
answer = 4

sentence = 'The quick brown fox jumped over the lazy dog.'

query = sentence.find('quick')
query_two = sentence.index('quick')

print(query)
print(query_two)
answer = 4, 4


sentence = 'The quick brown fox jumped over the lazy dog.'

query = 'fox' in sentence

print(query)
answer = True

str.find(sub[, start[, end]])
Return the lowest index in the string where substring sub is found within the slice s[start:end]. 
Optional arguments >start and end are interpreted as in slice notation. Return -1 if sub is not found

The find() method should be used only if you need to know the position of sub. To check if sub is a substring or >not, use the in operator

str.index(sub[, start[, end]])
Like find(), but raise ValueError when the substring is not found.