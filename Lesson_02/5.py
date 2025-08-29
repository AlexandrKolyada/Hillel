num = int(input("Enter your number: "))

print((((num % 1000) % 100) % 10),((num // 10) % 10),((num % 1000) // 100),((num // 999) % 10),((num // 9999) % 10))