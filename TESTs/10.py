numbers = [3, 7, 2, 9, 4]
best_val = None
best_idx = -1
for ind, val in enumerate(numbers):
    if best_val is None or val < best_val:
        best_val = val
        best_idx = ind
print(best_idx)