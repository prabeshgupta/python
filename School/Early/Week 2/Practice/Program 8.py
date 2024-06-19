#Append existing file

def append(text):
    try:
        f = open('/home/aayushgupta/Documents/Python/School/Week 2/Practice/Modify.txt', "a")
        f.write(text)
    except FileNotFoundError:
        print("File not found")
    else:
        print("Appended successfully")
    finally:
        f.close()

append("Null Pointer Variable")