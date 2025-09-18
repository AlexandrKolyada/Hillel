def second_index(text, letter):

    index1 = text.find(letter)
    if index1 == -1:
        return None
    else:
        index2 = text.find(letter, index1 + 1)
    return index2