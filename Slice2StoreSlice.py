# here are times where you may not know or you may not want to hard code in this slice range. 
# And so in cases like that Python actually has a special class called slice which we can call and store whatever these ranges we want 
# biggest reasons why you'd ever use this slice class over using just this explicit version slice(1, 4, 2) is whenever you want to define 
# your ranges and your steps and those kinds of elements and you want to store them in a variable and then simply call them later on and or 
# also another opportunity where this would be a very good fit is if you're maybe calling this on different datasets.

# SLICE

tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]

# print(tags[:2])

slice_obj = slice(2)

print(tags[slice_obj])
answer = ['python', 'development']

# similar when working with explicet slice
# working with an explicit slice and when we passed in a range the only difference is that

print(tags[:2])
# the key differences here is we can call store this method inside of another object inside
# of a variable and then we can call that anywhere in the program. 
# so this is a very nice way of being able to store your slice so that you can reuse it on any other kinds of lists. 
print(tags[slice_obj])

# with slice, you can see there are three potential arguments inside of this object and the first one is our start point. So we're going to have a start. 
# going to have an end and then we're going to have a step which if you remember exactly with what we had with ranges and with these explicit type of 
# slices we could pass in say [2:4:2]. And then this is going to bring us every other element because the last 2 is our step. This first 2 is our start
#  and this 4 is our stop or this is our endpoint.
tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]

# print(tags[2:4:2])

slice_obj = slice(2)

print(slice_obj)
print(tags[slice_obj])
answer = slice(None, 2, None)['python', 'development']

tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]

print(tags[1:4:2])

slice_obj = slice(1, 4, 2)



print(tags[slice_obj])
answer = ['development', 'code']['development', 'code']


# working on a machine learning algorithm and you want to know in some other part of the program where the range started where it stopped and what 
# the step interval was.

tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]

print(tags[1:4:2])

slice_obj = slice(1, 4, 2)

print(slice_obj.start)
print(slice_obj.stop)
print(slice_obj.step)
print(tags[slice_obj])
answer =
['development', 'code']
14
2
['development', 'code']







tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]

print(tags[1:4:2])

slice_obj = slice(1, 4, 2)

print(slice_obj.start)
print(slice_obj.stop)
print(slice_obj.step)

print(tags[slice_obj])
answer =
['development', 'code']
14
2
['development', 'code']