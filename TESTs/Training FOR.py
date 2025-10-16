n = int(input("Введіть число: "))

for i in range(1, n + 1):
    sq = i * i
    print(sq, end=" " if i < n else "")
print()