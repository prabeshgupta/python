def even_list(num):
    temp = []
    while num > 0:
        if num % 2 == 0:
            temp.append(num)
        num -=1
    return temp

print(even_list(201))