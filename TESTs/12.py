numbers = [5, 5, 2, 5]

best_val = None
best_idx = -1
count = 0
for ind, val in enumerate(numbers):
    if best_val is None or val > best_val:
        best_val = val
        count = 1
    elif val == best_val:
        count +=1
print(count)