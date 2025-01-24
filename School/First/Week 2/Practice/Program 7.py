#Remove duplicates from list

list1 = [1,3,6,3,6,10,15,63,43]

#Set method
# list2 = list(set(list1))
# print(list2)

#List comprehension
list3 = []
[list3.append(x) for x in list1 if x not in list3]
print(list3)


