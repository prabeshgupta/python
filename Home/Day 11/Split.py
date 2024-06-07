#Splitting is reverse operation of Joining. Joining merges multiple arrays into one and Splitting breaks one array into multiple.

import numpy as np

arr = np.array([1,2,3,4,5,7,7])
narr = np.array_split(arr, 3)
print(narr[0])