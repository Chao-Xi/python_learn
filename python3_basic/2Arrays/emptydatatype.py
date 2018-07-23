# Empty Lists
empty_list = []
print(type(empty_list))
empty_list = list()
print(type(empty_list))

# Empty Tuples
empty_tuple = ()
print(type(empty_tuple))
empty_tuple = tuple()
print(type(empty_tuple))

# Empty Sets
empty_set = {} # This isn't right! It's a dict
print(type(empty_set))
#<class 'dict'>
empty_set = set()
print(type(empty_set))
#<class 'set'>

empty_dict = dict()
print(type(empty_dict))