list_a = [1, 2, 3, 4, 5, 6, 7, [55,66]]
if len(list_a) <= 1:
    print(list_a)
else:
    list_a.insert(0, list_a.pop())
    print(list_a)
