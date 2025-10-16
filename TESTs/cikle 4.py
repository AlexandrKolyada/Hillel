numbers = [5, 3, -1, 10, -3]

res = -1
for index, val in enumerate(numbers):
    if val < 0:
        res = index
        break
print(res)