def is_palindrome(some_text):
    some_text = "madam"
    some_text.islower()
    return some_text == some_text[:: -1]

print(is_palindrome(some_text=""))
