#To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element. Dimension represents row and index present column

import numpy as np

arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('4th element on 2nd row: ', arr2[1, 3])

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr3[0, 1, 2])