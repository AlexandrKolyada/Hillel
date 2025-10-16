numbers = [-5, -2, -10]

res = None
for i in numbers:
    if res is None or i > res:
        res = i
print(res)