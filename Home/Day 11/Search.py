# Search an element in an array and return its index.

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)
y= np.where(arr%2 != 0)

print(x)
print(y)

#Find the indexes where the values 2, 4, and 6 should be inserted:

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)

