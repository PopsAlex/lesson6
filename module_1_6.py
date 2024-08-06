my_dict = {'Alex': 2004, 'Artem': 2000, 'Oleg': 1966}
print('Dict:', my_dict)
print('Existing value:', my_dict['Alex'])
print('Not existing value:', my_dict.get('Afanasiy'))
my_dict.update({'Nadya': 2011,
                'Lena': 1997})
a = my_dict.pop('Artem')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)

my_set = {1, 1, 45, 45, 45, 'dada', 'sss', 'dada'}
print('Set:', my_set)
my_set.update({200, 'draste'})
my_set.remove(45)
print('Modified set:', my_set)