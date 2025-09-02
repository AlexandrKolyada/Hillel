num = int(input("Enter your number: "))

# print(((num % 1000) % 100) % 10)
# print((num // 10) % 10)
# print((num % 1000) // 100)
# print((num // 999) % 10)
# print((num // 9999) % 10)

a = (((num % 1000) % 100) % 10) * 10000
b = ((num // 10) % 10) * 1000
c = ((num % 1000) // 100) * 100
d = ((num // 999) % 10) * 10
x = (num // 9999) % 10

print(a + b + c + d + x)
