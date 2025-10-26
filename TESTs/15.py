numbers = [1, 2, 2, 3]

count = 0
for i in range(len(numbers)-1):
    if numbers[i] == numbers[i+1]:
        count += 1

print(count)