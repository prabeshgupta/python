#The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

#The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

#The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

import numpy as np

arr = np.array((1,2,4,4,2,53,4))
arr1 = arr.copy()
arr2 = arr.view()
print(arr, arr1, arr2)