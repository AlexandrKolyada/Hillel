first_number = int(input("Enter your first number: "))
next_number = int(input("Enter your next number: "))
action = str(input("Enter action: "))


if action == "+":
    print("Result:", first_number + next_number)
elif action == "-":
    print("Result:", first_number - next_number)
elif action == "*":
    print("Result:", first_number * next_number)
elif action == "/":
    if next_number == 0:
        print("You cannot divide by 0.")
    else:
     print("Result:", first_number / next_number)
else:
    print("Incorrect action")