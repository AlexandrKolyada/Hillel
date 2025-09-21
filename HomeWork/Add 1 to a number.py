def add_one(gen_list):

    number = [9, 9, 9, 9]
    gen = [str(i) for  i in number]
    string_number = "".join(gen)
    new_list = int(string_number) + 1
    gen_list = [int(i) for i in str(new_list)]
    return (gen_list)

print(add_one(gen_list=""))