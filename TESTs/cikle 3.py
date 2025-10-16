numbers = [5, 3, -1, 10]
total = 0
for i in numbers:
    if i < 0:
        break
    total += i

print(total)