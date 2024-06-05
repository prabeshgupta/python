
def bubbleSort(nums):
    count = len(nums)

    for i in range(count):
        swapped= False
        for j in range(0, count-1-i):
            if nums[j] > nums[j+1]: 
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
    
nums = [1,6,43,63,42,54,21,22]
bubbleSort(nums)
print(nums)