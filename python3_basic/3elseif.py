language = 'Java '

if language == 'Python':
	print('Conditional is Python')
elif language == 'Java':
	print('Conditional is Java')
else:
	print('No match')	

#and
#or
#not
user= 'Admin'
Password ='Password'
logged_in = True

if user == 'Admin' and Password == 'Password' and logged_in:
	print('welcome to the admin page')
else:
	print('stay at login page')	


a = [1, 2, 3]
b = [1, 2, 3]
print('a==b: ',a == b)
print('a is b: ',a is b)

print(id(a))
print(id(b))

c = a
print(id(a) == id(c))