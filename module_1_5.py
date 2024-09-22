
tuple_= [False, 1, '2']
immutable_var = tuple_
print(immutable_var)

a = 3
tuple_.append(a)
print(immutable_var)

a += 1
# immutable_var[3]=a
# print(immutable_var)
# Кортежи представляют концепцию фиксированных наборов значений, которые не должны изменяться.

list_ = [0, True, '2']
mutable_list = list_
print(mutable_list)

a = 3
list_.append(a)
print(mutable_list)

a += 1
mutable_list[3]=a
print(mutable_list)

