#Loop stands for repetion of code until the desired output is achieved.

#For Loop 
phones  =  ['Apple', 'Samsung', 'Nokia', 'Huwawei']
for x in phones:
    print(x)

'To loop through a set of code a specified number of times, we can use the range() function. Starts at 0 and incremented by 1'
for x in range(10):
    print(x)

for x in range(2, 10):
    print(x)

for x in range(0,51,5):
    print(x)


#While Loop

i = 0
while i < 10:
    print(i)
    i+=1