itemCount = input("How many items do you want in the list? ")
data = []
for i in range(int(itemCount)):
    j = input(f"Enter the item {i+1}: ")
    data.append(int(j))
print(data)

temp = 0
for k in data:
    temp = k + temp;

print(temp)