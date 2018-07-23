
#Sets
AC_list = {'Origin', 'Revolution', 'Syndicate', 'Chronicles', 'Odyssey'}
print('Sets order alway change:', AC_list)
#Sets dont care about order



AC_list1 = {'Origin', 'Unity', 'Syndicate', 'Chronicles', 'Rogue'}
AC_list2 = {'Origin', 'IV Black Flag', 'Syndicate', 'Odyssey', 'Rogue'}

print('intersection same : ', AC_list1.intersection(AC_list2))

print('difference : ', AC_list1.difference(AC_list2))
print('difference : ', AC_list2.difference(AC_list1))

print(AC_list1.union(AC_list2))