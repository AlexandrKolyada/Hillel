def first_word(text) -> str:

    """
    Пошук першого слова
    """

    import  string
    new_punctuation = string.punctuation.replace("'","")
    mapping = str.maketrans({ch: " " for ch in new_punctuation})
    cleaned_text = text.translate(mapping).split()
    print(cleaned_text[0])
    return cleaned_text[0]

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')