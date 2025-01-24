print("List Index Finder")

userInput = int(input("Enter the number of list items: "))
userList = []

for i in range(userInput):
    val = input(f"Enter the value {i+1}: ")
    userList.append(val)

print(userList)

findIndex = input("Enter the value to get index: ")

def search(listData, indexData):
    if indexData in listData:
        return listData.index(indexData)
    else:
        pass

print(search(userList, findIndex))


name = "Prabesh Gupta"
#String index
print(name.index("h"))
#String Split
spName=name.split(" ")

for i in range(len(spName)):
    print(spName[i].upper())