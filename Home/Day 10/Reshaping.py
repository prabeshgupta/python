#Reshaping means changing the shape of an array. By reshaping we can add or remove dimensions or change number of elements in each dimension.

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

#1D -> 2D
newarr = arr.reshape(4, 3)

print(newarr)


#Flattening array means converting a multidimensional array into a 1D array.

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)