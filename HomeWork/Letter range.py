import string

letter_range = input(str("Enter you letter range: "))
letters = string.ascii_letters
first_letter, end_letter = letter_range.split("-")
start_index = letters.index(first_letter)
end_index = letters.index(end_letter)

for char in letters[start_index:end_index+1]:
    if char == 0:
        print(char)
    else:
        print(char, end="")
print()