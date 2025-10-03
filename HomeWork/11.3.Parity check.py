def is_even(number):

    """
    :param number: якесь число користувача
    :return: повертає True - якщо число парне, і False - якщо не парне
    """

    number = str(number)
    number_comparison = ['0', '2', '4', '6', '8']
    if number[-1] in number_comparison:
        return True
    else:
        return False
assert is_even(2494563894038 ** 2) == True, 'Test1'
assert is_even(1056897 ** 2) == False, 'Test2'
assert is_even(24945638940387 ** 3) == False, 'Test3'
print('OK')