#Alternate print

list1=[10,20,30,40]
list2=[100,200,300,400]

for i,j in zip(list1, reversed(list2)):
    print(i,j)

# for i in range(len(list1)):
#     print(list1[i], list2[len(list2)-1-i])