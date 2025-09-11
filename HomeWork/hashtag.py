import string

my_string = input("Enter you text: ")
modify_string = my_string[:140].title().translate(str.maketrans("", "", string.punctuation)).replace(" ", "")
print(f"#{modify_string}")
