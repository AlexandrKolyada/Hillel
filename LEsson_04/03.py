my_list = [1, '66', 'er', 66, 79, 12, [2, 3, 1], 11, 1, 0, 5, 34, 're']

list_copy = my_list.copy()
list_copy_2 = my_list[:]

print(id(my_list))
print(id(list_copy))
print(id(list_copy_2))

my_list.append('TTTT')
print(my_list)
my_list.append(99)
print(my_list)

my_list.insert(2, 'AA')
print(my_list)

my_list[3] = 'BB'
print(my_list)

my_list.remove(66)
print(my_list)
my_list[6].pop()
print(my_list)
my_list[6].append(1)
print(my_list)
a = my_list[6].pop(0)
print(a)

print(5 in my_list)
print(3 in my_list)
print()