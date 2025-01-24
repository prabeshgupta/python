#Count vowels

data = "aeiouf"
c = data.lower()
temp = 0
for i in c:
 if (i == 'a' or i == 'e' or i == 'i' or i == "o" or i== "u"):
  temp = temp+1
print(temp)