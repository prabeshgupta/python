#Reverse a string

city="kathmandu"
temp = ""
for i in range(len(city)-1,-1,-1):
    temp =  temp+ city[i]
print(temp)