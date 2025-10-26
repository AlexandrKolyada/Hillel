numbers = [3, 1, 2, 5, 4, 6]

best_val = None

res = 0
for ind, val in enumerate(numbers):
    if best_val is None or val > best_val:
        best_val = val
        res += 1

print(res)
