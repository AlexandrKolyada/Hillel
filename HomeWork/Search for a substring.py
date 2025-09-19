def second_index(text, letter):

    index1 = text.find(letter)
    if index1 == -1:
        return None

    index2 = text.find(letter, index1 + 1)
    if index2 == -1:
        return None
    return index2

print(second_index("hi", "h"))