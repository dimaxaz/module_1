my_dict = {
    'a1':123456,
    'a2':234567,
    'a3':345678
}
print(my_dict.get('a1'))
print(my_dict['a2'])
my_dict.update({
    'a4':456789,
    'a5':567890
})
del my_dict['a3']
my_dict.pop('a2')
#print(my_dict['a2']) #этот элемент отсустует
print(my_dict.items())

set_ = {1, 2, 3, False, (4 ,5 ,6), 'a', (4, 5, 6), False}
my_set = set_
print(my_set)

my_set.update({3.14, "xaxa"})
print(my_set)

my_set.discard((4, 5, 6))
print(my_set)



