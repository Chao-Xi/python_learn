''
AC_list = ['Origin', 'Revolution', 'Syndicate', 'Chronicles', 'Odyssey']
AC_list1 = ['Origin', 'Revolution', 'Syndicate', 'Chronicles', 'Odyssey']
AC_list2 = ['Origin', 'Revolution', 'Syndicate', 'Chronicles', 'Odyssey']

print (AC_list)
print ('Lenth of assassin creed list:', len(AC_list))

print (AC_list[4])
print (AC_list[-1])
print (AC_list[2:])

# AC_list.append('Black flag')
# print (AC_list)
# ['Origin', 'Revolution', 'Syndicate', 'Chronicles', 'Odyssey', 'Black flag']

# AC_list.insert(0, 'IV Black Flag')
# print(AC_list)
# ['IV Black Flag', 'Origin', 'Revolution', 'Syndicate', 'Chronicles', 'Odyssey']

AC_list_old = ['IV Black Flag', 'Rogue']

AC_list.extend(AC_list_old)
print('extend:', AC_list)

AC_list1.append(AC_list_old)
print('append:', AC_list1)

AC_list2.insert(0, AC_list_old)
print('insert:', AC_list2)

AC_list1.remove('Odyssey')
print('remove:', AC_list1)

AC_list2_popped = AC_list2.pop()
print('pop:', AC_list2)
print('popped:', AC_list2_popped)

AC_list.reverse()
print('reverse:', AC_list)

num_list = [0, 32, 98, 27, 19, 20]
num_list1 = [0, 32, 98, 27, 19, 20]
num_list2 = [0, 32, 98, 27, 19, 20]

num_list.sort()
print('sort method:', num_list)

num_list1.sort(reverse=True)
print('reverse sort:', num_list1 )

num_list3 = sorted (num_list2 )
print('sort function:', num_list2 )
print('sort function:', num_list3 )

print('index:', AC_list )
print('index:', AC_list.index('Syndicate'))

print('Brotherhood in the list:', 'Brotherhood' in AC_list)
print('Chronicles in the list:', 'Chronicles' in AC_list)

for ac in AC_list:
	print('for loop:', ac)

for index, ac in enumerate(AC_list):
	print('index', index, 'in loop is', ac)

print('###########################')

for index, ac in enumerate(AC_list, start=1):
	print('index', index, 'in loop is', ac)


AC_list_Arrow = ' ->  '.join(AC_list)
print('join:', AC_list_Arrow )
print(type(AC_list_Arrow))
new_AC_List = AC_list_Arrow.split(' -> ')
print('split:' ,new_AC_List )
