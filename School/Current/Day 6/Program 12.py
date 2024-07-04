from cmath import inf

def max_num(nums):
    temp = float(-inf)
    for num in nums:
        if num > temp:
            temp = num
    return temp

print(max_num([10,2,734,646,23,64,35,574,343,999,109]))