#Sum List Number

def sumCalculate():
    item =  input("How many items do you want to add in the list? ")
    temp = []
    for i in range(int(item)):
        put = input(f"Enter number {i+1}: ")
        temp.append(int(put))
    print(sum(temp))

sumCalculate()

