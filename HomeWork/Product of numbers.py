your_number = input("Enter your number: ")
num = list(your_number)
gen = [int(digit) for digit in your_number]
while True:
    res = 1
    for i in gen:
        res *= i
        gen = [int(d) for d in str(res)]
    if res <= 9:
        break
print(res)