numbers = [1, 2, 2, 3]

total = 0
for ind, i in enumerate(numbers):
    if numbers[i] < numbers[i+1]:
        total += 1
print(total)