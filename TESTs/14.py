numbers = [3, 1, 2, 0, 0, -1]
best_val = None
count = 0
for ind, val in enumerate(numbers):
    if best_val is None or val < best_val:
        best_val = val
        count += 1

print(count)