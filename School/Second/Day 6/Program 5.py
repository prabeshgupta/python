def check_upper(word):
    first_char = word[0]
    if first_char == first_char.upper():
        return True
    else:
        return False

print(check_upper("my Lord"))