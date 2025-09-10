import random

full_list = list(range(1, 101))
min_len = 3
max_len = 10
max_start_index = len(full_list) - min_len

if max_start_index < 0:
    print('FALSE')
else:
    start_index = random.randint(0, max_start_index)
    random_len = random.randint(min_len, max_len)
    end_index = min(start_index + random_len, len(full_list))
    random_slice = full_list[start_index:end_index]
    new_list2 = [random_slice[0], random_slice[2], random_slice[-2]]
    print(random_slice)
    print(new_list2)
