#Reverse the loop
list1 = [1,3,6,4,6,3,6,34,4,3]

#Method 1
# list1.reverse()
# print(list1)


# Method 2
# temp = []
# count= len(list1)-1
# for i in range(count,-1,-1):
#     temp.append(list1[i])
# print(temp)


#Method 3
temp = []
count = len(list1) -1
while count >=0:
    temp.append(list1[count])
    count=count-1
print(temp)