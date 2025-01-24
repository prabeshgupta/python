import copy

#Shallow Copy -> Shares the same memory address so changes in one object will change the copied second object

a = [1,3,5,[7,9]]

b = copy.copy(a)
b[3][0] = 10
print(a)
print(b)


#Deep Copy -> Copies the content of first object into second in another address

c = [1,3,5,[7,9]]

d = copy.deepcopy(c)
d[3][0] = 10
print(c)
print(d)