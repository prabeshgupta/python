def check_palindrome(word):
    reverse = word[::-1].lower()

    if word.lower() == reverse:
        return True
    else:
        return False

print(check_palindrome("daD"))
print(check_palindrome("Cat"))