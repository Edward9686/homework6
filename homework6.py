my_dict = {'Edward': 2000, 'Alisha': 2001, 'Nina': 1981}
print(my_dict)
print(my_dict.get('Nina'))
print(my_dict.get('Mom'))
my_dict.update({'Alex': 123456, 'Kris': 12312423})
print(my_dict.pop('Alex'))
print(my_dict)
print(' ')
my_set = {1, 2, 3, 4, 2, 3, 4, 1, 'String', True, 22.12}
print(set(my_set))
my_set.update({5, 6, 'Hard', 1.6})
my_set.remove('String')
print(my_set)