my_dict = {'Misha': 1999, 'Olga': 2006}
print(my_dict)
print(my_dict['Misha'])
my_dict['Kostya'] = 2003
print(my_dict)
my_dict.update({'Kseniya': 2000, 'Alex': 1985})
print(my_dict)
my_dict.pop('Olga')
print(my_dict.get('Olga'))
print(my_dict)
my_set = {1, 2, 3, 2, 3, 1, 'a', 'b', 'c', 'a', 'c'}
print(my_set)
print(my_set.add(4))
print(my_set.add('d'))
print(my_set)
print(my_set.discard(3))
print(my_set)
