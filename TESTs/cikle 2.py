m = int(input("Введіть число: "))

for i in range(1, m + 1):
    sq = i ** 2
    if sq > m:
        break
    print(sq, end=" " if (i+1)** 2 <= m else "")
print()