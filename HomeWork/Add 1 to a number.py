def add_one(some_list):


    gen = [str(i) for  i in some_list]
    string_number = "".join(gen)
    new_list = int(string_number) + 1
    some_list = [int(i) for i in str(new_list)]
    return (some_list)

print(add_one(some_list=[9, 9, 9]))