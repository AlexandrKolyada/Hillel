numbers = [3, 7, 2, 9, 4]
best_val = None
best_idx = -1
for idx, i in enumerate(numbers):
    if best_val is None or i > best_val:
        best_val = i
        best_idx = idx
print(best_idx)
print(best_val)