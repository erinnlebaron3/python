#  build what is called the and operator into our system.

# joining these conditions and whenever we're using the and condition what it's going to do is it's going to say 
# that everything on the left-hand side of the hand and the right-hand side have to be true in order for the code block to be executed.

# and operator gives u more resrtiction

username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenorth'

# and operator
#  that everything on the left-hand side of the hand and the right-hand side have to be true in order for the code block to be executed.

if username == 'jonsnow' and password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')
  answer = Access permitted

# or first then and
if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')

# or operator
# more flexibility
if username == 'jonsnow' or password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


logged_in = True
standard_user = False

if logged_in and not standard_user:
  print('You can access the admin dashboard')
else:
  print('You can only access the standard dashboard')