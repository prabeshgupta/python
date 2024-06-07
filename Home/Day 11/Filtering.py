#Getting some elements out of an existing array and creating a new array out of them is called filtering.

#A boolean index list is a list of booleans corresponding to indexes in the array.

import numpy as np

arr = np.array([1,2,3,4])
narr = arr[[True, False, True, False]]
print(narr)


arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)