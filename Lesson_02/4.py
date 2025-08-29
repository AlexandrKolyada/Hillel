num = int(input("Enter your number: "))

print(num // 1000)
print((num % 1000) // 100)
print((num // 10) % 10)
print(((num % 1000) % 100) % 10)