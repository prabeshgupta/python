#Reverse a string

def reverse(word):
    print(word[::-1])

reverse("work")


name = input("Enter your name: ")

def stringRev(name):
    for i in range(len(name)-1, -1,-1):
        print(name[i], end="")

stringRev(name)