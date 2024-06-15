myList = ["prabesh", "rosa", "upahar", "aayush", "sohil", "hanamontana"]
temp = 0
for i in range(len(myList)):
    j = len(myList[i])
    if j > temp:
        temp = j
        data = myList[i]

print(data)