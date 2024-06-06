#The function nditer() is a helping function that can be used from very basic to very advanced iterations

import numpy as np

arr = np.array([[[12,3,4,5],[23,4,35,5]], [[323,23,64,23],[3,43,7,2]]])

for i in np.nditer(arr):
    print(i)


# op_dtypes is argument to change the datatype of elements while iterating. 

# NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer. 

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)
