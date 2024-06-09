#A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa. The permutation() method returns a re-arranged array (and leaves the original array un-changed).

#Shuffle means changing arrangement of elements in an array. The shuffle() method makes changes to the original array.

from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)

