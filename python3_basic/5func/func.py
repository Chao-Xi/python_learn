def hello_func():
	return "Assassin's Creed"

print(hello_func().upper())	

def bonjour_func(greeting):
	return '{} Mademoiselle'.format(greeting)

print(bonjour_func('Bonsoir'))

print('*****************************')

def bonjour_lady(greeting, name='Louise'):
	return '{}, Mademoiselle {}'.format(greeting, name)

print(bonjour_lady('Bonsoir'))
print(bonjour_lady('Bonsoir','Chloe'))

print('*****************************')

# * and ** for unpack list or dict
def student_info(*args, **kwargs):
	print(args)
	print(kwargs)

courses = ['Math', 'Art']
info = {'name':'John', 'age':'22'}

student_info(courses, info)
print('------------------------------')
student_info(*courses, info)
print('------------------------------')
student_info(courses, *info)
print('------------------------------')
student_info(courses, **info)
print('------------------------------')
student_info(*courses, **info)