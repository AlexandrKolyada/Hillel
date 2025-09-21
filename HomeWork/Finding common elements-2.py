def common_elements(set):

    my_list = [i for i in range(0, 100) if i % 3 == 0 and i % 5 ==0]
    set = set(my_list)
    return (set)

print(common_elements(set))