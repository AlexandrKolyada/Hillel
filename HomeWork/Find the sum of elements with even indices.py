my_list = [0, 1, 7, 2,  4, 8]
i = 0
len_list = len(my_list)
result_list = []

while i < len_list:
    if len(my_list) == 0:
        print(0)
    even_list = sum(my_list[::2])
    result_list = even_list * my_list[-1]
    len_list -=1
else:
    i += 1
print(result_list)
