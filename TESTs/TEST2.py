my_list = ()

some_numbers  = list(map(lambda x: x if x > 0 else abs(x),my_list))

result = max(some_numbers) - min(some_numbers)

print(result)