import math

new_list = []
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


if len(list_b) == 0:
    print(new_list[:])
else:
    half_list = len(list_b) // 2 + 1
    firs_half_list = list_b[:half_list]
    next_half_list = list_b[half_list:]
    new_list.append(firs_half_list)
    new_list.append(next_half_list)


    print(new_list)

