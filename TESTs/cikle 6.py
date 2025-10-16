numbers = [5, 3, -1, 10, -3]

first_max = None
second_max = None

for i in numbers:
    if first_max is None or i > first_max:
        second_max = first_max
        first_max = i
    elif i == first_max:
        continue
    elif second_max is None or i > second_max:
        second_max = i

print(second_max)