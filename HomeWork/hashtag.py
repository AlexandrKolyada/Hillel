import string

my_string = input("Enter you text: ")
modify_string = my_string.title().translate(str.maketrans("", "", string.punctuation)).replace(" ", "")[:140]
print(f"#{modify_string}")
