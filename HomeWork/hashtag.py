symbol_for_delete = ".,/?!-/ "
table = str.maketrans('', '', symbol_for_delete)
my_string = input("Enter you text: ")
modify_string = my_string[0:140].title().translate(table)
format_list = "#{}"
print(f"#{modify_string}")
