def is_palindrome(some_text):
    some_text.lower()
    return some_text == some_text[:: -1]

print(is_palindrome(some_text="A man, a plan, a canal: Panama"))
