person = {
    "name" :"Prabesh Gupta",
    "age":22
}

for key, value in person.items():
    print(key, value)


for items in range(10):
    print(items, end='') #Prevents new line change
    if items % 2 == 0:
        print("Even")

for items in range(10,1,-1):
    print(items)


for items in range(10):
    print("*")


for items in range(7):
    for elements in range(5):
        print("*",end='')
    print()

print()


for items in range(5):
    for elements in range(items, 5):
        print("*",end='')
    print()


print()

for items in range(6):
    for elements in range(6):
        if items >= elements:
            print("*", end="")
    print()


stri = "Asus"
print(stri[::-1])


for i in range(5):
    for j in range(4,0,-1):
        if j>i:
            print("0", end="")
    for k in range(5):
        if i>=k:    
            print("*", end="")
    print()


print()


for i in range(5):
    for k in range(1,5):
        if i>=k:
            print("0",end="")

    for j in range(5,0,-1):
        if j>i:
            print("*", end="")
    print()