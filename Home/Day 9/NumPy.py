#NumPy stands for Numerical Python, is a Python library used for working with arrays.

import numpy as np

nums = np.array([12,4,4,54,343,53])
print(nums, "\n"+np.__version__)

#Dimension in arrays: Array depth (nested array)

# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

#An array that has 1-D arrays as its elements is called a 2-D array. It represents a matrix

arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr2)
print()

#An array that has 2-D arrays (matrices) as its elements is called 3-D array.

arr3 = np.array([[[1,23,56],[2,5,743]],[[12,36,4],[1,26,4]]])
print(arr3.ndim)


#You can define the number of dimensions by using the ndmin argument

arr4 = np.array([1,2,3,4,5], ndmin=4)
print(arr4.ndim)
