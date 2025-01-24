#Check palindrome

def palindrome(word):
    temp = ""
    count = len(word)-1
    while count > -1:
        temp += word[count]
        count-=1
    if temp == word:
        return "Palindrome"
    else:
        return "Not Palindrome"

print(palindrome("DaD"))


