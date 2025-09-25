def popular_words(text, words):

    text = text.lower().split()
    result = {word: text.count(word) for word in words}
    return result

print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))


