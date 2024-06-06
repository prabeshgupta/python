import numpy as np

ninja = '123456789'

for i in range(3,6):
    print(ninja[i], end=" ")
    print(type(ninja[i]))
    print(isinstance(ninja[i],str))

print()
if '10' is str: 
    print(True) 
else:
    print(False)
print()


hero = ["SM","BM","H","F"]
print(len(hero))
for i in range(4):
    print(hero[i])

for i in hero:
    print(i)


for i in range(10):
    if i == 4:
        continue
    print(i)


arr = np.array([[1,2,34],[36,6,7]])
print(arr[0,1])
print(type(arr))
