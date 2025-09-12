import keyword


my_variable = "some_super_pupper_value"
all_words = keyword.kwlist

for i in range(0, len(my_variable[1])):
    if my_variable[i] == my_variable[i-1]:
        break
    else:
        print("FALSE")

# if my_variable in all_words:
#     print("FALSE")
# elif any(symbol.isupper() for symbol in my_variable):
#     print("FALSE")
# elif any(symbol in r"!\"#$%&'()*+,-./:;<=>?@[\]^`{|}~" for symbol in my_variable):
#     print("FALSE")
# elif " " in my_variable:
#     print("FALSE")
# elif my_variable.count("_") > 1:
#     print("FALSE")
# elif not my_variable:
#     print("FALSE")
# elif my_variable[0].isdigit():
#     print("FALSE")
# else:
#     print('TRUE')
