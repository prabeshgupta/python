#Add lists

list1= ['M', 'na', 'i', 'Ke']
list2= ['y', 'me', 's' ,'lly']

#Method 1

# for i in range(len(list1)):
#     list1[i] += list2[i]
# print(list1)


#Method 2
# listNew=[]
# for i in range(len(list1)):
#  listNew.append(list1[i]+list2[i])
# print(listNew)


#Method 3

# for i, j in zip(list1, list2):
#    print(i+j)


for i in range(len(list1)):
    data =  list1[i] +list2[i]
    if "name" in data:
        list1[i] = list1[i] + list2[i]

print(list1)
