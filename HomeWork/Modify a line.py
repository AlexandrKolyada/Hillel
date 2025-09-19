def correct_sentence (text):
    if text.endswith('.'):
        return text[0].upper() + text[1:]
    else:
        return (f"{text[0].upper() + text[1:]}.")
print(correct_sentence("greetings, friends"))

