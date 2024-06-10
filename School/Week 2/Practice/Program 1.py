#2nd Largest element

nums = [1,36,32,74,233,64]

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]<nums[j]:
            nums[i], nums [j] = nums[j], nums[i]
print(nums[len(nums)-2])