def first_consonant(word):
    for char in word:
        if not(char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char == "I" or char == "O" or char == "U"):
            break
    return char

print(first_consonant("rabesh"))