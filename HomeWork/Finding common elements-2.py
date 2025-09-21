def common_elements(my_set):

    my_list = [i for i in range(0, 100) if i % 3 == 0 and i % 5 ==0]
    my_set = set(my_list)
    return (my_set)

print(common_elements(my_set=""))