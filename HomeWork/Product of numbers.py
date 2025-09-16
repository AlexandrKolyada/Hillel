from unicodedata import digit

your_number = input("Enter your number: ")

num = list(your_number)
gen = [int(digit) for digit in your_number]
res = 1

for i in gen:
    res *= i
print(res)

for i in res:
    res *= i
print(res)