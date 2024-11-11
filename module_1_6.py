my_dict = {'Anna' : int(1990), 'Ivan' : int(1988), 'Luiza' : int(1993) }
print(my_dict)
print(my_dict['Ivan'])
print(my_dict.get('Marat'))
my_dict.update({'Olga' : 1997, 'Petr' : 1985})
print(my_dict)
a = my_dict.pop('Ivan')
print(a)
print(my_dict)

my_set = {1, 9, 7, 1, 9, 8, 5, 5, 7}
print(my_set)
my_set.add(2)
my_set.add(3)
print(my_set)
my_set.discard(5)
print(my_set)