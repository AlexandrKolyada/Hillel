num = int(input("Enter your number: "))


print(str((((num % 1000) % 100) % 10))+str(((num // 10) % 10))+str(((num % 1000) // 100))+str(((num // 999) % 10))+str(((num // 9999) % 10)))