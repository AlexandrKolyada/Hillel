numbers = [5, 3, -1, 10, -3]

res = -1
for index, vol in enumerate(numbers):
    if vol < 0:
        res = index

print(res)