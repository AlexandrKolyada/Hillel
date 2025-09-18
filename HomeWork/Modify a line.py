def correct_sentence (text):

    if text.endswith('.'):
        return str(text).capitalize()
    else:
        return (f"{text}.").capitalize()

