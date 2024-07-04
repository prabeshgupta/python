def check_vowel(word):
    lower_word = word.lower()
    temp = False
    for char in lower_word:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            temp = True
            break
    if temp:
        print(f"{word} contains vowel")
    else:
        print(f"{word} doesn't contain vowel")

check_vowel("ppllk")
check_vowel("Fast and Furious")