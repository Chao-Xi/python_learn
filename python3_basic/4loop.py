
AC_list = ['Origin', 'Revolution', 'Syndicate', 'Chronicles', 'Odyssey']

for ac in AC_list:
	if ac == 'Revolution':
		print('Found, it is supposed to be Unity')
		continue
	print(ac)
print('######################################')
for ac in AC_list:
	for rank in ['good', 'ok', 'bad']:
		print(ac, rank)
print('######################################')
for i in range(1, 11):
	print(i)
print('######################################')
x = 0	
while x < 10:
	print(x)
	x += 1

print('######################################')	
x = 0
while True:
	if x == 5:
		break
	print(x)
	x += 1		