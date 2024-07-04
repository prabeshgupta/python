def count_vowel(word):
    temp = 0
    for char in word.lower():
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            temp +=1
    return temp

print(count_vowel("Tokyo Drift"))
