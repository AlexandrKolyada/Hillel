def is_palindrome(some_text):
    import string
    cleaned_text = some_text.lower().translate(str.maketrans("", "", string.punctuation)).replace(" ", "")
    return cleaned_text == cleaned_text[:: -1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
print(is_palindrome(some_text="A man, a plan, a canal: Panama"))
