def count_consonant(word):
    temp = 0
    for char in word.lower():
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == " ":
            pass
        else: 
            temp +=1
    return temp

print(count_consonant("Tokyo Drift"))
print(count_consonant("pink pink"))
