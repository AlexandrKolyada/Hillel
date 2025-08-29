num = int(input("Enter your number: "))

print(((num % 1000) % 100) % 10)
print((num // 10) % 10)
print((num % 999) // 100)
print((num // 999) % 10)
print((num // 9999) % 10)
