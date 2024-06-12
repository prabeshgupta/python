f = open("/home/aayushgupta/Documents/Python/School/Week 3/File.txt","r")
arr =  f.readlines()

narr = []
for i in range(len(arr)): #0-4
    narr= narr+ arr[i].strip().split(",")

print(narr)
print(len(narr))

diction={}
for i in range(len(narr)): #0-19
    if narr[i] not in diction:
        diction[narr[i]] = narr.count(narr[i])

print(diction)

f.close()


whitespace = " My name is Prabesh .\n Good Good\n"
removedws = whitespace.strip()
print(removedws)
print("Hello")