my_list = [2, 2, 2]
i = 0
len_list = len(my_list)
last_element = my_list[-1]
even = my_list[::2]
result_list = []

while i < len_list:
    if len(my_list) == 0:
        print(0)
    even_list = sum(my_list[::2])
    result_list = even_list * last_element
    len_list -=1
else:
    i += 1
print(result_list)
