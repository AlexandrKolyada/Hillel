import keyword


my_variable = str(input('Enter your variable: '))
all_words = keyword.kwlist

if my_variable in all_words:
    print("FALSE")
elif any(symbol.isupper() for symbol in my_variable):
    print("FALSE")
elif any(symbol in r"!\"#$%&'()*+,-./:;<=>?@[\]^`{|}~" for symbol in my_variable):
    print("FALSE")
elif my_variable.count("_") > 1:
    print("FALSE")
elif my_variable[0].isdigit():
    print("FALSE")
else:
    print('TRUE')
