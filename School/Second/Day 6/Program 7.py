def check_digit(word):
    temp = False
    for char in word:
        if char.isdigit():
            temp = True
            break
    if temp:
        print("Word contains digit")
    else:
        print("Word doesn't contain digit")

check_digit("GTA Nintynine")