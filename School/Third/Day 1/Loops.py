#While loop

i = 1
while i<10:
    print(f"I love programming {i} much.")
    i+=1

#Range
for i in range(10): #0 is inclusive and 10 is exclusive
    print(i)

for j in range(5, 10):
    print(j)

for k in range(0,30,3):
    print(k)

for l in range(10,0,-1):
    print(l)

#For loop with array
my_array = [1,2,3,4,5,6,7,8,9]
my_array_len = len(my_array)
for i in range(my_array_len):
    print(my_array[i])