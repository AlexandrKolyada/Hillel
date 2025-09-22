def add_one(some_list):


    gen = [str(i) for  i in some_list]
    string_number = "".join(gen)
    input_list = int(string_number) + 1
    output_list = [int(i) for i in str(input_list)]
    return (output_list)

print(add_one(some_list=[9, 9, 9, 8]))