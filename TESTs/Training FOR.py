nums = int(input("Введіть число: "))

total = 1
for i in range(1, nums + 1):
    total *= i
print(total)