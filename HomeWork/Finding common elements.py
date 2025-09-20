def common_elements(plural):

    my_list = list(range(0, 100))
    my_list1 =[]
    my_list2 =[]
    # my_set1 = set(my_list1)
    # my_set2 = set(my_list2)
    # plural = my_set1.union(my_set2)

    for i in my_list:
        if i % 3 == 0:
            my_list1.append(i)

        if i % 5 == 0:
            my_list2.append(i)

    my_set1 = set(my_list1)
    my_set2 = set(my_list2)
    plural = my_set1.intersection(my_set2)

    return (plural)

print(common_elements(plural=""))
