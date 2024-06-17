#Append List

myList = ["Nike", "Puma","Adidas"]
item = input("How many item do you want to append item? ")
for i in range(int(item)):
    data = input(f"Enter item {i+1}: ")
    myList.append(data)

print(myList)