#Reverse array using while loop

vals = ["AI","ML","DL","NN","BD","DS","NLP","CV"]

count = len(vals)-1

temp=[]
while count >=0:
    temp.append(vals[count])
    count -= 1

print(temp)