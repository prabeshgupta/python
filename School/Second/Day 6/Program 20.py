def filter(num):
    even = []
    odd = []
    while num > 0:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
        num -=1
    return even, odd

#Unpacking tuple
even, odd = filter(201)
print(even)
print(odd)