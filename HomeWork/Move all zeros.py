my_list = [0, 1, 0, 12, 3, 1, 0]
len_my_list = len(my_list)
i = 0
while i < len_my_list:
    if my_list[i] == 0:
        my_list.pop(i)
        my_list.append(0)
        len_my_list -= 1
    else:
        i += 1
print(my_list)
