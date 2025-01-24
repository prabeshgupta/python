def check_consonant(word):
    lower_word = word.lower()
    temp = False
    for char in lower_word:
        if not (char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
            temp = True
            break
    if temp:
        print(f"{word} contains consonant")
    else:
        print(f"{word} doesn't contain consonant")

check_consonant("apple")
check_consonant("oooojasjdgsdjfasdk")