#Check palindrome

word = input("Enter a word: ")
rword = word[::-1]

if word == rword:
    print("Palindrome")