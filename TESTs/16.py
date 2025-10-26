numbers = [5, 1, 5, 1, 5]
sum = 0
for ind, i in enumerate(numbers):
    if ind % 2 == 0:
        sum += i
print(sum)