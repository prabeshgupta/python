#Count the "Python" word from file

def readFile(word):
    f = open("/home/aayushgupta/Documents/Python/School/Week 2/Practice/Work.txt","r");

    arr = f.readlines()

    count = 0;
    for i in arr:
        if word in i:
            count+=1;
    
    f.close()
    return count

print(readFile("Python"))

