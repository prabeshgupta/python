#Add list1 with each list2 items

list1 = ["Hello","take"]
list2=["Dear", "Sir"]
temp=[]

for i in range(len(list1)):
    for j in range(len(list1)):
        temp.append(list1[i]+" "+list2[j])
print(temp)