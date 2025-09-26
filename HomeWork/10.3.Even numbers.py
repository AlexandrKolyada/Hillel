from unicodedata import digit


def is_even(digit):

    """Функція is_even  повертає True якщо число парне, і False якщо число непарне."""

    return  True if digit % 2 == 0 else False

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
is_even(2)