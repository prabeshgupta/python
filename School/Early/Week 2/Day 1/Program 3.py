from cmath import inf

#Find the largest element of an array

nums = [1,90,5,6,7,34,46,34,34,63]

#Method 1
temp = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] < nums[j]:
             temp = nums[i]
             nums[i] = nums[j]           
             nums[j] = temp
print(nums)
print(nums[9])

#Method 2
nums.sort()
print(nums[len(nums)-1])


#Method 3
val = float(-inf) #Negative Infinity
for i in range(len(nums)):
    if nums[i] > val:
        val = nums[i]
print(val)




        

