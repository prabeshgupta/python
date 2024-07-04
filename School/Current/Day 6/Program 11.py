def even_list(nums):
    temp = []
    for i in nums:
        if i % 2 == 0:
            temp.append(i)
    return temp

print(even_list([1,3,64,23,4,26,23,62,27, 0, 100, 99]))