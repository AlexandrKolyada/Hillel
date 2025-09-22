def find_unique_value():
    my_list = [2, 3, 3, 3, 5, 5]
    for unique_value in my_list:
        if my_list.count(unique_value) == 1:
            return (unique_value)


print(find_unique_value())
