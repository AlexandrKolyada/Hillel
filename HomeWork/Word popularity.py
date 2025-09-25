def popular_words(text, words):

    text = text.lower().split()
    result = {words: text.count(words) for words in words}
    return result

print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))


