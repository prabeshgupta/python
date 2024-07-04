def first_vowel(word):
    for char in word:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
            break
    return char

print(first_vowel("BINOD"))

            