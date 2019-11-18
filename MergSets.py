# these functions wont be named
# how one set interacts with another
# pipe character | merges sets togeather

tags_one = {
    'python',
    'coding',
    'tutorials',
    'coding'
}

tags_two = {
    'ruby',
    'coding',
    'tutorials',
    'development'
}

# to create a new variable here called merged tags and I'm going to assign this to tags_one 
# and then I'm going to use this pipe character and then tags_two.

# Merged tags
# all of the elements
merged_tags = tags_one | tags_two
print(merged_tags)
answer = 'ruby', 'coding', 'tutorials', 'python', 'development'

# tags in tags_one but not in tags_two
# master tag/set for elements in certain tags
exclusive_to_tag_one = tags_one - tags_two
print(exclusive_to_tag_one)
answer = {'python'}

exclusive_to_tag_two = tags_two- tags_one
print(exclusive_to_tag_two)
answer = {'ruby', 'development'}

# tags found in both tags_one and tags_two
# for only shared items
universal_tags = tags_one + tags_two
print(universal_tags)
answer = {'coding', 'tutorials'}