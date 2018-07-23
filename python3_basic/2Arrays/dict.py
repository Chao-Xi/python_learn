
AS_dict_old = {'1': "Assassin's Creed", '2':["Assassin's Creed II", 'Brotherhood', 'Revelations'], "3":"Assassin's Creed III"}
print('dict:', AS_dict_old)
print('dict:', AS_dict_old['2'])

AS_dict_old['4'] = 'IV Black Flag'
print('get:', AS_dict_old.get('3'))
print('get:', AS_dict_old.get('4'))

print('dict:', AS_dict_old)

AS_dict_old.update({'4':"Assassin's Creed IV Black Flag"})
print('dict after update:', AS_dict_old)

as4 = AS_dict_old.pop('4')
print('dict after pop:', AS_dict_old)
print(as4)

print(len(AS_dict_old)) 
print(AS_dict_old.keys())
print(AS_dict_old.values())
print(AS_dict_old.items ())

for key, value in AS_dict_old.items():
	print(key, value)