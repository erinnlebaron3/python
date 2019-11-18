# use with FOR IN LOOP
# how to create and combine lists

#  how you can create and combine multiple lists together using the for in loop in Python.

# with a for in loop you can simply iterate over one list and then add each one of those elements into the new one.

#  with a four in loop what we're doing is we are iterating over a preexisting list and we're not even treating these 
# elements as anything except normal strings.

legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

# raw_db = [legacy_customers, new_customers]
# print(raw_db)
# answer = 
# ['Alice', 'Bob'],['Tiffany', 'Kristine']   got this
# ['Alice', 'Bob', 'Tiffany', 'Kristine']   looking for this


for legacy_customer in legacy_customers:
    new_customers.append(legacy_customer)

print(new_customers)
answer = ['Tiffany', 'Kristine', 'Alice', 'Bob']